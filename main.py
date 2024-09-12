#Ask the user to make a choice
#if choice is not valid
# print an error
# let the computer to make a choice
# print choices (emojis)
# determine the winner
# ask the user if they want to continue
# if not
# terminate

#continue keyword only be used in loop
import random
ROCK = 'r'
SCISSORS = 's'
PAPER = 'p'
emojis = {'r': '🗿', 'p': '📝', 's': '❌'}
choices = tuple(emojis.keys())

def get_user_choice():
    while True:
      user_choice = input('Rock, paper, or scissor? (r/p/s): ').lower()
      if user_choice in choices:
          return user_choice
      else:
          print('Invalid choice!')

def display_choices(user_choice, computer_choice):
    print(f'You chose {emojis[user_choice]}')
    print(f'Computer chose {emojis[computer_choice]}')

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print('Tie!')
    elif (
            (user_choice == 'r' and computer_choice == 's') or
            (user_choice == 's' and computer_choice == 'p') or
            (user_choice == 'p' and computer_choice == 'r')):
        print('you win')
    else:
        print('you lose')

def play_game():
   while True:
       user_choice = get_user_choice()
       computer_choice = random.choice(choices)

       display_choices(user_choice, computer_choice)

       determine_winner(user_choice, computer_choice)

       should_continue = input('Continue? (y/n): ').lower()
       if should_continue == 'n':
          break

play_game()