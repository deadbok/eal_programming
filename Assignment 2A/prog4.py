#!/usr/bin/env python
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
"""
Name: Program 4
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (13/11-2016)

Asks the user to enter the monthly costs for expenses incurred from operating
and owning an automobile. Print out the total cost of the expenses for a month
and a year.
"""
class Car(object):
    """
    Class to calculate the expenses incurred from operating and owning an
    automobile.
    """
    # Loan payment per month.
    loan_payment = 0
    # Insurance payment per month.
    insurance = 0
    # Expenses on gas per month.
    gas = 0
    # Expenses on oil per month.
    oil = 0
    # Expences on tires per month.
    tires = 0
    # Expenses on maintenance per moth.
    maintenance = 0

    def __init__(self):
        """
        Ask for values from the user, for expenses, when instantiating this
        object.
        """
        print('Enter the monthly payment for each of these expenses:')
        try:
            self.loan_payment = float(input('\tLoan payment: '))
            self.insurance = float(input('\tInsurance: '))
            self.gas = float(input('\tGas: '))
            self.oil = float(input('\tOil: '))
            self.tires = float(input('\tTires: '))
            self.maintenance = float(input('\tMaintainance: '))
        except ValueError:
            # Complain when something unexpected was entered.
            print('\nPlease use only numbers.')
            exit(1)

    def calc_expenses_for_months(self, current_expenses=None, months=1):
        """
        Calculate the expenses for an span of months.

        :param current_expenses: Tuple of the current expenses incurred up until
                                 the current call of the function.
        :param months: Span of months to calculate expenses for.
        :return: A dictionary with the total cost for each expense.
        """
        # If there are still more month to go.
        if months != 0:
            # If this is not the first call to this function.
            if current_expenses is not None:
                # Add monthly expenses to the current expenses.
                current_expenses['Loan payment'] += self.loan_payment
                current_expenses['Insurance'] += self.insurance
                current_expenses['Gas'] += self.gas
                current_expenses['Oil'] += self.oil
                current_expenses['Tires'] += self.tires
                current_expenses['Maintenance'] += self.maintenance
            else:
                # If this is the first call create a dictionary for the
                # expenses and add them for the current month.
                current_expenses = dict()
                current_expenses['Loan payment'] = self.loan_payment
                current_expenses['Insurance'] = self.insurance
                current_expenses['Gas'] = self.gas
                current_expenses['Oil'] = self.oil
                current_expenses['Tires'] = self.tires
                current_expenses['Maintenance'] = self.maintenance
            # Make the function recursive, to shoot myself in the foot when
            # I have to create the hierarchy diagram.
            # The function calls itself until month is 0.
            return(self.calc_expenses_for_months(current_expenses, months - 1))
        else:
            # If this is the final call, return a dictionary of the acumulated
            # expenses.
            return(current_expenses)

    def expenses_for_months(self, months=1):
        """
        Calculate and output the expenses for a span of months.

        :param months: Span of months to calculate expenses for.
        """
        # Print a header for the expenses output.
        print('\nExpenses for {} months: '.format(months))
        # Get a dictionary with the total expenses as values and expense name
        # as key.
        expenses = self.calc_expenses_for_months(None, months)
        # Variable to keep the total cost of all expenses.
        total_cost = 0
        # Run through all expenses in the dictionary printing their key
        # as description and value as result.
        for key, value in expenses.items():
            # Align both the description and the result using new style string
            # formatting.
            print('\t{:<12}: {:12.2f}'.format(key, value))
            total_cost += value
        #Print the total cost
        print('\t{:<12}: {:12.2f}'.format('Total cost', total_cost))


def main():
    """
    Program main entry point.
    """
    #Create the Car instance
    car = Car()
    # Calculate and print the expenses for one month.
    car.expenses_for_months(1)
    # Calcualte and print the expenses for a year.
    car.expenses_for_months(12)


# Run this when invoked directly
if __name__ == '__main__':
    main()
