class Participants():
    def __init__(self, name ):
        self.name = name
        self.points = 0
        self.choice = ""

    def toNumericalChoice(self):
        swticher = {
            "rock": 0,
            "paper": 1,
            "scissor" : 2,
            "lizard": 3,
            "spock": 4

        }
        return swticher[self.choice]
    
    def choose(self):
        self.choice = input("{name}, select rock, paper, scissors, liizard or spock: ".format(name = self.name))
        print("{name} selects {choice}".format(name = self.name, choice =self.choice))
    
    def incrementPoint(self):
        self.points += 1

class GameRound():
    def __init__(self, p1, p2):
        self.rules = [
            [0, -1, 1, 1,-1,],
            [1, 0, -1, -1, 1],
            [-1, 1, 0, 1, -1],
            [-1, 1, -1, 0, 1],
            [1, -1, 1, -1, 0]
        ]

        p1.choose()
        p2.choose()
        result = self.compareChoices(p1, p2)
        print("Round resulted in a {result}".format(result = self.getResultAsString(result)))

        if result > 0:
            p1.incremenPoint()
        elif result < 0:
            p2.incrementPoint()    


    def compareChoices(self, p1, p2):
        return self.rules[p1.toNumericalChoice()][p2.toNumericalChoice()]
    
    def getResultAsString(self, result):
        res = {
            0: "draw",
            1: "win",
            -1: "loss"
        }
        return res[result]
    
    def awardPoint(self):
        print("implement")

class Game():
    def __init__(self):
        self.endgame = False
        self.participants = Participants("you")
        self.secondparticipant = Participants("Marvel")

    def start(self):
        game_round = GameRound(self.participants, self.secondparticipant)

    def checkEndConition(self):
        answer = input("conitnue game yes / no: ")
        if answer == "yes":
            GameRound(self.participants, self.secondparticipant)
            self.checkEndConition()
        else:
            print("Game ended, {p1name} has {p1points}, and {p2name} has {p2points}".format(p1name =self.participants.name,p1points = self.participants.points, p2name = self.secondparticipant.name, p2points = self.secondparticipant.points))
            self.determinewinner()
            self.endgame == True
            

    def start(self):
        while not self.endgame:
            GameRound(self.participants, self.secondparticipant)
            self.checkEndConition()

    def determinewinner(self):
        resultString = "It's a draw"
        if self.participants.points > self.secondparticipant.points:
            resultString = "Winner is {name}".format(name = self.participants.name)
        elif self.participants.points < self.secondparticipant.points:
            resultString = "Winner is {name}".format(name = self.secondparticipant.name)
        print(resultString)


game = Game()
game.start()          