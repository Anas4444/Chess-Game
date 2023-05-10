import pygame
import sys

from settings import Settings
from game_stats import Stats
import game_functions as gf
from background import Background
from pieces import Pieces
from quit import Button

from pawn import Pawn
from rook import Rook
from king import King
from knight import Knight
from queen import Queen
from bishop import Bishop

def run_game():

    pygame.init()

    settings = Settings()
    stats = Stats()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height), pygame.FULLSCREEN)

    background = Background(settings, screen)
    pygame.display.set_caption("MyChess")

    piece = Pieces(settings, screen)
    pawn = Pawn(settings, screen)
    rook = Rook(settings, screen)
    king = King(settings, screen)
    queen = Queen(settings, screen)
    knight = Knight(settings, screen)
    bishop = Bishop(settings, screen)

    quit_button = Button(screen, settings)

    while True:
        gf.check_events(background, quit_button, stats, pawn, knight, rook, bishop, queen, king)

        gf.update_white_pieces(stats, background, pawn, rook, king, queen, knight, bishop)
        gf.update_black_pieces(stats, background, pawn, rook, king, queen, knight, bishop)
        gf.undo_check(stats, king)
        gf.king_check(stats, background, rook, pawn, knight, bishop, queen, king)

        gf.update_screen(piece, settings, quit_button, screen, background, pawn, rook, king, queen, knight, bishop)

run_game()
