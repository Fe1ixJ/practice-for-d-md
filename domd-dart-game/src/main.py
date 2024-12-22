from game.player import Player
from game.opponent import Opponent
from utils.constants import *

## Fix error with opponent score thing
## Fix ending on double error not working
## fix player busting on when hitting double that should end the game


def parse_score(score_input):
    """Parse score input and return numerical value"""
    score_input = score_input.upper().strip()
    
    # Handle special case for bulls
    if score_input in ['25', 'BULL']:
        return 25
    if score_input in ['50', 'DBULL']:
        return 50
    
    # Handle triples (T1-T20)
    if score_input.startswith('T'):
        try:
            number = int(score_input[1:])
            if 1 <= number <= 20:
                return globals()[f'T{number}']
        except ValueError:
            return None
            
    # Handle doubles (D1-D20)
    if score_input.startswith('D'):
        try:
            number = int(score_input[1:])
            if 1 <= number <= 20:
                return globals()[f'D{number}']
        except ValueError:
            return None
            
    # Handle regular numbers
    try:
        number = int(score_input)
        if 0 <= number <= 20:
            return number
    except ValueError:
        return None
        
    return None

def play_round(player, opponent):
    throws = 0
    while throws < 3:
        score_input = input(f"Throw {throws + 1}/3 - Enter your score (remaining: {player.score}) (or 'exit' to quit): ")
        if score_input.lower() == 'exit':
            return False
        
        score = parse_score(score_input)
        if score is None:
            print("Invalid score. Use format: number (0-20), T1-T20, D1-D20, 25 (bull), or 50 (double bull)")
            continue
            
        if score > 60:
            print("Invalid score. Maximum possible score is 60 (T20)")
            continue

        # Remind about double finish when score is getting low
        if player.score <= 60:
            print("Remember to finish on a double or bull!")
            
        if player.sub_score(score):  # Returns True if busted
            break
            
        if player.is_winner():
            return False  # End game if player wins
            
        throws += 1

    if not player.is_winner():
        opponent_score = opponent.generate_score()
        if opponent_score > opponent.score:
            print(f"Opponent busted with {opponent_score}")
        else:
            opponent.sub_score(opponent_score)
            print(f"Opponent scored: {opponent_score}")
            print(f"Opponent's remaining score: {opponent.score}")
            
            if opponent.is_winner():
                return False
        
        if player.busted:
            player.reset_bust()
            print(f"{player.name} remains on {player.score} points.")
    
    return True

def main():
    print("Welcome to Dömd!")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    while True:
        try:
            level = int(input("Choose opponent level (1-3): "))
            if 1 <= level <= 3:
                break
            print("Please enter 1, 2, or 3")
        except ValueError:
            print("Invalid input")
    
    opponent = Opponent(level)
    game_running = True
    
    while game_running:
        if not play_round(player, opponent):
            break
        
        if player.is_winner():
            print(f"Congratulations {player_name}! You won!")
            game_running = False
        elif opponent.is_winner():
            print("Opponent wins!")
            game_running = False

if __name__ == "__main__":
    main()