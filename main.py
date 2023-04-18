##########  Function is meant to be run in the morning after the games the previous night have been played #########

from datetime import date, timedelta 
import pandas as pd

import Pregame
import PregameScripts

import TeamBatting
import TeamBattingScripts

import TeamPitching
import TeamPitchingScripts

import TeamInfo
import TeamInfoScripts

import PlayerBatting
import PlayerBattingScripts

import PlayerPitching
import PlayerPitchingScripts


today = date.today()
yesterday = today - timedelta(days= 1)

#Collect set of game_id's from database of the previous night(Pregame.py)
print("\n##### Collecting GameIds for games played last night... #####")
gameIds = PregameScripts.GetGameIds()
print("GameIds List: {} \n".format(gameIds))

#Collect Team Data from the Games of the previous night using list of game_id's
print("##### Collecting TeamBatting info... #####\n")
#Collect Team Batting data and add it to the Database

dfBatting = pd.DataFrame({'col1': [], 'col2': [], 'col3': [], 'col4': [], 'col5': [], 'col6': [], 'col7': [], 'col8': [], 'col9': [], 'col10': [], 'col11': [], 'col12': [], 'col13': [], 'col14': [], 'col15': [], 'col16': [], 'col17': [], 'col18': [], 'col19': [], 'col20': [], 'col21': [], 'col22': [], 'col23': [], 'col24': []})
dfBatting.columns = ["team_id", "game_date", "team_name", "game_number", "home", "away", "opponent", "win", "loss", "runs", "doubles", "triples", "home_runs", "strike_outs", "base_on_balls", "hits", "average", "at_bats", "on_base_percentage", "slugging", "on_base_plus_slugging", "stolen_bases", "runs_batted_in", "left_on_base"]

for gameId in gameIds:
    print("Updating game for gameId: {}".format(gameId))
    awayTeamBatting = TeamBatting.TeamBatting()
    homeTeamBatting = TeamBatting.TeamBatting()

    #This function will also update the home_wins, home_games, away_wins, away_games in the team.teaminfo table
    gamesBattingStats = TeamBatting.GatherGameBattingStats(awayTeamBatting, homeTeamBatting, gameId, yesterday)
    dfBatting = dfBatting.append(gamesBattingStats)

    del awayTeamBatting
    del homeTeamBatting
    del gamesBattingStats

#Add the dfBatting dataframe to the team.batting table in the database
TeamBattingScripts.AddTeamBattingToDatabase(dfBatting)
del dfBatting

print("\n##### Collecting TeamPitching info... #####\n")
#Collect Team Pitching data and add it to the Database

dfPitching = pd.DataFrame({'col1': [], 'col2': [], 'col3': [], 'col4': [], 'col5': [], 'col6': [], 'col7': [], 'col8': [], 'col9': [], 'col10': [], 'col11': [], 'col12': [], 'col13': [], 'col14': [], 'col15': [], 'col16': [], 'col17': [], 'col18': [], 'col19': [], 'col20': [], 'col21': [], 'col22': [], 'col23': [], 'col24': []})
dfPitching.columns = ["team_id", "game_date", "team_name", "game_number", "home", "away", "opponent", "win", "loss", "runs", "doubles", "triples", "home_runs", "strike_outs", "base_on_balls", "hits", "at_bats", "on_base_percentage", "stolen_bases", "era", "earned_runs", "pitches_thrown", "strikes", "rbi"]


for gameId in gameIds:
    print("Updating game for gameId: {}".format(gameId))

    #Create TeamPitching objects for the home and away teams
    awayTeamPitching = TeamPitching.TeamPitching()
    homeTeamPitching = TeamPitching.TeamPitching()

    gamePitchingStatsDataFrame = TeamPitching.GatherGamePitchingStats(awayTeamPitching, homeTeamPitching, gameId, yesterday)
    dfPitching = dfPitching.append(gamePitchingStatsDataFrame)

    del awayTeamPitching
    del homeTeamPitching
    del gamePitchingStatsDataFrame


#Add the dfPitching dataframe to the team.pitching table in the database
TeamPitchingScripts.AddTeamPitchingToDatabase(dfPitching)
del dfPitching

print("##### Updating Team Ranks and Wins/Losses #####")
#Update the Team.teaminfo table of the database (division_rank, league_rank, wins, losses)
divisionIdsList = TeamInfoScripts.GetDivisionIds()
teamInfo = TeamInfo.GatherUpdatedTeamInfo(divisionIdsList)
TeamInfoScripts.AddTeamInfoToDatabase(teamInfo)

del divisionIdsList
del teamInfo

#Collect Player Data from the Games of the previous night
print("##### Collecting PlayerBatting info... #####\n")

#Collect Player Batting data and add it to the Database
for gameId in gameIds:
    
    #Create PlayerBatting objects for the home and away team of the game
    awayPlayerBatting = PlayerBatting.PlayerBatting()
    homePlayerBatting = PlayerBatting.PlayerBatting()

    #Gather Batting Stats for all players and assign a dataframe to it
    gameBattingStatsDataFrame = PlayerBatting.GatherPlayerBattingStats(awayPlayerBatting, homePlayerBatting, gameId, yesterday)

    #Add the PlayerBatting dataframe to the player.batting table in the database
    PlayerBattingScripts.AddPlayerBattingToDatabase(gameBattingStatsDataFrame)

    del awayPlayerBatting
    del homePlayerBatting
    del gameBattingStatsDataFrame


print("##### Collecting PlayerPitching info... #####\n")
#Collect Player Pitching data and add it to the Database
for gameId in gameIds:

    #Create PlayerPitching objects for the home and away team of the game
    awayPlayerPitching = PlayerPitching.PlayerPitching()
    homePlayerPitching = PlayerPitching.PlayerPitching()

    #Gather Pitching Stats for all players and assign a dataframe to it
    gamePitchingStatsDataFrame = PlayerPitching.GatherPlayerPitchingStats(awayPlayerPitching, homePlayerPitching, gameId, yesterday)

    #Add the PlayerPitching dataframe to the player.pitching table in the database
    PlayerPitchingScripts.AddPlayerPitchingToDatabase(gamePitchingStatsDataFrame)

    del awayPlayerPitching
    del homePlayerPitching
    del gamePitchingStatsDataFrame

print("##### Clearing Pregames from the Database #####")
#Delete Pregame data for the games of the previous night
PregameScripts.ClearPregamesFromDatabase()

print("##### Adding Pregames For Today #####")
#Collect Pregame data for the games of the day and add it to the database
pregameInfoToday = Pregame.GetPregameInfo(today)
PregameScripts.AddPregamesToDatabase(pregameInfoToday)

del pregameInfoToday
del gameIds