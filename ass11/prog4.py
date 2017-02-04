#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
"""
Name: Program 4 "Employee Class"
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (2017-02-04)

Program that uses a class to hold the personal information fo a few people.
"""
import employee


def print_employees(employees):
    """
    Print all employees in a nice tables.

    :param employees: List of employees.
    """
    print('| {:<30} '.format('Name') +
          '| {:^10}'.format('ID number') +
          '| {:^20} '.format('Department') +
          '| {:^20} |'.format('Job title'))
    print('|{:-^32}'.format('') +
          '|{:-^11}'.format('') +
          '|{:-^22}'.format('') +
          '|{:-^22}|'.format(''))

    # Print all employees.
    for single_emp in employees:
        print('| {:<30} '.format(single_emp.get_name()) +
              '| {:^10}'.format(single_emp.get_id()) +
              '| {:>20} '.format(single_emp.get_department()) +
              '| {:>20} |'.format(single_emp.get_title()))


def main():
    """
    Program main entry point.
    """
    # Create a list of employees.
    employees = list()
    # Populate 3 instances.
    employees.append(
        employee.Employee('Susan Meyers', '47899', 'Accounting',
                          'Vice President'))
    employees.append(
        employee.Employee('Mark Jones', '39119', 'IT', 'Programmer'))
    employees.append(
        employee.Employee('Joy Rogers', '81774', 'Manufacturing', 'Engineer'))

    # Print all employees.
    print_employees(employees)


# Run this when invoked directly
if __name__ == '__main__':
    main()
