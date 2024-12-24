import time
import random
from player import Player

last_dart_double = False

def main():
    print("Welcome to Dömd simulator!")
    player_name = input("Enter your name: ")
    AI_level = int(input("Enter AI level: (1-3) "))
    player = Player(player_name)
    AI_player = Player("Opponent")  # Simulating AI as another player
    AI_player.score = 301
    player.score = 301
    time.sleep(0.5)
    print("Did you win middling?")
    middling = input("y for Yes or n for No: ")

    player_turn = middling.lower() == "y"
    
    while player.score > 0 and AI_player.score > 0:
        if player_turn:
            print("\nYour turn!")
            play_round(player)
        else:
            print("\nOpponent's turn!")
            AI_turn(AI_level, AI_player)
        
        if check_game_over(player, AI_player):
            break

        player_turn = not player_turn  # Alternate turns

def parse_score(score_input):
    """Parse score input and return numerical value"""
    global last_dart_double  # Ensure global variable is updated
    score_input = score_input.upper().strip()
    
    if score_input in ['25', 'BULL']:
        return 25
    if score_input in ['50', 'DBULL']:
        return 50
    
    if score_input.startswith('T'):
        try:
            number = int(score_input[1:])
            if 1 <= number <= 20:
                return number * 3
        except ValueError:
            return None

    if score_input.startswith('D'):
        try:
            number = int(score_input[1:])
            if 1 <= number <= 20:
                last_dart_double = True
                return number * 2
        except ValueError:
            return None
    
    try:
        number = int(score_input)
        if 0 <= number <= 20:
            return number
    except ValueError:
        return None
        
    return None

def play_round(player):
    global last_dart_double
    throws = 0
    while throws < 3:
        last_dart_double = False
        remaining = player.score
        score_input = input(f"Throw {throws + 1}/3 - Enter your score: (remaining: {remaining}) (or 'exit' to quit): ")
        
        if score_input.lower() == 'exit':
            return
        
        score = parse_score(score_input)
        if score is None or score > 60 or score < 0:
            print("Invalid score: Please enter a valid score (e.g., 20, D10, T15)")
            continue

        player.sub_score(score)
        throws += 1
        
        if check_win(player, score):
            return  # End turn immediately on win or bust

def check_win(player, score):
    global last_dart_double
    if player.score == 0:
        if last_dart_double:
            print(f"{player.name} won!")
            return True  # End turn
        else:
            print(f"{player.name} busted!")
            busted(player, score)
            return True  # End turn
    elif player.score == 1 or player.score < 0:
        print(f"{player.name} busted!")
        busted(player, score)
        return True  # End turn
    return False

def busted(player, score):
    player.score += score
    print(f"{player.name}'s score reverted to {player.score} due to bust!")

def AI_turn(AI_level, AI_player):
    stats = [
        [0.9, 70, 10, 15, 2, 3, 0.3],  # Level 1
        [0.95, 50, 20, 20, 5, 5, 0.4], # Level 2
        [0.99, 30, 22, 33, 10, 5, 0.5] # Level 3
    ][AI_level - 1]
    
    throws = 0
    while throws < 3:
        # Check if AI needs a final double to win
        if AI_player.score % 2 == 0 and AI_player.score <= 40 or AI_player.score == 50:
            if random.random() < stats[6]:  # Probability of hitting the final double
                print(f"Opponent hits the final double {AI_player.score} and wins!")
                AI_player.score = 0
                return
            else:
                print(f"Opponent misses the final double {AI_player.score}.")
        
        # Regular AI throw logic
        throw = random.randint(1, 20)
        if random.random() < stats[0]:
            throw = throw
        else:
            throw = 0

        special_throw = random.uniform(0, 100)
        if special_throw < stats[1]:
            throw = throw
        elif special_throw < stats[1] + stats[2]:
            throw *= 2
        elif special_throw < stats[1] + stats[2] + stats[3]:
            throw *= 3
        elif special_throw < stats[1] + stats[2] + stats[3] + stats[4]:
            throw = 25
        elif special_throw < stats[1] + stats[2] + stats[3] + stats[4] + stats[5]:
            throw = 50
        
        AI_player.sub_score(throw)
        print(f"Opponent throws {throw}. Opponent's remaining score: {AI_player.score}")
        if check_win(AI_player, throw):
            return
        throws += 1


def check_game_over(player, AI_player):
    if player.score == 0:
        print(f"{player.name} wins!")
        return True
    if AI_player.score == 0:
        print("Opponent wins!")
        return True
    return False

if __name__ == "__main__":
    main()
