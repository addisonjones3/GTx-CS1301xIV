# !/usr/bin/env python
# Last problem, you wrote a function that generated the all-
# time win-loss-tie record for Georgia Tech against any other
# team.
# 
# That dataset had a lot of other information in it. Let's
# use it to answer some more questions. As a reminder, the
# data will be a CSV file, meaning that each line will be a
# comma-separated list of values. Each line will describe one
# game.
# 
# The columns, from left-to-right, are:
# 
#  - Date: the date of the game, in Year-Month-Day format.
#  - Opponent: the name of the opposing team
#  - Location: Home, Away, or Neutral
#  - Points For: Points scored by Georgia Tech
#  - Points Against: Points scored by the opponent

# This line will open the file:
#  record_file = open('../resource/lib/public/georgia_tech_football.csv', 'r')
import datetime

def gt_csv_to_dict(filename):
    with open(filename, 'r') as record_file:
        rows = record_file.read().split('\n')
        # delete header
        del rows[0]
        # debugging graded file
        if rows[-1] == '':
            del rows[-1]
        team_info = {}

        for row in rows:
            row = row.split(',')
            # massage data
            teamname = row[1]
            row[3] = int(row[3])
            row[4] = int(row[4])
            if teamname not in team_info.keys():
                team_info[teamname] = {'games': [],
                                       'total wins': 0,
                                       'home wins': 0,
                                       'away wins': 0,
                                       'neutral wins': 0,
                                       'total losses': 0,
                                       'home losses': 0,
                                       'away losses': 0,
                                       'neutral losses': 0,
                                       'total ties': 0,
                                       'home ties': 0,
                                       'away ties': 0,
                                       'neutral ties': 0,
                                       'points for': 0,
                                       'points against': 0}


            team_dict = team_info[teamname]
            if row[3] > row[4]:
                team_dict['total wins'] += 1
                row.append('win')
                if row[2] == 'Home':
                    team_dict['home wins'] += 1
                elif row[2] == 'Away':
                    team_dict['away wins'] += 1
                else:
                    team_dict['neutral wins'] += 1
            elif row[3] == row[4]:
                team_dict['total ties'] += 1
                row.append('tie')
                if row[2] == 'Home':
                    team_dict['home ties'] += 1
                elif row[2] == 'Away':
                    team_dict['away ties'] += 1
                else:
                    team_dict['neutral ties'] += 1
            else:
                team_dict['total losses'] += 1
                row.append('loss')
                if row[2] == 'Home':
                    team_dict['home losses'] += 1
                elif row[2] == 'Away':
                    team_dict['away losses'] += 1
                else:
                    team_dict['neutral losses'] += 1
            team_dict['points for'] += row[3]
            team_dict['points against'] += row[4]
            team_info[teamname]['games'].append(row)
        return team_info
# Here, add any code you want to allow you to answer the
# questions asked below over on edX. This is just a sandbox
# for you to explore the dataset: nothing is required for
# submission here.


def earliest_game(file_dict):
    first_game = {'team': '',
                  'date': None}
    for key in file_dict.keys():
        games = sorted(file_dict[key]['games'])
        game1 = games[0][0]
        game1 = datetime.datetime(int(game1[:4]), int(game1[5:7].lstrip('0')), int(game1[8:10])).date().strftime('%Y-%m-%d')
        if first_game['date'] is None:
            first_game['date'] = game1
            first_game['team'] = key
        elif game1 < first_game['date']:
            first_game['date'] = game1
            first_game['team'] = key
    return first_game
# gt_csv_to_dict('season2016.csv')


team_info = gt_csv_to_dict('Prob7Full.csv')
fgame = earliest_game(team_info)
print ('Earliest game was {0} against {1}'.format(fgame['date'], fgame['team']))
print ('Auburn points for {0}'.format(team_info['Auburn']['points for']))
print ('Auburn points against {0}'.format(team_info['Auburn']['points against']))

home_w = 0
home_l = 0
home_t = 0
for key in team_info.keys():
    home_w += team_info[key]['home wins']
    home_l += team_info[key]['home losses']
    home_t += team_info[key]['home ties']
print ('Home record: {0}-{1}-{2}'.format(home_w, home_l, home_t))

w_09 = 0
l_09 = 0
t_09 = 0

for team in team_info:
    for game in team_info[team]['games']:
        if game[0][0:4] == '2009':
            if 'win' in game:
                w_09 += 1
            elif 'tie' in game:
                t_09 += 1
            else:
                l_09 += 1
print ('2009 record: {0}-{1}-{2}'.format(w_09, l_09, t_09))

oct_w = 0
oct_l = 0
oct_t = 0

for team in team_info:
    for game in team_info[team]['games']:
        gamedate = game[0]
        if datetime.datetime(int(gamedate[:4]), int(gamedate[5:7].lstrip('0')), int(gamedate[8:10])).date().month == 10:
            if 'win' in game:
                oct_w += 1
            elif 'loss' in game:
                oct_l += 1
            else:
                oct_t += 1
print ('Oct record: {0}-{1}-{2}'.format(oct_w, oct_l, oct_t))

sec_w = 0
sec_l = 0
sec_t = 0

for team in team_info:
    for game in team_info[team]['games']:
        gamedate = game[0]
        if 1964 > datetime.datetime(int(gamedate[:4]), int(gamedate[5:7].lstrip('0')), int(gamedate[8:10])).date().year > 1932:
            if 'win' in game:
                sec_w += 1
            elif 'loss' in game:
                sec_l += 1
            else:
                sec_t += 1
print ('SEC record: {0}-{1}-{2}'.format(sec_w, sec_l, sec_t))

most_points_for = {'team': '', 'points': 0, 'no points': []}
for team in team_info.keys():
    if most_points_for['team'] == '':
        most_points_for['points'] = team_info[team]['points for']
        most_points_for['team'] = team
    if team_info[team]['points for'] > most_points_for['points']:
        most_points_for['points'] = team_info[team]['points for']
        most_points_for['team'] = team
    if team_info[team]['points against'] == 0:
        most_points_for['no points'].append(team)

no_points_for = []
for team in team_info.keys():
    if team_info[team]['points for'] == 0:
        no_points_for.append(team)

print('Scored most points, {0}, against {1}').format(most_points_for['points'], most_points_for['team'])
print('No points against {0}'.format(len(most_points_for['no points'])))
print ('GT never scored points against {0}'.format(no_points_for))
# print(team_info['Elon'])

pt_diff = {'team': '', 'diff': 0}
for team in team_info.keys():
    if abs(team_info[team]['points for'] - team_info[team]['points against']) > pt_diff['diff']:
        pt_diff['diff'] = abs(team_info[team]['points for']) - abs(team_info[team]['points against'])
        pt_diff['team'] = team

print ('Biggest point diff: {0} with {1} points'.format(pt_diff['team'], pt_diff['diff']))

highest_avg_score = {'team': '', 'score': 0}

for team in team_info.keys():
    if len(team_info[team]['games']) > 5:
        avg_score = abs(team_info[team]['points for'] - team_info[team]['points against']) / len(team_info[team]['games'])
        if avg_score > highest_avg_score['score']:
            highest_avg_score['team'] = team
            highest_avg_score['score'] = avg_score

print ('Highest avg score against >5 games played: {0} with {1} points'.format(highest_avg_score['team'], highest_avg_score['score']))