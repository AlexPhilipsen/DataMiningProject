from preprocess import *
from db_functions import *
import sqlite3
import json
import requests

import concurrent.futures
import time

# Function to get API response
def load_url(url):
    gid = int(url.split('/')[6])
    response = requests.get(url)
    if(response.status_code == 200):
        return (gid, response.json())
    else:
        return False

# Function to load game data and store them
def query(gid, num):
    # Generate url strings for amount of games
    urls = []
    for i in range(num):
        urls.append("http://logs.tf/api/v1/log/" + str(gid - i))

    # Concurrently retrieve game responses
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(load_url, urls)
    
    # Return the generator as a list
    return [result for result in list(results) if result]

# Function to write to file
def write(filename, res):
    with open(filename, 'w') as f:
        json.dump(res, f, indent=4)

# Function to clear file
def clear(filename):
    with open(filename, 'w') as f:
        pass

# Function to parse and store data
def store(filename, db, gid, num):
    # Start timer
    start_time = time.perf_counter()

    ### Process to query and write to file. Uncomment if 'log_outputs.json' is not generated
    # clear(filename)
    # res = query(gid, num)
    # write(filename, res)
    
    # Read into file
    with open(filename, 'r') as f:
        all_data = json.load(f)
        for game in all_data:
            gid = game[0]
            data = game[1]

            gamemode = data['info']['map'].split('_')[0]

            if(gamemode == 'cp' or gamemode == 'koth'):
                # Parse the data
                player_IDs = [player for player in data['players'] if player is not None]
                player_data = get_player_data(gid, data, player_IDs)
                player_class_data = get_player_class_data(gid, data, player_IDs)
                weapon_data = get_weapon_data(gid, data, player_IDs)
                round_data = get_round_data(gid, data)
                event_data = get_event_data(gid, data)
                game_data = get_game_data(gid, data, round_data)
                kill_data = get_class_kills(data, player_IDs)

                # Store the data
                insert_game_data(game_data, db)
                insert_round_data(round_data, db)
                insert_event_data(event_data, db)
                insert_player_data(player_data, db)
                insert_player_class_data(player_class_data, db)
                insert_weapon_data(weapon_data, db)
                insert_class_kill(kill_data, db)

    # Finish timer
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time} seconds\n")