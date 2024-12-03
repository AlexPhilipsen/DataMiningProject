from preprocess import *
from db_functions import *
import sqlite3
import json
import requests

def load_(filename, gid, querySuccessCode = 200):
    log_data = []
    with open('log_outputs.json', 'w') as f:
        URLQuery = "http://logs.tf/api/v1/log/" + str(gid)
        response = requests.get(URLQuery)
        if(response.status_code != querySuccessCode):
            print("An error has occured with query: {URLQuery}")
            return False
        data = response.json()
        log_data.append(data)
        json.dump(log_data, f, indent=4)
    return True

def clear_(filename):
    with open(filename, 'w') as f:
        pass

def query_store(filename, db, num):
    gid = 3736855
    i = 0
    count = 0
    while count < num:
        if(load_(filename, gid - i, 200)):
            with open(filename, 'r') as file:
                data = json.load(file)
                pass

            gamemode = data[0]['info']['map'].split('_')[0]
            
            if(gamemode == 'cp' or gamemode == 'koth'):
                # Parse the data
                player_IDs = [player for player in data[0]['players'] if player is not None]

                player_data = get_player_data(gid - i, data, player_IDs)
                player_class_data = get_player_class_data(gid - i, data, player_IDs)
                weapon_data = get_weapon_data(gid - i, data, player_IDs)
                round_data = get_round_data(gid - i, data)
                event_data = get_event_data(gid - i, data)
                game_data = get_game_data(gid - i, data, round_data)

                # Store the data
                insert_game_data(game_data, db)
                insert_round_data(round_data, db)
                insert_event_data(event_data, db)
                insert_player_data(player_data, db)
                insert_player_class_data(player_class_data, db)
                insert_weapon_data(weapon_data, db)
                count += 1
        i += 1
        clear_(filename)