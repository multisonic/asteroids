import pygame
from constants import *
from player import *

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	newplayer = Player((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))
	dt = 0


	#GAME LOOP
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		# newplayer.update(dt)
		for player in updatable:
			player.update(dt)
	
		screen.fill("black")
		for player in drawable:
			player.draw(screen)
		# newplayer.draw(screen)
		pygame.display.flip()

		# limit framerate to 60 FPS
		dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
