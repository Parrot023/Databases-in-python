import sqlite3

#Setting up the connection to the database
conn = sqlite3.connect('Highscores_database.db')
#Setting up the cursor
c = conn.cursor()

#Creates a table in the database
def create_table():
    #c.execute("CREATE TABLE IF NOT EXISTS table_name(colum1 TEXT, colum2 REAL, colum3 TEXT......)")
    c.execute("CREATE TABLE IF NOT EXISTS Highscores(Game TEXT, Score REAL, Player TEXT)")


def data_entry(Game, Score, Player):

    #inserts the data into the database
    c.execute("INSERT INTO Highscores (Game, Score, Player) VALUES (?, ?, ?)",(Game, Score, Player))

    #Commits/save the insertion to the database
    conn.commit()


def read(game):

    #selects rows in the database where game = game(given by the user)
    c.execute('SELECT * FROM Highscores WHERE Game = (?)', (game,))

    #fetching the data is like copying it to the variable data
    data = c.fetchall()

    #data is a 2D array
    #print(data[0][1])

    #returns the data
    return data


def update_DB(new_score, game):
    #dynamically updating data_entry. Note the "," after new score. the comma is needed by sglite
    #if you forget the "," sqlite will se the input as an integer.
    c.execute("UPDATE Highscores SET Score = ? WHERE Game = ?", (new_score, game))
    #commit/saves changes
    conn.commit()
    print("changed score where game = Snake")
