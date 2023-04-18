import statsapi 
import pandas as pd

#TeamPitching class and initial values for each attribute
class TeamPitching:
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
        self.at_bats = " "
        self.on_base_percentage = 0
        self.stolen_bases = " "
        self.era = " "
        self.earned_runs = " "
        self.pitches_thrown = 0
        self.stikes = 0
        self.rbi = 0

"""
def GetGameNumber(TeamBattingObj):
    conn = GetConnection()
    mycursor = conn.cursor()

    sql = SELECT game_number
                FROM team.batting
                WHERE team_id = %s
                ORDER BY game_number DESC

    mycursor.execute(sql, [TeamBattingObj.team_id])
    print(mycursor.fetchone()[0])
    gameNumber = mycursor.fetchone()[0]
    
    if TeamBattingObj.game_number == 'None':
        TeamBattingObj.game_number = 1

    conn.commit()
    conn.close()
"""

#This function will determine a win or loss for the team passed into the function
def GetWinLoss(homeRuns, awayRuns, TeamPitchingObj):

    if homeRuns > awayRuns and TeamPitchingObj.home == 1:
        TeamPitchingObj.win = 1
    elif homeRuns < awayRuns and TeamPitchingObj.home == 1:
        TeamPitchingObj.loss = 1
    elif homeRuns > awayRuns and TeamPitchingObj.away == 1:
        TeamPitchingObj.loss = 1
    else:
        TeamPitchingObj.win = 1

