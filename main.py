# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 15:12:48 2020

@author: Gerald
"""

# main.py

from app import app
from db_setup import init_db, db_session
from forms import ModelSearchForm
from flask import flash, render_template, request, redirect, send_file
from models import Model
from settings import Setting
from tables import Results, Settings

init_db()


@app.route('/', methods=['GET', 'POST'])
def index():
    search = ModelSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)

    return render_template('index.html', form=search)

# Calls the search function and returns the results in results.html
@app.route('/results')
def search_results(search):
    results = []
    search_string = search.data['search']

    if search_string:
        if search.data['select'] == 'System Type':
            qry = db_session.query(Model).filter(
                    Model.system_type.contains(search_string, autoescape=True))
            results = qry.all()
        elif search.data['select'] == 'Last Modified Date':
            qry = db_session.query(Model).filter(
                Model.date_added.contains(search_string, autoescape=True))
            results = qry.all()
        elif search.data['select'] == 'Descriptions':
            qry = db_session.query(Model).filter(
                Model.descriptions.contains(search_string, autoescape=True))
            results = qry.all()
        else:
            qry = db_session.query(Model)
            results = qry.all()
    else:
        qry = db_session.query(Model)
        results = qry.all()

    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        # display results
        result = Results(results)
        result.border = True

        search = ModelSearchForm(request.form)
        counter = 'Number of models found: ' + str(len(results))
        return render_template('results.html', form=search, result=result, counter=counter)

# Links to the respective download urls for the models based on their id
@app.route('/download/<string:id>')
def download(id):
#        qry = db_session.query(Model).filter(Model.id==id)
#        model = qry.first().
        path = "downloads/config/" + str(id) + ".zip"
#         path = "downloads/config/bmss1.ini"
        return send_file(path, as_attachment=True)

# Links to the respective settings for the models based on their id
@app.route('/settings/<string:id>')
def settings(id):
        results = []
        qry = db_session.query(Setting).filter(Setting.id==id)
        results = qry.all()
        table = Settings(results)
        search = ModelSearchForm(request.form)
        return render_template('settings.html', form=search, table=table)

# Links to the respective genetic circuit diagrams based on their ids
@app.route('/display/<string:id>')
def display(id):
    search=ModelSearchForm(request.form)
    num_id = int(''.join(filter(str.isdigit, str(id))))
    if num_id <= 13:
        return render_template('inducible.html', form=search)
    elif num_id <= 17:
        return render_template('constitutive.html', form=search)
    elif num_id <= 21:
        return render_template('constitutivevariedpromoter.html', form=search)
    elif num_id <= 23:
        return render_template('constitutivevariedrbs.html', form=search)
    elif num_id <= 27:
        return render_template('NOTgate.html', form=search)
    elif num_id <= 33:
        return render_template('ANDgate.html', form=search)
    elif num_id <= 44:
        return render_template('ORgate.html', form=search)
    else:
        return render_template('diagramerror.html', form=search)
        

if __name__ == '__main__':
    import os
    if 'WINGDB_ACTIVE' in os.environ:
        app.debug = False
    app.run(threaded = True, port=5000)