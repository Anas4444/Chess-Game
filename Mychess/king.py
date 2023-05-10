import pygame
from background import Background

class King(Background):

    def __init__(self, settings, screen):
        Background.__init__(self, settings, screen)
        self.defaut_rect = settings.rect_size

        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.white = settings.WHITE
        self.color = (20, 100, 20)

        self.white_king_image = pygame.image.load("Pieces\white_king.png")
        self.white_king_imageu = pygame.transform.scale(self.white_king_image, (
                                                       int(80 * (self.defaut_rect / 100)),
                                                       int(80 * (self.defaut_rect / 100))))

        self.black_king_image = pygame.image.load("Pieces\\black_king.png")
        self.black_king_imageu = pygame.transform.scale(self.black_king_image, (
                                                       int(80 * (self.defaut_rect / 100)),
                                                       int(80 * (self.defaut_rect / 100))))

        self.white_king_image.set_colorkey(self.white)
        self.black_king_image.set_colorkey(self.white)
        self.white_king_imageu.set_colorkey(self.white)
        self.black_king_imageu.set_colorkey(self.white)

        self.white_king_rect = self.white_king_imageu.get_rect()
        self.black_king_rect = self.black_king_imageu.get_rect()

        self.white_big_king_rect = pygame.Rect(self.white_king_rect)
        self.black_big_king_rect = pygame.Rect(self.black_king_rect)

        self.white_king_move = ['']
        self.black_king_move = ['']

        self.white_king_no_move = True
        self.black_king_no_move = True
        self.wpc = None
        self.bpc = None

        self.white_king_attack = []
        self.black_king_attack = []
        self.white_king_death = False
        self.black_king_death = False

        self.white_king_position = ["e", 1]
        self.black_king_position = ["e", 8]

        self.white_check = False
        self.black_check = False

        self.wk = [False, False, False, False, False]
        self.bk = [False, False, False, False, False]
        self.white_check_mvt = []
        self.black_check_mvt = []

        self.white_king_clicked = False
        self.black_king_clicked = False

        self.white_king_death = False
        self.black_king_death = False

        self.white_king_rect.center = (self.screen_rect.width / 2 + (self.defaut_rect * 0.5), self.screen_rect.height / 2 + (self.defaut_rect * 3.5))
        self.black_king_rect.center = (self.screen_rect.width / 2 + (self.defaut_rect * 0.5), self.screen_rect.height / 2 - (self.defaut_rect * 3.5))

    def update_white_king(self):
        pass

    def update_black_king(self):
        pass

    def draw_big_king(self, piece):
        piece.draw_big_piece(self.white_big_king_rect, self.white_king_rect, self.white_king_clicked, self.white_king_image, self.white_king_death)
        piece.draw_big_piece(self.black_big_king_rect, self.black_king_rect, self.black_king_clicked, self.black_king_image, self.black_king_death)

    def draw_circle(self, settings):
        settings.draw_circle(self.screen, self.white_king_clicked, self.board_rect)
        settings.draw_circle(self.screen, self.black_king_clicked, self.board_rect)

    def draw_king(self):
        if not self.white_king_clicked:
            self.screen.blit(self.white_king_imageu, self.white_king_rect)

        if not self.black_king_clicked:
            self.screen.blit(self.black_king_imageu, self.black_king_rect)

    def draw_king_mvts(self, settings):

        if self.white_king_move[0] != "" and not self.white_check:
            self.screen.fill((155, 240, 20), self.white_king_move[0])

        if len(self.white_king_move) > 1:
            for mvt in self.white_king_move[1:]:
                pygame.draw.circle(self.screen, (130, 151, 105), mvt.center, int(self.defaut_rect / 7.5))

        if (len(self.white_king_attack) > 0):
            for attack in self.white_king_attack:
                self.screen.fill((255, 0, 0), attack)
                settings.draw_lines(self.screen, attack, (180, 0, 0))

        if self.black_king_move[0] != "" and not self.black_check:
            self.screen.fill((155, 240, 20), self.black_king_move[0])

        if len(self.black_king_move) > 1:
            for mvt in self.black_king_move[1:]:
                pygame.draw.circle(self.screen, (130, 151, 105), mvt.center, int(self.defaut_rect / 7.5))

        if (len(self.black_king_attack) > 0):
            for attack in self.black_king_attack:
                self.screen.fill((255, 0, 0), attack)
                settings.draw_lines(self.screen, attack, (180, 0, 0))

    def draw_white_check(self):
        if self.white_check:
            pygame.draw.circle(self.screen, (180, 0, 0), self.white_check_mvt[0].center, int(self.defaut_rect / 2))
            pygame.draw.circle(self.screen, (255, 0, 0), self.white_check_mvt[0].center, int(self.defaut_rect / 2.5))
            self.screen.fill((155, 240, 20), self.white_check_mvt[1])

    def draw_black_check(self):
        if self.black_check:
            pygame.draw.circle(self.screen, (180, 0, 0), self.black_check_mvt[0].center, int(self.defaut_rect / 2))
            pygame.draw.circle(self.screen, (255, 0, 0), self.black_check_mvt[0].center, int(self.defaut_rect / 2.5))
            self.screen.fill((155, 240, 20), self.black_check_mvt[1])

