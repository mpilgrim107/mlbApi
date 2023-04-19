## mlbApi

This program will gather MLB Stats from the 2023-24 season using the 'mlb-statsapi' package in Python.  

The 'AddTables.sql' file is a script to add all of the tables to the local database that has been set up.

Once the data has been collected, the data will then be stored in the local database using the 'psycopg2' Python package.

First, you will need to run the Pregame.py file in order to retrieve the games played on a certain date.  The date passed into the function will be the date in which all of the games are retrieved in that table in the database (game.pregame).

Once the pregame data has been added, you can run the main.py file in order to collect team and player data and add it to the database.
