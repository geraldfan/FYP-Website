# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 15:22:22 2020

@author: Gerald
"""

from flask_table import Table, Col, LinkCol

# Overriding the Col class to format the content 
class FormatCol(Col):
    def td_format(self, content):
        output = []
        for char in content:
            if char == ',':
                char += '<br/>'
            output.append(char)
        return output
    
class ParameterBoundsCol(Col):
    def td_format(self, content):
        output = []
        for char in content:
            if char ==']':
                char += '<br/>'
            output.append(char)
        return output
class DescriptionCol(Col):
    def td_format(self, content):
        output = []
        title = ['t','i','t','l','e']
        author = ['a','u','t','h','o','r']
        journal = ['j','o','u','r','n','a','l']
        for i in range(len(content) - 1):
            if content[i] == '\\' and content[i + 1] == 'n':
                output.append("<br/>")
            elif content[i-1] == '\'':
                output.append(content[i].upper())
            elif content[i] == '!':
                output.append('&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp')
            elif content[i] == 't':
                isTitle = self.capitalize(i, title, content)
                if isTitle == True:
                    output.append(content[i].upper())
                else:
                    output.append(content[i])
            elif content[i] == 'a':
                isAuthor = self.capitalize(i, author, content)
                if isAuthor:
                    output.append(content[i].upper())
                else:
                    output.append(content[i])
            elif content[i] == 'j':
                isJournal = self.capitalize(i, journal, content)
                if isJournal:
                    output.append(content[i].upper())
                else:
                    output.append(content[i])
                        
            elif not ((content[i] == 'n' and content [i - 1] == '\\') or (content[i] == '{' or content[i] == '\'' or content[i] == '}')):
                output.append(content[i])
        return output
    def capitalize(self,i, word, content):
        isWord = True
        for j in range(len(word)):
            if not(content[i] == word[j]):
                isWord = False
                break
            else:
                i += 1
        return isWord

# Result html table outputted on the website.
class Results(Table):
    classes = ['blueTable']
    id = Col('Id', show=False)
    system_type = Col('System Type')
    states = Col('States')
    parameters = Col('Parameters')
    inputs = Col('Inputs')
    equations = FormatCol('Equations')
    descriptions = DescriptionCol('Descriptions')
    last_modified_date = Col('Last Modified Date')
    genetic_circuit_diagrams = LinkCol('Genetic Circuit Diagram', 'display', url_kwargs=dict(id='id'))
    download = LinkCol('Download', 'download', url_kwargs=dict(id='id'))
    settings = LinkCol('Settings', 'settings', url_kwargs=dict(id='id'))

# Settings html table outputted on the website
class Settings(Table):
    classes = ['blueTable']
    id = Col('Id', show=False)
    system_type = Col('System Type')
    settings_name = Col('Settings Name')
    units = FormatCol('Units')
    init = Col('Init')
    priors = Col('Priors')
    parameter_bounds = ParameterBoundsCol('Parameter Bounds')
    fixed_parameters = Col('Fixed Parameters')
    solver_args = Col('Solver Args')