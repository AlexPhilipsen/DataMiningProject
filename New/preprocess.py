import json

class Game:
    def __init__(self, gid = '', map = '', time = 0, blu_fc = 0, red_fc = 0, blu_score = 0, red_score = 0, winner = ''):
        self.gid = gid
        self.map = map
        self.time = time
        self.blu_fc = blu_fc
        self.red_fc = red_fc
        self.blu_score = blu_score 
        self.red_score = red_score
        self.winner = winner

class Round:
    def __init__(self, gid = '', round_num = 0, blu_dmg = 0, blu_kills = 0, blu_ubers = 0, red_dmg = 0, red_kills = 0, red_ubers = 0, winner = '', fc = '', length = 0):
        self.gid = gid
        self.round_num = round_num
        self.blu_dmg = blu_dmg
        self.blu_kills = blu_kills
        self.blu_ubers = blu_ubers
        self.red_dmg = red_dmg
        self.red_kills = red_kills
        self.red_ubers = red_ubers
        self.winner = winner
        self.fc = fc
        self.length = length

class Event:
    def __init__(self, gid = '', round_num = 0, num = 0, team = '', name = '', time = 0):
        self.gid = gid
        self.round_num = round_num
        self.num = num
        self.team = team
        self.name = name
        self.time = time

class Player:
    def __init__(self, gid = '', pid = '', team = '', k = 0, d = 0, a = 0, dmg = 0, medkits = 0, ubers = 0, hr = 0, healing = 0):
        self.gid = gid
        self.pid = pid
        self.team = team
        self.k = k
        self.d = d
        self.a = a
        self.dmg = dmg
        self.medkits = medkits
        self.ubers = ubers
        self.hr = hr
        self.healing = healing

class Specific_Class:
    def __init__(self, gid = '', pid = '', class_name = '', time = 0, k = 0, d = 0, a = 0, ubers = 0, hr = 0, healing = 0):
        self.gid = gid
        self.pid = pid
        self.class_name = class_name
        self.time = time
        self.k = k
        self.d = d
        self.a = a

class Player_Weapons:
    def __init__(self, gid = '', pid = '', weapon_name = '', kills = 0, dmg = 0, avg_dmg = 0, shots = 0, hits = 0):
        self.gid = gid
        self.pid = pid
        self.weapon_name = weapon_name
        self.kills = kills
        self.dmg = dmg
        self.avg_dmg = avg_dmg
        self.shots = shots
        self.hits = hits

def get_game_data(gid, data, rounds):
    gid = gid
    map = data[0]['info']['map']
    time = data[0]['info']['total_length']
    blu_fc = 0
    red_fc = 0
    blu_score = 0
    red_score = 0
    
    for round in rounds:
        if(round.fc == 'Blue'):
            blu_fc += 1
        elif(round.fc == 'Red'):
            red_fc += 1

        if(round.winner == 'Blue'):
            blu_score += 1
        elif(round.winner == 'Red'):
            red_score += 1

    if(blu_score == red_score):
        winner = 'Tie'
    elif(blu_score < red_score):
        winner = 'Red'
    else:
        winner = 'Blu'
    
    return Game(gid, map, time, blu_fc, red_fc, blu_score, red_score, winner)

def get_round_data(gid, data):
    gid = gid
    round_num = 1
    blu_dmg = 0
    blu_kills = 0
    blu_ubers = 0
    red_dmg = 0
    red_kills = 0
    red_ubers = 0
    winner = ''
    fc = ''
    length = 0

    rounds = []

    # Create a class for each round
    for round in data[0]['rounds']:
        gid = gid
        round_num = round_num
        blu_dmg = round['team']['Blue']['dmg']
        blu_kills = round['team']['Blue']['kills']
        blu_ubers = round['team']['Blue']['ubers']
        red_dmg = round['team']['Red']['dmg']
        red_kills = round['team']['Red']['kills']
        red_ubers = round['team']['Red']['ubers']
        winner = round['winner']
        fc = round['firstcap']
        length = round['length']

        rounds.append(Round(gid, round_num, blu_dmg, blu_kills, blu_ubers, red_dmg, red_kills, red_ubers, winner, fc, length))
        round_num += 1
    
    return rounds

def get_event_data(gid, data):
    gid = gid
    round_num = 1
    event_num = 1
    team = ''
    event_name = ''
    time = 0

    events = []

    # Create a class for each event
    for round in data[0]['rounds']:
        for i in range(len(round['events'])):
            gid = gid
            round_num = round_num
            event_num = i + 1
            team = round['events'][i]['team']
            time = round['events'][i]['type']

            events.append(Event(gid, round_num, event_num, team, time))
        round_num += 1

    return events

def get_player_data(gid, data, player_IDs):
    player_IDs = player_IDs

    gid = gid
    pid = ''
    team = ''
    k = 0
    d = 0
    a = 0
    dmg = 0
    medkits = 0
    ubers = 0
    hr = 0
    healing = 0

    players_info = []

    # Create a class for each player and store in an array
    for player in player_IDs:
        gid = gid
        pid = player
        team = data[0]['players'][player]['team']
        k = data[0]['players'][player]['kills']
        d = data[0]['players'][player]['deaths']
        a = data[0]['players'][player]['assists']
        dmg = data[0]['players'][player]['dmg']
        medkits = data[0]['players'][player]['medkits']
        ubers = data[0]['players'][player]['ubers']
        hr = data[0]['players'][player]['hr']
        healing = data[0]['players'][player]['heal']

        players_info.append(Player(gid, pid, team, k, d, a, dmg, medkits, ubers, hr, healing))
    
    return players_info

def get_player_class_data(gid, data, player_IDs):
    player_IDs = player_IDs

    gid = gid
    pid = ''
    player_class = ''
    time = 0
    k = 0
    d = 0
    a = 0

    players_classes = []

    # Create a class for each player and classes picked
    for player in player_IDs:
        gid = gid
        pid = player
        for specific_class in data[0]['players'][player]['class_stats']:
            player_class = specific_class['type']
            time = specific_class['total_time']
            k = specific_class['kills']
            d = specific_class['deaths']
            a = specific_class['assists']
            players_classes.append(Specific_Class(gid, pid, player_class, time, k, d, a))

    return players_classes

def get_weapon_data(gid, data, player_IDs):
    player_IDs = player_IDs

    gid = gid
    pid = ''
    weapon_name = ''
    kills = 0
    dmg = 0
    avg_dmg = 0
    shots = 0
    hits = 0

    player_weapons = []

    # Create a class for each player and weapons equipped
    for player in player_IDs:
        gid = gid
        pid = player
        for specific_class in data[0]['players'][player]['class_stats']:
            for weapon in specific_class['weapon']:
                weapon_name = weapon
                kills = specific_class['weapon'][weapon_name]['kills']
                dmg = specific_class['weapon'][weapon_name]['dmg']
                avg_dmg = specific_class['weapon'][weapon_name]['avg_dmg']
                shots = specific_class['weapon'][weapon_name]['shots']
                hits = specific_class['weapon'][weapon_name]['hits']
                player_weapons.append(Player_Weapons(gid, pid, weapon_name, kills, dmg, avg_dmg, shots, hits))
                pass

    return player_weapons