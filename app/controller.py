from app import app
from flask import render_template, request, redirect
from tests.src.game import compare_choices
from tests.src.player import Player


@app.route('/')
def index():
    return render_template('index.html', title = 'Home')

