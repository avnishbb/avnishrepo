def write_notes(filename):
    """Writes new notes to a file (overwrites existing content)."""
    with open(filename, 'w') as file:
        note = input("Enter your note: ")
        file.write(note + '\n')
        print("Note written successfully!")


def read_notes(filename):
    """Reads and displays notes from the file."""
    try:
        with open(filename, 'r') as file:
            notes = file.readlines()
            if notes:
                print("\nYour notes:")
                for idx, note in enumerate(notes, 1):
                    print(f"{idx}. {note.strip()}")
            else:
                print("No notes found.")
    except FileNotFoundError:
        print("No notes file found. Please add a note first.")


def append_notes(filename):
    """Appends new notes to the existing file."""
    with open(filename, 'a') as file:
        note = input("Enter your note to append: ")
        file.write(note + '\n')
        print("Note appended successfully!")


def main():
    filename = 'notes.txt'

    while True:
        print("\nMenu:")
        print("1. Write new notes (overwrite)")
        print("2. Read existing notes")
        print("3. Append new notes")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            write_notes(filename)
        elif choice == '2':
            read_notes(filename)
        elif choice == '3':
            append_notes(filename)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
