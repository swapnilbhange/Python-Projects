import random
import time
import os

# ANSI Colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

# ASCII Art Dictionary
art = {
    "rock": "🪨 ROCK",
    "paper": "📄 PAPER",
    "scissors": "✂️ SCISSORS"
}

# Clear screen function
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Slow print effect
def slow_print(text, delay=0.04):
    for c in text:
        print(c, end='', flush=True)
        time.sleep(delay)
    print()

clear()
slow_print(CYAN + "🎮 Welcome to Rock, Paper, Scissors!" + RESET)
print()

user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]

while True:
    print(YELLOW + "\nType Rock/Paper/Scissors or Q to Quit" + RESET)
    user_input = input("👉 Your move: ").lower()

    if user_input == "q":
        break

    if user_input not in options:
        print(RED + "❌ Invalid input! Try again." + RESET)
        continue

    computer_pick = random.choice(options)
    print(f"\nYou chose:     {GREEN + art[user_input] + RESET}")
    print(f"Computer chose:{RED + art[computer_pick] + RESET}")
    time.sleep(0.5)

    if user_input == computer_pick:
        print(YELLOW + "🤝 It's a tie!" + RESET)
    elif (user_input == "rock" and computer_pick == "scissors") or \
         (user_input == "paper" and computer_pick == "rock") or \
         (user_input == "scissors" and computer_pick == "paper"):
        print(GREEN + "✅ You Won!" + RESET)
        user_wins += 1
    else:
        print(RED + "❌ You Lost!" + RESET)
        computer_wins += 1

    print(f"\n🏆 Score → You: {user_wins} | Computer: {computer_wins}")

print(CYAN + "\nGame Over! 🕹️" + RESET)
print(f"Final Score: You {user_wins} - {computer_wins} Computer")
print(GREEN + "Thanks for playing!" + RESET)
