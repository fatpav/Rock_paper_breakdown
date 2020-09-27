from app import app
from flask import render_template, request, redirect
from tests.src.game import compare_choices
from tests.src.player import Player


@app.route('/')
def index():
    return render_template('index.html', title = 'Home')

@app.route('/players')
def players():
    return render_template('players.html')

@app.route('/players', method=['POST'])
def get_result():
    player_1_choice = request.form["player_1_choice"]
    player_2_choice = request.form["player_2_choice"]
    compare_choices(player1_choice, player2_choice)
    return ("")

    