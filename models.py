# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 15:36:19 2020

@author: Gerald
"""

from app import db

# Class for the "model" table in the Mbase.db file
class Model(db.Model):
    __tablename__ = "models"

    id = db.Column(db.String, primary_key=True)
    system_type = db.Column(db.String)
    states = db.Column(db.String)
    parameters = db.Column(db.String)
    inputs = db.Column(db.String)
    equations = db.Column(db.String)
    descriptions = db.Column(db.String)
    last_modified_date = db.Column(db.String)



    def __repr__(self):
        return "{}".format(self.system_type)