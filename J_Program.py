# Journal Program
print("Welcome to your Personal Journal")

# Global Variables
entries = []

# Function
def load_entries():
    """Loads entries from the journal file."""
    try:
        with open("journal.txt", "r") as file:
            for line in file:
                entries.append(line.strip())
    except FileNotFoundError:
        print("No previous journal entries found. Starting fresh!")

def save_entries():
    """Saves all entries to the journal file."""
    with open("journal.txt", "w") as file:
        for entry in entries:
            file.write(entry + "\n")
    print("Entries saved successfully!")

def add_entry():
    """Adds a new entry to the journal."""
    entry = input("Enter your journal entry: ")
    entries.append(entry)
    print("Entry added!")

def view_entries():
    """Displays all journal entries."""
    if entries:
        print("Your Journal Entries:")
        for i, entry in enumerate(entries, 1):
            print(f"{i}. {entry}")
    else:
        print("No entries found.")

def search_entries():
    """Searches entries by a keyword."""
    keyword = input("Enter a keyword to search for: ").lower()
    found = False
    for entry in entries:
        if keyword in entry.lower():
            print(f"Found: {entry}")
            found = True
    if not found:
        print("No entries found with that keyword.")

# Main program loop
def main():
    greet_user()
    load_entries()  # Load previous entries at the start

    while True:
        print("\nChoose an option:")
        print("1. Add Entry")
        print("2. View All Entries")
        print("3. Search Entries")
        print("4. Save Entries and Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            search_entries()
        elif choice == "4":
            save_entries()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the journal program
main()
