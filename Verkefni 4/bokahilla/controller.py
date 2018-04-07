from flask import Flask, render_template
from bokahilla import app
from bokahilla import models

listi=models.listi
@app.route('/')

@app.route('/index')
def index():
    return render_template('forsida.html',listi=listi)

@app.route('/hafdusamband')
def bokin(book=None):
    return render_template('nanar.html')

@app.route('/leikarar')
def leik():
    return render_template('leika.html',listi=listi)