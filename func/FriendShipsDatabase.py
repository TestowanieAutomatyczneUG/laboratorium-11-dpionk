from func.FriendShips import FriendShips

class FriendShipsDatabase:
	def __init__(self):
		self.database = FriendShips({
			'Pionk': ['Kowalski', 'Nowak', 'Bobkowska'],
			'Kowalski': ['Pionk'],
			'Nowak': ['Pionk'],
			'Bobkowska': ['Pionk'],
			'Malinowski': []
		})
	
	def makeFriends(self,person1,person2):
		self.database.makeFriends(person1, person2)

	def getFriendsList(self, person):
		return self.database.getFriendsList(person)

	def areFriends(self, person1, person2):
		return self.database.areFriends(person1, person2)