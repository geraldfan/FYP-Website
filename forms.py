# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 15:19:51 2020

@author: Gerald
"""

# forms.py

from wtforms import Form, StringField, SelectField, validators

# Class for the search form
class ModelSearchForm(Form):
    choices = [('System Type', 'System Type'),
               ('Last Modified Date', 'Last Modified Date'),
               ('Descriptions', 'Descriptions')]
    select = SelectField('Search for model:', choices=choices)
    search = StringField('')