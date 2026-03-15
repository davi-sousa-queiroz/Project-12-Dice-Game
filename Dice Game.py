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

def check_guess(guess):
    global money

    print("Rolling dice...")
    time.sleep(1)
    dice_number = random.randint(1, 6)
    print("You rolled " + str(dice_number))
    time.sleep(1)

    if guess == dice_number:
        print("You win!")
        time.sleep(1)
        money += 450
        print("+450$")
    else:
        print("You lose!")
        time.sleep(1)
        money -= 75
        print("-75$")
# -------------- MAIN GAME LOOP -----------------
