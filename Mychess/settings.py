import pygame

class Settings:

    def __init__(self):
        self.clock = pygame.time.Clock()

        self.BLACK = (70, 70, 70)
        self.WHITE = (255, 255, 255)
        self.BG = (60, 60, 60)

        # Button settings:
        self.button_color = [(255, 132, 132), (125, 125, 125)]
        self.green = (41, 199, 7)
        self.blue = (86, 95, 245)

        self.bg_color = (255, 255, 255)

        self.screen_width = 800
        self.screen_height = 800

        if self.screen_width <= self.screen_height:
            self.rect_size = self.screen_width / 8
        else:
            self.rect_size = self.screen_height / 8

    def draw_lines(self, screen, mvt, color):
        pygame.draw.line(screen, color, (mvt.x, mvt.y), (mvt.x + mvt.width, mvt.y), int(self.rect_size * 0.05))
        pygame.draw.line(screen, color, (mvt.x, mvt.y + mvt.height), (mvt.x + mvt.width, mvt.y + mvt.height), int(self.rect_size * 0.05))
        pygame.draw.line(screen, color, (mvt.x, mvt.y), (mvt.x, mvt.y + mvt.height), int(self.rect_size * 0.05))
        pygame.draw.line(screen, color, (mvt.x + mvt.width, mvt.y), (mvt.x + mvt.width, mvt.y + mvt.height), int(self.rect_size * 0.05))

    def draw_circle(self, screen, piece_clicked, board_rect):
        if piece_clicked in [True, False]:
            if piece_clicked:
                mx, my = pygame.mouse.get_pos()
                for key in board_rect.keys():
                    for rect in board_rect[key].values():
                        if rect.collidepoint(mx, my):
                            pygame.draw.circle(screen, (240, 148, 36), rect.center,
                                               int(self.rect_size / 2.143))

        else:
            for click in piece_clicked.values():
                if click:
                    mx, my = pygame.mouse.get_pos()
                    for key in board_rect.keys():
                        for rect in board_rect[key].values():
                            if rect.collidepoint(mx, my):
                                pygame.draw.circle(screen, (240, 148, 36), rect.center, int(self.rect_size / 2.143))