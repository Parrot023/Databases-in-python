#Database administration program
class Highscore(object):

    def __init__(self, game, score):

        self.game = game
        self.score = score

a = Highscore("Snake", 20)

print(a.game)
