class Player:
    def __init__(self, name):
        self.name = name
        self.score = 301
    
    def sub_score(self, score):
        new_score = self.score - score

        self.score = new_score
        print(f"{self.name} has {self.score} points left")