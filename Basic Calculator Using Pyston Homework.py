import random
attempts_list = []
def show_score():
  if len(attempts_list) == 0:
    print("There is currently no high score")
  else:
    print("The current high score is {min(attempts_list)} attempts")
def start_game():
  random_number = int(random.randint(1,10))
  pname = input("Enter your name")
  wanna_play = input("Hi, {pname}, Would you like to play the guessing game? (Enter yes/no)").lower()
  attempts = 0
  while wanna_play == "yes":
