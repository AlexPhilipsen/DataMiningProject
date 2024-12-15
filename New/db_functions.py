import sqlite3
from preprocess import *

def insert_game_data(game_data, db):
    con = sqlite3.connect(db)
    c = con.cursor()

    data = (game_data.gid, game_data.map, game_data.time, game_data.blu_fc, game_data.red_fc, game_data.blu_score, game_data.red_score, game_data.winner)
    c.execute("""INSERT OR IGNORE INTO game_table VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", data)

    con.commit()
    con.close()

def insert_round_data(round_data, db):
    con = sqlite3.connect(db)
    c = con.cursor()

    for round in round_data:
        data = (round.gid, round.round_num, round.blu_dmg, round.blu_kills, round.blu_ubers, round.red_dmg, round.red_kills, round.red_ubers, round.winner, round.fc, round.length)
        c.execute("""INSERT OR IGNORE INTO game_round VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", data)

    con.commit()
    con.close()

def insert_event_data(event_data, db):
    con = sqlite3.connect(db)
    c = con.cursor()

    for event in event_data:
        data = (event.gid, event.round_num, event.num, event.team, event.name, event.time)
        c.execute("""INSERT OR IGNORE INTO game_event VALUES (?, ?, ?, ?, ?, ?)""", data)

    con.commit()
    con.close()

def insert_player_data(player_data, db):
    con = sqlite3.connect(db)
    c = con.cursor()

    for player in player_data:
        data = (player.gid, player.pid, player.team, player.k, player.d, player.a, player.dmg, player.medkits, player.ubers, player.hr, player.healing)
        c.execute("""INSERT OR IGNORE INTO game_player VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", data)

    con.commit()
    con.close()

def insert_player_class_data(player_class_data, db):
    con = sqlite3.connect(db)
    c = con.cursor()

    for player_class in player_class_data:
        data = (player_class.gid, player_class.pid, player_class.class_name, player_class.time, player_class.k, player_class.d, player_class.a)
        c.execute("""INSERT OR IGNORE INTO player_class VALUES (?, ?, ?, ?, ?, ?, ?)""", data)

    con.commit()
    con.close()

def insert_weapon_data(weapon_data, db):
    con = sqlite3.connect(db)
    c = con.cursor()

    for weapon in weapon_data:
        data = (weapon.gid, weapon.pid, weapon.weapon_name, weapon.kills, weapon.dmg, weapon.avg_dmg, weapon.shots, weapon.hits)
        c.execute("""INSERT OR IGNORE INTO player_weapon VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", data)
        
    con.commit()
    con.close()

def insert_class_kill(class_kill_data, db):
    con = sqlite3.connect(db)
    c = con.cursor()

    for data in class_kill_data:
        c.execute("""INSERT OR IGNORE INTO class_kill VALUES (?, ?, ?)""", data)

    con.commit()
    con.close()