from app import app
from flask import render_template, request, redirect
from tests.src.game import *

@app.route('/')
def index():
    return render_template('index.html', title = 'Home')