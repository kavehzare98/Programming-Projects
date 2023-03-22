import random

# Variable used to playing infinite times unless user chooses to stop playing.
still_playing = True

# FUNCTIONS:

# Displays grid layout and welcomes player.
def welcome_and_layout():
    print("Welcome to Kaveh's Tic-Tac-Toe Game!\n")
    print("Here is the layout of the grid:\n")
    grid_layout = " 1 | 2 | 3\n-----------\n 4 | 5 | 6\n-----------\n 7 | 8 | 9\n\n"
    print(grid_layout)

# Displays the current grid.
def display_grid():
    grid_status = f" {grid_input[0]} | {grid_input[1]} | {grid_input[2]}\n-----------\n {grid_input[3]} | {grid_input[4]} | {grid_input[5]}\n-----------\n {grid_input[6]} | {grid_input[7]} | {grid_input[8]}\n\n"
    print("Here's the current grid:\n")
    print(grid_status)

def user_move():
    #Takes user's input as an integer
    user_input = int(input("Please make a choice: ")) - 1
    # Checks to see if user is not overriding any of the currently chosen positions.
    while user_input not in available_choices:
        user_input = int(input("That's not currently available. Please make another choice: ")) - 1
    
    # Finds the index of user's input in the available_choices list
    user_index = available_choices.index(user_input)
    # Uses the previously found index and pops user's choice from the available_choices list
    available_choices.pop(user_index)
    # Marks the grid with an X to represent the user's choice on the grid
    grid_input[user_input] = "X"

def computer_move():
    computer_input = random.choice(available_choices)
    computer_index = available_choices.index(computer_input)
    available_choices.pop(computer_index)
    grid_input[computer_input] = "O"

def determine_winner():
    # Checks Rows
    if grid_input[0] == grid_input[1] and grid_input[1] == grid_input[2]:
        winner = grid_input[0]
    elif grid_input[3] == grid_input[4] and grid_input[4] == grid_input[5]:
        winner = grid_input[3]
    elif grid_input[6] == grid_input[7] and grid_input[7] == grid_input[8]:
        winner = grid_input[6]
    # Columns
    elif grid_input[0] == grid_input[3] and grid_input[3] == grid_input[6]:
        winner = grid_input[0]
    elif grid_input[1] == grid_input[4] and grid_input[4] == grid_input[7]:
        winner = grid_input[1]
    elif grid_input[2] == grid_input[5] and grid_input[5] == grid_input[8]:
        winner = grid_input[2]
    # Diagonals
    elif grid_input[0] == grid_input[4] and grid_input[4] == grid_input[8]:
        winner = grid_input[0]
    elif grid_input[2] == grid_input[4] and grid_input[4] == grid_input[6]:
        winner = grid_input[2]
    # Tie
    else:
        winner = 0
    
    return winner

def display_winner():
    if determine_winner() == "X":
        winner_ID = "Congrats! YOU are the winner."
    elif determine_winner() == "O":
        winner_ID = "You lost. Tough luck! The COMPUTER won."
    else:
        winner_ID = "The game ended in a TIE!"
    print(winner_ID)

# GAME STARTS HERE!
while still_playing:

    want_to_play = input("Would you like to play (Y/N)? ")
    
    # Global variables:
    grid_input = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
    available_choices = list(range(9))
    game_over = False

    # This is where you play the game
    if want_to_play == "Y":

        # Welcomes user and shows grid layout
        welcome_and_layout()
        
        display_grid()

        while len(available_choices) > 0 and game_over == False:

            user_move()

            if len(available_choices) <= 4:
            
                determine_winner()

                if determine_winner() != 0:
                    display_grid()
                    game_over = True

            computer_move()
            
            display_grid()
        
        display_winner()

    else:
        still_playing = False
