from sys import exit
from random import randint

class Death(object):
	def __init__(self):
		self.quips = [
		"You died. You kinda suck at this.",
		"Your mom would be proud. If she were smarter.",
		"Such a loser.",
		"I have a small puppy that's better at this."
		]

	def play(self):
		print(self.quips[randint(0, len(self.quips)-1)])
		exit(1)