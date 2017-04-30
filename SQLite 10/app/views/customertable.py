# -*- coding: utf-8 -*-
"""
Name: Customer table view.
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0.0 (2017-04-30)
"""
from flask import render_template
from flask.views import MethodView

from app.models import CustomerDB


class CustomerTable(MethodView):
    '''
    View to show the customer data
    '''
    # Only support GET requests.
    methods = ['GET']

    def get(self):
        '''
        Render the status information.
        '''
        # Render the template for teh customer table.
        customers = CustomerDB().getAll()
        if customers is None:
            customers = []
        for customer in customers:
            for value in customer:
                print(value)
        return render_template('table.html', customers=customers)
