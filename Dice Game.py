# ----------- IMPORTS AND GAME INTRO ------------
import time
import random
# -------------- GAME VARIABLES ----------------
money = 250
# ----------------- FUNCTIONS -------------------
def guess_number():
    guess = input("What's your guess? (1-6): ")

def roll():
    print("Rolling dice...")
    time.sleep(1)
    dice_number = random.randint(1, 6)
    print("You rolled " + str(dice_number))
    time.sleep(1)
# -------------- MAIN GAME LOOP -----------------
