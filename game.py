import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 560))
a = pygame.Rect(50, 50, 700, 450)
b = pygame.Rect(75, 70, 650, 75)
с = pygame.Rect(75, 180, 650, 75)
d = pygame.Rect(75, 290, 650, 75)
f = pygame.Rect(75, 400, 650, 75)
pygame.draw.rect(screen, (250, 250, 250), a, 0)
pygame.draw.rect(screen, (0, 0, 0), b, 0)
pygame.draw.rect(screen, (0, 0, 0), с, 0)
pygame.draw.rect(screen, (0, 0, 0), d, 0)
pygame.draw.rect(screen, (0, 0, 0), f, 0)

font = pygame.font.SysFont('yugothicuisemilight', 50)
img = font.render('Menu', True, (255, 255, 255))
screen.blit(img, (325, 1))

font = pygame.font.SysFont('yugothicuisemilight', 50)
img = font.render('Quit', True, (255, 255, 255))
screen.blit(img, (350, 410))

font = pygame.font.SysFont('yugothicuisemilight', 50)
img = font.render('New Game', True, (255, 255, 255))
screen.blit(img, (265, 82))

font = pygame.font.SysFont('yugothicuisemilight', 50)
img = font.render('Resume', True, (255, 255, 255))
screen.blit(img, (310, 192))

font = pygame.font.SysFont('yugothicuisemilight', 50)
img = font.render('Donate', True, (255, 255, 255))
screen.blit(img, (315, 300))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
