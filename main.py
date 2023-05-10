# main module for the game

import pygame

pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("The Unlit Spire")

background = pygame.image.load('assets/bg1-unlit-spire.jpg').convert_alpha()
# function to draw the background
def draw_bg():
    screen.blit(background, (0, 0))


# Game loop
run = True
while run:

    # draw background
    draw_bg()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # update display window
    pygame.display.update()

pygame.quit()
