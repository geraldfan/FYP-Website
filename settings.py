# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 10:41:58 2020

@author: Gerald
"""

from app import db
from models import Model

# Class for the "setting" table in the Mbase.db file
class Setting(db.Model):
    __tablename__ = "settings"
    
    id = db.Column(db.String, db.ForeignKey("models.id"), primary_key = True)
    system_type = db.Column(db.String)
    settings_name = db.Column(db.String)
    units = db.Column(db.String)
    init = db.Column(db.String)
    priors = db.Column(db.String)
    parameter_bounds = db.Column(db.String)
    fixed_parameters = db.Column(db.String)
    solver_args = db.Column(db.String)
    
    model = db.relationship("Model", backref=db.backref("settings", order_by=id), lazy=True)
    
    def __repr__(self):
        return "{}".format(self.system_type)