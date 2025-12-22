import random
from enum import IntEnum
from collections import Counter # To analyze frequencies efficiently. We imported the Counter library
class GameAction(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2

class GameResult(IntEnum):
    Victory = 0
    Defeat = 1
    Tie = 2

class RPSGame:
    def __init__(self):
        # We add the global variables as properties of the RPSGame class
        self.user_history = []

        self.victories = {
            GameAction.Rock: GameAction.Paper,     
            GameAction.Paper: GameAction.Scissors, 
            GameAction.Scissors: GameAction.Rock    
        }

    def get_computer_action(self):
        if not self.user_history:
            selection = random.randint(0, len(GameAction) - 1)
        else:
            # The prediction is maintained
            most_common_user_move = Counter(self.user_history).most_common(1)[0][0]
            selection = self.victories[most_common_user_move]

        action = GameAction(selection)
        print(f"Computer picked {action.name}.")
        return action

    def assess_game(self, user_action, computer_action):
        # We remove the if/else series
        if user_action == computer_action:
            print(f"Both picked {user_action.name}. Draw!")
            return GameResult.Tie

        # If the computer's movement overcomes the user's movement:
        if computer_action == self.victories[user_action]:
            print(f"{computer_action.name} beats {user_action.name}. You lost!")
            return GameResult.Defeat
        
        # In any other case (other than a draw or a loss), it is a victory
        print(f"{user_action.name} beats {computer_action.name}. You won!")
        return GameResult.Victory

    def get_user_action(self):
        # We capture the user input
        choices = [f"{a.name}[{a.value}]" for a in GameAction]
        choices_str = ", ".join(choices)
        try:
            selection = int(input(f"\nPick a choice ({choices_str}): "))
            return GameAction(selection)
        except (ValueError, KeyError):
            raise ValueError(f"Invalid selection. Range: [0, {len(GameAction)-1}]")

    def play(self):
        # Main loop of the game
        while True:
            try:
                user_action = self.get_user_action()
            except ValueError as e:
                print(e)
                continue

            computer_action = self.get_computer_action()
            self.assess_game(user_action, computer_action)
            
            # We save the player's history
            self.user_history.append(user_action)

            while True:
                next_round = input("\nAnother round? (y/n): ").lower()
                if next_round in ('y', 'n'):
                    
                    break
                # If you choose something other than 'y' or 'n', it asks again if you want another round or not.
                print("Invalid option. Please type 'y' to continue or 'n' to exit.")
            
            # Having validated the above, if you choose 'n' the game ends
            if next_round == 'n':
                print("Game over. Thanks for playing!")
                break

if __name__ == "__main__":
    game = RPSGame()
    game.play()