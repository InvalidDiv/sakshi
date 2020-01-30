# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 15:23:57 2020

@author: divtech
"""

# Importing flask module in the project is mandatory 
# An object of Flask class is our WSGI application. 
from flask import Flask, redirect, url_for, request
import urllib
import json
import os
import sys


# Flask constructor takes the name of 
# current module (__name__) as argument. 
app = Flask(__name__) 

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function. 
@app.route('/sakshi') 
# ‘/’ URL is bound with hello_world() function. 
def hello_world(): 
	return 'Hello, welcome to sakshi. Please go to /test for our trial webpage'

@app.route('/login',methods = ['POST', 'GET']) 
def login(): 
   if request.method == 'POST': 
      user = request.form['nm'] 
      return redirect(url_for('success',name = user)) 
   else: 
      user = request.args.get('nm') 
      return redirect(url_for('success',name = user)) 
  


# main driver function 
if __name__ == '__main__': 

	# run() method of Flask class runs the application 
	# on the local development server. 
	app.run() 
