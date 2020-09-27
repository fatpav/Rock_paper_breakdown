from app import app
from flask import render_template, request, redirect, url_for
from tests.src.game import *
from tests.src.player import *
from app.models.game_choices import *


@app.route('/')
def index():
    return render_template('index.html', title = 'Home')

@app.route('/players')
def players():
    return render_template('players.html')