class Central_corridor(object):
	def play(self):
		print("The Gothons of Planet Percal #25 have invaded your ship and destroyed")
		print("your entire crew. You are the last surviving member and your last")
		print("mission is to get the neutron destruct bomb from the Weapons Armory,")
		print("put it in the bridge, and blow the ship up after getting into an ")
		print("escape pod.")
		print("\n")
		print("You're running down the central corridor to the Weapons Armory when")
		print("a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume")
		print("flowing around his hate filled body. He's blocking the door to the")
		print("Armory and about to pull a weapon to blast you.")
		while True:
			action = input("> ")
			try:
				room = getattr(self, action)
				move = room()
				return move
			except Exception:
				print("DOES NOT COMPUTE!")
			

	def shoot(self):
		print("Quick on the draw you yank out your blaster and fire it at the Gothon.")
		print("His clown costume is flowing and moving around his body, which throws")
		print("off your aim. Your laser hits his costume but misses him entirely. This")
		print("completely ruins his brand new costume his mother bought him, which")
		print("makes him fly into an insane rage and blast you repeatedly in the face until")
		print("you are dead. Then he eats you.")
		return 'death'

	def dodge(self):
		print("Like a world class boxer you dodge, weave, slip and slide right")
		print("as the Gothon's blaster cranks a laser past your head.")
		print("In the middle of your artful dodge your foot slips and you")
		print("bang your head on the metal wall and pass out.")
		print("You wake up shortly after only to die as the Gothon stomps on")
		print("your head and eats you.")
		return 'death'

	def tell_a_joke(self):
		print("Lucky for you they made you learn Gothon insults in the academy.")
		print("You tell the one Gothon joke you know:")
		print("Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur")
		print("The Gothon stops, tries not to laugh, then busts out laughing and can't")
		print("While he's laughing you run up and shoot him square in the head")
		print("putting him down, then jump through the Weapon Armory door.")
		return 'laser_weapon_armory'
