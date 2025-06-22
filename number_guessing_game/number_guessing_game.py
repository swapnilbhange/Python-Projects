import random
import time
import os

# ANSI Colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def slow_print(text, delay=0.05):
    for c in text:
        print(c, end='', flush=True)
        time.sleep(delay)
    print()

clear_screen()
slow_print(CYAN + "🎮 Welcome to the Advanced Number Guessing Game!" + RESET)
time.sleep(1)

# Input number safely
def get_number(prompt, condition=lambda x: True):
    while True:
        value = input(prompt)
        if value.isdigit():
            value = int(value)
            if condition(value):
                return value
            else:
                print(RED + "Number doesn't meet the condition!" + RESET)
        else:
            print(RED + "Please enter a valid number." + RESET)

lower = get_number(YELLOW + "Enter the lower bound: " + RESET)
upper = get_number(YELLOW + "Enter the upper bound: " + RESET, lambda x: x > lower)

print(GREEN + "\nSelect Difficulty Level:" + RESET)
print("1. Easy   (Unlimited attempts)")
print("2. Medium (10 attempts)")
print("3. Hard   (5 attempts)")

difficulty = input(YELLOW + "Enter choice (1/2/3): " + RESET)
max_attempts = None

if difficulty == "2":
    max_attempts = 10
elif difficulty == "3":
    max_attempts = 5

random_number = random.randint(lower, upper)
guesses = 0

while True:
    print(CYAN + f"\nGuess a number between {lower} and {upper}" + RESET)
    if max_attempts:
        print(YELLOW + f"Attempts left: {max_attempts - guesses}" + RESET)

    guess = get_number("Your guess: ")
    guesses += 1

    if guess == random_number:
        print(GREEN + "\n🎉 YOU GOT IT!" + RESET)
        print(f"{GREEN}You guessed the number in {guesses} attempts.{RESET}")
        print(f"""{CYAN}
╔═══════════════════════╗
║      YOU WIN! 🏆      ║
╚═══════════════════════╝
{RESET}""")
        break
    elif abs(guess - random_number) <= 2:
        print(YELLOW + "🔥 Very close!" + RESET)
    elif guess > random_number:
        print(RED + "📉 Too high!" + RESET)
    else:
        print(RED + "📈 Too low!" + RESET)

    if max_attempts and guesses >= max_attempts:
        print(RED + "\n❌ Game Over! You've run out of attempts." + RESET)
        print(f"The correct number was: {random_number}")
        print(f"""{RED}
╔═══════════════════════╗
║     GAME OVER 💀      ║
╚═══════════════════════╝
{RESET}""")
        break

# Play again prompt
play_again = input(YELLOW + "\nDo you want to play again? (yes/no): " + RESET).lower()
if play_again == "yes":
    print(CYAN + "\nRestart the script to play again!" + RESET)
else:
    print(GREEN + "Thanks for playing! 👋" + RESET)
