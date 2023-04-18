import statsapi 
import pandas as pd

#PlayerBatting class with initial values for each attribute
class PlayerBatting:
    def __init__(self):
        self.player_id = 0
        self.team_id = 0
        self.game_date = " "
        self.full_name = " "
        self.runs = 0
        self.doubles = 0
        self.triples = 0
        self.home_runs = 0
        self.strike_outs = 0
        self.base_on_balls = 0
        self.hits = 0
        self.at_bats = 0
        self.stolen_bases = 0
        self.rbi = 0
        self.left_on_base = 0

def GatherPlayerBattingStats(awayPlayerBattingObj, homePlayerBattingObj, gameId, gameDate):
    gameData = statsapi.boxscore_data(gameId)

    #Create empty dataframe as well as the column values of the dataframe
    df = pd.DataFrame({'col1': [], 'col2': [], 'col3': [], 'col4': [], 'col5': [], 'col6': [], 'col7': [], 'col8': [], 'col9': [], 'col10': [], 'col11': [], 'col12': [], 'col13': [], 'col14': [], 'col15': []})
    df.columns = ["player_id", "team_id", "game_date", "full_name", "runs", "doubles", "triples", "home_runs", "strike_outs", "base_on_balls", "hits", "at_bats", "stolen_bases", "rbi", "left_on_base", ]

    #These variables give a list of the away batters and pitchers in the boxscore_data endpoint
    awayPlayerBatters = gameData["away"]["batters"]
    awayPlayerPitchers = gameData["away"]["pitchers"]

    #Some boxscore_data endpoints for certain games list the pitcher IDs in the batter IDs section
    #If there are any pitchers listed in the batters section, those pitcher IDs will be removed from the list of batter IDs
    for element in awayPlayerPitchers:
        if element in awayPlayerBatters:
            awayPlayerBatters.remove(element)

    #Go through each away Batter ID that is listed
    for awayPlayer in awayPlayerBatters:

        #Create an empty list to store the values in
        awayPlayerStatsList = []

        #Each section of player data consists of 'ID' plus the playerID
        awayPlayer = "ID" + str(awayPlayer)

        #Collect the datapoints and add them to the list
        awayPlayerBattingObj.player_id = gameData["away"]["players"][awayPlayer]["person"]["id"]
        awayPlayerStatsList.append(awayPlayerBattingObj.player_id)

        awayPlayerBattingObj.team_id = gameData["away"]["players"][awayPlayer]["parentTeamId"]
        awayPlayerStatsList.append(awayPlayerBattingObj.team_id)

        awayPlayerBattingObj.game_date = gameDate
        awayPlayerStatsList.append(awayPlayerBattingObj.game_date)

        awayPlayerBattingObj.full_name = gameData["away"]["players"][awayPlayer]["person"]["fullName"]
        awayPlayerStatsList.append(awayPlayerBattingObj.full_name)

        awayPlayerBattingObj.runs = gameData["away"]["players"][awayPlayer]["stats"]["batting"]["runs"]
        awayPlayerStatsList.append(awayPlayerBattingObj.runs)

        awayPlayerBattingObj.doubles = gameData["away"]["players"][awayPlayer]["stats"]["batting"]["doubles"]
        awayPlayerStatsList.append(awayPlayerBattingObj.doubles)

        awayPlayerBattingObj.triples = gameData["away"]["players"][awayPlayer]["stats"]["batting"]["triples"]
        awayPlayerStatsList.append(awayPlayerBattingObj.triples)

        awayPlayerBattingObj.home_runs = gameData["away"]["players"][awayPlayer]["stats"]["batting"]["homeRuns"]
        awayPlayerStatsList.append(awayPlayerBattingObj.home_runs)

        awayPlayerBattingObj.strike_outs = gameData["away"]["players"][awayPlayer]["stats"]["batting"]["strikeOuts"]
        awayPlayerStatsList.append(awayPlayerBattingObj.strike_outs)

        awayPlayerBattingObj.base_on_balls = gameData["away"]["players"][awayPlayer]["stats"]["batting"]["baseOnBalls"]
        awayPlayerStatsList.append(awayPlayerBattingObj.base_on_balls)

        awayPlayerBattingObj.hits = gameData["away"]["players"][awayPlayer]["stats"]["batting"]["hits"]
        awayPlayerStatsList.append(awayPlayerBattingObj.hits)

        awayPlayerBattingObj.at_bats = gameData["away"]["players"][awayPlayer]["stats"]["batting"]["atBats"]
        awayPlayerStatsList.append(awayPlayerBattingObj.at_bats)

        awayPlayerBattingObj.stolen_bases = gameData["away"]["players"][awayPlayer]["stats"]["batting"]["stolenBases"]
        awayPlayerStatsList.append(awayPlayerBattingObj.stolen_bases)

        awayPlayerBattingObj.rbi = gameData["away"]["players"][awayPlayer]["stats"]["batting"]["rbi"]
        awayPlayerStatsList.append(awayPlayerBattingObj.rbi)

        awayPlayerBattingObj.left_on_base = gameData["away"]["players"][awayPlayer]["stats"]["batting"]["leftOnBase"]
        awayPlayerStatsList.append(awayPlayerBattingObj.left_on_base)
       
        #Add the list of datapoints to the end of the dataframe
        df.loc[len(df)] = awayPlayerStatsList

    #These variables give a list of the home batters and pitchers in the boxscore_data endpoint
    homePlayerBatters = gameData["home"]["batters"]
    homePlayerPitchers = gameData["home"]["pitchers"]

    #Some boxscore_data endpoints for certain games list the pitcher IDs in the batter IDs section
    #If there are any pitchers listed in the batters section, those pitcher IDs will be removed from the list of batter IDs
    for element in homePlayerPitchers:
        if element in homePlayerBatters:
            homePlayerBatters.remove(element)

    #Go through each home Batter ID that is listed
    for homePlayer in homePlayerBatters:
        #Create an empty list to store the values in
        homePlayerStatsList = []

        #Each section of player data consists of 'ID' plus the playerID
        homePlayer = "ID" + str(homePlayer)

        #Collect the datapoints and add them to the list
        homePlayerBattingObj.player_id = gameData["home"]["players"][homePlayer]["person"]["id"]
        homePlayerStatsList.append(homePlayerBattingObj.player_id)

        homePlayerBattingObj.team_id = gameData["home"]["players"][homePlayer]["parentTeamId"]
        homePlayerStatsList.append(homePlayerBattingObj.team_id)

        homePlayerBattingObj.game_date = gameDate
        homePlayerStatsList.append(homePlayerBattingObj.game_date)

        homePlayerBattingObj.full_name = gameData["home"]["players"][homePlayer]["person"]["fullName"]
        homePlayerStatsList.append(homePlayerBattingObj.full_name)

        homePlayerBattingObj.runs = gameData["home"]["players"][homePlayer]["stats"]["batting"]["runs"]
        homePlayerStatsList.append(homePlayerBattingObj.runs)

        homePlayerBattingObj.doubles = gameData["home"]["players"][homePlayer]["stats"]["batting"]["doubles"]
        homePlayerStatsList.append(homePlayerBattingObj.doubles)

        homePlayerBattingObj.triples = gameData["home"]["players"][homePlayer]["stats"]["batting"]["triples"]
        homePlayerStatsList.append(homePlayerBattingObj.triples)

        homePlayerBattingObj.home_runs = gameData["home"]["players"][homePlayer]["stats"]["batting"]["homeRuns"]
        homePlayerStatsList.append(homePlayerBattingObj.home_runs)

        homePlayerBattingObj.strike_outs = gameData["home"]["players"][homePlayer]["stats"]["batting"]["strikeOuts"]
        homePlayerStatsList.append(homePlayerBattingObj.strike_outs)

        homePlayerBattingObj.base_on_balls = gameData["home"]["players"][homePlayer]["stats"]["batting"]["baseOnBalls"]
        homePlayerStatsList.append(homePlayerBattingObj.base_on_balls)

        homePlayerBattingObj.hits = gameData["home"]["players"][homePlayer]["stats"]["batting"]["hits"]
        homePlayerStatsList.append(homePlayerBattingObj.hits)

        homePlayerBattingObj.at_bats = gameData["home"]["players"][homePlayer]["stats"]["batting"]["atBats"]
        homePlayerStatsList.append(homePlayerBattingObj.at_bats)

        homePlayerBattingObj.stolen_bases = gameData["home"]["players"][homePlayer]["stats"]["batting"]["stolenBases"]
        homePlayerStatsList.append(homePlayerBattingObj.stolen_bases)

        homePlayerBattingObj.rbi = gameData["home"]["players"][homePlayer]["stats"]["batting"]["rbi"]
        homePlayerStatsList.append(homePlayerBattingObj.rbi)

        homePlayerBattingObj.left_on_base = gameData["home"]["players"][homePlayer]["stats"]["batting"]["leftOnBase"]
        homePlayerStatsList.append(homePlayerBattingObj.left_on_base)
       
        #Add the list of datapoints to the end of the dataframe
        df.loc[len(df)] = homePlayerStatsList

    #Return the dataframe once the data has been collected from both teams
    return df