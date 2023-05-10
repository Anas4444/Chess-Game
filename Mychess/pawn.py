import pygame
from background import Background

class Pawn(Background):

    def __init__(self, settings, screen):
        Background.__init__(self, settings, screen)

        self.defaut_rect = settings.rect_size

        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.white = settings.WHITE
        self.black = settings.BLACK
        self.color = (20, 100, 20)

        self.white_pawn_image = pygame.image.load("Pieces\White_pawn.png")
        self.white_pawn_imageu = pygame.transform.scale(self.white_pawn_image,
                                                       (int(80 / (100 / self.defaut_rect)),
                                                        int(80 / (100 / self.defaut_rect))))

        self.black_pawn_image = pygame.image.load("Pieces\\black_pawn.png")
        self.black_pawn_imageu = pygame.transform.scale(self.black_pawn_image,
                                                       (int(80 / (100 / self.defaut_rect)),
                                                        int(80 / (100 / self.defaut_rect))))

        self.white_pawn_image.set_colorkey(self.white)
        self.black_pawn_image.set_colorkey(self.white)
        self.white_pawn_imageu.set_colorkey(self.white)
        self.black_pawn_imageu.set_colorkey(self.white)

        self.white_pawn_rect = self.white_pawn_imageu.get_rect()
        self.black_pawn_rect = self.black_pawn_imageu.get_rect()

        self.pieces_move = []

        self.black_pawn_rects = {"p1": pygame.Rect(0, 0, self.black_pawn_rect.width, self.black_pawn_rect.height),
                                 "p2": pygame.Rect(0, 0, self.black_pawn_rect.width, self.black_pawn_rect.height),
                                 "p3": pygame.Rect(0, 0, self.black_pawn_rect.width, self.black_pawn_rect.height),
                                 "p4": pygame.Rect(0, 0, self.black_pawn_rect.width, self.black_pawn_rect.height),
                                 "p5": pygame.Rect(0, 0, self.black_pawn_rect.width, self.black_pawn_rect.height),
                                 "p6": pygame.Rect(0, 0, self.black_pawn_rect.width, self.black_pawn_rect.height),
                                 "p7": pygame.Rect(0, 0, self.black_pawn_rect.width, self.black_pawn_rect.height),
                                 "p8": pygame.Rect(0, 0, self.black_pawn_rect.width, self.black_pawn_rect.height)}

        self.white_pawn_rects = {"p1": pygame.Rect(0, 0, self.white_pawn_rect.width, self.white_pawn_rect.height),
                                 "p2": pygame.Rect(0, 0, self.white_pawn_rect.width, self.white_pawn_rect.height),
                                 "p3": pygame.Rect(0, 0, self.white_pawn_rect.width, self.white_pawn_rect.height),
                                 "p4": pygame.Rect(0, 0, self.white_pawn_rect.width, self.white_pawn_rect.height),
                                 "p5": pygame.Rect(0, 0, self.white_pawn_rect.width, self.white_pawn_rect.height),
                                 "p6": pygame.Rect(0, 0, self.white_pawn_rect.width, self.white_pawn_rect.height),
                                 "p7": pygame.Rect(0, 0, self.white_pawn_rect.width, self.white_pawn_rect.height),
                                 "p8": pygame.Rect(0, 0, self.white_pawn_rect.width, self.white_pawn_rect.height)}

        self.white_pawn_mvs = {"p1": [False, False, False, False],
                               "p2": [False, False, False, False],
                               "p3": [False, False, False, False],
                               "p4": [False, False, False, False],
                               "p5": [False, False, False, False],
                               "p6": [False, False, False, False],
                               "p7": [False, False, False, False],
                               "p8": [False, False, False, False]}

        self.black_pawn_mvs = {"p1": [False, False, False, False],
                               "p2": [False, False, False, False],
                               "p3": [False, False, False, False],
                               "p4": [False, False, False, False],
                               "p5": [False, False, False, False],
                               "p6": [False, False, False, False],
                               "p7": [False, False, False, False],
                               "p8": [False, False, False, False]}

        self.white_pawn_position = {"p1": ["a", 2],
                                    "p2": ["b", 2],
                                    "p3": ["c", 2],
                                    "p4": ["d", 2],
                                    "p5": ["e", 2],
                                    "p6": ["f", 2],
                                    "p7": ["g", 2],
                                    "p8": ["h", 2]}

        self.black_pawn_position = {"p1": ["a", 7],
                                    "p2": ["b", 7],
                                    "p3": ["c", 7],
                                    "p4": ["d", 7],
                                    "p5": ["e", 7],
                                    "p6": ["f", 7],
                                    "p7": ["g", 7],
                                    "p8": ["h", 7]}

        self.white_pawn_death = {"p1": False,
                                 "p2": False,
                                 "p3": False,
                                 "p4": False,
                                 "p5": False,
                                 "p6": False,
                                 "p7": False,
                                 "p8": False}

        self.black_pawn_death = {"p1": False,
                                 "p2": False,
                                 "p3": False,
                                 "p4": False,
                                 "p5": False,
                                 "p6": False,
                                 "p7": False,
                                 "p8": False}

        self.white_pawn_attack = {"p1": [False, False],
                                  "p2": [False, False],
                                  "p3": [False, False],
                                  "p4": [False, False],
                                  "p5": [False, False],
                                  "p6": [False, False],
                                  "p7": [False, False],
                                  "p8": [False,  False]}

        self.black_pawn_attack = {"p1": [False, False],
                                  "p2": [False, False],
                                  "p3": [False, False],
                                  "p4": [False, False],
                                  "p5": [False, False],
                                  "p6": [False, False],
                                  "p7": [False, False],
                                  "p8": [False, False]}

        self.black_second_move = {"p1": True,
                                  "p2": True,
                                  "p3": True,
                                  "p4": True,
                                  "p5": True,
                                  "p6": True,
                                  "p7": True,
                                  "p8": True}

        self.white_second_move = {"p1": True,
                                  "p2": True,
                                  "p3": True,
                                  "p4": True,
                                  "p5": True,
                                  "p6": True,
                                  "p7": True,
                                  "p8": True}

        self.white_pawns_mv2 = {"p1": False,
                                "p2": False,
                                "p3": False,
                                "p4": False,
                                "p5": False,
                                "p6": False,
                                "p7": False,
                                "p8": False}

        self.black_pawns_mv2 = {"p1": False,
                                "p2": False,
                                "p3": False,
                                "p4": False,
                                "p5": False,
                                "p6": False,
                                "p7": False,
                                "p8": False}

        self.black_rect_x, self.black_rect_y = self.screen_rect.width / 2 - (self.defaut_rect * 3.5), self.screen_rect.height / 2 - (self.defaut_rect * 2.5)

        self.white_big_pawn_rects = {"p1": pygame.Rect(self.white_pawn_rects["p1"]),
                                     "p2": pygame.Rect(self.white_pawn_rects["p1"]),
                                     "p3": pygame.Rect(self.white_pawn_rects["p1"]),
                                     "p4": pygame.Rect(self.white_pawn_rects["p1"]),
                                     "p5": pygame.Rect(self.white_pawn_rects["p1"]),
                                     "p6": pygame.Rect(self.white_pawn_rects["p1"]),
                                     "p7": pygame.Rect(self.white_pawn_rects["p1"]),
                                     "p8": pygame.Rect(self.white_pawn_rects["p1"])}

        self.black_big_pawn_rects = {"p1": pygame.Rect(self.white_pawn_rects["p1"]),
                                     "p2": pygame.Rect(self.white_pawn_rects["p1"]),
                                     "p3": pygame.Rect(self.white_pawn_rects["p1"]),
                                     "p4": pygame.Rect(self.white_pawn_rects["p1"]),
                                     "p5": pygame.Rect(self.white_pawn_rects["p1"]),
                                     "p6": pygame.Rect(self.white_pawn_rects["p1"]),
                                     "p7": pygame.Rect(self.white_pawn_rects["p1"]),
                                     "p8": pygame.Rect(self.white_pawn_rects["p1"])}

        for key in self.black_pawn_rects.keys():
            self.black_pawn_rects[key].center = (self.black_rect_x, self.black_rect_y)
            self.black_rect_x += self.defaut_rect

        self.white_rect_x, self.white_rect_y = self.screen_rect.width / 2 - (self.defaut_rect * 3.5), self.screen_rect.height / 2 + (self.defaut_rect * 2.5)
        for key in self.white_pawn_rects.keys():
            self.white_pawn_rects[key].center = (self.white_rect_x, self.white_rect_y)
            self.white_rect_x += self.defaut_rect

        self.white_pawn_clicked = {"p1": False,
                                   "p2": False,
                                   "p3": False,
                                   "p4": False,
                                   "p5": False,
                                   "p6": False,
                                   "p7": False,
                                   "p8": False}

        self.black_pawn_clicked = {"p1": False,
                                   "p2": False,
                                   "p3": False,
                                   "p4": False,
                                   "p5": False,
                                   "p6": False,
                                   "p7": False,
                                   "p8": False}

        self.black_movements = ["", "", "", "", "", "", ""]
        self.white_movements = ["", "", "", "", "", "", ""]

    def update_white_pawn(self):
        for pawn, click in self.white_pawn_clicked.items():
            if not click:
                if self.white_pawn_attack[pawn][0] == True and self.white_pawn_attack[pawn][1] == False:

                    self.white_pawn_rects[pawn].x -= self.defaut_rect
                    self.white_pawn_rects[pawn].y -= self.defaut_rect
                    self.white_pawn_attack[pawn][0] = False

                    for key, black_pawn in self.black_pawn_position.items():
                        if black_pawn[1] == self.white_pawn_position[pawn][1] and black_pawn[0] == self.white_pawn_position[pawn][0]:
                            self.black_pawn_death[key] = True
                            self.black_pawn_rects[key].center = (self.screen_rect.right - 500, self.screen_rect.top)
                            self.pieces_move.append(pawn + chr(ord(self.white_pawn_position[pawn][0]) + 1) +
                                str(self.white_pawn_position[pawn][1] - 1) + 'x' + key + black_pawn[0] + str(black_pawn[1]))
                            break
                    print(self.pieces_move)

                elif self.white_pawn_attack[pawn][0] == True and self.white_pawn_attack[pawn][1] == True:

                    self.white_pawn_rects[pawn].x += self.defaut_rect
                    self.white_pawn_rects[pawn].y -= self.defaut_rect
                    self.white_pawn_attack[pawn][0] = False

                    for key, black_pawn in self.black_pawn_position.items():
                        if black_pawn[1] == self.white_pawn_position[pawn][1] and black_pawn[0] == self.white_pawn_position[pawn][0]:
                            self.black_pawn_death[key] = True
                            self.black_pawn_rects[key].center = (self.screen_rect.right - 500, self.screen_rect.top)
                            self.pieces_move.append(pawn + chr(ord(self.white_pawn_position[pawn][0]) + 1) +
                               str(self.white_pawn_position[pawn][1] - 1) + 'x' + key + black_pawn[0] + str(black_pawn[1]))
                            break
                    print(self.pieces_move)

                elif self.white_pawn_mvs[pawn][0]:

                    self.white_pawn_rects[pawn].y -= self.defaut_rect

                    self.white_pawn_mvs[pawn][0] = False
                    self.pieces_move.append(pawn + self.white_pawn_position[pawn][0] + str(self.white_pawn_position[pawn][1]))
                    print(self.pieces_move)

                elif self.white_pawn_mvs[pawn][1]:

                    self.white_pawn_rects[pawn].y -= self.defaut_rect * 2
                    self.white_pawns_mv2[pawn] = True

                    self.white_pawn_mvs[pawn][1] = False
                    self.pieces_move.append(pawn + self.white_pawn_position[pawn][0] + str(self.white_pawn_position[pawn][1]))
                    print(self.pieces_move)

                elif (self.white_big_pawn_rects[pawn].collidepoint(self.white_pawn_rects[pawn].x + self.defaut_rect,
                        self.white_pawn_rects[pawn].y - self.defaut_rect)) and (
                        self.white_pawn_position[pawn][0] != "h") and self.white_pawn_position[pawn][1] == 5:

                    for key0, black_pawn in self.black_pawn_position.items():
                        if self.white_pawn_position[pawn][1] == black_pawn[1] and (
                                self.white_pawn_position[pawn][0] == chr(ord(black_pawn[0]) - 1)) and (
                                self.pieces_move[len(self.pieces_move) - 1] == key0 + black_pawn[0] + str(
                                black_pawn[1])) and (self.black_pawns_mv2[key0]):

                            self.white_pawn_mvs[pawn][2] = True

                            self.white_pawn_rects[pawn].x += self.defaut_rect
                            self.white_pawn_rects[pawn].y -= self.defaut_rect

                            self.white_pawn_position[pawn][1] += 1
                            self.white_pawn_position[pawn][0] = chr(ord(self.white_pawn_position[pawn][0]) + 1)

                            self.black_pawn_death[key0] = True
                            self.black_pawn_rects[key0].center = (self.screen_rect.right - 500, self.screen_rect.top)

                            self.pieces_move.append(pawn + chr(ord(self.white_pawn_position[pawn][0]) - 1) + str(
                                self.white_pawn_position[pawn][1] - 1) + 'x' + key0 + black_pawn[0] + str(
                                black_pawn[1]) + '(' + self.white_pawn_position[pawn][0] + str(
                                self.white_pawn_position[pawn][1]) + ')')
                            print(self.pieces_move)

                elif (self.white_big_pawn_rects[pawn].collidepoint(self.white_pawn_rects[pawn].x - self.defaut_rect,
                        self.white_pawn_rects[pawn].y - self.defaut_rect)) and (
                        self.white_pawn_position[pawn][0] != "a") and self.white_pawn_position[pawn][1] == 5:

                    for key0, black_pawn in self.black_pawn_position.items():
                        if self.white_pawn_position[pawn][1] == black_pawn[1] and (
                                self.white_pawn_position[pawn][0] == chr(ord(black_pawn[0]) + 1)) and (
                                self.pieces_move[len(self.pieces_move) - 1] == key0 + black_pawn[0] + str(
                                black_pawn[1])) and (self.black_pawns_mv2[key0]):

                            self.white_pawn_mvs[pawn][3] = True

                            self.white_pawn_rects[pawn].x -= self.defaut_rect
                            self.white_pawn_rects[pawn].y -= self.defaut_rect

                            self.white_pawn_position[pawn][1] += 1
                            self.white_pawn_position[pawn][0] = chr(ord(self.white_pawn_position[pawn][0]) - 1)

                            self.black_pawn_death[key0] = True
                            self.black_pawn_rects[key0].center = (self.screen_rect.right - 500, self.screen_rect.top)

                            self.pieces_move.append(pawn + chr(ord(self.white_pawn_position[pawn][0]) + 1) + str(
                                self.white_pawn_position[pawn][1] - 1) + 'x' + key0 + black_pawn[0] + str(
                                black_pawn[1]) + '(' + self.white_pawn_position[pawn][0] + str(
                                self.white_pawn_position[pawn][1]) + ')')
                            print(self.pieces_move)

    def update_black_pawn(self):

        for pawn, click in self.black_pawn_clicked.items():
            if not click:
                if self.black_pawn_attack[pawn][0] == True and self.black_pawn_attack[pawn][1] == False:

                    self.black_pawn_rects[pawn].x -= self.defaut_rect
                    self.black_pawn_rects[pawn].y += self.defaut_rect
                    self.black_pawn_attack[pawn][0] = False

                    for key, white_pawn in self.white_pawn_position.items():
                        if white_pawn[1] == self.black_pawn_position[pawn][1] and white_pawn[0] == self.black_pawn_position[pawn][0]:
                            self.white_pawn_death[key] = True
                            self.white_pawn_rects[key].center = (self.screen_rect.right - 500, self.screen_rect.top)
                            self.pieces_move.append(pawn + chr(ord(self.black_pawn_position[pawn][0]) + 1) +
                                str(self.black_pawn_position[pawn][1] + 1) + 'x' + key + white_pawn[0] + str(white_pawn[1]))
                            break

                    print(self.pieces_move)

                elif self.black_pawn_attack[pawn][0] == True and self.black_pawn_attack[pawn][1] == True:

                    self.black_pawn_rects[pawn].x += self.defaut_rect
                    self.black_pawn_rects[pawn].y += self.defaut_rect
                    self.black_pawn_attack[pawn][0] = False

                    for key, white_pawn in self.white_pawn_position.items():
                        if white_pawn[1] == self.black_pawn_position[pawn][1] and white_pawn[0] == self.black_pawn_position[pawn][0]:
                            self.white_pawn_death[key] = True
                            self.white_pawn_rects[key].center = (self.screen_rect.right - 500, self.screen_rect.top)
                            self.pieces_move.append(pawn + chr(ord(self.black_pawn_position[pawn][0]) - 1) +
                                str(self.black_pawn_position[pawn][1] + 1) + 'x' + key + white_pawn[0] + str(white_pawn[1]))
                            break
                    print(self.pieces_move)

                elif self.black_pawn_mvs[pawn][0]:

                    self.black_pawn_rects[pawn].y += self.defaut_rect
                    self.black_pawn_mvs[pawn][0] = False
                    self.pieces_move.append(pawn + self.black_pawn_position[pawn][0] + str(self.black_pawn_position[pawn][1]))
                    print(self.pieces_move)

                elif self.black_pawn_mvs[pawn][1]:

                    self.black_pawn_rects[pawn].y += self.defaut_rect * 2
                    self.black_pawns_mv2[pawn] = True
                    self.black_pawn_mvs[pawn][1] = False

                    self.pieces_move.append(pawn + self.black_pawn_position[pawn][0] + str(self.black_pawn_position[pawn][1]))
                    print(self.pieces_move)

                elif (self.black_big_pawn_rects[pawn].collidepoint(self.black_pawn_rects[pawn].x + self.defaut_rect,
                        self.black_pawn_rects[pawn].y + self.defaut_rect)) and (
                        self.black_pawn_position[pawn][0] != "h") and self.black_pawn_position[pawn][1] == 4:

                    for key0, white_pawn in self.white_pawn_position.items():
                        if self.black_pawn_position[pawn][1] == white_pawn[1] and (
                                self.black_pawn_position[pawn][0] == chr(ord(white_pawn[0]) - 1)) and (
                                self.pieces_move[len(self.pieces_move) - 1] == key0 + white_pawn[0] + str(
                                white_pawn[1])) and (self.white_pawns_mv2[key0]):

                            self.black_pawn_rects[pawn].x += self.defaut_rect
                            self.black_pawn_rects[pawn].y += self.defaut_rect

                            self.black_pawn_mvs[pawn][2] = True

                            self.black_pawn_position[pawn][1] -= 1
                            self.black_pawn_position[pawn][0] = chr(ord(self.black_pawn_position[pawn][0]) + 1)

                            self.white_pawn_death[key0] = True
                            self.white_pawn_rects[key0].center = (self.screen_rect.right - 500, self.screen_rect.top)

                            self.pieces_move.append(pawn + chr(ord(self.black_pawn_position[pawn][0]) - 1) + str(
                                self.black_pawn_position[pawn][1] + 1) + 'x' + key0 + white_pawn[0] + str(
                                white_pawn[1]) + '(' + self.black_pawn_position[pawn][0] + str(
                                self.black_pawn_position[pawn][1]) + ')')
                            print(self.pieces_move)

                elif (self.black_big_pawn_rects[pawn].collidepoint(self.black_pawn_rects[pawn].x - self.defaut_rect,
                        self.black_pawn_rects[pawn].y + self.defaut_rect)) and (
                        self.black_pawn_position[pawn][0] != "a") and self.black_pawn_position[pawn][1] == 4:

                    for key0, white_pawn in self.white_pawn_position.items():
                        if self.black_pawn_position[pawn][1] == white_pawn[1] and (
                                self.black_pawn_position[pawn][0] == chr(ord(white_pawn[0]) + 1)) and (
                                self.pieces_move[len(self.pieces_move) - 1] == key0 + white_pawn[0] + str(
                                white_pawn[1])) and (self.white_pawns_mv2[key0]):

                            self.black_pawn_rects[pawn].x -= self.defaut_rect
                            self.black_pawn_rects[pawn].y += self.defaut_rect

                            self.black_pawn_mvs[pawn][3] = True

                            self.black_pawn_position[pawn][1] -= 1
                            self.black_pawn_position[pawn][0] = chr(ord(self.black_pawn_position[pawn][0]) - 1)

                            self.white_pawn_death[key0] = True
                            self.white_pawn_rects[key0].center = (self.screen_rect.right - 500, self.screen_rect.top)

                            self.pieces_move.append(pawn + chr(ord(self.black_pawn_position[pawn][0]) + 1) + str(
                                self.black_pawn_position[pawn][1] + 1) + 'x' + key0 + white_pawn[0] + str(
                                white_pawn[1]) + '(' + self.black_pawn_position[pawn][0] + str(
                                self.black_pawn_position[pawn][1]) + ')')
                            print(self.pieces_move)

    def draw_big_pawn(self, piece):
        piece.draw_big_piece(self.white_big_pawn_rects, self.white_pawn_rects, self.white_pawn_clicked, self.white_pawn_image, self.white_pawn_death)
        piece.draw_big_piece(self.black_big_pawn_rects, self.black_pawn_rects, self.black_pawn_clicked, self.black_pawn_image, self.black_pawn_death)

    def draw_circle(self, settings):
        settings.draw_circle(self.screen, self.white_pawn_clicked, self.board_rect)
        settings.draw_circle(self.screen, self.black_pawn_clicked, self.board_rect)

    def draw_pawn(self):
        for pawn, click in self.white_pawn_clicked.items():
            if not click and not self.white_pawn_death[pawn]:
                self.screen.blit(self.white_pawn_imageu, self.white_pawn_rects[pawn])

        for pawn, click in self.black_pawn_clicked.items():
            if not click and not self.black_pawn_death[pawn]:
                self.screen.blit(self.black_pawn_imageu, self.black_pawn_rects[pawn])

    def draw_pawn_mvts(self, settings):
        if self.white_movements[2] != "":
            self.screen.fill((155, 240, 20), self.white_movements[2])


        if self.white_movements[0] != "":
            pygame.draw.circle(self.screen, (130, 151, 105), self.white_movements[0].center, int(self.defaut_rect / 7.5))


        if self.white_movements[1] != "":
            pygame.draw.circle(self.screen, (130, 151, 105), self.white_movements[1].center, int(self.defaut_rect / 7.5))


        if self.white_movements[3] != "":
            self.screen.fill((255, 0, 0), self.white_movements[3])
            settings.draw_lines(self.screen, self.white_movements[3], (180, 0, 0))

        if self.white_movements[4] != "":
            self.screen.fill((255, 0, 0), self.white_movements[4])
            settings.draw_lines(self.screen, self.white_movements[4], (180, 0, 0))

        if self.white_movements[5] != "":
            pygame.draw.circle(self.screen, (130, 151, 105), self.white_movements[5].center, int(self.defaut_rect / 7.5))

        if self.white_movements[6] != "":
            pygame.draw.circle(self.screen, (130, 151, 105), self.white_movements[6].center, int(self.defaut_rect / 7.5))

        if self.black_movements[2] != "":
            self.screen.fill((155, 240, 20), self.black_movements[2])


        if self.black_movements[0] != "":
            pygame.draw.circle(self.screen, (130, 151, 105), self.black_movements[0].center, int(self.defaut_rect / 7.5))


        if self.black_movements[1] != "":
            pygame.draw.circle(self.screen, (130, 151, 105), self.black_movements[1].center, int(self.defaut_rect / 7.5))


        if self.black_movements[3] != "":
            self.screen.fill((255, 0, 0), self.black_movements[3])
            settings.draw_lines(self.screen, self.black_movements[3], (180, 0, 0))

        if self.black_movements[4] != "":
            self.screen.fill((255, 0, 0), self.black_movements[4])
            settings.draw_lines(self.screen, self.black_movements[4], (180, 0, 0))

        if self.black_movements[5] != "":
            pygame.draw.circle(self.screen, (130, 151, 105), self.black_movements[5].center, int(self.defaut_rect / 7.5))

        if self.black_movements[6] != "":
            pygame.draw.circle(self.screen, (130, 151, 105), self.black_movements[6].center, int(self.defaut_rect / 7.5))




