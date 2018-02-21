from flask import Flask, render_template, request, redirect, url_for
from peewee import *
import models as db

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/field')
def field():
    teams = db.team.select().tuples()
    teams = list(teams)

    return render_template('field.html', teams=teams)


@app.route('/field-submit', methods=['POST'])
def field_submit():
    name = request.form.get('name', None)
    team = request.form.get('team-no', None)
    match = request.form.get('match', None)
    auto_move = request.form.get('move-group', None)
    auto_switch_cubes = request.form.get('auto-cube-switch', None)
    auto_scale_cubes = request.form.get('auto-cube-scale', None)
    auto_comm = request.form.get('auto-comm', None)
    tele_switch_cubes = request.form.get('tele-cube-switch', None)
    tele_scale_cubes = request.form.get('tele-cube-scale', None)
    hang = request.form.get('hang', 'n')
    tele_comm = request.form.get('tele-comm', None)
    rating = request.form.get('rating', None)

    match = db.match(team_no=team, scout=name, auto_move=auto_move, auto_switch_cubes=auto_switch_cubes,
                     auto_scale_cubes=auto_scale_cubes, auto_comm=auto_comm, match_no=match,
                     tele_switch_cubes=tele_switch_cubes, tele_scale_cubes=tele_scale_cubes,
                     hang=hang, tele_comm=tele_comm, rate=rating)
    match.save()

    return redirect(url_for('field'))


if __name__ == '__main__':
    app.run()
