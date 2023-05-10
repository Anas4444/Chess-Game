import pygame

class Pieces:

    def __init__(self, settings, screen):
        self.screen = screen
        self.defaut_rect = settings.rect_size

    def draw_big_piece(self, big_piece_rect, piece_rect, piece_clicked, piece_image, piece_death):
        if piece_clicked in [True, False]:
            if piece_clicked and not piece_death:
                big_piece = pygame.transform.scale(piece_image, (
                                                   int((self.defaut_rect * 130) / 100),
                                                   int((self.defaut_rect * 130) / 100)))
                mx, my = pygame.mouse.get_pos()
                big_piece_rect.center = (mx - (self.defaut_rect / 4.5),
                                         my - (self.defaut_rect / 4.5))
                self.screen.blit(big_piece, big_piece_rect)
            else:
                big_piece_rect.center = piece_rect.center

        else:
            for piece, click in piece_clicked.items():
                if click and not piece_death[piece]:
                    big_piece = pygame.transform.scale(piece_image, (
                        int((self.defaut_rect * 130) / 100),
                        int((self.defaut_rect * 130) / 100)))
                    mx, my = pygame.mouse.get_pos()
                    big_piece_rect[piece].center = (mx - (self.defaut_rect / 4.5),
                                                    my - (self.defaut_rect / 4.5))
                    self.screen.blit(big_piece, big_piece_rect[piece])
                else:
                    big_piece_rect[piece].center = piece_rect[piece].center