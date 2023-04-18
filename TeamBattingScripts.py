from Connection import GetConnection 

#This function will take a dataframe of TeamBatting data and add it to the team.batting table of the database
def AddTeamBattingToDatabase(df):
        
    records = df.to_records(index=False)
    result = list(records)

    conn = GetConnection()

    mycursor = conn.cursor()

    #Script to insert the data into the team.batting table of the database
    sql = """INSERT INTO team.batting
                (team_id, game_date, team_name, game_number, home, away, opponent, win, loss, runs, doubles, triples, home_runs, strike_outs, base_on_balls, hits, average, at_bats, on_base_percentage, slugging, on_base_plus_slugging, stolen_bases, runs_batted_in, left_on_base)
             VALUES 
                (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

    mycursor.executemany(sql, result)
    conn.commit()

    print(mycursor.rowcount, "rows were inserted successfully. AddTeamBattingToDatabase()")