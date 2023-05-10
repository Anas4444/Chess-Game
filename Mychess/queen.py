import pygame
from background import Background

class Queen(Background):

    def __init__(self, settings, screen):
        Background.__init__(self, settings, screen)
        self.defaut_rect = settings.rect_size

        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.white = settings.WHITE
        self.color = (20, 100, 20)

        self.white_queen_image = pygame.image.load("Pieces\white_queen.png")
        self.black_queen_image = pygame.image.load("Pieces\\black_queen.png")

        self.white_queen_imageu = pygame.transform.scale(self.white_queen_image,
                                                         (int(80 * (self.defaut_rect / 100)),
                                                          int(80 * (self.defaut_rect / 100))))
        self.black_queen_imageu = pygame.transform.scale(self.black_queen_image,
                                                         (int(80 * (self.defaut_rect / 100)),
                                                          int(80 * (self.defaut_rect / 100))))

        self.white_queen_image.set_colorkey(self.white)
        self.black_queen_image.set_colorkey(self.white)
        self.white_queen_imageu.set_colorkey(self.white)
        self.black_queen_imageu.set_colorkey(self.white)

        self.white_queen_rect = self.white_queen_imageu.get_rect()
        self.black_queen_rect = self.black_queen_imageu.get_rect()

        self.white_big_queen_rect = pygame.Rect(self.white_queen_rect)
        self.black_big_queen_rect = pygame.Rect(self.black_queen_rect)

        self.white_queen_move = ['']
        self.black_queen_move = ['']

        self.white_queen_attack = []
        self.black_queen_attack = []

        self.white_queen_position = ["d", 1]
        self.black_queen_position = ["d", 8]

        self.white_queen_clicked = False
        self.black_queen_clicked = False

        self.white_queen_death = False
        self.black_queen_death = False

        self.white_queen_rect.center = (
        self.screen_rect.width / 2 - (self.defaut_rect * 0.5), self.screen_rect.height / 2 + (self.defaut_rect * 3.5))
        self.black_queen_rect.center = (
        self.screen_rect.width / 2 - (self.defaut_rect * 0.5), self.screen_rect.height / 2 - (self.defaut_rect * 3.5))

    def update_white_queen(self):
        pass

    def update_black_queen(self):
        pass

    def draw_big_queen(self, piece):
        piece.draw_big_piece(self.white_big_queen_rect, self.white_queen_rect, self.white_queen_clicked, self.white_queen_image, self.white_queen_death)
        piece.draw_big_piece(self.black_big_queen_rect, self.black_queen_rect, self.black_queen_clicked, self.black_queen_image, self.black_queen_death)

    def draw_circle(self, settings):
        settings.draw_circle(self.screen, self.white_queen_clicked, self.board_rect)
        settings.draw_circle(self.screen, self.black_queen_clicked, self.board_rect)

    def draw_queen(self):
        if not (self.white_queen_death or self.white_queen_clicked):
            self.screen.blit(self.white_queen_imageu, self.white_queen_rect)

        if not (self.black_queen_death or self.black_queen_clicked):
            self.screen.blit(self.black_queen_imageu, self.black_queen_rect)

    def draw_queen_mvts(self, settings):

        if self.white_queen_move[0] != "":
            self.screen.fill((155, 240, 20), self.white_queen_move[0])

        if len(self.white_queen_move) > 1:
            for mvt in self.white_queen_move[1:]:
                pygame.draw.circle(self.screen, (130, 151, 105), mvt.center, int(self.defaut_rect / 7.5))

        if (len(self.white_queen_attack) > 0):
            for attack in self.white_queen_attack:
                self.screen.fill((255, 0, 0), attack)
                settings.draw_lines(self.screen, attack, (180, 0, 0))

        if self.black_queen_move[0] != "":
            self.screen.fill((155, 240, 20), self.black_queen_move[0])

        if len(self.black_queen_move) > 1:
            for mvt in self.black_queen_move[1:]:
                pygame.draw.circle(self.screen, (130, 151, 105), mvt.center, int(self.defaut_rect / 7.5))

        if (len(self.black_queen_attack) > 0):
            for attack in self.black_queen_attack:
                self.screen.fill((255, 0, 0), attack)
                settings.draw_lines(self.screen, attack, (180, 0, 0))

