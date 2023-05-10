import pygame
from background import Background

class Bishop(Background):

    def __init__(self, settings, screen):
        Background.__init__(self, settings, screen)
        self.defaut_rect = settings.rect_size

        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.color = (20, 100, 20)
        self.white = settings.WHITE

        self.white_bishop_image = pygame.image.load("Pieces\white_bishop.png")
        self.black_bishop_image = pygame.image.load("Pieces\\black_bishop.png")

        self.white_bishop_imageu = pygame.transform.scale(self.white_bishop_image,
                                                         (int(80 / (100 / self.defaut_rect)),
                                                          int(80 / (100 / self.defaut_rect))))
        self.black_bishop_imageu = pygame.transform.scale(self.black_bishop_image,
                                                         (int(80 / (100 / self.defaut_rect)),
                                                          int(80 / (100 / self.defaut_rect))))

        self.white_bishop_image.set_colorkey(self.white)
        self.black_bishop_image.set_colorkey(self.white)
        self.white_bishop_imageu.set_colorkey(self.white)
        self.black_bishop_imageu.set_colorkey(self.white)

        self.white_bishop_rect = self.white_bishop_imageu.get_rect()
        self.black_bishop_rect = self.black_bishop_imageu.get_rect()

        self.white_bishop_rects = {"B1": pygame.Rect(0, 0, self.white_bishop_rect.width, self.white_bishop_rect.height),
                                   "B2": pygame.Rect(0, 0, self.white_bishop_rect.width, self.white_bishop_rect.height)}

        self.black_bishop_rects = {"B1": pygame.Rect(0, 0, self.black_bishop_rect.width, self.black_bishop_rect.height),
                                   "B2": pygame.Rect(0, 0, self.black_bishop_rect.width, self.black_bishop_rect.height)}

        self.white_big_bishop_rects = {"B1": pygame.Rect(self.white_bishop_rects["B1"]),
                                       "B2": pygame.Rect(self.white_bishop_rects["B2"])}

        self.black_big_bishop_rects = {"B1": pygame.Rect(self.white_bishop_rects["B1"]),
                                       "B2": pygame.Rect(self.white_bishop_rects["B2"])}

        self.white_bishop_move = {"B1": [""],
                                  "B2": [""]}

        self.black_bishop_move = {"B1": [""],
                                  "B2": [""]}

        self.white_bishop_attack = {"B1": [],
                                    "B2": []}

        self.black_bishop_attack = {"B1": [],
                                    "B2": []}

        self.white_bishop_position = {"B1": ["c", 1],
                                      "B2": ["f", 1]}
        self.black_bishop_position = {"B1": ["c", 8],
                                      "B2": ["f", 8]}

        self.white_bishop_clicked = {"B1": False,
                                     "B2": False}

        self.black_bishop_clicked = {"B1": False,
                                     "B2": False}

        self.white_bishop_death = {"B1": False,
                                   "B2": False}

        self.black_bishop_death = {"B1": False,
                                   "B2": False}

        self.white_bishop_rects["B1"].center = (
        self.screen_rect.width / 2 - (self.defaut_rect * 1.5), self.screen_rect.height / 2 + (self.defaut_rect * 3.5))
        self.white_bishop_rects["B2"].center = (
        self.screen_rect.width / 2 + (self.defaut_rect * 1.5), self.screen_rect.height / 2 + (self.defaut_rect * 3.5))

        self.black_bishop_rects["B1"].center = (
        self.screen_rect.width / 2 - (self.defaut_rect * 1.5), self.screen_rect.height / 2 - (self.defaut_rect * 3.5))
        self.black_bishop_rects["B2"].center = (
        self.screen_rect.width / 2 + (self.defaut_rect * 1.5), self.screen_rect.height / 2 - (self.defaut_rect * 3.5))

    def update_white_bishop(self):
        pass

    def update_black_bishop(self):
        pass

    def draw_big_bishop(self, piece):
        piece.draw_big_piece(self.white_big_bishop_rects, self.white_bishop_rects, self.white_bishop_clicked, self.white_bishop_image, self.white_bishop_death)
        piece.draw_big_piece(self.black_big_bishop_rects, self.black_bishop_rects, self.black_bishop_clicked, self.black_bishop_image, self.black_bishop_death)

    def draw_circle(self, settings):
        settings.draw_circle(self.screen, self.white_bishop_clicked, self.board_rect)
        settings.draw_circle(self.screen, self.black_bishop_clicked, self.board_rect)

    def draw_bishop(self):
        for key0, rect in self.white_bishop_rects.items():
            if not (self.white_bishop_death[key0] or self.white_bishop_clicked[key0]):
                self.screen.blit(self.white_bishop_imageu, rect)

        for key1, rect in self.black_bishop_rects.items():
            if not (self.black_bishop_death[key1] or self.black_bishop_clicked[key1]):
                self.screen.blit(self.black_bishop_imageu, rect)

    def draw_bishop_mvts(self, settings):

        for key, bishop_mvts in self.white_bishop_move.items():
            if bishop_mvts[0] != "":
                self.screen.fill((155, 240, 20), bishop_mvts[0])

            if len(bishop_mvts) > 1:
                for mvt in bishop_mvts[1:]:
                    pygame.draw.circle(self.screen, (130, 151, 105), mvt.center, int(self.defaut_rect / 7.5))

            if (len(self.white_bishop_attack[key]) > 0):
                for attack in self.white_bishop_attack[key]:
                    self.screen.fill((255, 0, 0), attack)
                    settings.draw_lines(self.screen, attack, (180, 0, 0))

        for key, bishop_mvts in self.black_bishop_move.items():
            if bishop_mvts[0] != "":
                self.screen.fill((155, 240, 20), bishop_mvts[0])


            if len(bishop_mvts) > 1:
                for mvt in bishop_mvts[1:]:
                    pygame.draw.circle(self.screen, (130, 151, 105), mvt.center, int(self.defaut_rect / 7.5))


            if (len(self.black_bishop_attack[key]) > 0):
                for attack in self.black_bishop_attack[key]:
                    self.screen.fill((255, 0, 0), attack)
                    settings.draw_lines(self.screen, attack, (180, 0, 0))
