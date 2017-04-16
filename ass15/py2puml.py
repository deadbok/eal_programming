#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# --------------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 42):
# <martin.groenholdt@gmail.com> wrote this file. As long as you retain this notice
# you can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return. Martin B. K. Grønholdt
# --------------------------------------------------------------------------------
# Program to parse Python classes and write their info to PlantUML files
# (see http://plantuml.com/) that can be used to generate UML files and GraphViz
# renderings of classes.
#
# Missing:
#  * Inheritance parsing
#  * Does not like end='' in print.
#
# History:
#
# Version 0.1.3
# * Change output file name to add ".classes.puml" to the original file name.
# Version 0.1.2
#  * Exception handling.
#
# Version 0.1.1
#  * Comments.
#
# Version 0.1.0
#  * First working version.

import argparse
import ast

__version__ = '0.1.3'

class ClassParser(ast.NodeVisitor):
    """
    Class to parse the stuff we're interested in from a class.

     * Methods and their visibility.
     * Members created in __init__ and their visibility.
    """
    # List to put the class data.
    puml_classes = list()

    def visit_ClassDef(self, node):
        """
        Class visitor that parses the info we want, when encountering a class definition.

        :param node: The node of the class.
        """
        #Dictionary containing the interesting parts of the classes structure
        puml_class = dict()
        puml_class['name'] = node.name
        puml_class['members'] = list()
        puml_class['methods'] = list()

        #Run through all children of the class definition.
        for child in node.body:
            # If we have a function definition, store it.
            if isinstance(child, ast.FunctionDef):
                # Check if it is "private".
                if child.name.startswith('__'):
                    puml_class['methods'].append('-' + child.name)
                else:
                    puml_class['methods'].append('+' + child.name)

                # Check if this s the constructor.
                if child.name == '__init__':
                    # Find all assignment expressions in the constructor.
                    for code in child.body:
                        if isinstance(code, ast.Assign):
                            # Find attributes since we want "self." + "something"
                            for target in code.targets:
                                if isinstance(target, ast.Attribute):
                                    # If the value is a name and its id is self.
                                    if isinstance(target.value, ast.Name):
                                        if target.value.id == 'self':
                                            # Check if it is "private".
                                            if target.attr.startswith('__'):
                                                puml_class['members'].append('-' + target.attr)
                                            else:
                                                puml_class['members'].append('+' + target.attr)

        # Save the class.
        self.puml_classes.append(puml_class)


if __name__ == '__main__':
    # Takes a python file as a parameter.
    parser = argparse.ArgumentParser(prog='py2puml')
    parser.add_argument('py_file', type=argparse.FileType('r'))
    args = parser.parse_args()

    # Output file name is input file +'.classes.puml'
    puml_file_name = args.py_file.name + '.class.puml'

    try:
        with open(puml_file_name, 'w') as puml_file:
            # Write the beginnings of the PlantUML file.
            puml_file.write('@startuml\nskinparam monochrome true\nskinparam classAttributeIconSize 0\nscale 2\n')

            # Use AST to parse the file.
            tree = ast.parse(args.py_file.read())
            class_writer = ClassParser()
            class_writer.visit(tree)

            # Write the resulting classes in PlantUML format.
            for puml_class in class_writer.puml_classes:
                puml_file.write('class ' + puml_class['name'] + '{\n')

                for member in puml_class['members']:
                    puml_file.write('    ' + member + '\n')

                for method in puml_class['methods']:
                    puml_file.write('    ' + method + '()\n')

                puml_file.write('}\n')

            # End the PlantUML files.
            puml_file.write('@enduml')
    except IOError:
        print('I/O error.')
    except SyntaxError as see:
        print('Syntax error in ', end='')
        print( args.py_file.name + ':' + str(see.lineno) + ':' + str(see.offset) + ': ' + see.text)