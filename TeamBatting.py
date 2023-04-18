import statsapi 
import pandas as pd
from TeamInfoScripts import UpdateHomeWinsGames, UpdateAwayWinsGames

#TeamBatting class with initial values for each attribute
class TeamBatting:
    def __init__(self):
        self.team_id = 0
        self.game_date = " "
        self.team_name = " "
        self.game_number = 0
        self.home = 0
        self.away = 0
        self.opponent = " "
        self.win = 0
        self.loss = 0
        self.runs = 0
        self.doubles = 0
        self.triples = 0
        self.home_runs = 0
        self.strike_outs = 0
        self.base_on_balls = 0
        self.hits = 0
        self.average = " "
        self.at_bats = 0
        self.on_base_percentage = " "
        self.slugging = " "
        self.on_base_plus_slugging = " "
        self.stolen_bases = 0
        self.runs_batted_in = 0
        self.left_on_base = 0

#This function will determine if the team passed in won or lost the game given the home and away runs
#Once the win or loss is determined, the win/loss record will be updated in the database
def GetWinLoss(homeRuns, awayRuns, TeamBattingObj):

    if homeRuns > awayRuns and TeamBattingObj.home == 1:
        TeamBattingObj.win = 1
        UpdateHomeWinsGames(TeamBattingObj)
    elif homeRuns < awayRuns and TeamBattingObj.home == 1:
        TeamBattingObj.loss = 1
        UpdateHomeWinsGames(TeamBattingObj)
    elif homeRuns > awayRuns and TeamBattingObj.away == 1:
        TeamBattingObj.loss = 1
        UpdateAwayWinsGames(TeamBattingObj)
    else:
        TeamBattingObj.win = 1
        UpdateAwayWinsGames(TeamBattingObj)

