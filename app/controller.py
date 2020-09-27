from app import app
from flask import render_template
from app.models.game import *
from app.models.player import *

@app.route('/<player_1_name>/<player_1_choice>/<player_2_name>/<player_2_choice>')
def index(player_1_name, player_1_choice, player_2_name, player_2_choice):
    player_1 = Player(player_1_name, player_1_choice)
    player_2 = Player(player_2_name, player_2_choice)
    game = Game()
    result = game.compare_choices(player_1, player_2)
    return render_template('index.html', game_result=result)
