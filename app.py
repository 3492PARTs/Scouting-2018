from flask import Flask, render_template, request, redirect, url_for, Response
from peewee import *
import models as db

app = Flask(__name__)


valid = False
event = -1


@app.route('/', methods=['GET', 'POST'])
def index():
    events = []
    passwrd = request.form.get('pass', None)

    if passwrd == "hello":
        global valid
        valid = True

        event_id = request.form.get('event', None)
        global event
        event = event_id
    else:
        events = db.event.select().order_by(db.event.event_id.asc()).tuples()
        events = list(events)

    return render_template('index.html', valid=valid, events=events)


@app.route('/field')
def field():
    if valid:
        teams = db.team.select().join(db.event_team_xref, JOIN_INNER, (db.team.team_no == db.event_team_xref.team_no) & (db.event_team_xref.event == event)).order_by(db.team.team_no.asc()).tuples()
        teams = list(teams)
        print(teams)
        return render_template('field.html', teams=teams)
    else:
        return redirect(url_for('index'))


@app.route('/field-submit', methods=['POST'])
def field_submit():
    if valid:
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

        match = db.match(event=event, team_no=team, scout=name, auto_move=auto_move, auto_switch_cubes=auto_switch_cubes,
                         auto_scale_cubes=auto_scale_cubes, auto_comm=auto_comm, match_no=match,
                         tele_switch_cubes=tele_switch_cubes, tele_scale_cubes=tele_scale_cubes,
                         hang=hang, tele_comm=tele_comm, rate=rating)
        match.save()

        return redirect(url_for('field'))
    else:
        return redirect(url_for('index'))


@app.route('/download')
def download():
    if valid:
        data = db.match.select().where(db.match.event == event).tuples()
        data = list(data)
        csv = ""
        for dp in data:
            csv += str(dp)[1:-1] + "\n"
        print(csv)
        return Response(
            csv,
            mimetype="text/csv",
            headers={"Content-disposition": "attachment; filename=dump.csv"})
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
