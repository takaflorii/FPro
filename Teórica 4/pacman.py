import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

x = 60
y = 240
frame = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y -= 5
    if keys[pygame.K_DOWN]:
        y += 5
    if keys[pygame.K_LEFT]:
        x -= 5
    if keys[pygame.K_RIGHT]:
        x += 5

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 255, 0), (x, y), 20)
    if frame % 20 < 10:
        pygame.draw.polygon(screen, (0, 0, 0), ((x, y), (x+20, y-14), (x+20, y+14)))

    pygame.display.flip()
    frame += 1
    clock.tick(60)

pygame.quit()
sys.exit()