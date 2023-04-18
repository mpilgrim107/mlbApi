import json 

import pandas as pd
import statsapi

from TeamInfoScripts import GetDivisionIds

#TeamInfo Class with initial values for each attribute
class TeamInfo:
    def __init__(self):
        self.team_id = 0
        self.division_rank = " "
        self.league_rank = " "
        self.wins = 0
        self.losses = 0
        self.games_back = 0.0

def GatherUpdatedTeamInfo(divisionIdsList):

    #Create empty dataframe with column values
    df = pd.DataFrame({'col1': [], 'col2': [], 'col3': [], 'col4': [], 'col5': [], 'col6': []})
    df.columns = ["division_rank", "league_rank", "wins", "losses", "games_back", "team_id"]

    #Get updated standings for each team
    standings = statsapi.standings_data(leagueId="103,104", division="all", include_wildcard=True, season=None, standingsTypes=None, date=None)

    #Iterate through each division (6 total divisions)
    for divisionId in divisionIdsList:

        division = standings[divisionId]["teams"]
        teamsCounter = len(division)

        #iterate through each team in the division
        for team in range(teamsCounter):

            #Create empty list to add data into
            teamInfoList = []

            #Create TeamInfo object to assign data points to
            teamObj = TeamInfo()

            #Assign data points to the team and add it to the list
            teamObj.division_rank = str(division[team]["div_rank"])
            teamInfoList.append(teamObj.division_rank)

            teamObj.league_rank = str(division[team]["league_rank"])
            teamInfoList.append(teamObj.league_rank)

            teamObj.wins = int(division[team]["w"])
            teamInfoList.append(teamObj.wins)

            teamObj.losses = int(division[team]["l"])
            teamInfoList.append(teamObj.losses)

            teamObj.games_back = str(division[team]["gb"])
            teamInfoList.append(teamObj.games_back)

            teamObj.team_id = int(division[team]["team_id"])
            teamInfoList.append(teamObj.team_id)

            #Add the team data to the end of the dataframe
            df.loc[len(df)] = teamInfoList

    #Return the dataframe
    return df