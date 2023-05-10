import pygame
from background import Background

class Rook(Background):

    def __init__(self, settings, screen):
        Background.__init__(self, settings, screen)

        self.defaut_rect = settings.rect_size

        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.white = settings.WHITE
        self.color = (20, 100, 20)

        self.white_rook_image = pygame.image.load("Pieces\White_rook.png")
        self.black_rook_image = pygame.image.load("Pieces\\black_rook.png")

        self.white_rook_imageu = pygame.transform.scale(self.white_rook_image,
                                                         (int(80 * (self.defaut_rect / 100)),
                                                          int(80 * (self.defaut_rect / 100))))
        self.black_rook_imageu = pygame.transform.scale(self.black_rook_image,
                                                         (int(80 * (self.defaut_rect / 100)),
                                                          int(80 * (self.defaut_rect / 100))))

        self.white_rook_image.set_colorkey(self.white)
        self.black_rook_image.set_colorkey(self.white)
        self.white_rook_imageu.set_colorkey(self.white)
        self.black_rook_imageu.set_colorkey(self.white)

        self.white_rook_rect = self.white_rook_imageu.get_rect()
        self.black_rook_rect = self.black_rook_imageu.get_rect()

        self.white_rook_rects = {"R1": pygame.Rect(0, 0, self.white_rook_rect.width, self.white_rook_rect.height),
                                 "R2": pygame.Rect(0, 0, self.white_rook_rect.width, self.white_rook_rect.height)}

        self.black_rook_rects = {"R1": pygame.Rect(0, 0, self.black_rook_rect.width, self.black_rook_rect.height),
                                 "R2": pygame.Rect(0, 0, self.black_rook_rect.width, self.black_rook_rect.height)}

        self.white_rook_move = {"R1": [""],
                                "R2": [""]}

        self.black_rook_move = {"R1": [""],
                                "R2": [""]}

        self.white_rook_no_move = {"R1": True,
                                   "R2": True}

        self.black_rook_no_move = {"R1": True,
                                   "R2": True}

        self.white_rook_attack = {"R1": [],
                                  "R2": []}

        self.black_rook_attack = {"R1": [],
                                  "R2": []}

        self.white_big_rook_rects = {"R1": pygame.Rect(self.white_rook_rects["R1"]),
                                     "R2": pygame.Rect(self.white_rook_rects["R2"])}

        self.black_big_rook_rects = {"R1": pygame.Rect(self.white_rook_rects["R1"]),
                                     "R2": pygame.Rect(self.white_rook_rects["R2"])}

        self.white_rook_position = {"R1": ["a", 1],
                                    "R2": ["h", 1]}
        self.black_rook_position = {"R1": ["a", 8],
                                    "R2": ["h", 8]}

        self.white_rook_clicked = {"R1": False,
                                   "R2": False}

        self.black_rook_clicked = {"R1": False,
                                   "R2": False}

        self.white_rook_death = {"R1": False,
                                 "R2": False}

        self.black_rook_death = {"R1": False,
                                 "R2": False}

        self.white_rook_rects["R1"].center = (
            self.screen_rect.width / 2 - (self.defaut_rect * 3.5),
            self.screen_rect.height / 2 + (self.defaut_rect * 3.5))
        self.white_rook_rects["R2"].center = (
            self.screen_rect.width / 2 + (self.defaut_rect * 3.5),
            self.screen_rect.height / 2 + (self.defaut_rect * 3.5))

        self.black_rook_rects["R1"].center = (
            self.screen_rect.width / 2 - (self.defaut_rect * 3.5),
            self.screen_rect.height / 2 - (self.defaut_rect * 3.5))
        self.black_rook_rects["R2"].center = (
            self.screen_rect.width / 2 + (self.defaut_rect * 3.5),
            self.screen_rect.height / 2 - (self.defaut_rect * 3.5))

    def draw_circle(self, settings):
        settings.draw_circle(self.screen, self.white_rook_clicked, self.board_rect)
        settings.draw_circle(self.screen, self.black_rook_clicked, self.board_rect)

    def draw_big_rook(self, piece):
        piece.draw_big_piece(self.white_big_rook_rects, self.white_rook_rects, self.white_rook_clicked, self.white_rook_image, self.white_rook_death)
        piece.draw_big_piece(self.black_big_rook_rects, self.black_rook_rects, self.black_rook_clicked, self.black_rook_image, self.black_rook_death)

    def draw_rook(self):
        for key0, rect in self.white_rook_rects.items():
            if not (self.white_rook_death[key0] or self.white_rook_clicked[key0]):
                self.screen.blit(self.white_rook_imageu, rect)

        for key1, rect in self.black_rook_rects.items():
            if not (self.black_rook_death[key1] or self.black_rook_clicked[key1]):
                self.screen.blit(self.black_rook_imageu, rect)

    def draw_rook_mvts(self, settings):

        for key, rook_mvts in self.white_rook_move.items():
            if rook_mvts[0] != "":
                self.screen.fill((155, 240, 20), rook_mvts[0])


            if len(rook_mvts) > 1:
                for mvt in rook_mvts[1:]:
                    pygame.draw.circle(self.screen, (130, 151, 105), mvt.center, int(self.defaut_rect / 7.5))


            if (len(self.white_rook_attack[key]) > 0):
                for attack in self.white_rook_attack[key]:
                    self.screen.fill((255, 0, 0), attack)
                    settings.draw_lines(self.screen, attack, (180, 0, 0))

        for key, rook_mvts in self.black_rook_move.items():
            if rook_mvts[0] != "":
                self.screen.fill((155, 240, 20), rook_mvts[0])


            if len(rook_mvts) > 1:
                for mvt in rook_mvts[1:]:
                    pygame.draw.circle(self.screen, (130, 151, 105), mvt.center, int(self.defaut_rect / 7.5))


            if (len(self.black_rook_attack[key]) > 0):
                for attack in self.black_rook_attack[key]:
                    self.screen.fill((255, 0, 0), attack)
                    settings.draw_lines(self.screen, attack, (180, 0, 0))






