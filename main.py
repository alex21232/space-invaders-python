# import requerid library
import pygame

#initialize pygame
pygame.init()

#Window size
screen_width = 800
screen_height = 600

# size variable
size = (screen_width, screen_height)

#Display the window
screen = pygame.display.set_mode( size )

#game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False