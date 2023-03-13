import random
# This variable is assigned so that it can be used to loop to play over and over.
still_playing = True



# This function displays the layout of the grid
def welcome_and_layout():
    print("Welcome to Kaveh's Tic-Tac-Toe Game!\n")
    print("Here is the layout of the grid:\n")
    grid_layout = " 1 | 2 | 3\n-----------\n 4 | 5 | 6\n-----------\n 7 | 8 | 9\n\n"
    print(grid_layout)

while still_playing:

    want_to_play = input("Would you like to play (Y/N)? ")

    # This is where you play the game
    if want_to_play == "Y":

        # Welcomes user and shows grid layout
        welcome_and_layout()
        
        #This resets the grid to original
        grid_input = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
        available_choices = list(range(9))
        winner = 0

        grid_status = f" {grid_input[0]} | {grid_input[1]} | {grid_input[2]}\n-----------\n {grid_input[3]} | {grid_input[4]} | {grid_input[5]}\n-----------\n {grid_input[6]} | {grid_input[7]} | {grid_input[8]}\n\n"

        print("Here's the current grid:\n")
        print(grid_status)

        while len(available_choices) > 0 and winner == 0:

            #Takes user's input as an integer
            user_input = int(input("Please make a choice: ")) - 1

            while user_input not in available_choices:
                user_input = int(input("That's not currently available. Please make another choice: ")) - 1
            
            #User's move
            user_index = available_choices.index(user_input)
            available_choices.pop(user_index)
            grid_input[user_input] = "X"

            #Computer's move
            computer_input = random.choice(available_choices)
            computer_index = available_choices.index(computer_input)
            available_choices.pop(computer_index)
            grid_input[computer_input] = "O"

             #Check for winner:
            if len(available_choices) <= 4:
               
                # Rows
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

            grid_status = f" {grid_input[0]} | {grid_input[1]} | {grid_input[2]}\n-----------\n {grid_input[3]} | {grid_input[4]} | {grid_input[5]}\n-----------\n {grid_input[6]} | {grid_input[7]} | {grid_input[8]}\n\n"
            print("Current grid:\n")
            print(grid_status)
        
        # Show who the winner is
        if winner == "X":
            winner_ID = "Congrats! YOU are the winner."
        elif winner == "O":
            winner_ID = "You lost. Tough luck! The COMPUTER won."
        else:
            winner_ID = "The game ended in a TIE!"
        
        print(winner_ID)
        

    else:
        still_playing = False
