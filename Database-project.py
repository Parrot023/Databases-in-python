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
#new object (highscore)
#DB.create_table()
#a = Create_Highscore()
# saves the object a to the database
#save_to_DB(a)
# loads a highscore from the database
#and creates an object
#a = load_from_DB("Andraes")
#updates a highscore in the database
#DB.update(30, "Andraes")
#deletes and highscore in the database
#DB.delete("Andraes")

#text user interface (i dont know if u can say that, but who cares)
def tui():

    print("Hi what du you want to do?")
    print("1: Add new highscore\n2: Check existing highscore\n3: Update existing highscore\n4: Delete existing highscore\n5: quit")

    #input from user
    user_input = input("")

    #5 different actions the user can choose
    #new highscore
    if user_input == 1:
        a = Create_Highscore()
        save_to_DB(a)

    #check existing highscore
    elif user_input == 2:
        game = raw_input("for which game do you want to check a highscore? ")
        a = load_from_DB(game)
        print("the highscore for the game " + str(game) + " is " + str(a.score))

    #updating existing score
    elif user_input == 3:
        score = input("what is the new score ")
        game = raw_input("in what game did the player get " + str(score))
        DB.update(score, game)

    #deleting existing score
    elif user_input == 4:
        game = raw_input("for which game do you want to delete a highscore? ")
        DB.delete(game)

    #quit
    elif user_input == 5:
        DB.close()
        exit()

    else:
        print("cant recognise user input (try again)")

DB.create_table()

while 1 == 1:

    tui()

    print("\n")



#print("i did my thing")
