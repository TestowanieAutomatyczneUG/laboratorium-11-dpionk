import unittest
import unittest.mock
from func.Operations import Operations

class TestOperations(unittest.TestCase):
	def setUp(self):
		self.temp = Operations()
	
	def test_readLines(self):
		with unittest.mock.patch('builtins.open', unittest.mock.mock_open(read_data='linijka')) as mock:
			self.assertEqual(self.temp.readLines('data/file.txt'), ['linijka'])
			mock.assert_called_with('data/file.txt', 'r')

	def test_writeSomethingInFile(self):
		with unittest.mock.patch('builtins.open', unittest.mock.mock_open(read_data='linijka')) as mock:
			self.temp.writeSomethingInFile('data/file.txt', 'nowa linijka')
			mock.assert_called_with('data/file.txt', 'w')

	@unittest.mock.patch('os.path.exists')
	@unittest.mock.patch('os.remove')
	
	def testDeleteFile(self, exists, mock):
		exists.return_value = True
		self.temp.deleteFile('../data/file.txt')
		mock.assert_called_with('../data/file.txt')

	@unittest.mock.patch('os.path.exists')
	def testDeleteFile_2(self, exists):
		exists.return_value = False
		with self.assertRaises(ValueError):
			self.temp.deleteFile('data/file.txt')

	def tearDown(self):
		self.temp = None
	

		
