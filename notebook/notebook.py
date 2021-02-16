import datetime

# Store the id available for the next note.
last_id = 0

class Note:
    '''
    Represent a piece of note with tags in a notebook. Match against a string.
    '''

    def __init__(self, memo, tags=''):
        '''Initialize a note with its memo, tags, creation_time and id'''

        self.memo = memo
        self.tags = tags
        self.creation_time = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        '''Check if the filter matches the memo or the tags of the note.'''

        return filter in self.memo or filter in self.tags


class Notebook:
    def __init__(self):
        self.notes = []

    def new_memo(self, memo, tags=''):
        self.notes.append(Note(memo, tags))

    def find_note(self, note_id):
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return None

    def modify_memo(self, note_id, memo):
        note = self.find_note(note_id)
        if note:
            note.memo = memo
            return True
        return False

    def modify_tags(self, note_id, tags):
        note = self.find_note(note_id)
        if note:
            note.tags = tags
            return True
        return False

    def search(self, filter):
        return [note for note in self.notes if note.match(filter)]
