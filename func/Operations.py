import os 

class Operations:

	def readLines(self, filepath):
		with open (filepath, 'r') as file:
			data = []
			for line in file:
				data.append(line.strip())
			return data

	def writeSomethingInFile(self, filepath, toWrite):
		with open (filepath, 'w') as file:
			file.write(toWrite)
		return toWrite
	
	def deleteFile(self, filepath):
		if os.path.exists(filepath):
				os.remove(filepath)
				return True
		else:
			raise ValueError('Wrong path')