#Note: This uses the user_resposne for both the keep playing mechanism and the players answer, those could be separated if someone wanted.  
import random
# start with the concept to play with 0 wins
user_response = "yes" 
playerWins = 0
computerWins = 0
winning_dict = {"Rock" : "Scissors", "Scissors" : "Paper", "Paper" : "Rock"}
while user_response != "q": 
    # get random number for computer's choice
    randomnum = random.randint(1,3)
    #Convert number to a playable option
    if randomnum == 1:
        response = "Rock"
    elif randomnum == 2:
        response = "Paper"
    else:
        response = "Scissors"

    #Gets users option
    user_response = input("Rock, Paper, or Scissors, type q to quit: ").capitalize() #the capitalize minimizes the mistakes the user can make
    print(f"The computer got {response}.")
    if user_response == response:
        user_response = input('It was a draw.  \nDid you want to keep playing, "yes" to keep playing or "q" to quit? ').lower() 
    elif user_response in winning_dict:
        if winning_dict[user_response] == response:
            playerWins += 1
            user_response = input(f'Congratulations!! You won! \nSo far the score is {playerWins} to {computerWins}. \nDid you want to keep playing, "yes" to keep playing or "q" to quit? ').lower() #keep_playing
        else:
            computerWins += 1
            user_response = input(f'Better luck next time. \nSo far the score is {playerWins} to {computerWins}. \nDid you want to keep playing, "yes" to keep playing or "q" to quit? ').lower() #keep_playing
    elif user_response == "Q":
        user_response ='q'
    else:
        print('You may have had a typo.  You must type "Rock", "Paper", "Scissors", or "q" exactly. ')
print("Game has quit!!")