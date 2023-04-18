#This program will search the games played on a certain date
#Once those games are found, the game id will be generated

import statsapi 
import pandas as pd
from Connection import GetConnection

#Pregame class with intial values for each attribute
class PregameInfo:
    def __init__(self):
        self.gameId = 0
        self.gameDate = " "
        self.awayId = 0
        self.awayName = " "
        self.awayProbPitcher = " "
        self.awayPitcherNote = " "
        self.homeId = 0
        self.homeName = " "
        self.homeProbPitcher = " "
        self.homePitcherNote = " "
        self.venueName = " "

def GetPregameInfo(date):

    #Get the games of the day given today's data passed in to the function
    games = statsapi.schedule(date)

    #Create an empty PregameInfo object
    pregame = PregameInfo()

    #Create and empty dataframe and assign column values
    df = pd.DataFrame({'col1': [], 'col2': [], 'col3': [], 'col4': [], 'col5': [], 'col6': [], 'col7': [], 'col8': [], 'col9': [], 'col10': [], 'col11': []})
    df.columns = ["game_id", "game_date", "away_id", "away_name", "away_prob_pitcher", "away_pitcher_note", "home_id", "home_name", "home_prob_pitcher", "home_pitcher_note", "venue_name"]

    #Iterate through each game
    for game in games:

        #Create an empty list for pregame data to be added
        pregameDataList = []

        #Collect pregame data and add it to the list
        pregame.gameId = game["game_id"]
        pregameDataList.append(pregame.gameId)

        pregame.gameDate = game["game_date"]
        pregameDataList.append(pregame.gameDate)

        pregame.awayId = int(game["away_id"])
        pregameDataList.append(pregame.awayId)

        pregame.awayName = game["away_name"]
        pregameDataList.append(pregame.awayName)

        pregame.awayProbPitcher = game["away_probable_pitcher"]
        pregameDataList.append(pregame.awayProbPitcher)

        pregame.awayPitcherNote = game["away_pitcher_note"]
        pregameDataList.append(pregame.awayPitcherNote)

        pregame.homeId = int(game["home_id"])
        pregameDataList.append(pregame.homeId)

        pregame.homeName = game["home_name"]
        pregameDataList.append(pregame.homeName)

        pregame.homeProbPitcher = game["home_probable_pitcher"]
        pregameDataList.append(pregame.homeProbPitcher)

        pregame.homePitcherNote = game["home_pitcher_note"]
        pregameDataList.append(pregame.homePitcherNote)

        pregame.venueName = game["venue_name"]
        pregameDataList.append(pregame.venueName)

        #Add each list to the end of the dataframe
        df.loc[len(df)] = pregameDataList

    #Return the dataframe
    return df