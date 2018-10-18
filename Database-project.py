#Database administration program

from modules import DB

#DB is a selfmade module to insert, read and edit the Database

#Highscore object
class Highscore():

    def __init__(self, _game, _score, _player_name):

        #defining variables needed by this object
        self.game = _game
        self.score = _score
        self.player_name = _player_name


#This function takes input from the user and creates a highscore object from it
def Create_Highscore():

    #raw_input is a way to take text format inputs from the user.
    #with the normal input function you only get integers
    game = raw_input("Which game do you want to set a highscore for? ")
    score = input("How many points did the player get? ")
    player_name = raw_input("what is the player called? ")

    #returns the created object
    return Highscore(game, score, player_name)

#saves a given object to the Highscores database
def save_to_DB(object_name):
    DB.data_entry(object_name.game, object_name.score, object_name.player_name)

#loads a highscore from DB and creates a highscore object from it
def load_from_DB(game):
    #read the data about the game from the database
    data = DB.read(game)
    #creates a highscore object from it
    return Highscore(data[0][0], data[0][1], data[0][2])



#creates a table in the database if it doesnt exist
DB.create_table()
# new object (highscore)
# a = Create_Highscore()
# saves the object a to the database
# save_to_DB(a)
# loads a highscore from the database
a = load_from_DB("Andraes")
print(a.score)

#prints the name of the player who entered his or her highscore
print("i did my thing")
