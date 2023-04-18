from Connection import GetConnection 

def AddPlayerBattingToDatabase(df):
   
   #Convert the dataframe into a list of tuples
   records = df.to_records(index=False)
   result = list(records)

   #Get Connection to the local Database
   conn = GetConnection()

   mycursor = conn.cursor()

   #Script to insert the values into the player.batting table
   sql = """INSERT INTO player.batting
                (player_id, team_id, game_date, full_name, runs, doubles, triples, home_runs, strike_outs, base_on_balls, hits, at_bats, stolen_bases, rbi, left_on_base)
             VALUES
                (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

   mycursor.executemany(sql, result)
   conn.commit()

   print(mycursor.rowcount, "rows were inserted successfully. AddPlayerBattingToDatabase()")