import statsapi 
import pandas as pd

#PlayerPitching class with initial values of each attribute
class PlayerPitching:
    def __init__(self):
        self.player_id = 0
        self.team_id = 0
        self.game_date = " "
        self.full_name = " "
        self.home = 0
        self.away = 0
        self.opponent = 0
        self.runs = 0
        self.doubles = 0
        self.triples = 0
        self.home_runs = 0
        self.strike_outs = 0
        self.base_on_balls = 0
        self.hits = 0
        self.at_bats = 0
        self.stolen_bases = 0
        self.innings_pitched = " "
        self.wins = 0
        self.losses = 0
        self.holds = 0
        self.blown_saves = 0

def GatherPlayerPitchingStats(awayPlayerPitchingObj, homePlayerPitchingObj, gamePk, gameDate):
    
    #Get game data according to the gameId (gamePk) variable passed in
    gameData = statsapi.boxscore_data(gamePk)

    #Create empty dataframe with column values
    df = pd.DataFrame({'col1': [], 'col2': [], 'col3': [], 'col4': [], 'col5': [], 'col6': [], 'col7': [], 'col8': [], 'col9': [], 'col10': [], 'col11': [], 'col12': [], 'col13': [], 'col14': [], 'col15': [], 'col16': [], 'col17': [], 'col18': [], 'col19': [], 'col20': [], 'col21': []})
    df.columns = ["player_id", "team_id", "game_date", "full_name", "home", "away", "opponent", "runs", "doubles", "triples", "home_runs", "strike_outs", "base_on_balls", "hits", "at_bats", "stolen_bases", "innings_pitched", "wins", "losses", "holds", "blown_saves"]

    #Get the IDs of the away pitchers in the game
    awayPlayerPitchers = gameData["away"]["pitchers"]
    awayTeam = gameData["teamInfo"]["away"]["teamName"]
    homeTeam = gameData["teamInfo"]["home"]["teamName"]

    #For loop that iterates through each away pitcher of the game
    for awayPlayer in awayPlayerPitchers:
        
        #Create empty list to add playerPitcher data
        awayPlayerStatsList = []

        #Each section of player data consists of 'ID' plus the playerID
        awayPlayer = "ID" + str(awayPlayer)

        #Gather player pitcher data points and add it the the list
        awayPlayerPitchingObj.player_id = gameData["away"]["players"][awayPlayer]["person"]["id"]
        awayPlayerStatsList.append(awayPlayerPitchingObj.player_id)

        awayPlayerPitchingObj.team_id = gameData["away"]["players"][awayPlayer]["parentTeamId"]
        awayPlayerStatsList.append(awayPlayerPitchingObj.team_id)

        awayPlayerPitchingObj.game_date = gameDate
        awayPlayerStatsList.append(awayPlayerPitchingObj.game_date)

        awayPlayerPitchingObj.full_name = gameData["away"]["players"][awayPlayer]["person"]["fullName"]
        awayPlayerStatsList.append(awayPlayerPitchingObj.full_name)

        awayPlayerPitchingObj.away = 1
        awayPlayerStatsList.append(awayPlayerPitchingObj.home)
        awayPlayerStatsList.append(awayPlayerPitchingObj.away)

        awayPlayerPitchingObj.opponent = homeTeam
        awayPlayerStatsList.append(awayPlayerPitchingObj.opponent)

        awayPlayerPitchingObj.runs = gameData["away"]["players"][awayPlayer]["stats"]["pitching"]["runs"]
        awayPlayerStatsList.append(awayPlayerPitchingObj.runs)

        awayPlayerPitchingObj.doubles = gameData["away"]["players"][awayPlayer]["stats"]["pitching"]["doubles"]
        awayPlayerStatsList.append(awayPlayerPitchingObj.doubles)

        awayPlayerPitchingObj.triples = gameData["away"]["players"][awayPlayer]["stats"]["pitching"]["triples"]
        awayPlayerStatsList.append(awayPlayerPitchingObj.triples)

        awayPlayerPitchingObj.home_runs = gameData["away"]["players"][awayPlayer]["stats"]["pitching"]["homeRuns"]
        awayPlayerStatsList.append(awayPlayerPitchingObj.home_runs)

        awayPlayerPitchingObj.strike_outs = gameData["away"]["players"][awayPlayer]["stats"]["pitching"]["strikeOuts"]
        awayPlayerStatsList.append(awayPlayerPitchingObj.strike_outs)

        awayPlayerPitchingObj.base_on_balls = gameData["away"]["players"][awayPlayer]["stats"]["pitching"]["baseOnBalls"]
        awayPlayerStatsList.append(awayPlayerPitchingObj.base_on_balls)

        awayPlayerPitchingObj.hits = gameData["away"]["players"][awayPlayer]["stats"]["pitching"]["hits"]
        awayPlayerStatsList.append(awayPlayerPitchingObj.hits)

        awayPlayerPitchingObj.at_bats = gameData["away"]["players"][awayPlayer]["stats"]["pitching"]["atBats"]
        awayPlayerStatsList.append(awayPlayerPitchingObj.at_bats)

        awayPlayerPitchingObj.stolen_bases = gameData["away"]["players"][awayPlayer]["stats"]["pitching"]["stolenBases"]
        awayPlayerStatsList.append(awayPlayerPitchingObj.stolen_bases)

        awayPlayerPitchingObj.innings_pitched = gameData["away"]["players"][awayPlayer]["stats"]["pitching"]["inningsPitched"]
        awayPlayerStatsList.append(awayPlayerPitchingObj.innings_pitched)

        awayPlayerPitchingObj.wins = gameData["away"]["players"][awayPlayer]["stats"]["pitching"]["wins"]
        awayPlayerStatsList.append(awayPlayerPitchingObj.wins)

        awayPlayerPitchingObj.losses = gameData["away"]["players"][awayPlayer]["stats"]["pitching"]["losses"]
        awayPlayerStatsList.append(awayPlayerPitchingObj.losses)

        awayPlayerPitchingObj.holds = gameData["away"]["players"][awayPlayer]["stats"]["pitching"]["holds"]
        awayPlayerStatsList.append(awayPlayerPitchingObj.holds)

        awayPlayerPitchingObj.blown_saves = gameData["away"]["players"][awayPlayer]["stats"]["pitching"]["blownSaves"]
        awayPlayerStatsList.append(awayPlayerPitchingObj.blown_saves)
       
        #Add the List of player pitching data to the end of the dataframe
        df.loc[len(df)] = awayPlayerStatsList

    #Get the IDs of the home pitchers in the game
    homePlayerPitchers = gameData["home"]["pitchers"]

    #For loop that iterates through each home pitcher of the game
    for homePlayer in homePlayerPitchers:

        #Create empty list to add playerPitcher data
        homePlayerStatsList = []

        #Each section of player data consists of 'ID' plus the playerID
        homePlayer = "ID" + str(homePlayer)

        #Gather player pitcher data points and add it the the list
        homePlayerPitchingObj.player_id = gameData["home"]["players"][homePlayer]["person"]["id"]
        homePlayerStatsList.append(homePlayerPitchingObj.player_id)

        homePlayerPitchingObj.team_id = gameData["home"]["players"][homePlayer]["parentTeamId"]
        homePlayerStatsList.append(homePlayerPitchingObj.team_id)

        homePlayerPitchingObj.game_date = gameDate
        homePlayerStatsList.append(homePlayerPitchingObj.game_date)

        homePlayerPitchingObj.full_name = gameData["home"]["players"][homePlayer]["person"]["fullName"]
        homePlayerStatsList.append(homePlayerPitchingObj.full_name)

        homePlayerPitchingObj.home = 1
        homePlayerStatsList.append(homePlayerPitchingObj.home)
        homePlayerStatsList.append(homePlayerPitchingObj.away)

        homePlayerPitchingObj.opponent = awayTeam
        homePlayerStatsList.append(homePlayerPitchingObj.opponent)

        homePlayerPitchingObj.runs = gameData["home"]["players"][homePlayer]["stats"]["pitching"]["runs"]
        homePlayerStatsList.append(homePlayerPitchingObj.runs)

        homePlayerPitchingObj.doubles = gameData["home"]["players"][homePlayer]["stats"]["pitching"]["doubles"]
        homePlayerStatsList.append(homePlayerPitchingObj.doubles)

        homePlayerPitchingObj.triples = gameData["home"]["players"][homePlayer]["stats"]["pitching"]["triples"]
        homePlayerStatsList.append(homePlayerPitchingObj.triples)

        homePlayerPitchingObj.home_runs = gameData["home"]["players"][homePlayer]["stats"]["pitching"]["homeRuns"]
        homePlayerStatsList.append(homePlayerPitchingObj.home_runs)

        homePlayerPitchingObj.strike_outs = gameData["home"]["players"][homePlayer]["stats"]["pitching"]["strikeOuts"]
        homePlayerStatsList.append(homePlayerPitchingObj.strike_outs)

        homePlayerPitchingObj.base_on_balls = gameData["home"]["players"][homePlayer]["stats"]["pitching"]["baseOnBalls"]
        homePlayerStatsList.append(homePlayerPitchingObj.base_on_balls)

        homePlayerPitchingObj.hits = gameData["home"]["players"][homePlayer]["stats"]["pitching"]["hits"]
        homePlayerStatsList.append(homePlayerPitchingObj.hits)

        homePlayerPitchingObj.at_bats = gameData["home"]["players"][homePlayer]["stats"]["pitching"]["atBats"]
        homePlayerStatsList.append(homePlayerPitchingObj.at_bats)

        homePlayerPitchingObj.stolen_bases = gameData["home"]["players"][homePlayer]["stats"]["pitching"]["stolenBases"]
        homePlayerStatsList.append(homePlayerPitchingObj.stolen_bases)

        homePlayerPitchingObj.innings_pitched = gameData["home"]["players"][homePlayer]["stats"]["pitching"]["inningsPitched"]
        homePlayerStatsList.append(homePlayerPitchingObj.innings_pitched)

        homePlayerPitchingObj.wins = gameData["home"]["players"][homePlayer]["stats"]["pitching"]["wins"]
        homePlayerStatsList.append(homePlayerPitchingObj.wins)

        homePlayerPitchingObj.losses = gameData["home"]["players"][homePlayer]["stats"]["pitching"]["losses"]
        homePlayerStatsList.append(homePlayerPitchingObj.losses)

        homePlayerPitchingObj.holds = gameData["home"]["players"][homePlayer]["stats"]["pitching"]["holds"]
        homePlayerStatsList.append(homePlayerPitchingObj.holds)

        homePlayerPitchingObj.blown_saves = gameData["home"]["players"][homePlayer]["stats"]["pitching"]["blownSaves"]
        homePlayerStatsList.append(homePlayerPitchingObj.blown_saves)
       
        #Add the List of player pitching data to the end of the dataframe
        df.loc[len(df)] = homePlayerStatsList

    #Return the dataframe once all of the data points for all pitchers have been added
    return df