import pygame

class Background:

    def __init__(self, settings, screen):

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.black = settings.BLACK
        self.white = settings.WHITE
        self.defaut_rect = settings.rect_size

        self.board_rect = {
             "a": {
                "1": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect),
                "2": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect),
                "3": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect),
                "4": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect),
                "5": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect),
                "6": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect),
                "7": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect),
                "8": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect)},
            "b": {
                "1": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect),
                "2": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect),
                "3": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect),
                "4": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect),
                "5": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect),
                "6": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect),
                "7": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect),
                "8": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect)},
            "c": {
                "1": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect),
                "2": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect),
                "3": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect),
                "4": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect),
                "5": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect),
                "6": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect),
                "7": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect),
                "8": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect)},
            "d": {
                "1": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect),
                "2": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect),
                "3": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect),
                "4": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect),
                "5": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect),
                "6": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect),
                "7": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect),
                "8": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect)},
            "e": {
                "1": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect),
                "2": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect),
                "3": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect),
                "4": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect),
                "5": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect),
                "6": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect),
                "7": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect),
                "8": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect)},
            "f": {
                "1": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect),
                "2": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect),
                "3": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect),
                "4": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect),
                "5": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect),
                "6": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect),
                "7": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect),
                "8": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect)},
            "g": {
                "1": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect),
                "2": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect),
                "3": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect),
                "4": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect),
                "5": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect),
                "6": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect),
                "7": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect),
                "8": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect)},
            "h": {
                "1": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect),
                "2": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect),
                "3": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect),
                "4": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect),
                "5": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect),
                "6": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect),
                "7": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect),
                "8": pygame.Rect(0, 0, self.defaut_rect, self.defaut_rect)},
        }

        self.board_move = {
            "a": {
                "1": True,
                "2": True,
                "3": False,
                "4": False,
                "5": False,
                "6": False,
                "7": True,
                "8": True},
            "b": {
                "1": True,
                "2": True,
                "3": False,
                "4": False,
                "5": False,
                "6": False,
                "7": True,
                "8": True},
            "c": {
                "1": True,
                "2": True,
                "3": False,
                "4": False,
                "5": False,
                "6": False,
                "7": True,
                "8": True},
            "d": {
                "1": True,
                "2": True,
                "3": False,
                "4": False,
                "5": False,
                "6": False,
                "7": True,
                "8": True},
            "e": {
                "1": True,
                "2": True,
                "3": False,
                "4": False,
                "5": False,
                "6": False,
                "7": True,
                "8": True},
            "f": {
                "1": True,
                "2": True,
                "3": False,
                "4": False,
                "5": False,
                "6": False,
                "7": True,
                "8": True},
            "g": {
                "1": True,
                "2": True,
                "3": False,
                "4": False,
                "5": False,
                "6": False,
                "7": True,
                "8": True},
            "h": {
                "1": True,
                "2": True,
                "3": False,
                "4": False,
                "5": False,
                "6": False,
                "7": True,
                "8": True}}

        rect_x, rect_y = screen.get_rect().width/2 - (self.defaut_rect * 3.5), screen.get_rect().height/2 + (self.defaut_rect * 3.5)
        for key in self.board_rect.keys():
            for index in self.board_rect[key].keys():
                self.board_rect[key][index].center = (rect_x, rect_y)
                rect_y -= self.defaut_rect
            rect_y = screen.get_rect().height / 2 + (self.defaut_rect * 3.5)
            rect_x += self.defaut_rect

    def draw_lines(self):
        pygame.draw.line(self.screen, self.black, (self.screen_rect.width / 2 - (self.defaut_rect * 4), self.screen_rect.height / 2 + (self.defaut_rect * 4.3)),
                         (self.screen_rect.width / 2 - (self.defaut_rect * 4), self.screen_rect.height / 2 - (self.defaut_rect * 4.3)), 5)
        pygame.draw.line(self.screen, self.black, (self.screen_rect.width / 2 + (self.defaut_rect * 4), self.screen_rect.height / 2 + (self.defaut_rect * 4.3)),
                         (self.screen_rect.width / 2 + (self.defaut_rect * 4), self.screen_rect.height / 2 - (self.defaut_rect * 4.3)), 5)
        pygame.draw.line(self.screen, self.black, (self.screen_rect.width / 2 - (self.defaut_rect * 4.3), self.screen_rect.height / 2 + (self.defaut_rect * 4)),
                         (self.screen_rect.width / 2 + (self.defaut_rect * 4.3), self.screen_rect.height / 2 + (self.defaut_rect * 4)), 5)
        pygame.draw.line(self.screen, self.black, (self.screen_rect.width / 2 - (self.defaut_rect * 4.3), self.screen_rect.height / 2 - (self.defaut_rect * 4)),
                         (self.screen_rect.width / 2 + (self.defaut_rect * 4.3), self.screen_rect.height / 2 - (self.defaut_rect * 4)), 5)

    def draw_board(self):

        for key0 in self.board_rect.keys():
            if key0 in ["a", "c", "e", "g"]:
                for key1, rect in self.board_rect[key0].items():

                    if int(key1) % 2 == 1:
                        pygame.draw.rect(self.screen, (181, 136, 99), rect)
                    else:
                        pygame.draw.rect(self.screen, (240, 217, 181), rect)

            else:
                for key1, rect in self.board_rect[key0].items():
                    if int(key1) % 2 == 1:
                        pygame.draw.rect(self.screen, (240, 217, 181), rect)
                    else:
                        pygame.draw.rect(self.screen, (181, 136, 99), rect)















