from sys import exit
from random import randint
from Roomzoned.Central_corridor import Central_corridor
from Roomzoned.Escape_pod import Escape_pod
from Roomzoned.Laser_weapon_armory import Laser_weapon_armory
from Roomzoned.The_bridge import The_bridge
from Roomzoned.Death import Death

def main():
	central_corridor=Central_corridor()
	escape_pod=Escape_pod()
	laser_weapon_armory=Laser_weapon_armory()
	the_bridge=The_bridge()
	death=Death()
	game={'central_corridor':central_corridor,
	      'escape_pod':escape_pod,
	      'laser_weapon_armory':laser_weapon_armory,
	      'the_bridge':the_bridge,
	      'death':death}

	room = 'central_corridor'
	while True:
			print("\n--------")
			print(room)
			room = game[room].play()


if __name__ == '__main__':
	main()