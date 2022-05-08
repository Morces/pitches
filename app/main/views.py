from app.main.forms import PitchForm
from . import main
from flask import render_template


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/pitches', methods=['GET', 'POST'])
def pitches():

    pitch_form = PitchForm()

    

    return render_template('pitches.html', pitch_form=pitch_form)
    