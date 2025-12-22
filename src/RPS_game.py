import random
from enum import IntEnum
from collections import Counter # To analyze frequencies efficiently. We imported the Counter library
class GameAction(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2
    Lizard = 3
    Spock = 4

class GameResult(IntEnum):
    Victory = 0
    Defeat = 1
    Tie = 2

class RPSGame:
    def __init__(self):
        # We add the global variables as properties of the RPSGame class
        self.user_history = []
        # Add the rules of the game. Now there are 2 options 
        self.rules = {
            GameAction.Rock: {
                GameAction.Scissors: "Rock smashes scissors",
                GameAction.Lizard: "Rock crushes lizard"
            },
            GameAction.Paper: {
                GameAction.Rock: "Paper covers rock",
                GameAction.Spock: "Paper disproves Spock"
            },
            GameAction.Scissors: {
                GameAction.Paper: "Scissors cuts paper",
                GameAction.Lizard: "Scissors decapitates lizard"
            },
            GameAction.Lizard: {
                GameAction.Spock: "Lizard poisons Spock",
                GameAction.Paper: "Lizard eats paper"
            },
            GameAction.Spock: {
                GameAction.Scissors: "Spock smashes scissors",
                GameAction.Rock: "Spock vaporizes rock"
            }
        }
        # Definition that the agent must choose to win a specific user move.
        self.counter_moves = {
            GameAction.Rock: [GameAction.Paper, GameAction.Spock],
            GameAction.Paper: [GameAction.Scissors, GameAction.Lizard],
            GameAction.Scissors: [GameAction.Rock, GameAction.Spock],
            GameAction.Lizard: [GameAction.Rock, GameAction.Scissors],
            GameAction.Spock: [GameAction.Paper, GameAction.Lizard]
        }

    def get_computer_action(self):
        if not self.user_history:
            # In case the number of those listed changes and they are not sequential
            selection = random.choice(list(GameAction))
        else:
            # The user's most frequent prediction
            most_common_user_move = Counter(self.user_history).most_common(1)[0][0]
            
            # Since there are now two possible winners, we choose one at random
            possible_winning_moves = self.counter_moves[most_common_user_move]
            selection = random.choice(possible_winning_moves)

        action = GameAction(selection)
        print(f"Computer picked {action.name}.")
        return action

    def assess_game(self, user_action, computer_action):
        # We remove the if/else series
        if user_action == computer_action:
            print(f"Both picked {user_action.name}. Draw!")
            return GameResult.Tie

        # User Victory: We check if the CPU action is on the User's victim list
        if computer_action in self.rules[user_action]:
            message = self.rules[user_action][computer_action]
            print(f"{message}. You won!")
            return GameResult.Victory
        
        # Defeat (If it's neither a draw nor a win, it's a defeat)
        message = self.rules[computer_action][user_action]
        print(f"{message}. You lost!")
        return GameResult.Defeat

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