from Connection import GetConnection 
import psycopg2

#this function will gather the teamIds from the team.teaminfo table in the database
def GetTeamIds():  
    conn = GetConnection()
    conn.autocommit = True

    mycursor = conn.cursor()

    #Script to gather the teamIds from each team
    sql = '''SELECT team_id FROM team.teaminfo'''

    mycursor.execute(sql)
    teamIds = mycursor.fetchall()

    conn.commit()
    conn.close()

    #Return the teamIds list
    return teamIds

#This function will insert data into the player.playerinfo table of the database given the player data list
def InsertPlayersIntoDatabase(dataset):
    conn = GetConnection()

    mycursor = conn.cursor()

    #Script to insert playerinfo data into the database
    sql = """INSERT INTO player.playerinfo
                (player_id, full_name, first_name, last_name, init_last_name, player_number, player_position, team_id, team_name)
            VALUES 
                (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""

    mycursor.executemany(sql, dataset)
    conn.commit()

    print(mycursor.rowcount, "rows were inserted successfully. InsertPlayersIntoDatabase()")