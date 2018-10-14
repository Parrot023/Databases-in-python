#Database administration program

from modules import DB

#Highscore object
class Highscore(object):

    def __init__(self, _game, _score, _player_name):

        #defining variables needed by this object
        self.game = _game
        self.score = _score
        self.player_name = _player_name


#This function takes input from the user an stores it in the 3 variables defined at the top
def New_Highscore():

    #global is needed to tell python that we are workin with global variables
    global game, score, player_name, a

    #raw_input is a way to take text format inputs from the user.
    #with the normal input function you only get integers
    game = raw_input("Which game do you want to set a highscore for? ")
    score = input("How many points did the player get? ")
    player_name = raw_input("what is the player called? ")

    #Creates a new highscore object
    a = Highscore(game, score, player_name)

#runs function New_Highscore
New_Highscore()
#DB.create_table()
DB.dynamic_data_entry(a.game, a.score, a.player_name)

#prints the name of the player who entered his or her highscore
print("the player who wrote their score is called " + a.player_name)
