import statsapi 
import pandas as pd
from PlayerInfoScripts import GetTeamIds, InsertPlayersIntoDatabase

#Create a Player class for storing all of the information on a single player
class Player:
    def __init__(self):
        self.id = 0
        self.fullName = " "
        self.firstName = " "
        self.lastName = " "
        self.primaryNumber = " "
        self.currentTeam = " "
        self.teamId = 0
        self.initLastName = " "
        self.position = " " 

def GetPlayerInfo():
    #Get list of 'id' values from the database
    teamIds = GetTeamIds()

    #Create empty list
    teamIdsList = []

    #Add each teamId to the list
    for teamId in teamIds:
        teamIdsList.append(teamId[0])

    #iterate through all teams through 'id'
    for teamId in teamIdsList:
        
        #Create empty DataFrame to add the player values to
        df = pd.DataFrame({'col1': [], 'col2': [], 'col3': [], 'col4': [], 'col5': [], 'col6': [], 'col7': [], 'col8': [], 'col9': []})
        df.columns = ["player_id", "full_name", "first_name", "last_name", "init_last_name", "player_number", "player_position", "team_id", "team_name"]

        #Look up the roster according to the teamId
        playerTeamName = pd.DataFrame(statsapi.lookup_team(teamId)).loc[0, "teamName"]

        #Get a DataFrame of the players on a certain Team
        players = pd.DataFrame(statsapi.lookup_player(teamId))
        p = Player()

        #Variables to use for iterating through all of the players
        counter = 0
        for i in range(len(players)):
            #Create Empty list to add the data that is going to the DataFrame per player
            playerDataList = []

            #Get teamId associated with player and check it matches the id of the team in the for loop
            p.teamId = str(players.loc[i, 'currentTeam']['id'])
            if p.teamId != str(teamId):
                continue

            #Assign the values to the Player Class and append it to the playerDataList
            p.id = str(players.loc[i, "id"])
            playerDataList.append(p.id)

            p.fullName = players.loc[i, "fullName"]
            playerDataList.append(p.fullName)

            p.firstName = players.loc[i, "firstName"]
            playerDataList.append(p.firstName)

            p.lastName = players.loc[i, "lastName"]
            playerDataList.append(p.lastName)

            p.initLastName = players.loc[i, 'initLastName']
            playerDataList.append(p.initLastName)

            p.primaryNumber = players.loc[i, 'primaryNumber']
            playerDataList.append(p.primaryNumber)

            p.position = players.loc[i, 'primaryPosition']['abbreviation']
            playerDataList.append(p.position)

            playerDataList.append(p.teamId)

            p.currentTeam = str(playerTeamName)
            playerDataList.append(p.currentTeam)

            #Add the list to the end of the dataframe and increment the counter
            df.loc[len(df)] = playerDataList
            counter = counter + 1

        #Convert the dataframe into a list of tuples
        records = df.to_records(index=False)
        result = list(records)
        
        #Insert the player data into the player.playerinfo table of the database
        InsertPlayersIntoDatabase(result)