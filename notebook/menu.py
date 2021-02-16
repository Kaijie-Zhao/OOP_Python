import sys
from notebook import Notebook, Note

class Menu:
    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.quit
        }

    def display_menu(self):
        print('''
        Notebook Menu
        
        1. Show all notes.
        2. Search a note.
        3. Add a new note.
        4. Modify a note.
        5. Quit
        
        ''')

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter a choice:")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def show_notes(self, notes=None):
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print("{0}: {1} \n {2}".format(note.id, note.tags, note.memo))

    def search_notes(self):
        filter = input("Search for:")
        notes = self.notebook.search(filter)
        if notes:
            self.show_notes(notes)
        else:
            print("Note not found!")

    def add_note(self):
        memo = input("Write a new memo: ")
        self.notebook.new_memo(memo)
        print("New note added")

    def modify_note(self):
        id = input("Enter the id of the note you wanna modify: ")
        memo = input("Enter a memo:")
        tags = input("Enter a tag: ")

        if self.notebook.find_note(id):
            if memo:
                self.notebook.modify_memo(id, memo)
                print("Memo Modified")
            if tags:
                self.notebook.modify_tags(id, tags)
                print("Tags Modified")
        else:
            print("ID not found!")

    def quit(self):
        print("Thanks for using")
        sys.exit(0)

if __name__ == '__main__':
    Menu().run()

