# ----------- IMPORTS AND GAME INTRO ------------
import time
import random
# -------------- GAME VARIABLES ----------------
money = 300
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
def main():
    intro()
    while money > 0 and money < 1000:
        guess = int(input("What's your guess? (1-6): "))
        check_guess(guess)
        time.sleep(1)
        print(f"Current money: {money}$")
    if money > 1000:
        print("You passed 1000$!")
        print("Great job!")
        time.sleep(1)
    else:
        print("You ran out of money!")
        time.sleep(1)
if __name__ == "__main__":
    main()
