from random import randint

class Laser_weapon_armory(object):
	def __init__(self):
		self.code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
		self.guesses = 0

	def play(self):
		print("You do a dive roll into the Weapon Armory, crouch and scan the room")
		print("for more Gothons that might be hiding. It's dead quiet, too quiet.")
		print("You stand up and run to the far side of the room and find the")
		print("neutron bomb in its container. There's a keypad lock on the box")
		print("and you need the code to get the bomb out. If you get the code")
		print("wrong 10 times then the lock closes forever and you can't")
		print("get the bomb. The code is 3 digits.")

		guess = input("[keypad]> ")
		
		while guess != self.code and self.guesses < 10:
			print("BZZZZEDDD!")
			self.guesses += 1
			guess = input("[keypad]> ")
		if guess == self.code:
			result = self.win()
		else:
			result = self.lose()
		return result

	def win(self):
		print("The container clicks open and the seal breaks, letting gas out.")
		print("You grab the neutron bomb and run as fast as you can to the")
		print("bridge where you must place it in the right spot.")
		return 'the_bridge'

	def lose(self):
		print("The lock buzzes one last time and then you hear a sickening")
		print("melting sound as the mechanism is fused together.")
		print("You decide to sit there, and finally the Gothons blow up the")
		print("ship from their ship and you die.")
		return 'death'
