import sys
import pygame

class image:
    def __init__(self, rect):
        self.rect = pygame.Rect(rect)
        self.rect.center = screen.get_rect().center
        self.click = False
        self.image = pygame.image.load("Pieces\White_pawn.png")

    def update(self, screen):
        if self.click:
            self.big_image = pygame.transform.scale(self.image, (int((self.rect.width/100)*120), int((self.rect.height/100)*120)))
            mx, my = pygame.mouse.get_pos()
            self.rect.center = (mx, my)
            screen.blit(self.big_image, self.rect)
        else:
            screen.blit(self.image, self.rect)


pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
image = image((0, 0, 100, 100))
image.rect.center = screen.get_rect().center

print(image.image.get_rect()[2])

while True:

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if image.rect.collidepoint(event.pos):
                image.click = True
        elif event.type == pygame.MOUSEBUTTONUP:
            image.click = False

        elif event.type == pygame.QUIT:
            sys.exit()

    screen.fill((255, 255, 255))

    image.update(screen)

    pygame.display.flip()
    clock.tick(60)


