import unittest
from func.Note import Note
from func.NotesService import NotesService
from func.NotesStorage import NotesStorage
import unittest.mock

class TestNotesService(unittest.TestCase):
	def test_note_service_add(self):
		notesService = NotesService()
		notatka = Note('notatka', 4.56)
		with unittest.mock.patch.object(NotesStorage, 'add', unittest.mock.MagicMock(return_value=True)):
			self.assertEqual(notesService.add(notatka), True)
		

	def test_averageOf_notes(self):
		notesService = NotesService()
		notatki = [Note('notatka', 5.0), Note('notatka', 4.5), Note('notatka', 5.5)]
		with unittest.mock.patch.object(NotesStorage, 'getAllNotesOf', unittest.mock.MagicMock(return_value=notatki)):
			self.assertEqual(notesService.averageOf('notatka'), 5.0)
		

	def test_averageOf_one_note(self):
		notesService = NotesService()
		notatki = [Note('notatka', 4.643)]
		with unittest.mock.patch.object(NotesStorage, 'getAllNotesOf', unittest.mock.MagicMock(return_value=notatki)):
			self.assertEqual(notesService.averageOf('notatka'), 4.643)
		
	def test_clear(self):
		notesService = NotesService()
		with unittest.mock.patch.object(NotesStorage, 'clear', unittest.mock.MagicMock(return_value=None)):
			self.assertIsNone(notesService.clear())