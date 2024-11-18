import random

# Display a welcome message for the game
print("***********************************")
print("  WELCOME TO ROCK-PAPER-SCISSORS GAME")
print("***********************************\n")

# Function to handle the main gameplay logic
def play_rock_paper_scissors():
    """
    This function allows the player to choose an option (Rock, Paper, or Scissors),
    compares it with the computer's choice, and determines the outcome (win, loss, or tie).
    """
    while True:
        global computer_choice
        global player_choice
        
        # List of valid choices for the game
        choices = ['Rock', 'Paper', 'Scissor']
        computer_choice = random.choice(choices).lower()

        # Display the options to the player
        print("\nChoose your option from the list below:")
        for number, item in enumerate(choices, start=1):
            print(f"{number}. {item}")
         
        # Take the player's input and convert it to lowercase for comparison
        player_choice = input("\nEnter your choice: ").lower()
        
        # Check if the input is valid
        if player_choice in ['rock', 'paper', 'scissor', '1', '2', '3']:
            # Display chosen options before showing the result
            print(f"\nYou chose: {player_choice.capitalize()}")
            print(f"Computer chose: {computer_choice.capitalize()}")

            # Game outcomes
            if player_choice == 'rock' and computer_choice == 'scissor':
                print("\nCongratulations! You have won against the computer!\n")

            elif player_choice == 'scissor' and computer_choice == 'paper':
                print("\nCongratulations! You have won against the computer!\n")

            elif player_choice == 'paper' and computer_choice == 'rock':
                print("\nCongratulations! You have won against the computer!\n")

            elif player_choice == 'scissor' and computer_choice == 'rock':
                print("\nYou lost! The computer won this round.\n")

            elif player_choice == 'paper' and computer_choice == 'scissor':
                print("\nYou lost! The computer won this round.\n")

            elif player_choice == 'rock' and computer_choice == 'paper':
                print("\nYou lost! The computer won this round.\n")

            elif player_choice == computer_choice:
                print("\nIt's a tie! Try again.\n")
            break  # Exit the loop if the input is valid and processed
        
        else:
            # Inform the player about invalid input
            print("\nInvalid input. Please choose a valid option from the list below.\n")

# Start the first round of the game
play_rock_paper_scissors()

# Loop to handle replaying the game or exiting
while True:
    play_again = input("Enter 'Yes' to play again or 'No' to exit: ").lower()
    
    if play_again == 'yes' or play_again == 'y':
        play_rock_paper_scissors()  # Restart the game
    elif play_again == 'no' or play_again == 'n':
        print("\nThank you for playing!")
        print("See you again! Goodbye!")
        break  # Exit the loop and end the program
    else:
        # Handle invalid input for replay options
        print("Invalid input. Please enter 'Yes' or 'No'.")