def GatherGameBattingStats(awayTeamBattingObj, homeTeamBattingObj, gamePk, gameDate):
    #Retrieve the game log given the gameId (gamePk)
    gameData = statsapi.boxscore_data(gamePk)

    #Create an empty dateframe and assign the column values
    df = pd.DataFrame({'col1': [], 'col2': [], 'col3': [], 'col4': [], 'col5': [], 'col6': [], 'col7': [], 'col8': [], 'col9': [], 'col10': [], 'col11': [], 'col12': [], 'col13': [], 'col14': [], 'col15': [], 'col16': [], 'col17': [], 'col18': [], 'col19': [], 'col20': [], 'col21': [], 'col22': [], 'col23': [], 'col24': []})
    df.columns = ["team_id", "game_date", "team_name", "game_number", "home", "away", "opponent", "win", "loss", "runs", "doubles", "triples", "home_runs", "strike_outs", "base_on_balls", "hits", "average", "at_bats", "on_base_percentage", "slugging", "on_base_plus_slugging", "stolen_bases", "runs_batted_in", "left_on_base"]

    #Create empty lists for home and away Batting
    awayTeamBattingList = []
    homeTeamBattingList = []

    #Collect away Batting data points and add it to the list
    awayTeamBattingObj.team_id = gameData["away"]["team"]["id"]
    awayTeamBattingList.append(awayTeamBattingObj.team_id)

    awayTeamBattingObj.game_date = gameDate
    awayTeamBattingList.append(awayTeamBattingObj.game_date)

    awayTeamBattingObj.team_name = gameData["teamInfo"]["away"]["teamName"]
    awayTeamBattingList.append(awayTeamBattingObj.team_name)

    awayTeamBattingObj.game_number = 1
    awayTeamBattingList.append(awayTeamBattingObj.game_number)

    awayTeamBattingObj.away = 1
    awayTeamBattingList.append(awayTeamBattingObj.home)
    awayTeamBattingList.append(awayTeamBattingObj.away)

    awayTeamBattingObj.opponent = gameData["teamInfo"]["home"]["teamName"]
    awayTeamBattingList.append(awayTeamBattingObj.opponent)

    homeRuns = gameData["away"]["teamStats"]["pitching"]["runs"]
    awayRuns = gameData["away"]["teamStats"]["batting"]["runs"]
    GetWinLoss(homeRuns, awayRuns, awayTeamBattingObj)
    awayTeamBattingList.append(awayTeamBattingObj.win)
    awayTeamBattingList.append(awayTeamBattingObj.loss)

    awayTeamBattingObj.runs = awayRuns
    awayTeamBattingList.append(awayTeamBattingObj.runs)

    awayTeamBattingObj.doubles = gameData["away"]["teamStats"]["batting"]["doubles"]
    awayTeamBattingList.append(awayTeamBattingObj.doubles)

    awayTeamBattingObj.triples = gameData["away"]["teamStats"]["batting"]["triples"]
    awayTeamBattingList.append(awayTeamBattingObj.triples)

    awayTeamBattingObj.home_runs = gameData["away"]["teamStats"]["batting"]["homeRuns"]
    awayTeamBattingList.append(awayTeamBattingObj.home_runs)

    awayTeamBattingObj.strike_outs = gameData["away"]["teamStats"]["batting"]["strikeOuts"]
    awayTeamBattingList.append(awayTeamBattingObj.strike_outs)

    awayTeamBattingObj.base_on_balls = gameData["away"]["teamStats"]["batting"]["baseOnBalls"]
    awayTeamBattingList.append(awayTeamBattingObj.base_on_balls)

    awayTeamBattingObj.hits = gameData["away"]["teamStats"]["batting"]["hits"]
    awayTeamBattingList.append(awayTeamBattingObj.hits)

    awayTeamBattingObj.average = gameData["away"]["teamStats"]["batting"]["avg"]
    awayTeamBattingList.append(awayTeamBattingObj.average)

    awayTeamBattingObj.at_bats = gameData["away"]["teamStats"]["batting"]["atBats"]
    awayTeamBattingList.append(awayTeamBattingObj.at_bats)

    awayTeamBattingObj.on_base_percentage = gameData["away"]["teamStats"]["batting"]["obp"]
    awayTeamBattingList.append(awayTeamBattingObj.on_base_percentage)

    awayTeamBattingObj.slugging = gameData["away"]["teamStats"]["batting"]["slg"]
    awayTeamBattingList.append(awayTeamBattingObj.slugging)

    awayTeamBattingObj.on_base_plus_slugging = gameData["away"]["teamStats"]["batting"]["ops"]
    awayTeamBattingList.append(awayTeamBattingObj.on_base_plus_slugging)

    awayTeamBattingObj.stolen_bases = gameData["away"]["teamStats"]["batting"]["stolenBases"]
    awayTeamBattingList.append(awayTeamBattingObj.stolen_bases)

    awayTeamBattingObj.runs_batted_in = gameData["away"]["teamStats"]["batting"]["rbi"]
    awayTeamBattingList.append(awayTeamBattingObj.runs_batted_in)

    awayTeamBattingObj.left_on_base = gameData["away"]["teamStats"]["batting"]["leftOnBase"]
    awayTeamBattingList.append(awayTeamBattingObj.left_on_base)

    #Add the list to the end of the dataframe
    df.loc[len(df)] = awayTeamBattingList

    #Collect home batting data points and add it to the list
    homeTeamBattingObj.team_id = gameData["home"]["team"]["id"]
    homeTeamBattingList.append(homeTeamBattingObj.team_id)

    homeTeamBattingObj.game_date = gameDate
    homeTeamBattingList.append(homeTeamBattingObj.game_date)

    homeTeamBattingObj.team_name = gameData["teamInfo"]["home"]["teamName"]
    homeTeamBattingList.append(homeTeamBattingObj.team_name)

    homeTeamBattingObj.game_number = 1
    homeTeamBattingList.append(awayTeamBattingObj.game_number)

    homeTeamBattingObj.home = 1
    homeTeamBattingList.append(homeTeamBattingObj.home)
    homeTeamBattingList.append(homeTeamBattingObj.away)

    homeTeamBattingObj.opponent = gameData["teamInfo"]["away"]["teamName"]
    homeTeamBattingList.append(homeTeamBattingObj.opponent)

    GetWinLoss(homeRuns, awayRuns, homeTeamBattingObj)
    homeTeamBattingList.append(homeTeamBattingObj.win)
    homeTeamBattingList.append(homeTeamBattingObj.loss)

    homeTeamBattingObj.runs = gameData["home"]["teamStats"]["batting"]["runs"]
    homeTeamBattingList.append(homeTeamBattingObj.runs)

    homeTeamBattingObj.doubles = gameData["home"]["teamStats"]["batting"]["doubles"]
    homeTeamBattingList.append(homeTeamBattingObj.doubles)

    homeTeamBattingObj.triples = gameData["home"]["teamStats"]["batting"]["triples"]
    homeTeamBattingList.append(homeTeamBattingObj.triples)

    homeTeamBattingObj.home_runs = gameData["home"]["teamStats"]["batting"]["homeRuns"]
    homeTeamBattingList.append(homeTeamBattingObj.home_runs)

    homeTeamBattingObj.strike_outs = gameData["home"]["teamStats"]["batting"]["strikeOuts"]
    homeTeamBattingList.append(homeTeamBattingObj.strike_outs)

    homeTeamBattingObj.base_on_balls = gameData["home"]["teamStats"]["batting"]["baseOnBalls"]
    homeTeamBattingList.append(homeTeamBattingObj.base_on_balls)

    homeTeamBattingObj.hits = gameData["home"]["teamStats"]["batting"]["hits"]
    homeTeamBattingList.append(homeTeamBattingObj.hits)

    homeTeamBattingObj.average = gameData["home"]["teamStats"]["batting"]["avg"]
    homeTeamBattingList.append(homeTeamBattingObj.average)

    homeTeamBattingObj.at_bats = gameData["home"]["teamStats"]["batting"]["atBats"]
    homeTeamBattingList.append(homeTeamBattingObj.at_bats)

    homeTeamBattingObj.on_base_percentage = gameData["home"]["teamStats"]["batting"]["obp"]
    homeTeamBattingList.append(homeTeamBattingObj.on_base_percentage)

    homeTeamBattingObj.slugging = gameData["home"]["teamStats"]["batting"]["slg"]
    homeTeamBattingList.append(homeTeamBattingObj.slugging)

    homeTeamBattingObj.on_base_plus_slugging = gameData["home"]["teamStats"]["batting"]["ops"]
    homeTeamBattingList.append(homeTeamBattingObj.on_base_plus_slugging)

    homeTeamBattingObj.stolen_bases = gameData["home"]["teamStats"]["batting"]["stolenBases"]
    homeTeamBattingList.append(homeTeamBattingObj.stolen_bases)

    homeTeamBattingObj.runs_batted_in = gameData["home"]["teamStats"]["batting"]["rbi"]
    homeTeamBattingList.append(homeTeamBattingObj.runs_batted_in)

    homeTeamBattingObj.left_on_base = gameData["home"]["teamStats"]["batting"]["leftOnBase"]
    homeTeamBattingList.append(homeTeamBattingObj.left_on_base)

    #Add list to the end of the dataframe
    df.loc[len(df)] = homeTeamBattingList
    
    #Return the dataframe
    return df