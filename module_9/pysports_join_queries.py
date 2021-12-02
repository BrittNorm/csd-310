""" 
    Brittany Normandin for assignment module 9.2
    Class: CSD 310
    Title: pysports_join_queries.py
    Date: 12/01/2021
    Description: Test program for joining the player and team tables
    Used: Professor Krasso test program with some modifications
"""

""" import statements """
import mysql.connector
from mysql.connector import errorcode

""" database config object """
config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
    """ try/catch block for handling potential MySQL database errors """ 
    
    # connect to the pysports database 
    db = mysql.connector.connect(**config) 

    cursor = db.cursor()

    # inner join query 
    query = "SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id "
    cursor.execute(query)

    # get the results from the cursor object 
    players = cursor.fetchall()

    print("\n  -- DISPLAYING PLAYER RECORDS --")
    
    # iterate over the player data set and display the results 
    for x in players:
        print("Player ID: {} ".format(x[0]))
        print("First Name: {} ".format(x[1]))
        print("Last Name: {} ".format(x[2]))
        print("Team ID: {} ".format(x[3]))
        print("")

    input("\n\n  Press any key to continue... ")

except mysql.connector.Error as err:
    """ handle errors """ 

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    """ close the connection to MySQL """

    db.close()
