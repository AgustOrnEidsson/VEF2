from flask import Flask, render_template
from bokahilla import app
from bokahilla import models

listi=models.listi
@app.route('/')

@app.route('/index')
def index():
    return render_template('index.tpl',listi=listi)

@app.route('/nanar/<book>')
def bokin(book=None):
    return render_template('nanar.tpl', bokin=models.URLCheck(listi,book).check())