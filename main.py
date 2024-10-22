import pygame
from constants import *

def main():
	pygame.init() 	# intialize pygame
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))	# set the size of the display area to our width / height in constants.py
	clock = pygame.time.Clock() # create clock object
	dt = 0 # create an empty dt (delta time) variable
	
	while True: # game loop
		# helpful logic to allow mac users to quit with close window button
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
	
		screen.fill("black") # fill the game window with black
		pygame.display.flip() # refresh the screen

		# limit framerate to 60 FPS
		dt = clock.tick(60) /1000 #clock.tick() returns amount of time since last called (delta time)

if __name__ == "__main__":
    main()
