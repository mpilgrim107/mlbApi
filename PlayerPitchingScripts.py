from Connection import GetConnection 

#This function will take a dataframe of PlayerPitching data points and add it to the player.pitching table in the database
def AddPlayerPitchingToDatabase(df):
        
   #convert the dataframe into a list of tuples    
   records = df.to_records(index=False)
   result = list(records)

   conn = GetConnection()

   mycursor = conn.cursor()

   #Script to insert the player pitching data points into the player.pitching table of the database
   sql = """INSERT INTO player.pitching
               (player_id, team_id, game_date, full_name, home, away, opponent, runs, doubles, triples, home_runs, strike_outs, base_on_balls, hits, at_bats, stolen_bases, innings_pitched, wins, losses, holds, blown_saves)
            VALUES
               (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

   mycursor.executemany(sql, result)
   conn.commit()

   print(mycursor.rowcount, "rows were inserted successfully. AddPlayerPitchingToDatabase()")