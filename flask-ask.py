# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 20:59:16 2020

@author: divtech
"""

from flask import Flask
from flask_assistant import Assistant, ask

app = Flask(__name__)
assist = Assistant(app, project_id='sakshi-qrsost')

@assist.action('Demo')
def hello_world():
    speech = 'hello'
    return ask(speech)

if __name__ == '__main__':
    app.run(debug=True)