def GatherGamePitchingStats(awayTeamPitchingObj, homeTeamPitchingObj, gamePk, gameDate):
    #collect game data given the gameId (gamePk)
    gameData = statsapi.boxscore_data(gamePk)

    #Create an empty dataframe and assign the column values
    df = pd.DataFrame({'col1': [], 'col2': [], 'col3': [], 'col4': [], 'col5': [], 'col6': [], 'col7': [], 'col8': [], 'col9': [], 'col10': [], 'col11': [], 'col12': [], 'col13': [], 'col14': [], 'col15': [], 'col16': [], 'col17': [], 'col18': [], 'col19': [], 'col20': [], 'col21': [], 'col22': [], 'col23': [], 'col24': []})
    df.columns = ["team_id", "game_date", "team_name", "game_number", "home", "away", "opponent", "win", "loss", "runs", "doubles", "triples", "home_runs", "strike_outs", "base_on_balls", "hits", "at_bats", "on_base_percentage", "stolen_bases", "era", "earned_runs", "pitches_thrown", "strikes", "rbi"]

    #Create empty TeamPitching lists for home and away teams
    awayTeamPitchingList = []
    homeTeamPitchingList = []

    #Collect awayTeamPitching data points and add it to the list
    awayTeamPitchingObj.team_id = gameData["away"]["team"]["id"]
    awayTeamPitchingList.append(awayTeamPitchingObj.team_id)

    awayTeamPitchingObj.game_date = gameDate
    awayTeamPitchingList.append(awayTeamPitchingObj.game_date)

    awayTeamPitchingObj.team_name = gameData["teamInfo"]["away"]["teamName"]
    awayTeamPitchingList.append(awayTeamPitchingObj.team_name)

    awayTeamPitchingObj.game_number = 1
    """GetGameNumber(awayTeamPitchingObj)
    if awayTeamPitchingObj.game_number == 'None':
        awayTeamPitchingObj.game_number = 1"""
    awayTeamPitchingList.append(awayTeamPitchingObj.game_number)

    awayTeamPitchingObj.away = 1
    awayTeamPitchingList.append(awayTeamPitchingObj.home)
    awayTeamPitchingList.append(awayTeamPitchingObj.away)

    awayTeamPitchingObj.opponent = gameData["teamInfo"]["home"]["teamName"]
    awayTeamPitchingList.append(awayTeamPitchingObj.opponent)

    homeRuns = gameData["away"]["teamStats"]["pitching"]["runs"]
    awayRuns = gameData["away"]["teamStats"]["batting"]["runs"]
    GetWinLoss(homeRuns, awayRuns, awayTeamPitchingObj)
    awayTeamPitchingList.append(awayTeamPitchingObj.win)
    awayTeamPitchingList.append(awayTeamPitchingObj.loss)

    awayTeamPitchingObj.runs = homeRuns
    awayTeamPitchingList.append(awayTeamPitchingObj.runs)

    awayTeamPitchingObj.doubles = gameData["away"]["teamStats"]["pitching"]["doubles"]
    awayTeamPitchingList.append(awayTeamPitchingObj.doubles)

    awayTeamPitchingObj.triples = gameData["away"]["teamStats"]["pitching"]["triples"]
    awayTeamPitchingList.append(awayTeamPitchingObj.triples)

    awayTeamPitchingObj.home_runs = gameData["away"]["teamStats"]["pitching"]["homeRuns"]
    awayTeamPitchingList.append(awayTeamPitchingObj.home_runs)

    awayTeamPitchingObj.strike_outs = gameData["away"]["teamStats"]["pitching"]["strikeOuts"]
    awayTeamPitchingList.append(awayTeamPitchingObj.strike_outs)

    awayTeamPitchingObj.base_on_balls = gameData["away"]["teamStats"]["pitching"]["baseOnBalls"]
    awayTeamPitchingList.append(awayTeamPitchingObj.base_on_balls)

    awayTeamPitchingObj.hits = gameData["away"]["teamStats"]["pitching"]["hits"]
    awayTeamPitchingList.append(awayTeamPitchingObj.hits)

    awayTeamPitchingObj.at_bats = gameData["away"]["teamStats"]["pitching"]["atBats"]
    awayTeamPitchingList.append(awayTeamPitchingObj.at_bats)

    awayTeamPitchingObj.on_base_percentage = gameData["away"]["teamStats"]["pitching"]["obp"]
    awayTeamPitchingList.append(awayTeamPitchingObj.on_base_percentage)

    awayTeamPitchingObj.stolen_bases = gameData["away"]["teamStats"]["pitching"]["stolenBases"]
    awayTeamPitchingList.append(awayTeamPitchingObj.stolen_bases)

    awayTeamPitchingObj.era = gameData["away"]["teamStats"]["pitching"]["era"]
    awayTeamPitchingList.append(awayTeamPitchingObj.era)

    awayTeamPitchingObj.earned_runs = gameData["away"]["teamStats"]["pitching"]["earnedRuns"]
    awayTeamPitchingList.append(awayTeamPitchingObj.earned_runs)

    awayTeamPitchingObj.pitches_thrown = gameData["away"]["teamStats"]["pitching"]["numberOfPitches"]
    awayTeamPitchingList.append(awayTeamPitchingObj.pitches_thrown)

    awayTeamPitchingObj.strikes = gameData["away"]["teamStats"]["pitching"]["strikes"]
    awayTeamPitchingList.append(awayTeamPitchingObj.strikes) 

    awayTeamPitchingObj.rbi = gameData["away"]["teamStats"]["pitching"]["rbi"]
    awayTeamPitchingList.append(awayTeamPitchingObj.rbi)

    #Add the list to the end of the dataframe
    df.loc[len(df)] = awayTeamPitchingList

    #Collect homeTeamPitching data points and add it to the list
    homeTeamPitchingObj.team_id = gameData["home"]["team"]["id"]
    homeTeamPitchingList.append(homeTeamPitchingObj.team_id)

    homeTeamPitchingObj.game_date = gameDate
    homeTeamPitchingList.append(homeTeamPitchingObj.game_date)

    homeTeamPitchingObj.team_name = gameData["teamInfo"]["home"]["teamName"]
    homeTeamPitchingList.append(homeTeamPitchingObj.team_name)

    homeTeamPitchingObj.game_number = 1
    """GetGameNumber(homeTeamPitchingObj)
    if homeTeamPitchingObj.game_number == 'None':
        homeTeamPitchingObj.game_number = 1"""
    homeTeamPitchingList.append(homeTeamPitchingObj.game_number)

    homeTeamPitchingObj.home = 1
    homeTeamPitchingList.append(homeTeamPitchingObj.home)
    homeTeamPitchingList.append(homeTeamPitchingObj.away)

    homeTeamPitchingObj.opponent = gameData["teamInfo"]["away"]["teamName"]
    homeTeamPitchingList.append(homeTeamPitchingObj.opponent)

    GetWinLoss(homeRuns, awayRuns, homeTeamPitchingObj)
    homeTeamPitchingList.append(homeTeamPitchingObj.win)
    homeTeamPitchingList.append(homeTeamPitchingObj.loss)

    homeTeamPitchingObj.runs = awayRuns
    homeTeamPitchingList.append(homeTeamPitchingObj.runs)

    homeTeamPitchingObj.doubles = gameData["home"]["teamStats"]["pitching"]["doubles"]
    homeTeamPitchingList.append(homeTeamPitchingObj.doubles)

    homeTeamPitchingObj.triples = gameData["home"]["teamStats"]["pitching"]["triples"]
    homeTeamPitchingList.append(homeTeamPitchingObj.triples)

    homeTeamPitchingObj.home_runs = gameData["home"]["teamStats"]["pitching"]["homeRuns"]
    homeTeamPitchingList.append(homeTeamPitchingObj.home_runs)

    homeTeamPitchingObj.strike_outs = gameData["home"]["teamStats"]["pitching"]["strikeOuts"]
    homeTeamPitchingList.append(homeTeamPitchingObj.strike_outs)

    homeTeamPitchingObj.base_on_balls = gameData["home"]["teamStats"]["pitching"]["baseOnBalls"]
    homeTeamPitchingList.append(homeTeamPitchingObj.base_on_balls)

    homeTeamPitchingObj.hits = gameData["home"]["teamStats"]["pitching"]["hits"]
    homeTeamPitchingList.append(homeTeamPitchingObj.hits)

    homeTeamPitchingObj.at_bats = gameData["home"]["teamStats"]["pitching"]["atBats"]
    homeTeamPitchingList.append(homeTeamPitchingObj.at_bats)

    homeTeamPitchingObj.on_base_percentage = gameData["home"]["teamStats"]["pitching"]["obp"]
    homeTeamPitchingList.append(homeTeamPitchingObj.on_base_percentage)

    homeTeamPitchingObj.stolen_bases = gameData["home"]["teamStats"]["pitching"]["stolenBases"]
    homeTeamPitchingList.append(homeTeamPitchingObj.stolen_bases)

    homeTeamPitchingObj.era = gameData["home"]["teamStats"]["pitching"]["era"]
    homeTeamPitchingList.append(homeTeamPitchingObj.era)

    homeTeamPitchingObj.earned_runs = gameData["home"]["teamStats"]["pitching"]["earnedRuns"]
    homeTeamPitchingList.append(homeTeamPitchingObj.earned_runs)

    homeTeamPitchingObj.pitches_thrown = gameData["home"]["teamStats"]["pitching"]["numberOfPitches"]
    homeTeamPitchingList.append(homeTeamPitchingObj.pitches_thrown)

    homeTeamPitchingObj.strikes = gameData["home"]["teamStats"]["pitching"]["strikes"]
    homeTeamPitchingList.append(homeTeamPitchingObj.strikes)

    homeTeamPitchingObj.rbi = gameData["home"]["teamStats"]["pitching"]["rbi"]
    homeTeamPitchingList.append(homeTeamPitchingObj.rbi)

    #Add the list to the end of the dataframe
    df.loc[len(df)] = homeTeamPitchingList
    
    #Return the dataframe
    return df