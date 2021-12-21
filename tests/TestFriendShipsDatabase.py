from func.FriendShipsDatabase import FriendShipsDatabase
import unittest
from unittest.mock import MagicMock



class TestFriendShipsDatabase(unittest.TestCase):

	def setUp(self):
		self.temp = FriendShipsDatabase()

	def test_add_friend(self):
		self.temp.database.addFriend = MagicMock(return_value=['Kowalski'])
		self.assertEqual(['Kowalski'], self.temp.database.addFriend('Malinowski', 'Kowalski'))
		self.temp.database.addFriend.assert_called_with('Malinowski', 'Kowalski')

	def test_add_friend_person_does_not_exist(self):
		self.temp.database.addFriend= MagicMock(side_effect=ValueError)	
		self.assertRaises(ValueError, self.temp.database.addFriend, 'sfsdfdsf', 'Kowalski')
		self.temp.database.addFriend.assert_called_with('sfsdfdsf', 'Kowalski')

	def test_add_friend_person_not_str(self):
		self.temp.database.addFriend= MagicMock(side_effect=ValueError)	
		self.assertRaises(ValueError, self.temp.database.addFriend, 3, 'Kowalski')
		self.temp.database.addFriend.assert_called_with(3, 'Kowalski')

	def test_make_friends(self):
		self.temp.database = MagicMock()
		self.temp.makeFriends('Pionk', 'Malinowski')
		self.temp.database.makeFriends.assert_called_with('Pionk', 'Malinowski')

	def test_make_friends_person1_not_str(self):
		self.temp.database.makeFriends = MagicMock(side_effect=ValueError)
		with self.assertRaises(ValueError):
			self.temp.makeFriends(2323, 'Pionk')
		self.temp.database.makeFriends.assert_called_with(2323, 'Pionk')

	def test_make_friends_person1_not_in_database(self):
		self.temp.database.makeFriends = MagicMock(side_effect=ValueError)
		with self.assertRaises(ValueError):
			self.temp.makeFriends('Pączek', 'Pionk')
		self.temp.database.makeFriends.assert_called_with('Pączek', 'Pionk')

	def test_make_friends_person2_not_str(self):
		self.temp.database.makeFriends = MagicMock(side_effect=ValueError)
		with self.assertRaises(ValueError):
			self.temp.makeFriends('Malinowski', [])
		self.temp.database.makeFriends.assert_called_with('Malinowski', [])

	def test_get_friends_ok(self):
		self.temp.database.getFriendsList= MagicMock(return_value=[])
		self.assertEqual(self.temp.getFriendsList('Malinowski'), [])
		self.temp.database.getFriendsList.assert_called_with('Malinowski')

	def test_get_friends_person_not_str(self):
		self.temp.database.getFriendsList = MagicMock(side_effect=ValueError)
		with self.assertRaises(ValueError):
			self.temp.getFriendsList(565464)
		self.temp.database.getFriendsList.assert_called_with(565464)

	def test_get_friends_person_not_in_database(self):
		self.temp.database.getFriendsList = MagicMock(side_effect=ValueError)
		with self.assertRaises(ValueError):
			self.temp.getFriendsList('Wyrzykowski')
		self.temp.database.getFriendsList.assert_called_with('Wyrzykowski')

	def test_are_friends_positive(self):
		self.temp.database.areFriends = MagicMock(return_value=True)
		self.assertTrue(self.temp.areFriends('Pionk', 'Bobkowska'))
		self.temp.database.areFriends.assert_called_with('Pionk', 'Bobkowska')

	def test_are_friends_false(self):
		self.temp.database.areFriends = MagicMock(return_value=False)
		self.assertFalse(self.temp.areFriends('Bobkowska', 'Malinowski'))
		self.temp.database.areFriends.assert_called_with('Bobkowska', 'Malinowski')

	def test_are_friends_person1_not_str(self):
		self.temp.database.areFriends= MagicMock(side_effect=ValueError)
		self.assertRaises(ValueError, self.temp.areFriends, 6546, 'Malinowski')
		self.temp.database.areFriends.assert_called_with(6546, 'Malinowski')

	def test_are_friends_person2_not_str(self):
		self.temp.database.areFriends= MagicMock(side_effect=ValueError)
		self.assertRaises(ValueError, self.temp.areFriends, 'Malinowski', None)
		self.temp.database.areFriends.assert_called_with('Malinowski', None)

	def test_are_friends_persons_not_existing(self):
		self.temp.database.areFriends= MagicMock(side_effect=ValueError)
		self.assertRaises(ValueError, self.temp.areFriends, 'Malinowska', 'Kowalskiii')
		self.temp.database.areFriends.assert_called_with('Malinowska', 'Kowalskiii')

	def tearDown(self):
		self.temp = None