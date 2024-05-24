import pygame
from math import pi

pygame.init()
screen = pygame.display.set_mode((300,300))


color = (0, 0, 0)
font_size = 1
screen.fill((255,255,255))

pygame.display.update()
while True:
    
    pygame.event.pump()    
    user_input = list(map(str, input().split()))
    
    if user_input[1] == 'color':
        r = int(user_input[2])
        g = int(user_input[3])
        b = int(user_input[4])
        color = (r, g, b)

    elif user_input[1] == 'size':
        size = int(user_input[2])
        font_size = size

    elif user_input[1] == 'line':
        a = int(user_input[2])
        b = int(user_input[3])
        c = int(user_input[4])
        d = int(user_input[5])
        pygame.draw.line(screen, color, (a, b), (c, d), font_size)

    elif user_input[1] == 'circle':
        a = int(user_input[2])
        b = int(user_input[3])
        c = int(user_input[4])
        pygame.draw.circle(screen, color, (a, b), c, font_size)
        
    elif user_input[1] == 'polygon':
        pygame.draw.polygon(screen, color, [(int(user_input[2]), int(user_input[3])), (int(user_input[4]), int(user_input[5])), (int(user_input[6]), int(user_input[7])), (int(user_input[8]), int(user_input[9]))], font_size)

    
    elif user_input[1] == 'drawing':
        pygame.image.save(screen, 'draw.png')
        break

    pygame.display.update()

