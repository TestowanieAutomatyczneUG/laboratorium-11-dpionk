class FriendShips:
	def __init__(self, friendships):
		self.friendships = friendships
	
	def addFriend(self, person, friend):
		if person not in self.friendships.keys():
			raise ValueError('Nie ma takiej osoby')
		else:
			self.friendships[person].append(friend)
			return self.friendships[person]

	def getFriendsList(self, person):
		if type(person) is not str:
			raise ValueError('Osoba musi być typu string')
		elif person not in self.friendships.keys():
			raise ValueError('Nie ma takiej osoby')
		return self.friendships[person]

	def areFriends(self, person1, person2):
		if type(person1) is not str or type(person2) is not str:
			raise ValueError('Osoba musi być typu string')
		if person1 not in self.friendships.keys() or person2 not in self.friendships.keys() :
			raise ValueError('Nie ma takiej osoby')
		elif person1 in self.friendships[person2] and person2 in self.friendships[person1]:
			return True
		return False

	def makeFriends(self, person1, person2):
		if type(person1) is not str or type(person2) is not str:
			raise ValueError('Osoba musi być typu string')
		elif person1 in self.friendships.keys() and person2 in self.friendships[person1]:
			raise ValueError('Relacja już istnieje')
		self.addFriend(person1, person2)
		self.addFriend(person2, person1)
		return self.friendships

	