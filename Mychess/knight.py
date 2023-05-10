import pygame
from background import Background

class Knight(Background):

    def __init__(self, settings, screen):
        Background.__init__(self, settings, screen)
        self.defaut_rect = settings.rect_size

        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.white = settings.WHITE
        self.black = settings.BLACK
        self.color = (20, 100, 20)

        self.white_knight_image = pygame.image.load("Pieces\white_knight.png")
        self.black_knight_image = pygame.image.load("Pieces\\black_knight.png")

        self.white_knight_imageu = pygame.transform.scale(self.white_knight_image,
                                                         (int(80 * (self.defaut_rect / 100)),
                                                          int(80 * (self.defaut_rect / 100))))
        self.black_knight_imageu = pygame.transform.scale(self.black_knight_image,
                                                         (int(80 * (self.defaut_rect / 100)),
                                                          int(80 * (self.defaut_rect / 100))))

        self.white_knight_image.set_colorkey(self.white)
        self.black_knight_image.set_colorkey(self.white)
        self.white_knight_imageu.set_colorkey(self.white)
        self.black_knight_imageu.set_colorkey(self.white)

        self.white_knight_rect = self.white_knight_imageu.get_rect()
        self.black_knight_rect = self.black_knight_imageu.get_rect()

        self.white_knight_rects = {"N1": pygame.Rect(0, 0, self.white_knight_rect.width, self.white_knight_rect.height),
                                   "N2": pygame.Rect(0, 0, self.white_knight_rect.width, self.white_knight_rect.height)}

        self.black_knight_rects = {"N1": pygame.Rect(0, 0, self.black_knight_rect.width, self.black_knight_rect.height),
                                   "N2": pygame.Rect(0, 0, self.black_knight_rect.width, self.black_knight_rect.height)}

        self.white_big_knight_rects = {"N1": pygame.Rect(self.white_knight_rects["N1"]),
                                       "N2": pygame.Rect(self.white_knight_rects["N2"])}

        self.black_big_knight_rects = {"N1": pygame.Rect(self.white_knight_rects["N1"]),
                                       "N2": pygame.Rect(self.white_knight_rects["N2"])}

        self.white_knight_position = {"N1": ["b", 1],
                                      "N2": ["g", 1]}
        self.black_knight_position = {"N1": ["b", 8],
                                      "N2": ["g", 8]}

        self.white_knight_move = {"N1": [""],
                                   "N2": [""]}

        self.black_knight_move = {"N1": [""],
                                  "N2": [""]}

        self.white_knight_attack = {"N1": [],
                                    "N2": []}

        self.black_knight_attack = {"N1": [],
                                    "N2": []}

        self.white_knight_clicked = {"N1": False,
                                     "N2": False}

        self.black_knight_clicked = {"N1": False,
                                     "N2": False}

        self.white_knight_death = {"N1": False,
                                   "N2": False}

        self.black_knight_death = {"N1": False,
                                   "N2": False}

        self.white_knight_rects["N1"].center = (
            self.screen_rect.width / 2 - (self.defaut_rect * 2.5),
            self.screen_rect.height / 2 + (self.defaut_rect * 3.5))
        self.white_knight_rects["N2"].center = (
            self.screen_rect.width / 2 + (self.defaut_rect * 2.5),
            self.screen_rect.height / 2 + (self.defaut_rect * 3.5))

        self.black_knight_rects["N1"].center = (
            self.screen_rect.width / 2 - (self.defaut_rect * 2.5),
            self.screen_rect.height / 2 - (self.defaut_rect * 3.5))
        self.black_knight_rects["N2"].center = (
            self.screen_rect.width / 2 + (self.defaut_rect * 2.5),
            self.screen_rect.height / 2 - (self.defaut_rect * 3.5))

    def update_white_knight(self):
        pass

    def update_black_knight(self):
        pass

    def draw_big_knight(self, piece):
        piece.draw_big_piece(self.white_big_knight_rects, self.white_knight_rects, self.white_knight_clicked, self.white_knight_image, self.white_knight_death)
        piece.draw_big_piece(self.black_big_knight_rects, self.black_knight_rects, self.black_knight_clicked, self.black_knight_image, self.black_knight_death)

    def draw_circle(self, settings):
        settings.draw_circle(self.screen, self.white_knight_clicked, self.board_rect)
        settings.draw_circle(self.screen, self.black_knight_clicked, self.board_rect)

    def draw_knight(self):
        for key0, rect in self.white_knight_rects.items():
            if not (self.white_knight_death[key0] or self.white_knight_clicked[key0]):
                self.screen.blit(self.white_knight_imageu, rect)

        for key1, rect in self.black_knight_rects.items():
            if not (self.black_knight_death[key1] or self.black_knight_clicked[key1]):
                self.screen.blit(self.black_knight_imageu, rect)

    def draw_knight_mvts(self, settings):

        for key, knight_mvts in self.white_knight_move.items():
            if knight_mvts[0] != "":
                self.screen.fill((155, 240, 20), knight_mvts[0])

            if len(knight_mvts) > 1:
                for mvt in knight_mvts[1:]:
                    pygame.draw.circle(self.screen, (130, 151, 105), mvt.center, int(self.defaut_rect / 7.5))

            if (len(self.white_knight_attack[key]) > 0):
                for attack in self.white_knight_attack[key]:
                    self.screen.fill((255, 0, 0), attack)
                    settings.draw_lines(self.screen, attack, (180, 0, 0))

        for key, knight_mvts in self.black_knight_move.items():
            if knight_mvts[0] != "":
                self.screen.fill((155, 240, 20), knight_mvts[0])

            if len(knight_mvts) > 1:
                for mvt in knight_mvts[1:]:
                    pygame.draw.circle(self.screen, (130, 151, 105), mvt.center, int(self.defaut_rect / 7.5))

            if (len(self.black_knight_attack[key]) > 0):
                for attack in self.black_knight_attack[key]:
                    self.screen.fill((255, 0, 0), attack)
                    settings.draw_lines(self.screen, attack, (180, 0, 0))

