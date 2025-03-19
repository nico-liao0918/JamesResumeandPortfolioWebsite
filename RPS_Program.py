# === Rock-Paper-Scissor Game Program ===
import random
import time

# === Global Variables ===
options = ("rock", "paper", "scissor")
playerscore = 0
computerscore = 0
totaltime = 0
running = True

# === Function to Save Game Entry to a File ===
def save_entry(playerscore, computerscore, totaltime, player, computer):
    """Saves the current round's results to GameSession.txt"""
    with open('GameSession.txt', "a") as file:
        file.write(f"Player Answer: {player}\n")
        file.write(f"Computer Answer: {computer}\n")
        file.write(f"Player Score: {playerscore}\n")
        file.write(f"Computer Score: {computerscore}\n")
        file.write(f"Total Reaction Time: {totaltime:.2f} seconds\n")
        file.write("=" * 30 + "\n") 
    print("Save Success!")

# === Main Game Loop ===
while running:
    player = None
    computer = random.choice(options)  # Random computer choice

    starttime = time.time()  # Start reaction time measurement

    # Get user input
    while player not in options:
        player = input("Enter a choice (rock, paper, scissor): ").strip().lower()

    print(f"Player : {player}")
    print(f"Computer: {computer}")

    # Calculate reaction time
    reacttime = time.time() - starttime
    totaltime += reacttime

    # === Game Logic & Scoring & Results Saving ===
    if player == computer:
        print("Tie!")
        playerscore, computerscore = 0, 0
        print(f"Your reaction time: {reacttime:.2f}")
        print(f"Your Score: {playerscore}")
        print(f"Computer Score: {computerscore}")
        save_entry(playerscore, computerscore, totaltime, player, computer)
    elif player == "rock" and computer == "scissor":
        print("Win!")
        playerscore += 1
        print(f"Your reaction time: {reacttime:.2f}")
        print(f"Your Score: {playerscore}")
        print(f"Computer Score: {computerscore}")
        save_entry(playerscore, computerscore, totaltime, player, computer)
    elif player == "paper" and computer == "rock":
        print("Win!")
        playerscore += 1
        print(f"Your reaction time: {reacttime:.2f}")
        print(f"Your Score: {playerscore}")
        print(f"Computer Score: {computerscore}")
        save_entry(playerscore, computerscore, totaltime, player, computer)
    elif player == "scissor" and computer == "paper":
        print("Win!")
        playerscore += 1
        print(f"Your reaction time: {reacttime:.2f}")
        print(f"Your Score: {playerscore}")
        print(f"Computer Score: {computerscore}")
        save_entry(playerscore, computerscore, totaltime, player, computer)
    else:
        print("Loss!")
        computerscore += 1
        print(f"Your reaction time: {reacttime:.2f}")
        print(f"Your Score: {playerscore}")
        print(f"Computer Score: {computerscore}")
        save_entry(playerscore, computerscore, totaltime, player, computer)

    # Ask if the player wants to continue
    playagain = input("Play again? (y/n): ").strip().lower()
    if not playagain == "y":
        running = False

# === End of Game Summary ===
print("\n=== Final Results ===")
print(f"Final Player Score: {playerscore}")
print(f"Final Computer Score: {computerscore}")
print(f"Total Reaction Time: {totaltime:.2f} seconds")
print("Thanks for playing!")
