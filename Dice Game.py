# ----------- IMPORTS AND GAME INTRO ------------
import time
import random
# -------------- GAME VARIABLES ----------------
money = 250
# ----------------- FUNCTIONS -------------------
def intro():
    global money
    print("Welcome to Dice Game! 🎲")
    time.sleep(1)
    print("Make 1000$ to win! 🤑")
    time.sleep(1)
    print("Go bankrupt to lose 😓💼...")
    time.sleep(1)
    print(f"Current money: {money}")

def check_guess(guess, dice_number):
    global money
    if guess == dice_number:
        print("You win!")
        time.sleep(1)
        money += 300
    else:
        print("You lose!")
        time.sleep(1)
        money -= 75


# -------------- MAIN GAME LOOP -----------------
