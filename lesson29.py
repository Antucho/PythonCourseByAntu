class Keyboard:
	def definition(self):
		print("The keyboard is an input device")
	def number_of_keys(self):
		print("My keyboard has 101 keys")


my_keyboard = Keyboard()
my_keyboard.definition()
my_keyboard.number_of_keys()
my_keyboard.brand = "A4Tech"
print(my_keyboard.brand)

new_keyboard = Keyboard()
new_keyboard.definition()
new_keyboard.brand = "Logitech"
print(new_keyboard.brand)
