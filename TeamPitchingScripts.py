from Connection import GetConnection 

def AddTeamPitchingToDatabase(df):
    
    #Convert the dataframe into a list of tuples
    records = df.to_records(index=False)
    result = list(records)

    conn = GetConnection()

    mycursor = conn.cursor()

    #Script to insert the TeamPitching data into the team.pitching table
    sql = """INSERT INTO team.pitching 
    (team_id, game_date, team_name, game_number, home, away, opponent, win, loss, runs, doubles, triples, home_runs, strike_outs, base_on_balls, hits, at_bats, on_base_percentage, stolen_bases, era, earned_runs, pitches_thrown, strikes, rbi)
    VALUES 
    (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

    mycursor.executemany(sql, result)
    conn.commit()

    print(mycursor.rowcount, "rows were inserted successfully. AddTeamPitchingToDatabase()")