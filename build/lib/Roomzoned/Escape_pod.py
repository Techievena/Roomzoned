from sys import exit
from random import randint

class Escape_pod(object):
	def __init__(self):
		self.good_pod = randint(1,5)
		self.guess = 'null'

	def play(self):
		print("You rush through the ship desperately trying to make it to")
		print("the escape pod before the whole ship explodes. It seems like")
		print("hardly any Gothons are on the ship, so your run is clear of")
		print("interference. You get to the chamber with the escape pods, and")
		print("now need to pick one to take. Some of them could be damaged")
		print("but you don't have time to look. There's 5 pods, which one")
		print("do you take?")
		self.guess = input("[pod #]> ")
		if int(self.guess) == self.good_pod:
			self.win()
		else:
			result = self.lose()
		return result

	def win(self):
		print("You jump into pod %s and hit the eject button." % self.guess)
		print("The pod easily slides out into space heading to")
		print("the planet below. As it flies to the planet, you look")
		print("back and see your ship implode then explode like a")
		print("bright star, taking out the Gothon ship at the same")
		print("time. You won!")
		exit(0)

	def lose(self):
		print("You jump into pod %s and hit the eject button." % self.guess)
		print("The pod escapes out into the void of space, then")
		print("implodes as the hull ruptures, crushing your body")
		print("into jam jelly.")
		return 'death'