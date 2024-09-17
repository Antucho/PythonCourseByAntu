class Keyboard:
	def __init__(self, language, connection):
		self.language = language
		self.connection = connection

my_keyboard = Keyboard('English', 'wired')
print(my_keyboard.language)
print(my_keyboard.connection)

class AboutMe:
	def __init__(self, name, address, occupation):
		self.name = name
		self.address = address
		self.occupation = occupation
	def talk(self):
		print(f"My name is {self.name}, I live in {self.address} And I am a {self.occupation}")

simanta = AboutMe("Simanta Chowdhury", "Chittagong", "Student")
simanta.talk()
