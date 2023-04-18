from Connection import GetConnection 

#This function will collect each divisionId from the team.teaminfo table of the database
def GetDivisionIds():

    conn = GetConnection()
    
    mycursor = conn.cursor()

    #Script to return all division_id values from the team.teaminfo table
    sql = '''SELECT DISTINCT division_id FROM team.teaminfo'''

    mycursor.execute(sql)
    divisionIds = mycursor.fetchall()
    
    conn.commit()
    conn.close()

    divisionIdsList = []

    #The divisionIds are returned in a tuple of 1 value, so I just gathered those values into 1 complete list
    for divisionId in divisionIds:
        divisionIdsList.append(divisionId[0])
    
    return divisionIdsList

def AddTeamInfoToDatabase(df):

    #Convert the dataframe into a list of tuples
    records = df.to_records(index=False)
    result = list(records)

    conn = GetConnection()

    mycursor = conn.cursor()

    #Script to update values in the team.teaminfo table
    sql = """UPDATE team.teaminfo
            SET
                division_rank=%s,
                league_rank=%s,
                wins=%s,
                losses=%s,
                games_back=%s
            WHERE
                team_id=%s"""
    
    mycursor.executemany(sql, result)
    conn.commit()

    print(mycursor.rowcount, "rows were updated successfully. AddTeamInfoToDatabase()")

def UpdateHomeWinsGames(HomeTeamObj):
    
    conn = GetConnection()
    mycursor = conn.cursor()
    teamId = HomeTeamObj.team_id

    #Get the current number of home wins from the team.teaminfo table of the database
    sqlHomeWins = """SELECT home_wins FROM team.teaminfo WHERE team_id = %s"""
    mycursor.execute(sqlHomeWins, (teamId,))
    homeWins = mycursor.fetchone()[0]

    #Get the current number of home games from the team.teaminfo table of the database
    sqlHomeGames = """SELECT home_games FROM team.teaminfo WHERE team_id = %s"""
    mycursor.execute(sqlHomeGames, (teamId,))
    homeGames = mycursor.fetchone()[0]

    updateList = []

    #If the object passed in shows a win, add 1 to the homeWins and homeGames variables
    if HomeTeamObj.win == 1:
        homeWins = homeWins + 1
        homeGames = homeGames + 1

        updateList = [homeWins, homeGames, teamId]

        #Sript to update the home_wins and home_games values according to the team_id
        sqlUpdate = """UPDATE team.teaminfo
                       SET
                            home_wins = %s,
                            home_games = %s
                        WHERE
                            team_id = %s"""
        
        mycursor.executemany(sqlUpdate, (updateList,))
        conn.commit()
        conn.close()

        print("Home Wins/Games have been updated for ", HomeTeamObj.team_name)

    else:
        #This is for the case of a loss
        #Just update the homeGames number by 1
        homeGames = homeGames + 1

        updateList = [homeGames, teamId]

        #Script to update the home_games given the team_id
        sqlUpdate = """UPDATE team.teaminfo
                       SET
                            home_games = %s
                        WHERE
                            team_id = %s"""
        
        mycursor.executemany(sqlUpdate, (updateList,))
        conn.commit()
        conn.close()

        print("Home Games have been updated for ", HomeTeamObj.team_name)

def UpdateAwayWinsGames(AwayTeamObj):
    
    conn = GetConnection()
    mycursor = conn.cursor()
    teamId = AwayTeamObj.team_id

    #Script to collect the number of awayWins for the team passed into the function
    sqlAwayWins = """SELECT away_wins FROM team.teaminfo WHERE team_id = %s"""
    mycursor.execute(sqlAwayWins, (teamId,))
    awayWins = mycursor.fetchone()[0]

    #Script to collect the number of awayGames for the team passed into the function
    sqlAwayGames = """SELECT away_games FROM team.teaminfo WHERE team_id = %s"""
    mycursor.execute(sqlAwayGames, (teamId,))
    awayGames = mycursor.fetchone()[0]

    updateList = []

    #If the object passed in shows a win, update the wins and games for the team passed into the function
    if AwayTeamObj.win == 1:
        awayWins = awayWins + 1
        awayGames = awayGames + 1

        updateList = [awayWins, awayGames, teamId]

        #Script to update the away_wins and away_games given the team_id passed into the function
        sqlUpdate = """UPDATE team.teaminfo
                       SET
                            away_wins = %s,
                            away_games = %s
                        WHERE
                            team_id = %s"""
        
        mycursor.executemany(sqlUpdate, (updateList,))
        conn.commit()
        conn.close()

        print("Away Wins/Games have been updated for ", AwayTeamObj.team_name)
    else:

        #Case for when the object passed into the function shows a loss
        #Just update the awayGames value in the database
        awayGames = awayGames + 1

        updateList = [awayGames, teamId]

        #Script to update the away_games by 1 given the team_id
        sqlUpdate = """UPDATE team.teaminfo
                       SET
                            away_games = %s
                        WHERE
                            team_id = %s"""
        
        mycursor.executemany(sqlUpdate, (updateList,))
        conn.commit()
        conn.close()

        print("Away Games have been updated for ", AwayTeamObj.team_name)