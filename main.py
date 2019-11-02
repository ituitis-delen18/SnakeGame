""""
    Emirhan Delen
    Snake Game: Made with python/pygame
    Made for only improving myself on python/pygame
"""

import pygame,sys,random

pygame.init()

window_size = (800,600)

screen = pygame.display.set_mode(window_size)

GREY = (128,128,128)

snakes = [[142,142], [142,162] , [142,182] , [162,182]]

all_points = []

for i in range(0,40):
    for j in range(0,30):
        all_points.append([(20 * i) + 2,(20 * j) + 2])

FPS = pygame.time.Clock()

def gameLoop():
    top = False
    bottom = False
    right = True
    left = False
    hareketDegistir = False
    elma = [310, 310]
    gecici_rect = []
    while True:
        FPS.tick(10)
        elma_rect = pygame.Rect(elma[0], elma[1], 3, 3)
        screen.fill((255,255,255))
        pygame.draw.circle(screen, (0,0,255), (elma[0], elma[1]), 3)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and (not right) and (not hareketDegistir):
                    hareketDegistir = True
                    top = False
                    bottom = False
                    right = False
                    left = True
                elif event.key == pygame.K_w and (not bottom) and (not hareketDegistir):
                    hareketDegistir = True
                    top = True
                    bottom = False
                    right = False
                    left = False
                elif event.key == pygame.K_d and (not left) and (not hareketDegistir):
                    hareketDegistir = True
                    top = False
                    bottom = False
                    right = True
                    left = False
                elif event.key == pygame.K_s and (not top) and (not hareketDegistir):
                    hareketDegistir = True
                    top = False
                    bottom = True
                    right = False
                    left = False
        hareketDegistir = False
        snake_rects = []
        for ij in snakes:
            snake_rects.append(pygame.Rect(ij[0], ij[1], 16, 16))
        if right:
            for i in range(1,len(snakes)):
                j = len(snakes) - i
                snakes[j][0] = snakes[j - 1][0]
                snakes[j][1] = snakes[j - 1][1]
            snakes[0][0] += 20
            if snakes[0][0] > 780:
                snakes[0][0] = 0
        elif left:
            for i in range(1, len(snakes)):
                j = len(snakes) - i
                snakes[j][0] = snakes[j - 1][0]
                snakes[j][1] = snakes[j - 1][1]
            snakes[0][0] -= 20
            if snakes[0][0] < 0:
                snakes[0][0] = 780
        elif bottom:
            for i in range(1, len(snakes)):
                j = len(snakes) - i
                snakes[j][0] = snakes[j - 1][0]
                snakes[j][1] = snakes[j - 1][1]
            snakes[0][1] += 20
            if snakes[0][1] > 580:
                snakes[0][1] = 0
        elif top:
            for i in range(1,len(snakes)):
                j = len(snakes) - i
                snakes[j][0] = snakes[j - 1][0]
                snakes[j][1] = snakes[j - 1][1]
            snakes[0][1] -= 20
            if snakes[0][1] < 0:
                snakes[0][1] = 580

        for snake in snakes:
            pygame.draw.rect(screen, (255, 0, 0), (snake[0], snake[1], 16,16))

        for snakee in snake_rects[1:]:
            if snake_rects[0].colliderect(snakee):
                print("Game Over")
                #sys.exit()
        if snake_rects[0].colliderect(elma_rect):
            print("point!")
            gecici_rect.append(elma_rect)
            possible_points = []
            for i in all_points:
                equal = False
                for j in snakes:
                    if i == j:
                        equal = True
                if not equal:
                    possible_points.append(i)
            x,y = random.choice(possible_points)
            elma = [x + 8, y + 8]
        for i in gecici_rect:
            if snake_rects[len(snake_rects) - 1].colliderect(i):
                snakes.append([i[0], i[1]])
                gecici_rect.pop(gecici_rect.index(i))
        pygame.display.update()

gameLoop()