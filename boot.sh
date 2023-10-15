#!/bin/bash

# Ask the user if they want to play rock-paper-scissors
read -p "Would you like to play "Rock Paper Scissors"? (yes/no): " answer

if [ "$answer" = "yes" ]; then
    # If the answer is 'yes', execute the Python script
    python3 rps.py
else
    # If the answer is 'no', inform the user
    echo "That's too bad, maybe next time."
fi
