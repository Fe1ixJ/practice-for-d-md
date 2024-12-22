import random

class Opponent:
    def __init__(self, level):
        if level not in [1, 2, 3]:
            raise ValueError("Level must be 1, 2, or 3")
        self.level = level
        self.score = 301
        self.throw_history = []

    def _single_throw(self):
        accuracy = {
            1: {'hit': 0.4, 'double': 0.1, 'triple': 0.05},
            2: {'hit': 0.6, 'double': 0.2, 'triple': 0.15},
            3: {'hit': 0.8, 'double': 0.3, 'triple': 0.25}
        }
        
        if random.random() > accuracy[self.level]['hit']:
            return 0  # Miss
            
        # Special case for bull (25) and double bull (50)
        if random.random() < 0.1:  # 10% chance to aim for bull
            return 50 if random.random() < accuracy[self.level]['double'] else 25
            
        target = random.randint(1, 20)
        roll = random.random()
        
        if roll < accuracy[self.level]['triple']:
            return target * 3
        elif roll < accuracy[self.level]['double']:
            return target * 2
        return target

    def generate_score(self):
        turn_score = 0
        darts_thrown = 0
        
        while darts_thrown < 3:
            throw = self._single_throw()
            if self.score - (turn_score + throw) >= 0:
                turn_score += throw
                darts_thrown += 1
            
        self.score -= turn_score
        self.throw_history.append(turn_score)
        return turn_score

    def get_score(self):
        return self.score

    def reset(self):
        self.score = 301
        self.throw_history = []