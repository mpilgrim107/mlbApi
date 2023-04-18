#The purpose of this function is to easily get information from the database for connection purposes
import psycopg2 

def GetConnection():
    conn = psycopg2.connect(database="MLB",
                        host="localhost",
                        user="postgres",
                        password="Longhorns10",
                        port="5432")
    
    return conn