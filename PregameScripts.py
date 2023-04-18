from Connection import GetConnection 

#This function will collect all game_id values and return them
def GetGameIds():

    conn = GetConnection()
    
    mycursor = conn.cursor()

    #Script to gather the gameIds from the game.pregame table
    sql = """SELECT game_id FROM game.pregame"""

    mycursor.execute(sql)
    gameIds = mycursor.fetchall()

    conn.commit()
    conn.close()

    gameIdsList = []

    #Since the gameIds come in tuples of just one element in each tuple, I added each gameId to a list to make it easier to iterate through
    for gameId in gameIds:
        gameIdsList.append(gameId[0])
    
    return gameIdsList

def AddPregamesToDatabase(df):

    #Convert the dataframe to a list of tuples    
    records = df.to_records(index=False)
    result = list(records)

    conn = GetConnection()

    mycursor = conn.cursor()

    #Script to insert the game data into the game.pregame table of the database
    sql = """INSERT INTO game.pregame 
                (game_id, game_date, away_id, away_name, away_prob_pitcher, away_pitcher_note, home_id, home_name, home_prob_pitcher, home_pitcher_note, venue_name)
             VALUES
                (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

    mycursor.executemany(sql, result)
    conn.commit()

    print(mycursor.rowcount, "rows were inserted successfully. AddPregamesToDatabase()")

    conn.close()

#This function will clear the game.pregame table before the new pregame data gets added
def ClearPregamesFromDatabase():
    conn = GetConnection()
    
    mycursor = conn.cursor()

    sql = """DELETE FROM game.pregame"""

    mycursor.execute(sql)

    conn.commit()
    conn.close()