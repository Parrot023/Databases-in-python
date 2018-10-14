import sqlite3

#Setting up the connection to the database
conn = sqlite3.connect('Highscores_database.db')
#Setting up the cursor
c = conn.cursor()

#Creates a table in the database
def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS Highscores(Game TEXT, Score REAL, Player TEXT)")


def dynamic_data_entry(Game, Score, Player):

    c.execute("INSERT INTO Highscores (Game, Score, Player) VALUES (?, ?, ?)",(Game, Score, Player))

    #Commits/save the insertion to the database
    conn.commit()
