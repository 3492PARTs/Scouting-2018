import models as db
__author__ = "Brandon Duke"

__version__ = ""
__email__ = "http://bduke.net"

insert = []

insert.append(db.event(event_nm='Greater Pittsburgh Regional', date_st='2018-03-21', date_end='2018-03-24'))

insert.append(db.team(team_no=117, team_nm='The Steel Dragons'))
insert.append(db.team(team_no=156, team_nm='RPM - Robotics Plus Mayhem'))
insert.append(db.team(team_no=217, team_nm='Thunder Chickens'))
insert.append(db.team(team_no=303, team_nm='The T.E.S.T. Team'))
insert.append(db.team(team_no=870, team_nm='TEAM R.I.C.E.'))
insert.append(db.team(team_no=945, team_nm='Team Banana'))
insert.append(db.team(team_no=1308, team_nm='Wildcats'))
insert.append(db.team(team_no=1708, team_nm='AMP\'D Robotics'))
insert.append(db.team(team_no=1743, team_nm='Short Circuits'))
insert.append(db.team(team_no=1787, team_nm='Flying Circuits'))
insert.append(db.team(team_no=2051, team_nm='The Beattie Bulldogs'))
insert.append(db.team(team_no=2053, team_nm='TigerTronics'))
insert.append(db.team(team_no=2641, team_nm='PCCR'))
insert.append(db.team(team_no=2656, team_nm='Quasics'))
insert.append(db.team(team_no=3061, team_nm='Huskie Robotics'))
insert.append(db.team(team_no=3062, team_nm='Spartan Robotics'))
insert.append(db.team(team_no=3171, team_nm='HURRICANES'))
insert.append(db.team(team_no=3511, team_nm='Road Dogs'))
insert.append(db.team(team_no=3954, team_nm='4-H Electrotechs'))
insert.append(db.team(team_no=3955, team_nm='4-H Gears'))
insert.append(db.team(team_no=3957, team_nm='4-H Robo Rangers'))
insert.append(db.team(team_no=4027, team_nm='Centre County 4-H Robotics'))
insert.append(db.team(team_no=4049, team_nm='Knoch Knights Robotics'))
insert.append(db.team(team_no=4050, team_nm='Biohazard'))
insert.append(db.team(team_no=4150, team_nm='FRobotics'))
insert.append(db.team(team_no=4269, team_nm='CardinalBots'))
insert.append(db.team(team_no=4522, team_nm='Team SCREAM'))
insert.append(db.team(team_no=4547, team_nm='WestyTek'))
insert.append(db.team(team_no=4930, team_nm='Electric Mayhem'))
insert.append(db.team(team_no=4991, team_nm='HorsePower'))
insert.append(db.team(team_no=5077, team_nm='RoboCards'))
insert.append(db.team(team_no=5472, team_nm='Stallion Robotics'))
insert.append(db.team(team_no=5842, team_nm='Royal Robotics'))
insert.append(db.team(team_no=6054, team_nm='The Dukes'))
insert.append(db.team(team_no=6414, team_nm='Voyager'))
insert.append(db.team(team_no=6947, team_nm='Savage Tumaz'))
insert.append(db.team(team_no=7165, team_nm='Perkins Pirates')) #TODO Check if already in db
insert.append(db.team(team_no=7274, team_nm='Brashear Bulls Robotics'))


insert.append(db.event_team_xref(team_no=48, event_id=2))
insert.append(db.event_team_xref(team_no=117, event_id=2))
insert.append(db.event_team_xref(team_no=156, event_id=2))
insert.append(db.event_team_xref(team_no=217, event_id=2))
insert.append(db.event_team_xref(team_no=303, event_id=2))
insert.append(db.event_team_xref(team_no=337, event_id=2))
insert.append(db.event_team_xref(team_no=870, event_id=2))
insert.append(db.event_team_xref(team_no=945, event_id=2))
insert.append(db.event_team_xref(team_no=1308, event_id=2))
insert.append(db.event_team_xref(team_no=1708, event_id=2))
insert.append(db.event_team_xref(team_no=1743, event_id=2))
insert.append(db.event_team_xref(team_no=1787, event_id=2))
insert.append(db.event_team_xref(team_no=2051, event_id=2))
insert.append(db.event_team_xref(team_no=2053, event_id=2))
insert.append(db.event_team_xref(team_no=2252, event_id=2))
insert.append(db.event_team_xref(team_no=2603, event_id=2))
insert.append(db.event_team_xref(team_no=2641, event_id=2))
insert.append(db.event_team_xref(team_no=2656, event_id=2))
insert.append(db.event_team_xref(team_no=3061, event_id=2))
insert.append(db.event_team_xref(team_no=3062, event_id=2))
insert.append(db.event_team_xref(team_no=3171, event_id=2))
insert.append(db.event_team_xref(team_no=3260, event_id=2))
insert.append(db.event_team_xref(team_no=3492, event_id=2))
insert.append(db.event_team_xref(team_no=3504, event_id=2))
insert.append(db.event_team_xref(team_no=3511, event_id=2))
insert.append(db.event_team_xref(team_no=3954, event_id=2))
insert.append(db.event_team_xref(team_no=3955, event_id=2))
insert.append(db.event_team_xref(team_no=3957, event_id=2))
insert.append(db.event_team_xref(team_no=4027, event_id=2))
insert.append(db.event_team_xref(team_no=4028, event_id=2))
insert.append(db.event_team_xref(team_no=4049, event_id=2))
insert.append(db.event_team_xref(team_no=4050, event_id=2))
insert.append(db.event_team_xref(team_no=4145, event_id=2))
insert.append(db.event_team_xref(team_no=4150, event_id=2))
insert.append(db.event_team_xref(team_no=4269, event_id=2))
insert.append(db.event_team_xref(team_no=4467, event_id=2))
insert.append(db.event_team_xref(team_no=4521, event_id=2))
insert.append(db.event_team_xref(team_no=4522, event_id=2))
insert.append(db.event_team_xref(team_no=4547, event_id=2))
insert.append(db.event_team_xref(team_no=4930, event_id=2))
insert.append(db.event_team_xref(team_no=4991, event_id=2))
insert.append(db.event_team_xref(team_no=5077, event_id=2))
insert.append(db.event_team_xref(team_no=5472, event_id=2))
insert.append(db.event_team_xref(team_no=5740, event_id=2))
insert.append(db.event_team_xref(team_no=5811, event_id=2))
insert.append(db.event_team_xref(team_no=5842, event_id=2))
insert.append(db.event_team_xref(team_no=6032, event_id=2))
insert.append(db.event_team_xref(team_no=6054, event_id=2))
insert.append(db.event_team_xref(team_no=6414, event_id=2))
insert.append(db.event_team_xref(team_no=6947, event_id=2))
insert.append(db.event_team_xref(team_no=7165, event_id=2))
insert.append(db.event_team_xref(team_no=7274, event_id=2))


for i in insert:
    i.save(force_insert=True)
    print(i)
