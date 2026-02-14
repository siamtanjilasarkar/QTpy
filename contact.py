import os
import sys  # Imported for clean exit

fileName = "contacts.txt"

# Create file if not exist.
if not os.path.exists(fileName):
    open(fileName, "w").close()

def newContact():
    name = input("Enter name: ")
    number = input("Enter number: ")

    if not name.strip() or not number.strip():
        print("Please give a valid input.")
        return

    with open(fileName, "a") as f:
        f.write(f"{number}-{name}\n")
        print(f"New contact added.\nName: {name}\nNumber: {number}")

def searchContact():
    q = input("Search contact: ")
    if q.strip() != '':
        contacts_found = 0
        print("\n--- Search Results ---")
        with open(fileName, "r") as f:
            for contact in f:
                if q.lower() in contact.lower():
                    # Robust splitting: limit split to 1 to handle names with hyphens
                    parts = contact.strip().split("-", 1)
                    if len(parts) == 2:
                        print(f"Name: {parts[1]}\nNumber: {parts[0]}\n")
                        contacts_found += 1
        
        if contacts_found == 0:
            print("No contact found with this search.\n")
        else:
            print(f"Total contacts found: {contacts_found}")

def printAllContact():
    print("\n--- All Contacts ---")
    contacts_found = 0
    with open(fileName, "r") as f:
        for contact in f:
            if contact.strip(): # Check if line is not just empty whitespace
                parts = contact.strip().split("-", 1)
                if len(parts) == 2:
                    print(f"Name: {parts[1]}\nNumber: {parts[0]}")
                    contacts_found += 1
    
    if contacts_found == 0:
        print("No contacts found.")
    else:
        print(f"\nTotal contacts: {contacts_found}")

# --- NEW FUNCTION: DELETE CONTACT ---
def deleteContact():
    q = input("Enter the Name or Number to delete: ")
    if not q.strip():
        print("Invalid input.")
        return

    lines = []
    deleted = False
    
    # 1. Read all lines
    with open(fileName, "r") as f:
        lines = f.readlines()

    # 2. Write back only the lines that DO NOT match the search
    with open(fileName, "w") as f:
        for line in lines:
            if q.lower() in line.lower():
                print(f"Deleted: {line.strip()}")
                deleted = True
            else:
                f.write(line)
    
    if not deleted:
        print("No contact found to delete.")

def printOptions():
    print("\n=========================")
    print("   CONTACT MANAGER")
    print("=========================")
    print("1. View all contacts")
    print("2. Add new contact")
    print("3. Find contact")
    print("4. Delete Contact")
    print("5. Exit")
    
    try:
        user_choice = int(input("Choose option (1-5): "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if user_choice == 1:
        printAllContact()
    elif user_choice == 2:
        newContact()
    elif user_choice == 3:
        searchContact()
    elif user_choice == 4:
        deleteContact()
    elif user_choice == 5:
        print("Exiting...")
        sys.exit() # Cleaner exit than os._exit
    else:
        print(f"Invalid option: {user_choice}")

# Main Loop
while True:
    printOptions()
