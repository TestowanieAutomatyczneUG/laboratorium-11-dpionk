import unittest
from func.FriendShips import FriendShips

class TestFriendShips(unittest.TestCase):
	def setUp(self):
		self.temp=FriendShips({
			'Pionk': ['Kowalski', 'Nowak', 'Bobkowska'],
			'Kowalski': ['Pionk'],
			'Nowak': ['Pionk'],
			'Bobkowska': ['Pionk'],
			'Malinowski': []
		})
	
	def test_add_friend(self):
		self.assertEqual(['Kowalski'], self.temp.addFriend('Malinowski', 'Kowalski'))

	def test_add_friend_person_does_not_exist(self):
		self.assertRaises(ValueError, self.temp.addFriend, 'sfsdfdsf', 'Kowalski')

	def test_add_friend_person_not_str(self):
		self.assertRaises(ValueError, self.temp.addFriend, 3, 'Kowalski')

	def test_make_friends(self):
		self.assertEqual({
			'Pionk': ['Kowalski', 'Nowak', 'Bobkowska', 'Malinowski'],
			'Kowalski': ['Pionk'],
			'Nowak': ['Pionk'],
			'Bobkowska': ['Pionk'],
			'Malinowski': ['Pionk']
		}, self.temp.makeFriends('Pionk', 'Malinowski'))

	def test_make_friends_person_not_str(self):
		self.assertRaises(ValueError, self.temp.makeFriends, 3, 'Kowalski')

	def test_make_friends_person2_not_str(self):
		self.assertRaises(ValueError, self.temp.makeFriends, 'Kowalski', [])
	
	def test_make_friends_already_friends(self):
		self.assertRaises(ValueError, self.temp.makeFriends, 'Kowalski', 'Pionk')

	def test_get_friends_list(self):
		self.assertEqual(self.temp.getFriendsList('Pionk'),['Kowalski', 'Nowak', 'Bobkowska'])

	def test_get_friends_list_error(self):
		self.assertRaises(ValueError, self.temp.getFriendsList, 434)

	def test_get_friends_list_error_2(self):
		self.assertRaises(ValueError, self.temp.getFriendsList, 'sdfdsfd')

	def test_are_friends_positive(self):
		self.assertTrue(self.temp.areFriends('Pionk', 'Bobkowska'))

	def test_are_friends_false(self):
		self.assertFalse(self.temp.areFriends('Bobkowska', 'Malinowski'))

	def test_are_friends_person1_not_str(self):
		self.assertRaises(ValueError, self.temp.areFriends, 6546, 'Malinowski')

	def test_are_friends_person2_not_str(self):
		self.assertRaises(ValueError, self.temp.areFriends, 'Malinowski', None)

	def test_are_friends_persons_not_existing(self):
		self.assertRaises(ValueError, self.temp.areFriends, 'Malinowska', 'Kowalskiii')