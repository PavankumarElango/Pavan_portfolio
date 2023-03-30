# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 15:57:56 2020

@author: pavan
"""

from flask import Flask, render_template

app = Flask(__name__)
app.debug = True
@app.route('/')
def landing_page():
    return render_template('index.html')
    
if __name__ == '__main__':
    app.run(debug=True)
