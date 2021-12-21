class Note:
    def __init__(self, name, note):
        if name is None:
            raise Exception('Name nie może być None')
        elif type(name) is not str:
            raise Exception('Name musi być ciągiem znaków')
        elif not name:
            raise Exception('Name nie może być puste')
        elif type(note) is not float:
            raise Exception('Note musi być typu float')
        elif not 2 <= note <= 6:
            raise Exception('Note musi być liczbą z przedziału <2,6>')
        self.name = name
        self.note = note
    
    def getName(self):
        return self.name

    def getNote(self):
        return self.note