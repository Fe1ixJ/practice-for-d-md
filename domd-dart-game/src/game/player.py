class Player:
    def __init__(self, name):
        self.name = name
        self.score = 301
        self.busted = False
        self.winner = False
        
    def sub_score(self, points):
        """Subtract points from score. Returns True if busted."""
        new_score = self.score - points
        
        # Check win condition first with double finish
        if new_score == 0:
            if self._is_valid_finish(points):
                self.score = new_score
                self.winner = True
                print(f"GAME SHOT! {self.name} wins!")
                return False
            else:
                print("Bust! Must finish on a double!")
                self.busted = True
                return True
                
        # Then check bust conditions
        if new_score < 0 or new_score == 1:
            print("Bust! Score too low!")
            self.busted = True
            return True
            
        self.score = new_score
        print(f"{self.name} has {self.score} points remaining.")
        return False

    def _is_valid_finish(self, points):
        """Check if score is a valid finish (double or double bull)"""
        return points == 50 or (points % 2 == 0 and str(points).startswith('D'))
    
    def reset_bust(self):
        self.busted = False
        
    def is_winner(self):
        return self.winner