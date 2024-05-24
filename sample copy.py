import pygame

pygame.init()
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("pygame window")

size = 1
color = (0, 0, 0)
white = (255, 255, 255)

screen.fill(white)
pygame.display.update()

while True:
    pygame.event.pump()

    while True:
        command = input("Enter Command :").strip().split()

        if command[0] == "end" and command[1] == "drawing":
            pygame.image.save(display, 'draw.png')
            break

        elif command[0] == "change" and command[1] == "size":
            size = int(command[2])

        elif command[0] == "change" and command[1] == "color":
            color = (int(command[2]), int(command[3]), int(command[4]))

        elif command[0] == "draw" and command[1] == "line":
            pygame.draw.line(screen, color, (int(command[2]), int(command[3])), (int(command[4]), int(command[5])), size)
            pygame.display.update()

        elif command[0] == "draw" and command[1] == "circle":
            pygame.draw.circle(screen, color, (int(command[2]), int(command[3])), int(command[4]), size)
            pygame.display.update()

        elif command[0] == "draw" and command[1] == "polygon":
            pygame.draw.polygon(screen, color, [(int(command[2]), int(command[3])), (int(command[4]), int(command[5])), (int(command[6]), int(command[7])), (int(command[8]), int(command[9]))], size)
            pygame.display.update()

    pygame.display.update()
