from func.Note import Note
from func.NotesStorage import NotesStorage

class NotesService:
    def __init__(self):
        self.notesStorage = NotesStorage()
    def add(self, note):
        return self.notesStorage.add(note)
    def averageOf(self, name):
        notes = self.notesStorage.getAllNotesOf(name)
        if len(notes) == 0:
            return None
        summary = 0
        for note in notes:
            summary += note.note
        return summary / len(notes)
    def clear(self):
        return self.notesStorage.clear()
