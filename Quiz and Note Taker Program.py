# Program: Quiz and Note Taker Program
print("Exercise: Python Quiz and Note Taker Program")

# Input for user's name
name = input("Enter your name:")

# Global Variables
scores = []  # Stores user scores
answers = []  # Stores user answers
entries = [] # Stores user entry for notes

# Constants
a = 15
b = 3
result = a * b  # Precomputed answer for the quiz
capitalF = {
    "France": "Paris",  # Country-capital mapping
}

# Functions
def greet_user():
    """Greet the user."""
    print(f"Welcome, {name}!")

def add_answer():
    """Save answers to a file."""
    with open("Answer.txt", "a") as file:
        for answer in answers:
            file.write(answer + "\n")
    print("Answers have been saved.")

def add_scores():
    """Save scores to a file."""
    with open("Score.txt", "a") as file:
        for score in scores:
            file.write(str(score) + "\n")
    print("Scores have been saved.")

def display_scores():
    """Display saved scores."""
    if scores:
        print("Your Scores:")
        for i, score in enumerate(scores, 1):
            print(f"{i}. {score}")
    else:
        print("No scores found.")

def quiz():
    """Conduct a quiz with the user."""
    score = 0

    # Question 1
    print("\nQuestion 1: What is 15 x 3?")
    try:
        ans1 = int(input("Enter your answer: "))
        if ans1 == result:
            print("Correct!")
            answers.append(f"Q1: {ans1}")
            score += 1
        else:
            print("Incorrect.")
    except ValueError:
        print("Invalid input! Please enter a number.")

    # Question 2
    print("\nQuestion 2: Which of the following is NOT a programming language?")
    print("a) Python\nb) HTML\nc) JavaScript\nd) Java")
    ans2 = input("Enter your answer (a/b/c/d): ").lower()
    if ans2 == "b":
        print("Correct!")
        answers.append(f"Q2: {ans2}")
        score += 1
    else:
        print("Incorrect. The correct answer is b (HTML).")

    # Question 3
    print("\nQuestion 3: What is the capital of France?")
    ans3 = input("Enter your answer: ").capitalize()
    if ans3 == capitalF["France"]:
        print("Correct!")
        answers.append(f"Q3: {ans3}")
        score += 1
    else:
        print(f"Incorrect. The correct answer is {capitalF['France']}.")

    # Save and display score
    scores.append(score)
    print(f"\nYour final score: {score}")

def pre_quiz():
    """Ask the user if they would like to take a quiz."""
    while True:
        response = input("Would you like to take a quiz? (yes/no): ").lower()
        if response == "yes":
            quiz()
            break
        elif response == "no":
            print("Thank you! Maybe next time.")
            break
        else:
            print("Invalid response. Please enter 'yes' or 'no'.")

def write_entry():
    """Adds a new entry to the notes."""
    entry = input("Enter your note entry: ")
    entries.append(entry)
    print("Note Added!")
    
def add_entry():
    """Saves notes to a file"""
    with open("notes.txt", "a") as file:
        for entry in entries:
            file.write(entry + "\n")
    print("Notes saved successfully!")
    
def view_entry():
    if entries:
        print("Your Notes Entries:")
        for i, entry in enumerate(entries, 1):
            print(f"{i}. {entry}")
    else:
        print("No entries found")
        
def main():
    """Main program loop."""
    greet_user()

    while True:
        print("\nPlease choose an option:")
        print("1: Take the quiz")
        print("2: See your scores")
        print("3: Write a note")
        print("4: View Notes")
        print("5: Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            pre_quiz()
        elif choice == "2":
            display_scores()
        elif choice == "3":
            write_entry()
        elif choice == "4":
            view_entry()
        elif choice == "5":
            add_answer()
            add_scores()
            add_entry()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
main()
