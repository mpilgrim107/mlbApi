#The purpose of this file is to test the endpoints of the statsapi library
#Nothing in this file will be called from the main.py file
#Able to test what kind of data is returned and in what format

import statsapi 
import datetime
import json
import pandas as pd
from Connection import GetConnection
import psycopg2
import array as arr
from datetime import date, timedelta
import PregameScripts

"""
gameData = statsapi.boxscore_data(718781)

awayPlayerBatters = gameData["away"]["batters"]
awayPlayerPitchers = gameData["away"]["pitchers"]

print(awayPlayerBatters)
print(awayPlayerPitchers)

for element in awayPlayerPitchers:
    if element in awayPlayerBatters:
        awayPlayerBatters.remove(element)


awayPlayerBatters = gameData["away"]["batters"]
print(awayPlayerBatters)


for awayPlayer in awayPlayerBatters:
    awayPlayer = "ID" + str(awayPlayer)
    print("PlayerId: ",awayPlayer)
    awayPlayerBattingObj = gameData["away"]["players"][awayPlayer]["stats"]
    print(json.dumps(awayPlayerBattingObj, indent=3))
"""



#Collect set of game_id's from database of the previous night(Pregame.py)
gameData = statsapi.boxscore_data(718558)

awayTeamPitchingObj = gameData["away"]["teamStats"]["pitching"]
print(json.dumps(awayTeamPitchingObj, indent=2))