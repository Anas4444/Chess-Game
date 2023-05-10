import sys
import pygame

def check_events(background, quit_button, stats, pawn, knight, rook, bishop, queen, king):

    mx, my = pygame.mouse.get_pos()
    quit = check_quit(quit_button, mx, my)
    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:

            if quit:
                sys.exit()
            check_white_pieces_click(background, stats, pawn, knight, rook, bishop, queen, king, mx, my)
            check_black_pieces_click(background, stats, pawn, knight, rook, bishop, queen, king, mx, my)

        elif event.type == pygame.MOUSEBUTTONUP:

            undo_white_pieces_click(pawn, rook, knight, bishop, queen, king)
            white_pawn_attack(background, stats, pawn, knight, rook, bishop, queen)

            undo_black_pieces_click(pawn, rook, knight, bishop, queen, king)
            black_pawn_attack(background, stats, pawn, knight, rook, bishop, queen)

        elif (event.type == pygame.QUIT):
            sys.exit()

def update_screen(piece, settings, quit_button, screen, background, pawn, rook, king, queen, knight, bishop):

    screen.fill(settings.BG)

    background.draw_board()
    draw_circle(settings, pawn, rook, king, queen, knight, bishop)

    king.draw_white_check()
    king.draw_black_check()
    king.draw_king_mvts(settings)
    queen.draw_queen_mvts(settings)
    bishop.draw_bishop_mvts(settings)
    rook.draw_rook_mvts(settings)
    pawn.draw_pawn_mvts(settings)
    knight.draw_knight_mvts(settings)

    draw_pieces(pawn, rook, king, queen, knight, bishop)
    draw_big_pieces(piece, pawn, rook, king, queen, knight, bishop)
    quit_button.prep_msg()
    quit_button.draw_quit_button()

    pygame.display.flip()
    settings.clock.tick(60)

def check_quit(quit_button, mx, my):
    if quit_button.rect1.collidepoint(mx, my):
        quit_button.quit_button_on = True
    else:
        quit_button.quit_button_on = False

    return(quit_button.rect1.collidepoint(mx, my))

def draw_circle(settings, pawn, rook, king, queen, knight, bishop):
    pawn.draw_circle(settings)
    rook.draw_circle(settings)
    king.draw_circle(settings)
    queen.draw_circle(settings)
    knight.draw_circle(settings)
    bishop.draw_circle(settings)

def draw_big_pieces(piece, pawn, rook, king, queen, knight, bishop):
    pawn.draw_big_pawn(piece)
    rook.draw_big_rook(piece)
    knight.draw_big_knight(piece)
    bishop.draw_big_bishop(piece)
    queen.draw_big_queen(piece)
    king.draw_big_king(piece)

def draw_pieces(pawn, rook, king, queen, knight, bishop):
    pawn.draw_pawn()
    rook.draw_rook()
    king.draw_king()
    queen.draw_queen()
    knight.draw_knight()
    bishop.draw_bishop()

def update_white_pieces(stats, background, pawn, rook, king, queen, knight, bishop):
    pawn.update_white_pawn()
    update_white_knight(stats, background, rook, pawn, knight, bishop, queen)
    update_white_rook(stats, background, rook, pawn, knight, bishop, queen, king)
    update_white_bishop(stats, background, rook, pawn, knight, bishop, queen)
    update_white_queen(stats, background, rook, pawn, knight, bishop, queen)
    update_white_king(stats, background, rook, pawn, knight, bishop, queen, king)

def update_black_pieces(stats, background, pawn, rook, king, queen, knight, bishop):
    pawn.update_black_pawn()
    update_black_knight(stats, background, rook, pawn, knight, bishop, queen)
    update_black_rook(stats, background, rook, pawn, knight, bishop, queen, king)
    update_black_bishop(stats, background, rook, pawn, knight, bishop, queen)
    update_black_queen(stats, background, rook, pawn, knight, bishop, queen)
    update_black_king(stats, background, rook, pawn, knight, bishop, queen, king)

def check_white_pieces_click(background, stats, pawn, knight, rook, bishop, queen, king, mx, my):
    if stats.white_turn:
        check_white_pawn_click(background, pawn, knight, rook, bishop, queen, king, mx, my)
        check_white_rook_click(background, pawn, knight, rook, bishop, queen, king, mx, my)
        check_white_knight_click(background, pawn, knight, rook, bishop, queen, king, mx, my)
        check_white_bishop_click(background, pawn, knight, rook, bishop, queen, king, mx, my)
        check_white_queen_click(background, pawn, knight, rook, bishop, queen, king, mx, my)
        check_white_king_click(background, pawn, knight, rook, bishop, queen, king, mx, my)

def check_black_pieces_click(background, stats, pawn, knight, rook, bishop, queen, king, mx, my):
    if stats.black_turn:
        check_black_pawn_click(background, pawn, knight, rook, bishop, queen, king, mx, my)
        check_black_rook_click(background, pawn, knight, rook, bishop, queen, king, mx, my)
        check_black_knight_click(background, pawn, knight, rook, bishop, queen, king, mx, my)
        check_black_bishop_click(background, pawn, knight, rook, bishop, queen, king, mx, my)
        check_black_queen_click(background, pawn, knight, rook, bishop, queen, king, mx, my)
        check_black_king_click(background, pawn, knight, rook, bishop, queen, king, mx, my)

def undo_white_pieces_click(pawn, rook, knight, bishop, queen, king):
    undo_white_pawn_click(pawn)
    undo_white_rook_click(rook)
    undo_white_knight_click(knight)
    undo_white_bishop_click(bishop)
    undo_white_queen_click(queen)
    undo_white_king_click(king)

def undo_black_pieces_click(pawn, rook, knight, bishop, queen, king):
    undo_black_pawn_click(pawn)
    undo_black_rook_click(rook)
    undo_black_knight_click(knight)
    undo_black_bishop_click(bishop)
    undo_black_queen_click(queen)
    undo_black_king_click(king)

def undo_white_pawn_click(pawn):
    for key, click in pawn.white_pawn_clicked.items():
        if click:
            pawn.white_pawn_clicked[key] = False
            pawn.white_movements = ["", "", "", "", "", "", ""]

def undo_white_rook_click(rook):
    for key, click in rook.white_rook_clicked.items():
        if click:
            rook.white_rook_clicked[key] = False
            rook.white_rook_move[key] = [""]
            rook.white_rook_attack[key] = []

def undo_white_knight_click(knight):
    for key, click in knight.white_knight_clicked.items():
        if click:
            knight.white_knight_clicked[key] = False
            knight.white_knight_move[key] = [""]
            knight.white_knight_attack[key] = []

def undo_white_bishop_click(bishop):
    for key, click in bishop.white_bishop_clicked.items():
        if click:
            bishop.white_bishop_clicked[key] = False
            bishop.white_bishop_move[key] = [""]
            bishop.white_bishop_attack[key] = []

def undo_white_queen_click(queen):
    if queen.white_queen_clicked:
        queen.white_queen_clicked = False
        queen.white_queen_move = ['']
        queen.white_queen_attack = []

def undo_white_king_click(king):
    if king.white_king_clicked:
        king.white_king_clicked = False
        king.white_king_move = [""]
        king.white_king_attack = []

def check_white_pawn_click(background, pawn, knight, rook, bishop, queen, king, mx, my):
    for key, white_pawn_rect in pawn.white_pawn_rects.items():
        if white_pawn_rect.collidepoint(mx, my):
            pawn.white_pawn_clicked[key] = True
            white_pawn_move(background, pawn, knight, rook, bishop, queen, king, key)

def check_white_rook_click(background, pawn, knight, rook, bishop, queen, king, mx, my):
    for key, white_rook_rect in rook.white_rook_rects.items():
        if white_rook_rect.collidepoint(mx, my):
            rook.white_rook_clicked[key] = True
            white_rook_mvts(background, pawn, knight, rook, bishop, queen, king, key)

def check_white_knight_click(background, pawn, knight, rook, bishop, queen, king, mx, my):
    for key, white_knight_rect in knight.white_knight_rects.items():
        if white_knight_rect.collidepoint(mx, my):
            knight.white_knight_clicked[key] = True
            white_knight_mvts(background, pawn, knight, rook, bishop, queen, king, key)

def check_white_bishop_click(background, pawn, knight, rook, bishop, queen, king, mx, my):
    for key, white_bishop_rect in bishop.white_bishop_rects.items():
        if white_bishop_rect.collidepoint(mx, my):
            bishop.white_bishop_clicked[key] = True
            white_bishop_mvts(background, pawn, knight, rook, bishop, queen, king, key)

def check_white_queen_click(background, pawn, knight, rook, bishop, queen, king, mx, my):
    if queen.white_queen_rect.collidepoint(mx, my):
        queen.white_queen_clicked = True
        white_queen_mvts(background, pawn, knight, queen, bishop, rook, king)

def check_white_king_click(background, pawn, knight, rook, bishop, queen, king, mx, my):
    if king.white_king_rect.collidepoint(mx, my):
        king.white_king_clicked = True
        white_king_mvts(background, pawn, knight, queen, bishop, rook, king)

def undo_black_pawn_click(pawn):
    for key, click in pawn.black_pawn_clicked.items():
        if click:
            pawn.black_pawn_clicked[key] = False
            pawn.black_movements = ["", "", "", "", "", "", ""]

def undo_black_rook_click(rook):
    for key, click in rook.black_rook_clicked.items():
        if click:
            rook.black_rook_clicked[key] = False
            rook.black_rook_move[key] = [""]
            rook.black_rook_attack[key] = []

def undo_black_knight_click(knight):
    for key, click in knight.black_knight_clicked.items():
        if click:
            knight.black_knight_clicked[key] = False
            knight.black_knight_move[key] = [""]
            knight.black_knight_attack[key] = []

def undo_black_bishop_click(bishop):
    for key, click in bishop.black_bishop_clicked.items():
        if click:
            bishop.black_bishop_clicked[key] = False
            bishop.black_bishop_move[key] = [""]
            bishop.black_bishop_attack[key] = []

def undo_black_queen_click(queen):
    if queen.black_queen_clicked:
        queen.black_queen_clicked = False
        queen.black_queen_move = [""]
        queen.black_queen_attack = []

def undo_black_king_click(king):
    if king.black_king_clicked:
        king.black_king_clicked = False
        king.black_king_move = [""]
        king.black_king_attack = []

def check_black_pawn_click(background, pawn, knight, rook, bishop, queen, king, mx, my):
    for key, black_pawn_rect in pawn.black_pawn_rects.items():
        if black_pawn_rect.collidepoint(mx, my):
            pawn.black_pawn_clicked[key] = True
            black_pawn_move(background, pawn, knight, rook, bishop, queen, king, key)

def check_black_rook_click(background, pawn, knight, rook, bishop, queen, king, mx, my):
    for key, black_rook_rect in rook.black_rook_rects.items():
        if black_rook_rect.collidepoint(mx, my):
            rook.black_rook_clicked[key] = True
            black_rook_mvts(background, pawn, knight, rook, bishop, queen, king, key)

def check_black_knight_click(background, pawn, knight, rook, bishop, queen, king, mx, my):
    for key, black_knight_rect in knight.black_knight_rects.items():
        if black_knight_rect.collidepoint(mx, my):
            knight.black_knight_clicked[key] = True
            black_knight_mvts(background, pawn, knight, rook, bishop, queen, king, key)

def check_black_bishop_click(background, pawn, knight, rook, bishop, queen, king, mx, my):
    for key, black_bishop_rect in bishop.black_bishop_rects.items():
        if black_bishop_rect.collidepoint(mx, my):
            bishop.black_bishop_clicked[key] = True
            black_bishop_mvts(background, pawn, knight, rook, bishop, queen, king, key)

def check_black_queen_click(background, pawn, knight, rook, bishop, queen, king, mx, my):
    if queen.black_queen_rect.collidepoint(mx, my):
        queen.black_queen_clicked = True
        black_queen_mvts(background, pawn, knight, rook, bishop, queen, king)

def check_black_king_click(background, pawn, knight, rook, bishop, queen, king, mx, my):
    if king.black_king_rect.collidepoint(mx, my):
        king.black_king_clicked = True
        black_king_mvts(background, pawn, knight, rook, bishop, queen, king)

def update_white_rook(stats, background, rook, pawn, knight, bishop, queen, king):
    for rook0, click in rook.white_rook_clicked.items():
        if not click:

            key0 = rook.white_rook_position[rook0][1] + 1
            key1 = rook.white_rook_position[rook0][1] - 1
            ch0 = chr(ord(rook.white_rook_position[rook0][0]) + 1)
            ch1 = chr(ord(rook.white_rook_position[rook0][0]) - 1)
            if rook.white_rook_position[rook0][0] < 'h':
                while (ch0 <= "h") and (not background.board_move[ch0][str(rook.white_rook_position[rook0][1])]):

                    if (rook.white_big_rook_rects[rook0].collidepoint(rook.white_rook_rects[rook0].x + (
                       rook.defaut_rect * (ord(ch0) - ord(rook.white_rook_position[rook0][0]))), rook.white_rook_rects[rook0].y)):

                        a = rook.white_rook_position[rook0][0]
                        p = piece_check(king.wk)
                        if (p != None):
                            background.board_move[ch0][str(rook.white_rook_position[rook0][1])] = True
                            background.board_move[a][str(rook.white_rook_position[rook0][1])] = False
                            verify_king_free(p, background, rook, pawn, knight, bishop, queen, king, 'w')
                            print('True')
                            if (not king.wk[p]):
                                print('True')
                                stats.white_turn = False
                                stats.black_turn = True
                                rook.white_rook_no_move[rook0] = False

                                rook.white_rook_position[rook0][0] = ch0
                                rook.white_rook_rects[rook0].x += (rook.defaut_rect * (ord(ch0) - ord(a)))
                                pawn.pieces_move.append(rook0 + ch0 + str(rook.white_rook_position[rook0][1]))
                                print(pawn.pieces_move)
                                break
                            else:
                                background.board_move[ch0][str(rook.white_rook_position[rook0][1])] = False
                                background.board_move[a][str(rook.white_rook_position[rook0][1])] = True
                                king.white_check = False
                                king.white_check_mvt = []
                                king.wk[p] = False
                                king.wpc = None

                        else:
                            background.board_move[a][str(rook.white_rook_position[rook0][1])] = False
                            background.board_move[ch0][str(rook.white_rook_position[rook0][1])] = True
                            king_check(stats, background, rook, pawn, knight, bishop, queen, king)
                            if (not king.white_check):

                                stats.white_turn = False
                                stats.black_turn = True
                                rook.white_rook_no_move[rook0] = False

                                rook.white_rook_rects[rook0].x += (rook.defaut_rect * (ord(ch0) - ord(a)))
                                rook.white_rook_position[rook0][0] = ch0
                                pawn.pieces_move.append(rook0 + ch0 + str(rook.white_rook_position[rook0][1]))
                                print(pawn.pieces_move)
                                break
                            else:
                                background.board_move[a][str(rook.white_rook_position[rook0][1])] = True
                                background.board_move[ch0][str(rook.white_rook_position[rook0][1])] = False
                                king_check(stats, background, rook, pawn, knight, bishop, queen, king)
                    ch0 = chr(ord(ch0) + 1)

                if (rook.white_big_rook_rects[rook0].collidepoint(rook.white_rook_rects[rook0].x + (
                       rook.defaut_rect * (ord(ch0) - ord(rook.white_rook_position[rook0][0]))), rook.white_rook_rects[rook0].y)):

                    aux = rook.white_rook_position[rook0][0]
                    if verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position, rook.black_rook_position,
                            bishop.black_bishop_position, queen.black_queen_position, pawn.black_pawn_death,
                            knight.black_knight_death, rook.black_rook_death, bishop.black_bishop_death,
                            queen.black_queen_death, [ch0, rook.white_rook_position[rook0][1]], 0, 0):

                        pp = piece_check(king.wk)
                        if (pp != None):

                            if (verify_king_safe([ch0, rook.white_rook_position[rook0][1]], king.wpc, rook.black_rook_position,
                                             pawn.black_pawn_position, knight.black_knight_position,
                                             bishop.black_bishop_position, queen.black_queen_position)):
                                stats.white_turn = False
                                stats.black_turn = True
                                rook.white_rook_no_move[rook0] = False

                                background.board_move[aux][str(rook.white_rook_position[rook0][1])] = False
                                background.board_move[ch0][str(rook.white_rook_position[rook0][1])] = True
                                rook.white_rook_position[rook0][0] = ch0
                                rook.white_rook_rects[rook0].x += (rook.defaut_rect * (ord(ch0) - ord(aux)))
                                eliminate_check_piece(rook0, king.wpc, rook, pawn, knight, bishop, queen, 'b')
                                king.wk[pp] = False
                                king.white_check = False
                                king.white_check_mvt = []
                                king.wpc = None

                        else:
                            background.board_move[aux][str(rook.white_rook_position[rook0][1])] = False
                            king_check(stats, background, rook, pawn, knight, bishop, queen, king)
                            if (not king.white_check):
                                print(True)
                                stats.white_turn = False
                                stats.black_turn = True
                                rook.white_rook_no_move[rook0] = False

                                rook.white_rook_position[rook0][0] = ch0
                                rook.white_rook_rects[rook0].x += (rook.defaut_rect * (ord(ch0) - ord(aux)))
                                queen.black_queen_death = eliminate_killed_piece(rook0, [ch0, rook.white_rook_position[rook0][1]], pawn.black_pawn_position,
                                                       knight.black_knight_position, bishop.black_bishop_position,
                                                       rook.black_rook_position, queen.black_queen_position,
                                                       pawn.black_pawn_death, knight.black_knight_death,
                                                       bishop.black_bishop_death,
                                                       rook.black_rook_death, queen.black_queen_death,
                                                       pawn.black_pawn_rects, knight.black_knight_rects,
                                                       bishop.black_bishop_rects,
                                                       rook.black_rook_rects, queen.black_queen_rect,
                                                       pawn, knight, bishop, rook, queen)
                            else:
                                background.board_move[aux][str(rook.white_rook_position[rook0][1])] = True
                                king_check(stats, background, rook, pawn, knight, bishop, queen, king)

            if rook.white_rook_position[rook0][0] > 'a':
                while (ch1 >= 'a') and (not background.board_move[ch1][str(rook.white_rook_position[rook0][1])]):

                    if (rook.white_big_rook_rects[rook0].collidepoint(rook.white_rook_rects[rook0].x - (
                           rook.defaut_rect * (ord(rook.white_rook_position[rook0][0]) - ord(ch1))), rook.white_rook_rects[rook0].y)):

                        a1 = rook.white_rook_position[rook0][0]
                        p1 = piece_check(king.wk)
                        if (p1 != None):

                            background.board_move[ch1][str(rook.white_rook_position[rook0][1])] = True
                            background.board_move[a1][str(rook.white_rook_position[rook0][1])] = False
                            verify_king_free(p1, background, rook, pawn, knight, bishop, queen, king, 'w')
                            print('True')
                            if (not king.wk[p1]):
                                stats.white_turn = False
                                stats.black_turn = True
                                rook.white_rook_no_move[rook0] = False

                                rook.white_rook_rects[rook0].x -= (rook.defaut_rect * (ord(a1) - ord(ch1)))
                                rook.white_rook_position[rook0][0] = ch1
                                pawn.pieces_move.append(rook0 + ch1 + str(rook.white_rook_position[rook0][1]))
                                print(pawn.pieces_move)
                                break
                            else:
                                background.board_move[ch1][str(rook.white_rook_position[rook0][1])] = False
                                background.board_move[a1][str(rook.white_rook_position[rook0][1])] = True
                                king.white_check = False
                                king.white_check_mvt = []
                                king.wk[p1] = False
                                king.wpc = None

                        else:
                            background.board_move[a1][str(rook.white_rook_position[rook0][1])] = False
                            background.board_move[ch1][str(rook.white_rook_position[rook0][1])] = True
                            king_check(stats, background, rook, pawn, knight, bishop, queen, king)
                            if (not king.white_check):
                                stats.white_turn = False
                                stats.black_turn = True
                                rook.white_rook_no_move[rook0] = False

                                rook.white_rook_rects[rook0].x -= (rook.defaut_rect * (ord(a1) - ord(ch1)))
                                rook.white_rook_position[rook0][0] = ch1
                                pawn.pieces_move.append(rook0 + ch1 + str(rook.white_rook_position[rook0][1]))
                                print(pawn.pieces_move)
                                break
                            else:
                                background.board_move[a1][str(rook.white_rook_position[rook0][1])] = True
                                background.board_move[ch1][str(rook.white_rook_position[rook0][1])] = False
                                king_check(stats, background, rook, pawn, knight, bishop, queen, king)
                    ch1 = chr(ord(ch1) - 1)

                if (rook.white_big_rook_rects[rook0].collidepoint(rook.white_rook_rects[rook0].x - (
                    rook.defaut_rect * (ord(rook.white_rook_position[rook0][0]) - ord(ch1))), rook.white_rook_rects[rook0].y)):

                    aux1 = rook.white_rook_position[rook0][0]
                    if verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position, rook.black_rook_position,
                            bishop.black_bishop_position, queen.black_queen_position, pawn.black_pawn_death,
                            knight.black_knight_death, rook.black_rook_death, bishop.black_bishop_death,
                            queen.black_queen_death, [ch1, rook.white_rook_position[rook0][1]], 0, 0):

                        pp1 = piece_check(king.wk)
                        if (pp1 != None):

                            if (verify_king_safe([ch1, rook.white_rook_position[rook0][1]], king.wpc, rook.black_rook_position,
                                             pawn.black_pawn_position, knight.black_knight_position,
                                             bishop.black_bishop_position, queen.black_queen_position)):
                                stats.white_turn = False
                                stats.black_turn = True
                                rook.white_rook_no_move[rook0] = False

                                rook.white_rook_position[rook0][0] = ch1
                                background.board_move[aux1][str(rook.white_rook_position[rook0][1])] = False
                                background.board_move[ch1][str(rook.white_rook_position[rook0][1])] = True
                                rook.white_rook_rects[rook0].x -= (rook.defaut_rect * (ord(aux1) - ord(ch1)))
                                eliminate_check_piece(rook0, king.wpc, rook, pawn, knight, bishop, queen, 'b')
                                king.wk[pp1] = False
                                king.white_check = False
                                king.white_check_mvt = []
                                king.wpc = None

                        else:
                            background.board_move[aux1][str(rook.white_rook_position[rook0][1])] = False
                            king_check(stats, background, rook, pawn, knight, bishop, queen, king)
                            if (not king.white_check):
                                stats.white_turn = False
                                stats.black_turn = True
                                rook.white_rook_no_move[rook0] = False

                                rook.white_rook_position[rook0][0] = ch1
                                rook.white_rook_rects[rook0].x -= (rook.defaut_rect * (ord(aux1) - ord(ch1)))
                                queen.black_queen_death = eliminate_killed_piece(rook0, rook.white_rook_position[rook0], pawn.black_pawn_position,
                                                           knight.black_knight_position, bishop.black_bishop_position,
                                                           rook.black_rook_position, queen.black_queen_position,
                                                           pawn.black_pawn_death, knight.black_knight_death,
                                                           bishop.black_bishop_death,
                                                           rook.black_rook_death, queen.black_queen_death,
                                                           pawn.black_pawn_rects, knight.black_knight_rects,
                                                           bishop.black_bishop_rects,
                                                           rook.black_rook_rects, queen.black_queen_rect,
                                                           pawn, knight, bishop, rook, queen)
                            else:
                                background.board_move[aux1][str(rook.white_rook_position[rook0][1])] = True
                                king_check(stats, background, rook, pawn, knight, bishop, queen, king)

            if rook.white_rook_position[rook0][1] < 8:
                while (key0 <= 8) and (not background.board_move[rook.white_rook_position[rook0][0]][str(key0)]):

                    if (rook.white_big_rook_rects[rook0].collidepoint(rook.white_rook_rects[rook0].x,
                       rook.white_rook_rects[rook0].y - (rook.defaut_rect * (key0 - rook.white_rook_position[rook0][1])))):

                        a2 = rook.white_rook_position[rook0][1]
                        p2 = piece_check(king.wk)
                        if (p2 != None):
                            background.board_move[rook.white_rook_position[rook0][0]][str(key0)] = True
                            background.board_move[rook.white_rook_position[rook0][0]][str(a2)] = False
                            verify_king_free(p2, background, rook, pawn, knight, bishop, queen, king, 'w')
                            print('True')
                            if (not king.wk[p2]):
                                stats.white_turn = False
                                stats.black_turn = True
                                rook.white_rook_no_move[rook0] = False

                                rook.white_rook_rects[rook0].y -= (rook.defaut_rect * (key0 - a2))
                                rook.white_rook_position[rook0][1] = key0
                                pawn.pieces_move.append(rook0 + rook.white_rook_position[rook0][0] + str(key0))
                                print(pawn.pieces_move)
                                break
                            else:
                                background.board_move[rook.white_rook_position[rook0][0]][str(key0)] = False
                                background.board_move[rook.white_rook_position[rook0][0]][str(a2)] = True
                                king_check(stats, background, rook, pawn, knight, bishop, queen, king)

                        else:
                            background.board_move[rook.white_rook_position[rook0][0]][str(a2)] = False
                            background.board_move[rook.white_rook_position[rook0][0]][str(key0)] = True
                            king_check(stats, background, rook, pawn, knight, bishop, queen, king)
                            if (not king.white_check):
                                stats.white_turn = False
                                stats.black_turn = True
                                rook.white_rook_no_move[rook0] = False

                                rook.white_rook_rects[rook0].y -= (rook.defaut_rect * (key0 - a2))
                                rook.white_rook_position[rook0][1] = key0
                                pawn.pieces_move.append(rook0 + rook.white_rook_position[rook0][0] + str(key0))
                                print(pawn.pieces_move)
                                break
                            else:
                                background.board_move[rook.white_rook_position[rook0][0]][str(a2)] = True
                                background.board_move[rook.white_rook_position[rook0][0]][str(key0)] = False
                                king_check(stats, background, rook, pawn, knight, bishop, queen, king)
                    key0 += 1

                if (rook.white_big_rook_rects[rook0].collidepoint(rook.white_rook_rects[rook0].x,
                    rook.white_rook_rects[rook0].y - (rook.defaut_rect * (key0 - rook.white_rook_position[rook0][1])))):

                    aux2 = rook.white_rook_position[rook0][1]
                    if verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position, rook.black_rook_position,
                            bishop.black_bishop_position, queen.black_queen_position, pawn.black_pawn_death,
                            knight.black_knight_death, rook.black_rook_death, bishop.black_bishop_death,
                            queen.black_queen_death, [rook.white_rook_position[rook0][0], key0], 0, 0):

                        pp2 = piece_check(king.wk)
                        if (pp2 != None):
                            if (verify_king_safe([rook.white_rook_position[rook0][0], key0], king.wpc, rook.black_rook_position,
                                             pawn.black_pawn_position, knight.black_knight_position,
                                             bishop.black_bishop_position, queen.black_queen_position)):
                                stats.white_turn = False
                                stats.black_turn = True
                                rook.white_rook_no_move[rook0] = False

                                rook.white_rook_position[rook0][1] = key0
                                background.board_move[rook.white_rook_position[rook0][0]][str(aux2)] = False
                                background.board_move[rook.white_rook_position[rook0][0]][str(key0)] = True
                                rook.white_rook_rects[rook0].y -= (rook.defaut_rect * (key0 - aux2))
                                eliminate_check_piece(rook0, king.wpc, rook, pawn, knight, bishop, queen, 'b')
                                king.wk[pp2] = False
                                king.white_check = False
                                king.white_check_mvt = []
                                king.wpc = None

                        else:
                            background.board_move[rook.white_rook_position[rook0][0]][str(aux2)] = False
                            king_check(stats, background, rook, pawn, knight, bishop, queen, king)
                            if (not king.white_check):
                                stats.white_turn = False
                                stats.black_turn = True
                                rook.white_rook_no_move[rook0] = False

                                rook.white_rook_position[rook0][1] = key0
                                rook.white_rook_rects[rook0].y -= (rook.defaut_rect * (key0 - aux2))
                                queen.black_queen_death = eliminate_killed_piece(rook0, rook.white_rook_position[rook0], pawn.black_pawn_position,
                                                       knight.black_knight_position, bishop.black_bishop_position,
                                                       rook.black_rook_position, queen.black_queen_position,
                                                       pawn.black_pawn_death, knight.black_knight_death,
                                                       bishop.black_bishop_death,
                                                       rook.black_rook_death, queen.black_queen_death,
                                                       pawn.black_pawn_rects, knight.black_knight_rects,
                                                       bishop.black_bishop_rects,
                                                       rook.black_rook_rects, queen.black_queen_rect,
                                                       pawn, knight, bishop, rook, queen)
                            else:
                                background.board_move[rook.white_rook_position[rook0][0]][str(aux2)] = True
                                king_check(stats, background, rook, pawn, knight, bishop, queen, king)

            if rook.white_rook_position[rook0][1] > 1:
                while (key1 >= 1) and (not background.board_move[rook.white_rook_position[rook0][0]][str(key1)]):

                    if (rook.white_big_rook_rects[rook0].collidepoint(rook.white_rook_rects[rook0].x,
                        rook.white_rook_rects[rook0].y + (rook.defaut_rect * (rook.white_rook_position[rook0][1] - key1)))):

                        a3 = rook.white_rook_position[rook0][1]
                        p3 = piece_check(king.wk)
                        if (p3 != None):
                            background.board_move[rook.white_rook_position[rook0][0]][str(key1)] = True
                            background.board_move[rook.white_rook_position[rook0][0]][str(a3)] = False
                            verify_king_free(p3, background, rook, pawn, knight, bishop, queen, king, 'w')
                            print('True')
                            if (not king.wk[p3]):
                                stats.white_turn = False
                                stats.black_turn = True
                                rook.white_rook_no_move[rook0] = False

                                rook.white_rook_rects[rook0].y += (rook.defaut_rect * (a3 - key1))
                                rook.white_rook_position[rook0][1] = key1
                                pawn.pieces_move.append(rook0 + rook.white_rook_position[rook0][0] + str(key1))
                                print(pawn.pieces_move)
                                break
                            else:
                                background.board_move[rook.white_rook_position[rook0][0]][str(key1)] = False
                                background.board_move[rook.white_rook_position[rook0][0]][str(a3)] = True
                                king_check(stats, background, rook, pawn, knight, bishop, queen, king)

                        else:
                            background.board_move[rook.white_rook_position[rook0][0]][str(a3)] = False
                            background.board_move[rook.white_rook_position[rook0][0]][str(key1)] = True
                            king_check(background, rook, pawn, knight, bishop, queen, king)
                            if (not king.white_check):
                                stats.white_turn = False
                                stats.black_turn = True
                                rook.white_rook_no_move[rook0] = False

                                rook.white_rook_rects[rook0].y += (rook.defaut_rect * (a3 - key1))
                                rook.white_rook_position[rook0][1] = key1
                                pawn.pieces_move.append(rook0 + rook.white_rook_position[rook0][0] + str(key1))
                                print(pawn.pieces_move)
                                break
                            else:
                                background.board_move[rook.white_rook_position[rook0][0]][str(a3)] = True
                                background.board_move[rook.white_rook_position[rook0][0]][str(key1)] = False
                                king_check(stats, background, rook, pawn, knight, bishop, queen, king)
                    key1 -= 1

                if (rook.white_big_rook_rects[rook0].collidepoint(rook.white_rook_rects[rook0].x,
                    rook.white_rook_rects[rook0].y + (rook.defaut_rect * (rook.white_rook_position[rook0][1] - key1)))):

                    aux3 = rook.white_rook_position[rook0][1]
                    if verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position, rook.black_rook_position,
                            bishop.black_bishop_position, queen.black_queen_position, pawn.black_pawn_death,
                            knight.black_knight_death, rook.black_rook_death, bishop.black_bishop_death,
                            queen.black_queen_death, [rook.white_rook_position[rook0][0], key1], 0, 0):

                        pp3 = piece_check(king.wk)
                        if (pp3 != None):
                            if (verify_king_safe([rook.white_rook_position[rook0][0], key1], king.wpc, rook.black_rook_position,
                                     pawn.black_pawn_position, knight.black_knight_position,
                                     bishop.black_bishop_position, queen.black_queen_position)):
                                stats.white_turn = False
                                stats.black_turn = True
                                rook.white_rook_no_move[rook0] = False

                                rook.white_rook_position[rook0][1] = key1
                                background.board_move[rook.white_rook_position[rook0][0]][str(aux3)] = False
                                background.board_move[rook.white_rook_position[rook0][0]][str(key1)] = True
                                rook.white_rook_rects[rook0].y += (rook.defaut_rect * (aux3 - key1))
                                eliminate_check_piece(rook0, king.wpc, rook, pawn, knight, bishop, queen, 'b')
                                king.wk[pp3] = False
                                king.white_check = False
                                king.white_check_mvt = []
                                king.wpc = None

                        else:
                            background.board_move[rook.white_rook_position[rook0][0]][str(aux3)] = False
                            king_check(stats, background, rook, pawn, knight, bishop, queen, king)
                            if (not king.white_check):
                                stats.white_turn = False
                                stats.black_turn = True
                                rook.white_rook_no_move[rook0] = False

                                rook.white_rook_position[rook0][1] = key1
                                rook.white_rook_rects[rook0].y += (rook.defaut_rect * (aux3 - key1))
                                queen.black_queen_death = eliminate_killed_piece(rook0, rook.white_rook_position[rook0], pawn.black_pawn_position,
                                                       knight.black_knight_position, bishop.black_bishop_position,
                                                       rook.black_rook_position, queen.black_queen_position,
                                                       pawn.black_pawn_death, knight.black_knight_death,
                                                       bishop.black_bishop_death,
                                                       rook.black_rook_death, queen.black_queen_death,
                                                       pawn.black_pawn_rects, knight.black_knight_rects,
                                                       bishop.black_bishop_rects,
                                                       rook.black_rook_rects, queen.black_queen_rect,
                                                       pawn, knight, bishop, rook, queen)
                            else:
                                background.board_move[rook.white_rook_position[rook0][0]][str(aux3)] = True
                                king_check(stats, background, rook, pawn, knight, bishop, queen, king)

def update_black_rook(stats, background, rook, pawn, knight, bishop, queen, king):
    for rook0, click in rook.black_rook_clicked.items():
        if not click:

            key0 = rook.black_rook_position[rook0][1] + 1
            key1 = rook.black_rook_position[rook0][1] - 1
            ch0 = chr(ord(rook.black_rook_position[rook0][0]) + 1)
            ch1 = chr(ord(rook.black_rook_position[rook0][0]) - 1)
            if rook.black_rook_position[rook0][0] < 'h':
                while (ch0 <= "h") and (not background.board_move[ch0][str(rook.black_rook_position[rook0][1])]):

                    if (rook.black_big_rook_rects[rook0].collidepoint(rook.black_rook_rects[rook0].x + (
                       rook.defaut_rect * (ord(ch0) - ord(rook.black_rook_position[rook0][0]))),
                       rook.black_rook_rects[rook0].y)):

                        a = rook.black_rook_position[rook0][0]
                        p = piece_check(king.bk)
                        if (p != None):
                            background.board_move[ch0][str(rook.black_rook_position[rook0][1])] = True
                            background.board_move[a][str(rook.black_rook_position[rook0][1])] = False
                            verify_king_free(p, background, rook, pawn, knight, bishop, queen, king, 'b')
                            print('True')
                            if (not king.bk[p]):
                                stats.black_turn = False
                                stats.white_turn = True
                                rook.black_rook_no_move[rook0] = False
                                rook.black_rook_rects[rook0].x += (rook.defaut_rect * (ord(ch0) - ord(a)))
                                rook.black_rook_position[rook0][0] = ch0
                                pawn.pieces_move.append(rook0 + ch0 + str(rook.black_rook_position[rook0][1]))
                                print(pawn.pieces_move)
                                break
                            else:
                                background.board_move[ch0][str(rook.black_rook_position[rook0][1])] = False
                                background.board_move[a][str(rook.black_rook_position[rook0][1])] = True
                                king.black_check = False
                                king.black_check_mvt = []
                                king.bk[piece_check(king.bk)] = False
                                king.bpc = None

                        else:
                            background.board_move[a][str(rook.black_rook_position[rook0][1])] = False
                            background.board_move[ch0][str(rook.black_rook_position[rook0][1])] = True
                            king_check(stats, background, rook, pawn, knight, bishop, queen, king)
                            if (not king.black_check):
                                stats.black_turn = False
                                stats.white_turn = True
                                rook.black_rook_no_move[rook0] = False
                                rook.black_rook_rects[rook0].x += (rook.defaut_rect * (ord(ch0) - ord(a)))
                                rook.black_rook_position[rook0][0] = ch0
                                pawn.pieces_move.append(rook0 + ch0 + str(rook.black_rook_position[rook0][1]))
                                print(pawn.pieces_move)
                                break
                            else:
                                background.board_move[a][str(rook.black_rook_position[rook0][1])] = True
                                background.board_move[ch0][str(rook.black_rook_position[rook0][1])] = False
                                king.black_check = False
                                king.black_check_mvt = []
                                king.bk[piece_check(king.bk)] = False
                                king.bpc = None
                    ch0 = chr(ord(ch0) + 1)

                if (rook.black_big_rook_rects[rook0].collidepoint(rook.black_rook_rects[rook0].x + (
                    rook.defaut_rect * (ord(ch0) - ord(rook.black_rook_position[rook0][0]))), rook.black_rook_rects[rook0].y)):

                    aux1 = rook.black_rook_position[rook0][0]
                    if verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position, rook.white_rook_position,
                                           bishop.white_bishop_position, queen.white_queen_position, pawn.white_pawn_death,
                                           knight.white_knight_death, rook.white_rook_death, bishop.white_bishop_death,
                                           queen.white_queen_death, [ch0, rook.black_rook_position[rook0][1]], 0, 0):
                        if (king.bpc != None):
                            if (verify_king_safe([ch0, rook.black_rook_position[rook0][1]], king.bpc, rook.white_rook_position,
                                             pawn.white_pawn_position, knight.white_knight_position,
                                             bishop.white_bishop_position, queen.white_queen_position)):
                                stats.black_turn = False
                                stats.white_turn = True
                                rook.black_rook_no_move[rook0] = False
                                background.board_move[aux1][str(rook.black_rook_position[rook0][1])] = False
                                background.board_move[ch0][str(rook.black_rook_position[rook0][1])] = True
                                rook.black_rook_position[rook0][0] = ch0
                                rook.black_rook_rects[rook0].x += (rook.defaut_rect * (ord(ch0) - ord(aux1)))
                                eliminate_check_piece(rook0, king.bpc, rook, pawn, knight, bishop, queen, 'w')
                                king.bk[piece_check(king.bk)] = False
                                king.black_check = False
                                king.black_check_mvt = []
                                king.bpc = None

                        else:
                            background.board_move[aux1][str(rook.black_rook_position[rook0][1])] = False
                            king_check(stats, background, rook, pawn, knight, bishop, queen, king)
                            if (not king.black_check):

                                stats.black_turn = False
                                stats.white_turn = True
                                rook.black_rook_no_move[rook0] = False

                                background.board_move[ch0][str(rook.black_rook_position[rook0][1])] = True
                                rook.black_rook_position[rook0][0] = ch0
                                rook.black_rook_rects[rook0].x += (rook.defaut_rect * (ord(ch0) - ord(aux1)))
                                queen.white_queen_death = eliminate_killed_piece(rook0, rook.black_rook_position[rook0], pawn.white_pawn_position,
                                                       knight.white_knight_position, bishop.white_bishop_position,
                                                       rook.white_rook_position, queen.white_queen_position,
                                                       pawn.white_pawn_death, knight.white_knight_death,
                                                       bishop.white_bishop_death,
                                                       rook.white_rook_death, queen.white_queen_death,
                                                       pawn.white_pawn_rects, knight.white_knight_rects,
                                                       bishop.white_bishop_rects,
                                                       rook.white_rook_rects, queen.white_queen_rect,
                                                       pawn, knight, bishop, rook, queen)
                            else:
                                background.board_move[aux1][str(rook.black_rook_position[rook0][1])] = True
                                king.black_check = False
                                king.black_check_mvt = []
                                king.bk[piece_check(king.bk)] = False
                                king.bpc = None

            if rook.black_rook_position[rook0][0] > 'a':
                while (ch1 >= 'a') and (not background.board_move[ch1][str(rook.black_rook_position[rook0][1])]):

                    if (rook.black_big_rook_rects[rook0].collidepoint(rook.black_rook_rects[rook0].x - (
                           rook.defaut_rect * (ord(rook.black_rook_position[rook0][0]) - ord(ch1))), rook.black_rook_rects[rook0].y)):

                        a1 = rook.black_rook_position[rook0][0]
                        p1 = piece_check(king.bk)
                        if (p1 != None):
                            background.board_move[ch1][str(rook.black_rook_position[rook0][1])] = True
                            background.board_move[a1][str(rook.black_rook_position[rook0][1])] = False
                            verify_king_free(p1, background, rook, pawn, knight, bishop, queen, king, 'b')
                            print('True')
                            if (not king.bk[p1]):
                                stats.black_turn = False
                                stats.white_turn = True
                                rook.black_rook_no_move[rook0] = False

                                rook.black_rook_rects[rook0].x -= (rook.defaut_rect * (ord(a1) - ord(ch1)))
                                rook.black_rook_position[rook0][0] = ch1
                                pawn.pieces_move.append(rook0 + ch1 + str(rook.black_rook_position[rook0][1]))
                                print(pawn.pieces_move)
                                break
                            else:
                                background.board_move[a1][str(rook.black_rook_position[rook0][1])] = True
                                background.board_move[ch1][str(rook.black_rook_position[rook0][1])] = False
                                king.black_check = False
                                king.black_check_mvt = []
                                king.bk[piece_check(king.bk)] = False
                                king.bpc = None

                        else:
                            background.board_move[a1][str(rook.black_rook_position[rook0][1])] = False
                            background.board_move[ch1][str(rook.black_rook_position[rook0][1])] = True
                            king_check(stats, background, rook, pawn, knight, bishop, queen, king)
                            if (not king.black_check):
                                stats.black_turn = False
                                stats.white_turn = True
                                rook.black_rook_no_move[rook0] = False

                                rook.black_rook_rects[rook0].x -= (rook.defaut_rect * (ord(a1) - ord(ch1)))
                                rook.black_rook_position[rook0][0] = ch1
                                pawn.pieces_move.append(rook0 + ch1 + str(rook.black_rook_position[rook0][1]))
                                print(pawn.pieces_move)
                                break
                            else:
                                background.board_move[a1][str(rook.black_rook_position[rook0][1])] = True
                                background.board_move[ch1][str(rook.black_rook_position[rook0][1])] = False
                                king.black_check = False
                                king.black_check_mvt = []
                                king.bk[piece_check(king.bk)] = False
                                king.bpc = None
                    ch1 = chr(ord(ch1) - 1)

                if (rook.black_big_rook_rects[rook0].collidepoint(rook.black_rook_rects[rook0].x - (
                    rook.defaut_rect * (ord(rook.black_rook_position[rook0][0]) - ord(ch1))), rook.black_rook_rects[rook0].y)):

                    aux2 = rook.black_rook_position[rook0][0]
                    if verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position, rook.white_rook_position,
                                           bishop.white_bishop_position, queen.white_queen_position, pawn.white_pawn_death,
                                           knight.white_knight_death, rook.white_rook_death, bishop.white_bishop_death,
                                           queen.white_queen_death, [ch1, rook.black_rook_position[rook0][1]], 0, 0):

                        if (king.bpc != None):
                            if (verify_king_safe([ch1, rook.black_rook_position[rook0][1]], king.bpc, rook.white_rook_position,
                                             pawn.white_pawn_position, knight.white_knight_position,
                                             bishop.white_bishop_position, queen.white_queen_position)):
                                stats.black_turn = False
                                stats.white_turn = True
                                rook.black_rook_no_move[rook0] = False

                                rook.black_rook_position[rook0][0] = ch1
                                background.board_move[aux2][str(rook.black_rook_position[rook0][1])] = False
                                background.board_move[ch1][str(rook.black_rook_position[rook0][1])] = True
                                rook.black_rook_rects[rook0].x -= (rook.defaut_rect * (ord(aux2) - ord(ch1)))
                                eliminate_check_piece(rook0, king.bpc, rook, pawn, knight, bishop, queen, 'w')
                                king.bk[piece_check(king.bk)] = False
                                king.black_check = False
                                king.black_check_mvt = []
                                king.bpc = None

                        else:
                            background.board_move[aux2][str(rook.black_rook_position[rook0][1])] = False
                            king_check(stats, background, rook, pawn, knight, bishop, queen, king)
                            if (not king.black_check):

                                stats.black_turn = False
                                stats.white_turn = True
                                rook.black_rook_no_move[rook0] = False

                                rook.black_rook_rects[rook0].x -= (rook.defaut_rect * (ord(aux2) - ord(ch1)))
                                rook.black_rook_position[rook0][0] = ch1
                                queen.white_queen_death = eliminate_killed_piece(rook0, rook.black_rook_position[rook0], pawn.white_pawn_position,
                                                       knight.white_knight_position, bishop.white_bishop_position,
                                                       rook.white_rook_position, queen.white_queen_position,
                                                       pawn.white_pawn_death, knight.white_knight_death,
                                                       bishop.white_bishop_death,
                                                       rook.white_rook_death, queen.white_queen_death,
                                                       pawn.white_pawn_rects, knight.white_knight_rects,
                                                       bishop.white_bishop_rects,
                                                       rook.white_rook_rects, queen.white_queen_rect,
                                                       pawn, knight, bishop, rook, queen)
                            else:
                                background.board_move[aux2][str(rook.black_rook_position[rook0][1])] = True
                                king.black_check = False
                                king.black_check_mvt = []
                                king.bk[piece_check(king.bk)] = False
                                king.bpc = None

            if rook.black_rook_position[rook0][1] < 8:
                while (key0 <= 8) and (not background.board_move[rook.black_rook_position[rook0][0]][str(key0)]):

                    if (rook.black_big_rook_rects[rook0].collidepoint(rook.black_rook_rects[rook0].x,
                        rook.black_rook_rects[rook0].y - (rook.defaut_rect * (key0 - rook.black_rook_position[rook0][1])))):

                        a2 = rook.black_rook_position[rook0][1]
                        p2 = piece_check(king.bk)
                        if (p2 != None):
                            background.board_move[rook.black_rook_position[rook0][0]][str(key0)] = True
                            background.board_move[rook.black_rook_position[rook0][0]][str(a2)] = False
                            verify_king_free(p2, background, rook, pawn, knight, bishop, queen, king, 'b')
                            print('True')
                            if (not king.bk[p2]):
                                stats.black_turn = False
                                stats.white_turn = True
                                rook.black_rook_no_move[rook0] = False

                                rook.black_rook_rects[rook0].y -= (rook.defaut_rect * (key0 - a2))
                                rook.black_rook_position[rook0][1] = key0
                                pawn.pieces_move.append(rook0 + rook.black_rook_position[rook0][0] + str(key0))
                                print(pawn.pieces_move)
                                break
                            else:
                                background.board_move[rook.black_rook_position[rook0][0]][str(key0)] = False
                                background.board_move[rook.black_rook_position[rook0][0]][str(a2)] = True
                                king.black_check = False
                                king.black_check_mvt = []
                                king.bk[piece_check(king.bk)] = False
                                king.bpc = None

                        else:
                            background.board_move[rook.black_rook_position[rook0][0]][str(a2)] = False
                            background.board_move[rook.black_rook_position[rook0][0]][str(key0)] = True
                            king_check(stats, background, rook, pawn, knight, bishop, queen, king)
                            if (not king.black_check):
                                stats.black_turn = False
                                stats.white_turn = True
                                rook.black_rook_no_move[rook0] = False

                                rook.black_rook_rects[rook0].y -= (rook.defaut_rect * (key0 - a2))
                                rook.black_rook_position[rook0][1] = key0
                                pawn.pieces_move.append(rook0 + rook.black_rook_position[rook0][0] + str(key0))
                                print(pawn.pieces_move)
                                break
                            else:
                                background.board_move[rook.black_rook_position[rook0][0]][str(a2)] = True
                                background.board_move[rook.black_rook_position[rook0][0]][str(key0)] = False
                                king.black_check = False
                                king.black_check_mvt = []
                                king.bk[piece_check(king.bk)] = False
                                king.bpc = None
                    key0 += 1

                if (rook.black_big_rook_rects[rook0].collidepoint(rook.black_rook_rects[rook0].x,
                    rook.black_rook_rects[rook0].y - (rook.defaut_rect * (key0 - rook.black_rook_position[rook0][1])))):

                    aux3 = rook.black_rook_position[rook0][1]
                    if verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position, rook.white_rook_position,
                                           bishop.white_bishop_position, queen.white_queen_position, pawn.white_pawn_death,
                                           knight.white_knight_death, rook.white_rook_death, bishop.white_bishop_death,
                                           queen.white_queen_death, [rook.black_rook_position[rook0][0], key0], 0, 0):
                        if (king.bpc != None):
                            if (verify_king_safe([rook.black_rook_position[rook0][0], key0], king.bpc, rook.white_rook_position,
                                             pawn.white_pawn_position, knight.white_knight_position,
                                             bishop.white_bishop_position, queen.white_queen_position)):
                                stats.black_turn = False
                                stats.white_turn = True
                                rook.black_rook_no_move[rook0] = False

                                rook.black_rook_position[rook0][1] = key0
                                background.board_move[rook.black_rook_position[rook0][0]][str(aux3)] = False
                                background.board_move[rook.black_rook_position[rook0][0]][str(key0)] = True
                                rook.black_rook_rects[rook0].y -= (rook.defaut_rect * (key0 - aux3))
                                eliminate_check_piece(rook0, king.bpc, rook, pawn, knight, bishop, queen, 'w')
                                king.bk[piece_check(king.bk)] = False
                                king.black_check = False
                                king.black_check_mvt = []
                                king.bpc = None

                        else:
                            background.board_move[rook.black_rook_position[rook0][0]][str(aux3)] = False
                            king_check(stats, background, rook, pawn, knight, bishop, queen, king)
                            if (not king.black_check):

                                stats.black_turn = False
                                stats.white_turn = True
                                rook.black_rook_no_move[rook0] = False

                                rook.black_rook_position[rook0][1] = key0
                                rook.black_rook_rects[rook0].y -= (rook.defaut_rect * (key0 - aux3))
                                queen.white_queen_death = eliminate_killed_piece(rook0, rook.black_rook_position[rook0], pawn.white_pawn_position,
                                                       knight.white_knight_position, bishop.white_bishop_position,
                                                       rook.white_rook_position, queen.white_queen_position,
                                                       pawn.white_pawn_death, knight.white_knight_death,
                                                       bishop.white_bishop_death,
                                                       rook.white_rook_death, queen.white_queen_death,
                                                       pawn.white_pawn_rects, knight.white_knight_rects,
                                                       bishop.white_bishop_rects,
                                                       rook.white_rook_rects, queen.white_queen_rect,
                                                       pawn, knight, bishop, rook, queen)
                            else:
                                background.board_move[rook.black_rook_position[rook0][0]][str(aux3)] = True
                                king.black_check = False
                                king.black_check_mvt = []
                                king.bk[piece_check(king.bk)] = False
                                king.bpc = None

            if rook.black_rook_position[rook0][1] > 1:
                while (key1 >= 1) and (not background.board_move[rook.black_rook_position[rook0][0]][str(key1)]):

                    if (rook.black_big_rook_rects[rook0].collidepoint(rook.black_rook_rects[rook0].x,
                        rook.black_rook_rects[rook0].y + (rook.defaut_rect * (rook.black_rook_position[rook0][1] - key1)))):

                        a3 = rook.black_rook_position[rook0][1]
                        p3 = piece_check(king.bk)
                        if (p3 != None):
                            background.board_move[rook.black_rook_position[rook0][0]][str(key1)] = True
                            background.board_move[rook.black_rook_position[rook0][0]][str(a3)] = False
                            verify_king_free(p3, background, rook, pawn, knight, bishop, queen, king, 'b')
                            print('True')
                            if (not king.bk[p3]):
                                stats.black_turn = False
                                stats.white_turn = True
                                rook.black_rook_no_move[rook0] = False

                                background.board_move[rook.black_rook_position[rook0][0]][str(a3)] = False
                                background.board_move[rook.black_rook_position[rook0][0]][str(key1)] = True
                                rook.black_rook_rects[rook0].y += (rook.defaut_rect * (a3 - key1))
                                rook.black_rook_position[rook0][1] = key1
                                pawn.pieces_move.append(rook0 + rook.black_rook_position[rook0][0] + str(key1))
                                print(pawn.pieces_move)
                                break
                            else:
                                background.board_move[rook.black_rook_position[rook0][0]][str(key1)] = False
                                background.board_move[rook.black_rook_position[rook0][0]][str(a3)] = True
                                king.black_check = False
                                king.black_check_mvt = []
                                king.bk[piece_check(king.bk)] = False
                                king.bpc = None

                        else:
                            background.board_move[rook.black_rook_position[rook0][0]][str(key1)] = True
                            background.board_move[rook.black_rook_position[rook0][0]][str(a3)] = False
                            king_check(stats, background, rook, pawn, knight, bishop, queen, king)
                            if (not king.black_check):
                                stats.black_turn = False
                                stats.white_turn = True
                                rook.black_rook_no_move[rook0] = False

                                rook.black_rook_rects[rook0].y += (rook.defaut_rect * (a3 - key1))
                                rook.black_rook_position[rook0][1] = key1
                                pawn.pieces_move.append(rook0 + rook.black_rook_position[rook0][0] + str(key1))
                                print(pawn.pieces_move)
                                break
                            else:
                                background.board_move[rook.black_rook_position[rook0][0]][str(key1)] = False
                                background.board_move[rook.black_rook_position[rook0][0]][str(a3)] = True
                                king.black_check = False
                                king.black_check_mvt = []
                                king.bk[piece_check(king.bk)] = False
                                king.bpc = None
                    key1 -= 1

                if (rook.black_big_rook_rects[rook0].collidepoint(rook.black_rook_rects[rook0].x,
                    rook.black_rook_rects[rook0].y + (rook.defaut_rect * (rook.black_rook_position[rook0][1] - key1)))):

                    aux4 = rook.black_rook_position[rook0][1]
                    if verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position, rook.white_rook_position,
                                           bishop.white_bishop_position, queen.white_queen_position, pawn.white_pawn_death,
                                           knight.white_knight_death, rook.white_rook_death, bishop.white_bishop_death,
                                           queen.white_queen_death, [rook.black_rook_position[rook0][0], key1], 0, 0):
                        if (king.bpc != None):
                            if (verify_king_safe([rook.black_rook_position[rook0][0], key1], king.bpc, rook.white_rook_position,
                                             pawn.white_pawn_position, knight.white_knight_position,
                                             bishop.white_bishop_position, queen.white_queen_position)):
                                print(True)
                                stats.black_turn = False
                                stats.white_turn = True
                                rook.black_rook_no_move[rook0] = False

                                rook.black_rook_position[rook0][1] = key1
                                background.board_move[rook.black_rook_position[rook0][0]][str(aux4)] = False
                                background.board_move[rook.black_rook_position[rook0][0]][str(key1)] = True
                                rook.black_rook_rects[rook0].y += rook.defaut_rect * (aux4 - key1)
                                eliminate_check_piece(rook0, king.bpc, rook, pawn, knight, bishop, queen, 'w')
                                king.bk[piece_check(king.bk)] = False
                                king.black_check = False
                                king.black_check_mvt = []
                                king.bpc = None

                        else:
                            background.board_move[rook.black_rook_position[rook0][0]][str(aux4)] = False
                            king_check(stats, background, rook, pawn, knight, bishop, queen, king)
                            if (not king.black_check):
                                print(True)
                                stats.black_turn = False
                                stats.white_turn = True
                                rook.black_rook_no_move[rook0] = False

                                rook.black_rook_position[rook0][1] = key1
                                rook.black_rook_rects[rook0].y += rook.defaut_rect * (aux4 - key1)
                                queen.white_queen_death = eliminate_killed_piece(rook0, rook.black_rook_position[rook0], pawn.white_pawn_position,
                                                       knight.white_knight_position, bishop.white_bishop_position,
                                                       rook.white_rook_position, queen.white_queen_position,
                                                       pawn.white_pawn_death, knight.white_knight_death,
                                                       bishop.white_bishop_death,
                                                       rook.white_rook_death, queen.white_queen_death,
                                                       pawn.white_pawn_rects, knight.white_knight_rects,
                                                       bishop.white_bishop_rects,
                                                       rook.white_rook_rects, queen.white_queen_rect,
                                                       pawn, knight, bishop, rook, queen)
                            else:
                                background.board_move[rook.black_rook_position[rook0][0]][str(aux4)] = True
                                king.black_check = False
                                king.black_check_mvt = []
                                king.bk[piece_check(king.bk)] = False
                                king.bpc = None

def white_rook_mvts(background, pawn, knight, rook, bishop, queen, king, key):

    rook.white_rook_move[key][0] = background.board_rect[rook.white_rook_position[key][0]][str(rook.white_rook_position[key][1])]

    ch0 = chr(ord(rook.white_rook_position[key][0]) + 1)
    ch1 = chr(ord(rook.white_rook_position[key][0]) - 1)
    index0 = rook.white_rook_position[key][1] + 1
    index1 = rook.white_rook_position[key][1] - 1

    if rook.white_rook_position[key][0] < 'h':
        while (ch0 <= 'h') and (not background.board_move[ch0][str(rook.white_rook_position[key][1])]):
            rook.white_rook_move[key].append(background.board_rect[ch0][str(rook.white_rook_position[key][1])])
            ch0 = chr(ord(ch0) + 1)

        aux0 = rook.white_rook_position[key][0]
        rook.white_rook_position[key][0] = ch0
        if verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position, rook.black_rook_position,
                            bishop.black_bishop_position, queen.black_queen_position, pawn.black_pawn_death,
                            knight.black_knight_death, rook.black_rook_death, bishop.black_bishop_death,
                            queen.black_queen_death, rook.white_rook_position[key], 0, 0):

            rook.white_rook_attack[key].append(background.board_rect[ch0][str(rook.white_rook_position[key][1])])
        rook.white_rook_position[key][0] = aux0

    if rook.white_rook_position[key][0] > 'a':
        while (ch1 >= 'a') and (not background.board_move[ch1][str(rook.white_rook_position[key][1])]):
            rook.white_rook_move[key].append(background.board_rect[ch1][str(rook.white_rook_position[key][1])])
            ch1 = chr(ord(ch1) - 1)

        aux1 = rook.white_rook_position[key][0]
        rook.white_rook_position[key][0] = ch1
        if verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position, rook.black_rook_position,
                            bishop.black_bishop_position, queen.black_queen_position, pawn.black_pawn_death,
                            knight.black_knight_death, rook.black_rook_death, bishop.black_bishop_death,
                            queen.black_queen_death, rook.white_rook_position[key], 0, 0):

            rook.white_rook_attack[key].append(background.board_rect[ch1][str(rook.white_rook_position[key][1])])
        rook.white_rook_position[key][0] = aux1

    if rook.white_rook_position[key][1] < 8:
        while (index0 <= 8) and (not background.board_move[rook.white_rook_position[key][0]][str(index0)]):
            rook.white_rook_move[key].append(background.board_rect[rook.white_rook_position[key][0]][str(index0)])
            index0 += 1

        aux2 = rook.white_rook_position[key][1]
        rook.white_rook_position[key][1] = index0
        if verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position, rook.black_rook_position,
                            bishop.black_bishop_position, queen.black_queen_position, pawn.black_pawn_death,
                            knight.black_knight_death, rook.black_rook_death, bishop.black_bishop_death,
                            queen.black_queen_death, rook.white_rook_position[key], 0, 0):

            rook.white_rook_attack[key].append(background.board_rect[rook.white_rook_position[key][0]][str(index0)])
        rook.white_rook_position[key][1] = aux2

    if rook.white_rook_position[key][1] > 1:
        while (index1 >= 1) and (not background.board_move[rook.white_rook_position[key][0]][str(index1)]):
            rook.white_rook_move[key].append(background.board_rect[rook.white_rook_position[key][0]][str(index1)])
            index1 -= 1

        aux3 = rook.white_rook_position[key][1]
        rook.white_rook_position[key][1] = index1
        if verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position, rook.black_rook_position,
                            bishop.black_bishop_position, queen.black_queen_position, pawn.black_pawn_death,
                            knight.black_knight_death, rook.black_rook_death, bishop.black_bishop_death,
                            queen.black_queen_death, rook.white_rook_position[key], 0, 0):

            rook.white_rook_attack[key].append(background.board_rect[rook.white_rook_position[key][0]][str(index1)])
        rook.white_rook_position[key][1] = aux3

def black_rook_mvts(background, pawn, knight, rook, bishop, queen, king, key):

    rook.black_rook_move[key][0] = background.board_rect[rook.black_rook_position[key][0]][str(rook.black_rook_position[key][1])]

    ch0 = chr(ord(rook.black_rook_position[key][0]) + 1)
    ch1 = chr(ord(rook.black_rook_position[key][0]) - 1)
    index0 = rook.black_rook_position[key][1] + 1
    index1 = rook.black_rook_position[key][1] - 1

    if rook.black_rook_position[key][0] < 'h':
        while (ch0 <= 'h') and (not background.board_move[ch0][str(rook.black_rook_position[key][1])]):
            rook.black_rook_move[key].append(background.board_rect[ch0][str(rook.black_rook_position[key][1])])
            ch0 = chr(ord(ch0) + 1)

        aux0 = rook.black_rook_position[key][0]
        rook.black_rook_position[key][0] = ch0
        if verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position, rook.white_rook_position,
                                           bishop.white_bishop_position, queen.white_queen_position, pawn.white_pawn_death,
                                           knight.white_knight_death, rook.white_rook_death, bishop.white_bishop_death,
                                           queen.white_queen_death, rook.black_rook_position[key], 0, 0):

            rook.black_rook_attack[key].append(background.board_rect[ch0][str(rook.black_rook_position[key][1])])
        rook.black_rook_position[key][0] = aux0

    if rook.black_rook_position[key][0] > 'a':
        while (ch1 >= 'a') and (not background.board_move[ch1][str(rook.black_rook_position[key][1])]):
            rook.black_rook_move[key].append(background.board_rect[ch1][str(rook.black_rook_position[key][1])])
            ch1 = chr(ord(ch1) - 1)

        aux1 = rook.black_rook_position[key][0]
        rook.black_rook_position[key][0] = ch1
        if verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position, rook.white_rook_position,
                                           bishop.white_bishop_position, queen.white_queen_position, pawn.white_pawn_death,
                                           knight.white_knight_death, rook.white_rook_death, bishop.white_bishop_death,
                                           queen.white_queen_death, rook.black_rook_position[key], 0, 0):

            rook.black_rook_attack[key].append(background.board_rect[ch1][str(rook.black_rook_position[key][1])])
        rook.black_rook_position[key][0] = aux1

    if rook.black_rook_position[key][1] < 8:
        while (index0 <= 8) and (not background.board_move[rook.black_rook_position[key][0]][str(index0)]):
            rook.black_rook_move[key].append(background.board_rect[rook.black_rook_position[key][0]][str(index0)])
            index0 += 1

        aux2 = rook.black_rook_position[key][1]
        rook.black_rook_position[key][1] = index0
        if verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position, rook.white_rook_position,
                                           bishop.white_bishop_position, queen.white_queen_position, pawn.white_pawn_death,
                                           knight.white_knight_death, rook.white_rook_death, bishop.white_bishop_death,
                                           queen.white_queen_death, rook.black_rook_position[key], 0, 0):

            rook.black_rook_attack[key].append(background.board_rect[rook.black_rook_position[key][0]][str(index0)])
        rook.black_rook_position[key][1] = aux2

    if rook.black_rook_position[key][1] > 1:
        while (index1 >= 1) and (not background.board_move[rook.black_rook_position[key][0]][str(index1)]):
            rook.black_rook_move[key].append(background.board_rect[rook.black_rook_position[key][0]][str(index1)])
            index1 -= 1

        aux3 = rook.black_rook_position[key][1]
        rook.black_rook_position[key][1] = index1
        if verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position, rook.white_rook_position,
                                           bishop.white_bishop_position, queen.white_queen_position, pawn.white_pawn_death,
                                           knight.white_knight_death, rook.white_rook_death, bishop.white_bishop_death,
                                           queen.white_queen_death, rook.black_rook_position[key], 0, 0):

            rook.black_rook_attack[key].append(background.board_rect[rook.black_rook_position[key][0]][str(index1)])
        rook.black_rook_position[key][1] = aux3

def white_king_mvts(background, pawn, knight, queen, bishop, rook, king):
    king.white_king_move[0] = background.board_rect[king.white_king_position[0]][str(king.white_king_position[1])]

    ch = king.white_king_position[0]
    k = king.white_king_position[1]
    if (king.white_king_position[0] > 'a'):
        if (not background.board_move[chr(ord(ch) - 1)][str(k)]):
            king.white_king_move.append(background.board_rect[chr(ord(ch) - 1)][str(k)])

        elif verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position,
                                                rook.black_rook_position, bishop.black_bishop_position,
                                                queen.black_queen_position,
                                                pawn.black_pawn_death, knight.black_knight_death, rook.black_rook_death,
                                                bishop.black_bishop_death, queen.black_queen_death,
                                                king.white_king_position, 0, -1):

            king.white_king_attack.append(background.board_rect[chr(ord(ch) - 1)][str(k)])

        if (king.white_king_position[1] > 1):
            if (not background.board_move[chr(ord(ch) - 1)][str(k - 1)]):
                king.white_king_move.append(background.board_rect[chr(ord(ch) - 1)][str(k - 1)])

            elif verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position,
                                         rook.black_rook_position, bishop.black_bishop_position,
                                         queen.black_queen_position,
                                         pawn.black_pawn_death, knight.black_knight_death, rook.black_rook_death,
                                         bishop.black_bishop_death, queen.black_queen_death,
                                         king.white_king_position, -1, -1):

                king.white_king_attack.append(background.board_rect[chr(ord(ch) - 1)][str(k - 1)])

        if (king.white_king_position[1] < 8):
            if (not background.board_move[chr(ord(ch) - 1)][str(k + 1)]):
                king.white_king_move.append(background.board_rect[chr(ord(ch) - 1)][str(k + 1)])

            elif verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position,
                                         rook.black_rook_position, bishop.black_bishop_position,
                                         queen.black_queen_position,
                                         pawn.black_pawn_death, knight.black_knight_death, rook.black_rook_death,
                                         bishop.black_bishop_death, queen.black_queen_death,
                                         king.white_king_position, 1, -1):

                king.white_king_attack.append(background.board_rect[chr(ord(ch) - 1)][str(k + 1)])

    if (king.white_king_position[0] < 'h'):
        if (not background.board_move[chr(ord(ch) + 1)][str(k)]):
            king.white_king_move.append(background.board_rect[chr(ord(ch) + 1)][str(k)])

        elif verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position,
                                     rook.black_rook_position, bishop.black_bishop_position,
                                     queen.black_queen_position,
                                     pawn.black_pawn_death, knight.black_knight_death, rook.black_rook_death,
                                     bishop.black_bishop_death, queen.black_queen_death,
                                     king.white_king_position, 0, 1):

            king.white_king_attack.append(background.board_rect[chr(ord(ch) + 1)][str(k)])

        if (king.white_king_position[1] > 1):
            if (not background.board_move[chr(ord(ch) + 1)][str(k - 1)]):
                king.white_king_move.append(background.board_rect[chr(ord(ch) + 1)][str(k - 1)])

            elif verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position,
                                         rook.black_rook_position, bishop.black_bishop_position,
                                         queen.black_queen_position,
                                         pawn.black_pawn_death, knight.black_knight_death, rook.black_rook_death,
                                         bishop.black_bishop_death, queen.black_queen_death,
                                         king.white_king_position, -1, 1):

                king.white_king_attack.append(background.board_rect[chr(ord(ch) + 1)][str(k - 1)])

        if (king.white_king_position[1] < 8):
            if (not background.board_move[chr(ord(ch) + 1)][str(k + 1)]):
                king.white_king_move.append(background.board_rect[chr(ord(ch) + 1)][str(k + 1)])

            elif verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position,
                                         rook.black_rook_position, bishop.black_bishop_position,
                                         queen.black_queen_position,
                                         pawn.black_pawn_death, knight.black_knight_death, rook.black_rook_death,
                                         bishop.black_bishop_death, queen.black_queen_death,
                                         king.white_king_position, 1, 1):

                king.white_king_attack.append(background.board_rect[chr(ord(ch) + 1)][str(k + 1)])

    if (king.white_king_position[1] < 8):
        if (not background.board_move[ch][str(k + 1)]):
            king.white_king_move.append(background.board_rect[ch][str(k + 1)])

        elif verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position,
                                     rook.black_rook_position, bishop.black_bishop_position,
                                     queen.black_queen_position,
                                     pawn.black_pawn_death, knight.black_knight_death, rook.black_rook_death,
                                     bishop.black_bishop_death, queen.black_queen_death,
                                     king.white_king_position, 1, 0):

            king.white_king_attack.append(background.board_rect[ch][str(k + 1)])

    if (king.white_king_position[1] > 1):
        if (not background.board_move[ch][str(k - 1)]):
            king.white_king_move.append(background.board_rect[ch][str(k - 1)])

        elif verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position,
                                     rook.black_rook_position, bishop.black_bishop_position,
                                     queen.black_queen_position,
                                     pawn.black_pawn_death, knight.black_knight_death, rook.black_rook_death,
                                     bishop.black_bishop_death, queen.black_queen_death,
                                     king.white_king_position, -1, 0):

            king.white_king_attack.append(background.board_rect[ch][str(k - 1)])

    if king.white_king_no_move and rook.white_rook_no_move['R1']:
        if (not background.board_move[chr(ord(ch) - 1)][str(k)]) and (not background.board_move[chr(ord(ch) - 2)][str(k)]) and (
            (not background.board_move[chr(ord(ch) - 3)][str(k)])):
            king.white_king_move.append(background.board_rect[chr(ord(ch) - 2)][str(k)])
            king.white_king_move.append(background.board_rect[chr(ord(ch) - 1)][str(k)])

    if king.white_king_no_move and rook.white_rook_no_move['R2']:
        if (not background.board_move[chr(ord(ch) + 1)][str(k)]) and (not background.board_move[chr(ord(ch) + 2)][str(k)]):
            king.white_king_move.append(background.board_rect[chr(ord(ch) + 2)][str(k)])
            king.white_king_move.append(background.board_rect[chr(ord(ch) + 1)][str(k)])

def black_king_mvts(background, pawn, knight, rook, bishop, queen, king):
    king.black_king_move[0] = background.board_rect[king.black_king_position[0]][str(king.black_king_position[1])]

    ch = king.black_king_position[0]
    k = king.black_king_position[1]
    if (king.black_king_position[0] > 'a'):
        if (not background.board_move[chr(ord(ch) - 1)][str(k)]):
            king.black_king_move.append(background.board_rect[chr(ord(ch) - 1)][str(k)])

        elif verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position, rook.white_rook_position,
                                           bishop.white_bishop_position, queen.white_queen_position, pawn.white_pawn_death,
                                           knight.white_knight_death, rook.white_rook_death, bishop.white_bishop_death,
                                           queen.white_queen_death, king.black_king_position, 0, -1):

            king.black_king_attack.append(background.board_rect[chr(ord(ch) - 1)][str(k)])

        if (king.black_king_position[1] > 1):
            if (not background.board_move[chr(ord(ch) - 1)][str(k - 1)]):
                king.black_king_move.append(background.board_rect[chr(ord(ch) - 1)][str(k - 1)])

            elif verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position, rook.white_rook_position,
                                           bishop.white_bishop_position, queen.white_queen_position, pawn.white_pawn_death,
                                           knight.white_knight_death, rook.white_rook_death, bishop.white_bishop_death,
                                           queen.white_queen_death, king.black_king_position, -1, -1):

                king.black_king_attack.append(background.board_rect[chr(ord(ch) - 1)][str(k - 1)])

        if (king.black_king_position[1] < 8):
            if (not background.board_move[chr(ord(ch) - 1)][str(k + 1)]):
                king.black_king_move.append(background.board_rect[chr(ord(ch) - 1)][str(k + 1)])

            elif verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position, rook.white_rook_position,
                                           bishop.white_bishop_position, queen.white_queen_position, pawn.white_pawn_death,
                                           knight.white_knight_death, rook.white_rook_death, bishop.white_bishop_death,
                                           queen.white_queen_death, king.black_king_position, 1, -1):

                king.black_king_attack.append(background.board_rect[chr(ord(ch) - 1)][str(k + 1)])

    if (king.black_king_position[0] < 'h'):
        if (not background.board_move[chr(ord(ch) + 1)][str(k)]):
            king.black_king_move.append(background.board_rect[chr(ord(ch) + 1)][str(k)])

        elif verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position, rook.white_rook_position,
                                           bishop.white_bishop_position, queen.white_queen_position, pawn.white_pawn_death,
                                           knight.white_knight_death, rook.white_rook_death, bishop.white_bishop_death,
                                           queen.white_queen_death, king.black_king_position, 0, 1):

            king.black_king_attack.append(background.board_rect[chr(ord(ch) + 1)][str(k)])

        if (king.black_king_position[1] > 1):
            if (not background.board_move[chr(ord(ch) + 1)][str(k - 1)]):
                king.black_king_move.append(background.board_rect[chr(ord(ch) + 1)][str(k - 1)])

            elif verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position, rook.white_rook_position,
                                           bishop.white_bishop_position, queen.white_queen_position, pawn.white_pawn_death,
                                           knight.white_knight_death, rook.white_rook_death, bishop.white_bishop_death,
                                           queen.white_queen_death, king.black_king_position, -1, 1):

                king.black_king_attack.append(background.board_rect[chr(ord(ch) + 1)][str(k - 1)])

        if (king.black_king_position[1] < 8):
            if (not background.board_move[chr(ord(ch) + 1)][str(k + 1)]):
                king.black_king_move.append(background.board_rect[chr(ord(ch) + 1)][str(k + 1)])

            elif verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position, rook.white_rook_position,
                                           bishop.white_bishop_position, queen.white_queen_position, pawn.white_pawn_death,
                                           knight.white_knight_death, rook.white_rook_death, bishop.white_bishop_death,
                                           queen.white_queen_death, king.black_king_position, 1, 1):

                king.black_king_attack.append(background.board_rect[chr(ord(ch) + 1)][str(k + 1)])

    if (king.black_king_position[1] < 8):
        if (not background.board_move[ch][str(k + 1)]):
            king.black_king_move.append(background.board_rect[ch][str(k + 1)])

        elif verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position, rook.white_rook_position,
                                           bishop.white_bishop_position, queen.white_queen_position, pawn.white_pawn_death,
                                           knight.white_knight_death, rook.white_rook_death, bishop.white_bishop_death,
                                           queen.white_queen_death, king.black_king_position, 1, 0):

            king.black_king_attack.append(background.board_rect[ch][str(k + 1)])

    if (king.black_king_position[1] > 1):
        if (not background.board_move[ch][str(k - 1)]):
            king.black_king_move.append(background.board_rect[ch][str(k - 1)])

        elif verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position, rook.white_rook_position,
                                           bishop.white_bishop_position, queen.white_queen_position, pawn.white_pawn_death,
                                           knight.white_knight_death, rook.white_rook_death, bishop.white_bishop_death,
                                           queen.white_queen_death, king.black_king_position, -1, 0):

            king.black_king_attack.append(background.board_rect[ch][str(k - 1)])

    if king.black_king_no_move and rook.black_rook_no_move['R1']:
        if (not background.board_move[chr(ord(ch) - 1)][str(k)]) and (not background.board_move[chr(ord(ch) - 2)][str(k)]) and (
                (not background.board_move[chr(ord(ch) - 3)][str(k)])):
            king.black_king_move.append(background.board_rect[chr(ord(ch) - 2)][str(k)])
            king.black_king_move.append(background.board_rect[chr(ord(ch) - 1)][str(k)])

    if king.black_king_no_move and rook.black_rook_no_move['R2']:
        if (not background.board_move[chr(ord(ch) + 1)][str(k)]) and (not background.board_move[chr(ord(ch) + 2)][str(k)]):
            king.black_king_move.append(background.board_rect[chr(ord(ch) + 2)][str(k)])
            king.black_king_move.append(background.board_rect[chr(ord(ch) + 1)][str(k)])

def white_queen_mvts(background, pawn, knight, queen, bishop, rook, king):

    queen.white_queen_move[0] = background.board_rect[queen.white_queen_position[0]][str(queen.white_queen_position[1])]

    ch0 = chr(ord(queen.white_queen_position[0]) + 1)
    ch1 = chr(ord(queen.white_queen_position[0]) - 1)
    index0 = queen.white_queen_position[1] + 1
    index1 = queen.white_queen_position[1] - 1

    if queen.white_queen_position[0] < 'h':
        while (ch0 <= 'h') and (not background.board_move[ch0][str(queen.white_queen_position[1])]):
            queen.white_queen_move.append(background.board_rect[ch0][str(queen.white_queen_position[1])])
            ch0 = chr(ord(ch0) + 1)

        aux0 = queen.white_queen_position[0]
        queen.white_queen_position[0] = ch0
        if verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position, rook.black_rook_position,
                            bishop.black_bishop_position, queen.black_queen_position, pawn.black_pawn_death,
                            knight.black_knight_death, rook.black_rook_death, bishop.black_bishop_death,
                            queen.black_queen_death, queen.white_queen_position, 0, 0):

            queen.white_queen_attack.append(background.board_rect[ch0][str(queen.white_queen_position[1])])
        queen.white_queen_position[0] = aux0

    if queen.white_queen_position[0] > 'a':
        while (ch1 >= 'a') and (not background.board_move[ch1][str(queen.white_queen_position[1])]):
            queen.white_queen_move.append(background.board_rect[ch1][str(queen.white_queen_position[1])])
            ch1 = chr(ord(ch1) - 1)

        aux1 = queen.white_queen_position[0]
        queen.white_queen_position[0] = ch1
        if verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position, rook.black_rook_position,
                            bishop.black_bishop_position, queen.black_queen_position, pawn.black_pawn_death,
                            knight.black_knight_death, rook.black_rook_death, bishop.black_bishop_death,
                            queen.black_queen_death, queen.white_queen_position, 0, 0):

            queen.white_queen_attack.append(background.board_rect[ch1][str(queen.white_queen_position[1])])
        queen.white_queen_position[0] = aux1

    if queen.white_queen_position[1] < 8:
        while (index0 <= 8) and (not background.board_move[queen.white_queen_position[0]][str(index0)]):
            queen.white_queen_move.append(background.board_rect[queen.white_queen_position[0]][str(index0)])
            index0 += 1

        aux2 = queen.white_queen_position[1]
        queen.white_queen_position[1] = index0
        if verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position, rook.black_rook_position,
                            bishop.black_bishop_position, queen.black_queen_position, pawn.black_pawn_death,
                            knight.black_knight_death, rook.black_rook_death, bishop.black_bishop_death,
                            queen.black_queen_death, queen.white_queen_position, 0, 0):

            queen.white_queen_attack.append(background.board_rect[queen.white_queen_position[0]][str(index0)])
        queen.white_queen_position[1] = aux2

    if queen.white_queen_position[1] > 1:
        while (index1 >= 1) and (not background.board_move[queen.white_queen_position[0]][str(index1)]):
            queen.white_queen_move.append(background.board_rect[queen.white_queen_position[0]][str(index1)])
            index1 -= 1

        aux3 = queen.white_queen_position[1]
        queen.white_queen_position[1] = index1
        if verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position, rook.black_rook_position,
                            bishop.black_bishop_position, queen.black_queen_position, pawn.black_pawn_death,
                            knight.black_knight_death, rook.black_rook_death, bishop.black_bishop_death,
                            queen.black_queen_death, queen.white_queen_position, 0, 0):

            queen.white_queen_attack.append(background.board_rect[queen.white_queen_position[0]][str(index1)])
        queen.white_queen_position[1] = aux3

    key2 = queen.white_queen_position[1] + 1
    ch2 = chr(ord(queen.white_queen_position[0]) + 1)
    key3 = queen.white_queen_position[1] - 1
    ch3 = chr(ord(queen.white_queen_position[0]) - 1)

    if (queen.white_queen_position[0]) < 'h' and (queen.white_queen_position[1] < 8):
        while (ch2 <= "h") and (key2 <= 8) and (not background.board_move[ch2][str(key2)]):
            queen.white_queen_move.append(background.board_rect[ch2][str(key2)])
            ch2 = chr(ord(ch2) + 1)
            key2 += 1

        aux4 = queen.white_queen_position[0]
        aux5 = queen.white_queen_position[1]
        queen.white_queen_position[0] = ch2
        queen.white_queen_position[1] = key2
        if verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position, rook.black_rook_position,
                            bishop.black_bishop_position, queen.black_queen_position, pawn.black_pawn_death,
                            knight.black_knight_death, rook.black_rook_death, bishop.black_bishop_death,
                            queen.black_queen_death, queen.white_queen_position, 0, 0):

            queen.white_queen_attack.append(background.board_rect[ch2][str(key2)])
        queen.white_queen_position[0] = aux4
        queen.white_queen_position[1] = aux5

    if (queen.white_queen_position[0] > 'a') and (queen.white_queen_position[1] > 1):
        while (ch3 >= "a") and (key3 >= 1) and (not background.board_move[ch3][str(key3)]):
            queen.white_queen_move.append(background.board_rect[ch3][str(key3)])
            ch3 = chr(ord(ch3) - 1)
            key3 -= 1

        aux6 = queen.white_queen_position[0]
        aux7 = queen.white_queen_position[1]
        queen.white_queen_position[0] = ch3
        queen.white_queen_position[1] = key3
        if verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position, rook.black_rook_position,
                            bishop.black_bishop_position, queen.black_queen_position, pawn.black_pawn_death,
                            knight.black_knight_death, rook.black_rook_death, bishop.black_bishop_death,
                            queen.black_queen_death, queen.white_queen_position, 0, 0):

            queen.white_queen_attack.append(background.board_rect[ch3][str(key3)])
        queen.white_queen_position[0] = aux6
        queen.white_queen_position[1] = aux7

    ch4 = chr(ord(queen.white_queen_position[0]) - 1)
    key4 = queen.white_queen_position[1] + 1
    if (queen.white_queen_position[0] > 'a') and (queen.white_queen_position[1] < 8):
        while (ch4 >= "a") and (key4 <= 8) and (not background.board_move[ch4][str(key4)]):
            queen.white_queen_move.append(background.board_rect[ch4][str(key4)])
            ch4 = chr(ord(ch4) - 1)
            key4 += 1

        aux8 = queen.white_queen_position[0]
        aux9 = queen.white_queen_position[1]
        queen.white_queen_position[0] = ch4
        queen.white_queen_position[1] = key4
        if verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position, rook.black_rook_position,
                            bishop.black_bishop_position, queen.black_queen_position, pawn.black_pawn_death,
                            knight.black_knight_death, rook.black_rook_death, bishop.black_bishop_death,
                            queen.black_queen_death, queen.white_queen_position, 0, 0):

            queen.white_queen_attack.append(background.board_rect[ch4][str(key4)])
        queen.white_queen_position[0] = aux8
        queen.white_queen_position[1] = aux9

    ch5 = chr(ord(queen.white_queen_position[0]) + 1)
    key5 = queen.white_queen_position[1] - 1
    if (queen.white_queen_position[0] < 'h') and (queen.white_queen_position[1] > 1):
        while (ch5 <= "h") and (key5 >= 1) and (not background.board_move[ch5][str(key5)]):
            queen.white_queen_move.append(background.board_rect[ch5][str(key5)])
            ch5 = chr(ord(ch5) + 1)
            key5 -= 1

        aux10 = queen.white_queen_position[0]
        aux11 = queen.white_queen_position[1]
        queen.white_queen_position[0] = ch5
        queen.white_queen_position[1] = key5
        if verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position, rook.black_rook_position,
                            bishop.black_bishop_position, queen.black_queen_position, pawn.black_pawn_death,
                            knight.black_knight_death, rook.black_rook_death, bishop.black_bishop_death,
                            queen.black_queen_death, queen.white_queen_position, 0, 0):
            queen.white_queen_attack.append(background.board_rect[ch5][str(key5)])
        queen.white_queen_position[0] = aux10
        queen.white_queen_position[1] = aux11

def black_queen_mvts(background, pawn, knight, rook, bishop, queen, king):

    queen.black_queen_move[0] = background.board_rect[queen.black_queen_position[0]][str(queen.black_queen_position[1])]

    ch0 = chr(ord(queen.black_queen_position[0]) + 1)
    ch1 = chr(ord(queen.black_queen_position[0]) - 1)
    index0 = queen.black_queen_position[1] + 1
    index1 = queen.black_queen_position[1] - 1
    if queen.black_queen_position[0] < 'h':
        while (ch0 <= 'h') and (not background.board_move[ch0][str(queen.black_queen_position[1])]):
            queen.black_queen_move.append(background.board_rect[ch0][str(queen.black_queen_position[1])])
            ch0 = chr(ord(ch0) + 1)

        aux0 = queen.black_queen_position[0]
        queen.black_queen_position[0] = ch0
        if verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position, rook.white_rook_position,
                                           bishop.white_bishop_position, queen.white_queen_position, pawn.white_pawn_death,
                                           knight.white_knight_death, rook.white_rook_death, bishop.white_bishop_death,
                                           queen.white_queen_death, queen.black_queen_position, 0, 0):

            queen.black_queen_attack.append(background.board_rect[ch0][str(queen.black_queen_position[1])])
        queen.black_queen_position[0] = aux0

    if queen.black_queen_position[0] > 'a':
        while (ch1 >= 'a') and (not background.board_move[ch1][str(queen.black_queen_position[1])]):
            queen.black_queen_move.append(background.board_rect[ch1][str(queen.black_queen_position[1])])
            ch1 = chr(ord(ch1) - 1)

        aux1 = queen.black_queen_position[0]
        queen.black_queen_position[0] = ch1
        if verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position, rook.white_rook_position,
                                           bishop.white_bishop_position, queen.white_queen_position, pawn.white_pawn_death,
                                           knight.white_knight_death, rook.white_rook_death, bishop.white_bishop_death,
                                           queen.white_queen_death, queen.black_queen_position, 0, 0):

            queen.black_queen_attack.append(background.board_rect[ch1][str(queen.black_queen_position[1])])
        queen.black_queen_position[0] = aux1

    if queen.black_queen_position[1] < 8:
        while (index0 <= 8) and (not background.board_move[queen.black_queen_position[0]][str(index0)]):
            queen.black_queen_move.append(background.board_rect[queen.black_queen_position[0]][str(index0)])
            index0 += 1

        aux2 = queen.black_queen_position[1]
        queen.black_queen_position[1] = index0
        if verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position, rook.white_rook_position,
                                           bishop.white_bishop_position, queen.white_queen_position, pawn.white_pawn_death,
                                           knight.white_knight_death, rook.white_rook_death, bishop.white_bishop_death,
                                           queen.white_queen_death, queen.black_queen_position, 0, 0):

            queen.black_queen_attack.append(background.board_rect[queen.black_queen_position[0]][str(index0)])
        queen.black_queen_position[1] = aux2

    if queen.black_queen_position[1] > 1:
        while (index1 >= 1) and (not background.board_move[queen.black_queen_position[0]][str(index1)]):
            queen.black_queen_move.append(background.board_rect[queen.black_queen_position[0]][str(index1)])
            index1 -= 1

        aux3 = queen.black_queen_position[1]
        queen.black_queen_position[1] = index1
        if verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position, rook.white_rook_position,
                                           bishop.white_bishop_position, queen.white_queen_position, pawn.white_pawn_death,
                                           knight.white_knight_death, rook.white_rook_death, bishop.white_bishop_death,
                                           queen.white_queen_death, queen.black_queen_position, 0, 0):

            queen.black_queen_attack.append(background.board_rect[queen.black_queen_position[0]][str(index1)])
        queen.black_queen_position[1] = aux3

    key2 = queen.black_queen_position[1] + 1
    ch2 = chr(ord(queen.black_queen_position[0]) + 1)
    key3 = queen.black_queen_position[1] - 1
    ch3 = chr(ord(queen.black_queen_position[0]) - 1)

    if (queen.black_queen_position[0]) < 'h' and (queen.black_queen_position[1] < 8):
        while (ch2 <= "h") and (key2 <= 8) and (not background.board_move[ch2][str(key2)]):
            queen.black_queen_move.append(background.board_rect[ch2][str(key2)])
            ch2 = chr(ord(ch2) + 1)
            key2 += 1

        aux4 = queen.black_queen_position[0]
        aux5 = queen.black_queen_position[1]
        queen.black_queen_position[0] = ch2
        queen.black_queen_position[1] = key2
        if verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position, rook.white_rook_position,
                                           bishop.white_bishop_position, queen.white_queen_position, pawn.white_pawn_death,
                                           knight.white_knight_death, rook.white_rook_death, bishop.white_bishop_death,
                                           queen.white_queen_death, queen.black_queen_position, 0, 0):

            queen.black_queen_attack.append(background.board_rect[ch2][str(key2)])
        queen.black_queen_position[0] = aux4
        queen.black_queen_position[1] = aux5

    if (queen.black_queen_position[0] > 'a') and (queen.black_queen_position[1] > 1):
        while (ch3 >= "a") and (key3 >= 1) and (not background.board_move[ch3][str(key3)]):
            queen.black_queen_move.append(background.board_rect[ch3][str(key3)])
            ch3 = chr(ord(ch3) - 1)
            key3 -= 1

        aux6 = queen.black_queen_position[0]
        aux7 = queen.black_queen_position[1]
        queen.black_queen_position[0] = ch3
        queen.black_queen_position[1] = key3
        if verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position, rook.white_rook_position,
                                           bishop.white_bishop_position, queen.white_queen_position, pawn.white_pawn_death,
                                           knight.white_knight_death, rook.white_rook_death, bishop.white_bishop_death,
                                           queen.white_queen_death, queen.black_queen_position, 0, 0):

            queen.black_queen_attack.append(background.board_rect[ch3][str(key3)])
        queen.black_queen_position[0] = aux6
        queen.black_queen_position[1] = aux7

    ch4 = chr(ord(queen.black_queen_position[0]) - 1)
    key4 = queen.black_queen_position[1] + 1
    if (queen.black_queen_position[0] > 'a') and (queen.black_queen_position[1] < 8):
        while (ch4 >= "a") and (key4 <= 8) and (not background.board_move[ch4][str(key4)]):
            queen.black_queen_move.append(background.board_rect[ch4][str(key4)])
            ch4 = chr(ord(ch4) - 1)
            key4 += 1

        aux8 = queen.black_queen_position[0]
        aux9 = queen.black_queen_position[1]
        queen.black_queen_position[0] = ch4
        queen.black_queen_position[1] = key4
        if verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position, rook.white_rook_position,
                                           bishop.white_bishop_position, queen.white_queen_position, pawn.white_pawn_death,
                                           knight.white_knight_death, rook.white_rook_death, bishop.white_bishop_death,
                                           queen.white_queen_death, queen.black_queen_position, 0, 0):

            queen.black_queen_attack.append(background.board_rect[ch4][str(key4)])
        queen.black_queen_position[0] = aux8
        queen.black_queen_position[1] = aux9

    ch5 = chr(ord(queen.black_queen_position[0]) + 1)
    key5 = queen.black_queen_position[1] - 1
    if (queen.black_queen_position[0] < 'h') and (queen.black_queen_position[1] > 1):
        while (ch5 <= "h") and (key5 >= 1) and (not background.board_move[ch5][str(key5)]):
            queen.black_queen_move.append(background.board_rect[ch5][str(key5)])
            ch5 = chr(ord(ch5) + 1)
            key5 -= 1

        aux10 = queen.black_queen_position[0]
        aux11 = queen.black_queen_position[1]
        queen.black_queen_position[0] = ch5
        queen.black_queen_position[1] = key5
        if verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position, rook.white_rook_position,
                                           bishop.white_bishop_position, queen.white_queen_position, pawn.white_pawn_death,
                                           knight.white_knight_death, rook.white_rook_death, bishop.white_bishop_death,
                                           queen.white_queen_death, queen.black_queen_position, 0, 0):

            queen.black_queen_attack.append(background.board_rect[ch5][str(key5)])
        queen.black_queen_position[0] = aux10
        queen.black_queen_position[1] = aux11

def white_bishop_mvts(background, pawn, knight, rook, bishop, queen, king, key):
    bishop.white_bishop_move[key][0] = background.board_rect[bishop.white_bishop_position[key][0]][
        str(bishop.white_bishop_position[key][1])]

    key0 = bishop.white_bishop_position[key][1] + 1
    ch0 = chr(ord(bishop.white_bishop_position[key][0]) + 1)
    key1 = bishop.white_bishop_position[key][1] - 1
    ch1 = chr(ord(bishop.white_bishop_position[key][0]) - 1)

    if (bishop.white_bishop_position[key][0]) < 'h' and (bishop.white_bishop_position[key][1] < 8):
        while (ch0 <= "h") and (key0 <= 8) and (not background.board_move[ch0][str(key0)]):
            bishop.white_bishop_move[key].append(background.board_rect[ch0][str(key0)])
            ch0 = chr(ord(ch0) + 1)
            key0 += 1

        aux0 = bishop.white_bishop_position[key][0]
        aux1 = bishop.white_bishop_position[key][1]
        bishop.white_bishop_position[key][0] = ch0
        bishop.white_bishop_position[key][1] = key0
        if verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position, rook.black_rook_position,
                            bishop.black_bishop_position, queen.black_queen_position, pawn.black_pawn_death,
                            knight.black_knight_death, rook.black_rook_death, bishop.black_bishop_death,
                            queen.black_queen_death, bishop.white_bishop_position[key], 0, 0):

            bishop.white_bishop_attack[key].append(background.board_rect[ch0][str(key0)])
        bishop.white_bishop_position[key][0] = aux0
        bishop.white_bishop_position[key][1] = aux1

    if (bishop.white_bishop_position[key][0] > 'a') and (bishop.white_bishop_position[key][1] > 1):
        while (ch1 >= "a") and (key1 >= 1) and (not background.board_move[ch1][str(key1)]):
            bishop.white_bishop_move[key].append(background.board_rect[ch1][str(key1)])
            ch1 = chr(ord(ch1) - 1)
            key1 -= 1

        aux2 = bishop.white_bishop_position[key][0]
        aux3 = bishop.white_bishop_position[key][1]
        bishop.white_bishop_position[key][0] = ch1
        bishop.white_bishop_position[key][1] = key1
        if verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position, rook.black_rook_position,
                            bishop.black_bishop_position, queen.black_queen_position, pawn.black_pawn_death,
                            knight.black_knight_death, rook.black_rook_death, bishop.black_bishop_death,
                            queen.black_queen_death, bishop.white_bishop_position[key], 0, 0):

            bishop.white_bishop_attack[key].append(background.board_rect[ch1][str(key1)])
        bishop.white_bishop_position[key][0] = aux2
        bishop.white_bishop_position[key][1] = aux3

    ch2 = chr(ord(bishop.white_bishop_position[key][0]) - 1)
    key2 = bishop.white_bishop_position[key][1] + 1
    if (bishop.white_bishop_position[key][0] > 'a') and (bishop.white_bishop_position[key][1] < 8):
        while (ch2 >= "a") and (key2 <= 8) and (not background.board_move[ch2][str(key2)]):
            bishop.white_bishop_move[key].append(background.board_rect[ch2][str(key2)])
            ch2 = chr(ord(ch2) - 1)
            key2 += 1

        aux4 = bishop.white_bishop_position[key][0]
        aux5 = bishop.white_bishop_position[key][1]
        bishop.white_bishop_position[key][0] = ch2
        bishop.white_bishop_position[key][1] = key2
        if verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position, rook.black_rook_position,
                            bishop.black_bishop_position, queen.black_queen_position, pawn.black_pawn_death,
                            knight.black_knight_death, rook.black_rook_death, bishop.black_bishop_death,
                            queen.black_queen_death, bishop.white_bishop_position[key], 0, 0):

            bishop.white_bishop_attack[key].append(background.board_rect[ch2][str(key2)])
        bishop.white_bishop_position[key][0] = aux4
        bishop.white_bishop_position[key][1] = aux5

    ch3 = chr(ord(bishop.white_bishop_position[key][0]) + 1)
    key3 = bishop.white_bishop_position[key][1] - 1
    if (bishop.white_bishop_position[key][0] < 'h') and (bishop.white_bishop_position[key][1] > 1):
        while (ch3 <= "h") and (key3 >= 1) and (not background.board_move[ch3][str(key3)]):
            bishop.white_bishop_move[key].append(background.board_rect[ch3][str(key3)])
            ch3 = chr(ord(ch3) + 1)
            key3 -= 1

        aux6 = bishop.white_bishop_position[key][0]
        aux7 = bishop.white_bishop_position[key][1]
        bishop.white_bishop_position[key][0] = ch3
        bishop.white_bishop_position[key][1] = key3
        if verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position, rook.black_rook_position,
                            bishop.black_bishop_position, queen.black_queen_position, pawn.black_pawn_death,
                            knight.black_knight_death, rook.black_rook_death, bishop.black_bishop_death,
                            queen.black_queen_death, bishop.white_bishop_position[key], 0, 0):

            bishop.white_bishop_attack[key].append(background.board_rect[ch3][str(key3)])
        bishop.white_bishop_position[key][0] = aux6
        bishop.white_bishop_position[key][1] = aux7

def black_bishop_mvts(background, pawn, knight, rook, bishop, queen, king, key):

    bishop.black_bishop_move[key][0] = background.board_rect[bishop.black_bishop_position[key][0]][str(bishop.black_bishop_position[key][1])]

    key0 = bishop.black_bishop_position[key][1] + 1
    ch0 = chr(ord(bishop.black_bishop_position[key][0]) + 1)
    key1 = bishop.black_bishop_position[key][1] - 1
    ch1 = chr(ord(bishop.black_bishop_position[key][0]) - 1)

    if (bishop.black_bishop_position[key][0]) < 'h' and (bishop.black_bishop_position[key][1] < 8):
        while (ch0 <= "h") and (key0 <= 8) and (not background.board_move[ch0][str(key0)]):
            bishop.black_bishop_move[key].append(background.board_rect[ch0][str(key0)])
            ch0 = chr(ord(ch0) + 1)
            key0 += 1

        aux0 = bishop.black_bishop_position[key][0]
        aux1 = bishop.black_bishop_position[key][1]
        bishop.black_bishop_position[key][0] = ch0
        bishop.black_bishop_position[key][1] = key0
        if verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position, rook.white_rook_position,
                                           bishop.white_bishop_position, queen.white_queen_position, pawn.white_pawn_death,
                                           knight.white_knight_death, rook.white_rook_death, bishop.white_bishop_death,
                                           queen.white_queen_death, bishop.black_bishop_position[key], 0, 0):

            bishop.black_bishop_attack[key].append(background.board_rect[ch0][str(key0)])
        bishop.black_bishop_position[key][0] = aux0
        bishop.black_bishop_position[key][1] = aux1

    if (bishop.black_bishop_position[key][0] > 'a') and (bishop.black_bishop_position[key][1] > 1):
        while (ch1 >= "a") and (key1 >= 1) and (not background.board_move[ch1][str(key1)]):
            bishop.black_bishop_move[key].append(background.board_rect[ch1][str(key1)])
            ch1 = chr(ord(ch1) - 1)
            key1 -= 1

        aux2 = bishop.black_bishop_position[key][0]
        aux3 = bishop.black_bishop_position[key][1]
        bishop.black_bishop_position[key][0] = ch1
        bishop.black_bishop_position[key][1] = key1
        if verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position, rook.white_rook_position,
                                           bishop.white_bishop_position, queen.white_queen_position, pawn.white_pawn_death,
                                           knight.white_knight_death, rook.white_rook_death, bishop.white_bishop_death,
                                           queen.white_queen_death, bishop.black_bishop_position[key], 0, 0):

            bishop.black_bishop_attack[key].append(background.board_rect[ch1][str(key1)])
        bishop.black_bishop_position[key][0] = aux2
        bishop.black_bishop_position[key][1] = aux3

    ch2 = chr(ord(bishop.black_bishop_position[key][0]) - 1)
    key2 = bishop.black_bishop_position[key][1] + 1
    if (bishop.black_bishop_position[key][0] > 'a') and (bishop.black_bishop_position[key][1] < 8):
        while (ch2 >= "a") and (key2 <= 8) and (not background.board_move[ch2][str(key2)]):
            bishop.black_bishop_move[key].append(background.board_rect[ch2][str(key2)])
            ch2 = chr(ord(ch2) - 1)
            key2 += 1

        aux4 = bishop.black_bishop_position[key][0]
        aux5 = bishop.black_bishop_position[key][1]
        bishop.black_bishop_position[key][0] = ch2
        bishop.black_bishop_position[key][1] = key2
        if verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position, rook.white_rook_position,
                                           bishop.white_bishop_position, queen.white_queen_position, pawn.white_pawn_death,
                                           knight.white_knight_death, rook.white_rook_death, bishop.white_bishop_death,
                                           queen.white_queen_death, bishop.black_bishop_position[key], 0, 0):

            bishop.black_bishop_attack[key].append(background.board_rect[ch2][str(key2)])
        bishop.black_bishop_position[key][0] = aux4
        bishop.black_bishop_position[key][1] = aux5

    ch3 = chr(ord(bishop.black_bishop_position[key][0]) + 1)
    key3 = bishop.black_bishop_position[key][1] - 1
    if (bishop.black_bishop_position[key][0] < 'h') and (bishop.black_bishop_position[key][1] > 1):
        while (ch3 <= "h") and (key3 >= 1) and (not background.board_move[ch3][str(key3)]):
            bishop.black_bishop_move[key].append(background.board_rect[ch3][str(key3)])
            ch3 = chr(ord(ch3) + 1)
            key3 -= 1

        aux6 = bishop.black_bishop_position[key][0]
        aux7 = bishop.black_bishop_position[key][1]
        bishop.black_bishop_position[key][0] = ch3
        bishop.black_bishop_position[key][1] = key3
        if verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position, rook.white_rook_position,
                                           bishop.white_bishop_position, queen.white_queen_position, pawn.white_pawn_death,
                                           knight.white_knight_death, rook.white_rook_death, bishop.white_bishop_death,
                                           queen.white_queen_death, bishop.black_bishop_position[key], 0, 0):

            bishop.black_bishop_attack[key].append(background.board_rect[ch3][str(key3)])
        bishop.black_bishop_position[key][0] = aux6
        bishop.black_bishop_position[key][1] = aux7

def white_knight_mvts(background, pawn, knight, rook, bishop, queen, king, key):

    knight.white_knight_move[key][0] = background.board_rect[knight.white_knight_position[key][0]][
        str(knight.white_knight_position[key][1])]

    ch = knight.white_knight_position[key][0]
    k = knight.white_knight_position[key][1]
    if (knight.white_knight_position[key][0] < "g") and (
            knight.white_knight_position[key][1] > 1):

        if (not background.board_move[chr(ord(ch) + 2)][str(k - 1)]):
            knight.white_knight_move[key].append(background.board_rect[chr(ord(ch) + 2)][str(k - 1)])

        elif verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position, rook.black_rook_position,
                            bishop.black_bishop_position, queen.black_queen_position, pawn.black_pawn_death,
                            knight.black_knight_death, rook.black_rook_death, bishop.black_bishop_death,
                            queen.black_queen_death, knight.white_knight_position[key], -1, 2):

            knight.white_knight_attack[key].append(background.board_rect[chr(ord(ch) + 2)][str(k - 1)])

    if (knight.white_knight_position[key][0] < "g") and (
            knight.white_knight_position[key][1] < 8):

        if (not background.board_move[chr(ord(ch) + 2)][str(k + 1)]):
            knight.white_knight_move[key].append(background.board_rect[chr(ord(ch) + 2)][str(k + 1)])

        elif verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position, rook.black_rook_position,
                                     bishop.black_bishop_position, queen.black_queen_position, pawn.black_pawn_death,
                                     knight.black_knight_death, rook.black_rook_death, bishop.black_bishop_death,
                                     queen.black_queen_death, knight.white_knight_position[key], 1, 2):

            knight.white_knight_attack[key].append(background.board_rect[chr(ord(ch) + 2)][str(k + 1)])

    if (knight.white_knight_position[key][0] > "b") and (
            knight.white_knight_position[key][1] > 1):

        if (not background.board_move[chr(ord(ch) - 2)][str(k - 1)]):
            knight.white_knight_move[key].append(background.board_rect[chr(ord(ch) - 2)][str(k - 1)])

        elif verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position,
                                     rook.black_rook_position,
                                     bishop.black_bishop_position, queen.black_queen_position,
                                     pawn.black_pawn_death,
                                     knight.black_knight_death, rook.black_rook_death, bishop.black_bishop_death,
                                     queen.black_queen_death, knight.white_knight_position[key], -1, -2):

            knight.white_knight_attack[key].append(background.board_rect[chr(ord(ch) - 2)][str(k - 1)])

    if (knight.white_knight_position[key][0] > "b") and (
            knight.white_knight_position[key][1] < 8):

        if (not background.board_move[chr(ord(ch) - 2)][str(k + 1)]):
            knight.white_knight_move[key].append(background.board_rect[chr(ord(ch) - 2)][str(k + 1)])

        elif verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position,
                                     rook.black_rook_position,
                                     bishop.black_bishop_position, queen.black_queen_position,
                                     pawn.black_pawn_death,
                                     knight.black_knight_death, rook.black_rook_death, bishop.black_bishop_death,
                                     queen.black_queen_death, knight.white_knight_position[key], 1, -2):

            knight.white_knight_attack[key].append(background.board_rect[chr(ord(ch) - 2)][str(k + 1)])

    if (knight.white_knight_position[key][0] > "a") and (
            knight.white_knight_position[key][1] > 2):

        if (not background.board_move[chr(ord(ch) - 1)][str(k - 2)]):
            knight.white_knight_move[key].append(background.board_rect[chr(ord(ch) - 1)][str(k - 2)])

        elif verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position, rook.black_rook_position,
                                     bishop.black_bishop_position, queen.black_queen_position, pawn.black_pawn_death,
                                     knight.black_knight_death, rook.black_rook_death, bishop.black_bishop_death,
                                     queen.black_queen_death, knight.white_knight_position[key], -2, -1):

            knight.white_knight_attack[key].append(background.board_rect[chr(ord(ch) - 1)][str(k - 2)])

    if (knight.white_knight_position[key][0] > "a") and (
            knight.white_knight_position[key][1] < 7):

        if (not background.board_move[chr(ord(ch) - 1)][str(k + 2)]):
            knight.white_knight_move[key].append(background.board_rect[chr(ord(ch) - 1)][str(k + 2)])
        elif verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position,
                                     rook.black_rook_position,
                                     bishop.black_bishop_position, queen.black_queen_position,
                                     pawn.black_pawn_death,
                                     knight.black_knight_death, rook.black_rook_death, bishop.black_bishop_death,
                                     queen.black_queen_death, knight.white_knight_position[key], 2, -1):

            knight.white_knight_attack[key].append(background.board_rect[chr(ord(ch) - 1)][str(k + 2)])

    if (knight.white_knight_position[key][0] < "h") and (
            knight.white_knight_position[key][1] > 2):

        if (not background.board_move[chr(ord(ch) + 1)][str(k - 2)]):
            knight.white_knight_move[key].append(background.board_rect[chr(ord(ch) + 1)][str(k - 2)])

        elif verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position, rook.black_rook_position,
                                     bishop.black_bishop_position, queen.black_queen_position, pawn.black_pawn_death,
                                     knight.black_knight_death, rook.black_rook_death, bishop.black_bishop_death,
                                     queen.black_queen_death, knight.white_knight_position[key], -2, 1):

            knight.white_knight_attack[key].append(background.board_rect[chr(ord(ch) + 1)][str(k - 2)])

    if (knight.white_knight_position[key][0] < "h") and (
            knight.white_knight_position[key][1] < 7):

        if (not background.board_move[chr(ord(ch) + 1)][str(k + 2)]):
            knight.white_knight_move[key].append(background.board_rect[chr(ord(ch) + 1)][str(k + 2)])

        elif verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position, rook.black_rook_position,
                            bishop.black_bishop_position, queen.black_queen_position, pawn.black_pawn_death,
                            knight.black_knight_death, rook.black_rook_death, bishop.black_bishop_death,
                            queen.black_queen_death, knight.white_knight_position[key], 2, 1):

            knight.white_knight_attack[key].append(background.board_rect[chr(ord(ch) + 1)][str(k + 2)])

def black_knight_mvts(background, pawn, knight, rook, bishop, queen, king, key):

    knight.black_knight_move[key][0] = background.board_rect[knight.black_knight_position[key][0]][
        str(knight.black_knight_position[key][1])]

    ch = knight.black_knight_position[key][0]
    k = knight.black_knight_position[key][1]
    if (knight.black_knight_position[key][0] < "g") and (
            knight.black_knight_position[key][1] > 1):

        if (not background.board_move[chr(ord(ch) + 2)][str(k - 1)]):
            knight.black_knight_move[key].append(background.board_rect[chr(ord(ch) + 2)][str(k - 1)])

        elif verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position, rook.white_rook_position,
                                   bishop.white_bishop_position, queen.white_queen_position, pawn.white_pawn_death,
                                   knight.white_knight_death, rook.white_rook_death, bishop.white_bishop_death,
                                   queen.white_queen_death, knight.black_knight_position[key], -1, 2):

            knight.black_knight_attack[key].append(background.board_rect[chr(ord(ch) + 2)][str(k - 1)])

    if (knight.black_knight_position[key][0] < "g") and (
            knight.black_knight_position[key][1] < 8):

        if (not background.board_move[chr(ord(ch) + 2)][str(k + 1)]):
            knight.black_knight_move[key].append(background.board_rect[chr(ord(ch) + 2)][str(k + 1)])

        elif verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position, rook.white_rook_position,
                                     bishop.white_bishop_position, queen.white_queen_position, pawn.white_pawn_death,
                                     knight.white_knight_death, rook.white_rook_death, bishop.white_bishop_death,
                                     queen.white_queen_death, knight.black_knight_position[key], 1, 2):

            knight.black_knight_attack[key].append(background.board_rect[chr(ord(ch) + 2)][str(k + 1)])

    if (knight.black_knight_position[key][0] > "b") and (
            knight.black_knight_position[key][1] > 1):

        if (not background.board_move[chr(ord(ch) - 2)][str(k - 1)]):
            knight.black_knight_move[key].append(background.board_rect[chr(ord(ch) - 2)][str(k - 1)])

        elif verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position, rook.white_rook_position,
                                     bishop.white_bishop_position, queen.white_queen_position, pawn.white_pawn_death,
                                     knight.white_knight_death, rook.white_rook_death, bishop.white_bishop_death,
                                     queen.white_queen_death, knight.black_knight_position[key], -1, -2):

            knight.black_knight_attack[key].append(background.board_rect[chr(ord(ch) - 2)][str(k - 1)])

    if (knight.black_knight_position[key][0] > "b") and (
            knight.black_knight_position[key][1] < 8):

        if (not background.board_move[chr(ord(ch) - 2)][str(k + 1)]):
            knight.black_knight_move[key].append(background.board_rect[chr(ord(ch) - 2)][str(k + 1)])

        elif verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position, rook.white_rook_position,
                                     bishop.white_bishop_position, queen.white_queen_position, pawn.white_pawn_death,
                                     knight.white_knight_death, rook.white_rook_death, bishop.white_bishop_death,
                                     queen.white_queen_death, knight.black_knight_position[key], 1, -2):

            knight.black_knight_attack[key].append(background.board_rect[chr(ord(ch) - 2)][str(k + 1)])

    if (knight.black_knight_position[key][0] > "a") and (
            knight.black_knight_position[key][1] > 2):

        if (not background.board_move[chr(ord(ch) - 1)][str(k - 2)]):
            knight.black_knight_move[key].append(background.board_rect[chr(ord(ch) - 1)][str(k - 2)])

        elif verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position, rook.white_rook_position,
                                     bishop.white_bishop_position, queen.white_queen_position, pawn.white_pawn_death,
                                     knight.white_knight_death, rook.white_rook_death, bishop.white_bishop_death,
                                     queen.white_queen_death, knight.black_knight_position[key], -2, -1):

            knight.black_knight_attack[key].append(background.board_rect[chr(ord(ch) - 1)][str(k - 2)])

    if (knight.black_knight_position[key][0] > "a") and (
            knight.black_knight_position[key][1] < 7):

        if (not background.board_move[chr(ord(ch) - 1)][str(k + 2)]):
            knight.black_knight_move[key].append(background.board_rect[chr(ord(ch) - 1)][str(k + 2)])

        elif verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position, rook.white_rook_position,
                                     bishop.white_bishop_position, queen.white_queen_position, pawn.white_pawn_death,
                                     knight.white_knight_death, rook.white_rook_death, bishop.white_bishop_death,
                                     queen.white_queen_death, knight.black_knight_position[key], 2, -1):

            knight.black_knight_attack[key].append(background.board_rect[chr(ord(ch) - 1)][str(k + 2)])

    if (knight.black_knight_position[key][0] < "h") and (
            knight.black_knight_position[key][1] > 2):

        if (not background.board_move[chr(ord(ch) + 1)][str(k - 2)]):
            knight.black_knight_move[key].append(background.board_rect[chr(ord(ch) + 1)][str(k - 2)])

        elif verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position, rook.white_rook_position,
                                     bishop.white_bishop_position, queen.white_queen_position, pawn.white_pawn_death,
                                     knight.white_knight_death, rook.white_rook_death, bishop.white_bishop_death,
                                     queen.white_queen_death, knight.black_knight_position[key], -2, 1):

            knight.black_knight_attack[key].append(background.board_rect[chr(ord(ch) + 1)][str(k - 2)])

    if (knight.black_knight_position[key][0] < "h") and (
            knight.black_knight_position[key][1] < 7):

        if (not background.board_move[chr(ord(ch) + 1)][str(k + 2)]):
            knight.black_knight_move[key].append(background.board_rect[chr(ord(ch) + 1)][str(k + 2)])

        elif verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position, rook.white_rook_position,
                                     bishop.white_bishop_position, queen.white_queen_position, pawn.white_pawn_death,
                                     knight.white_knight_death, rook.white_rook_death, bishop.white_bishop_death,
                                     queen.white_queen_death, knight.black_knight_position[key], 2, 1):

            knight.black_knight_attack[key].append(background.board_rect[chr(ord(ch) + 1)][str(k + 2)])

def update_white_knight(stats, background, rook, pawn, knight, bishop, queen):

    for N, click in knight.white_knight_clicked.items():
        if not click:

            if (knight.white_knight_position[N][0] < "g") and (
                    knight.white_knight_position[N][1] > 1) and (
                    knight.white_big_knight_rects[N].collidepoint(
                        knight.white_knight_rects[N].x + (2 * knight.defaut_rect),
                        knight.white_knight_rects[N].y + knight.defaut_rect)):

                ch = knight.white_knight_position[N][0]
                k = knight.white_knight_position[N][1]
                if (not background.board_move[chr(ord(ch) + 2)][str(k - 1)]) or (
                        verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position,
                                                rook.black_rook_position, bishop.black_bishop_position,
                                                queen.black_queen_position,
                                                pawn.black_pawn_death, knight.black_knight_death, rook.black_rook_death,
                                                bishop.black_bishop_death, queen.black_queen_death,
                                                knight.white_knight_position[N], -1, 2)):

                    background.board_move[chr(ord(ch) + 2)][str(k - 1)] = True
                    background.board_move[ch][str(k)] = False
                    knight.white_knight_position[N][0] = chr(ord(ch) + 2)
                    knight.white_knight_position[N][1] -= 1
                    knight.white_knight_rects[N].x += 2 * knight.defaut_rect
                    knight.white_knight_rects[N].y += knight.defaut_rect
                    queen.black_queen_death = eliminate_killed_piece(N, knight.white_knight_position[N], pawn.black_pawn_position,
                                           knight.black_knight_position, bishop.black_bishop_position,
                                           rook.black_rook_position, queen.black_queen_position,
                                           pawn.black_pawn_death, knight.black_knight_death,
                                           bishop.black_bishop_death,
                                           rook.black_rook_death, queen.black_queen_death,
                                           pawn.black_pawn_rects, knight.black_knight_rects,
                                           bishop.black_bishop_rects,
                                           rook.black_rook_rects, queen.black_queen_rect,
                                           pawn, knight, bishop, rook, queen)
                    stats.white_turn = False
                    stats.black_turn = True

            if (knight.white_knight_position[N][0] < "g") and (
                    knight.white_knight_position[N][1] < 8) and (
                    knight.white_big_knight_rects[N].collidepoint(
                        knight.white_knight_rects[N].x + (2 * knight.defaut_rect),
                        knight.white_knight_rects[N].y - knight.defaut_rect)):

                ch1 = knight.white_knight_position[N][0]
                k1 = knight.white_knight_position[N][1]
                if (not background.board_move[chr(ord(ch1) + 2)][str(k1 + 1)]) or (
                        verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position,
                                                rook.black_rook_position, bishop.black_bishop_position,
                                                queen.black_queen_position,
                                                pawn.black_pawn_death, knight.black_knight_death, rook.black_rook_death,
                                                bishop.black_bishop_death, queen.black_queen_death,
                                                knight.white_knight_position[N], 1, 2)):

                    background.board_move[chr(ord(ch1) + 2)][str(k1 + 1)] = True
                    background.board_move[ch1][str(k1)] = False
                    knight.white_knight_position[N][0] = chr(ord(ch1) + 2)
                    knight.white_knight_position[N][1] += 1
                    knight.white_knight_rects[N].x += 2 * knight.defaut_rect
                    knight.white_knight_rects[N].y -= knight.defaut_rect
                    queen.black_queen_death = eliminate_killed_piece(N, knight.white_knight_position[N], pawn.black_pawn_position,
                                           knight.black_knight_position, bishop.black_bishop_position,
                                           rook.black_rook_position, queen.black_queen_position,
                                           pawn.black_pawn_death, knight.black_knight_death,
                                           bishop.black_bishop_death,
                                           rook.black_rook_death, queen.black_queen_death,
                                           pawn.black_pawn_rects, knight.black_knight_rects,
                                           bishop.black_bishop_rects,
                                           rook.black_rook_rects, queen.black_queen_rect,
                                           pawn, knight, bishop, rook, queen)
                    stats.white_turn = False
                    stats.black_turn = True

            if (knight.white_knight_position[N][0] > "b") and (
                    knight.white_knight_position[N][1] > 1) and (
                    knight.white_big_knight_rects[N].collidepoint(
                        knight.white_knight_rects[N].x - (2 * knight.defaut_rect),
                        knight.white_knight_rects[N].y + knight.defaut_rect)):

                ch2 = knight.white_knight_position[N][0]
                k2 = knight.white_knight_position[N][1]
                if (not background.board_move[chr(ord(ch2) - 2)][str(k2 - 1)]) or (
                        verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position,
                                                rook.black_rook_position, bishop.black_bishop_position,
                                                queen.black_queen_position,
                                                pawn.black_pawn_death, knight.black_knight_death, rook.black_rook_death,
                                                bishop.black_bishop_death, queen.black_queen_death,
                                                knight.white_knight_position[N], -1, -2)):

                    background.board_move[chr(ord(ch2) - 2)][str(k2 - 1)] = True
                    background.board_move[ch2][str(k2)] = False
                    knight.white_knight_position[N][0] = chr(ord(ch2) - 2)
                    knight.white_knight_position[N][1] -= 1
                    knight.white_knight_rects[N].x -= 2 * knight.defaut_rect
                    knight.white_knight_rects[N].y += knight.defaut_rect
                    queen.black_queen_death = eliminate_killed_piece(N, knight.white_knight_position[N], pawn.black_pawn_position,
                                           knight.black_knight_position, bishop.black_bishop_position,
                                           rook.black_rook_position, queen.black_queen_position,
                                           pawn.black_pawn_death, knight.black_knight_death,
                                           bishop.black_bishop_death,
                                           rook.black_rook_death, queen.black_queen_death,
                                           pawn.black_pawn_rects, knight.black_knight_rects,
                                           bishop.black_bishop_rects,
                                           rook.black_rook_rects, queen.black_queen_rect,
                                           pawn, knight, bishop, rook, queen)
                    stats.white_turn = False
                    stats.black_turn = True

            if (knight.white_knight_position[N][0] > "b") and (
                    knight.white_knight_position[N][1] < 8) and (
                    knight.white_big_knight_rects[N].collidepoint(
                        knight.white_knight_rects[N].x - (2 * knight.defaut_rect),
                        knight.white_knight_rects[N].y - knight.defaut_rect)):

                ch3 = knight.white_knight_position[N][0]
                k3 = knight.white_knight_position[N][1]
                if (not background.board_move[chr(ord(ch3) - 2)][str(k3 + 1)]) or (
                        verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position,
                                                rook.black_rook_position, bishop.black_bishop_position,
                                                queen.black_queen_position,
                                                pawn.black_pawn_death, knight.black_knight_death, rook.black_rook_death,
                                                bishop.black_bishop_death, queen.black_queen_death,
                                                knight.white_knight_position[N], 1, -2)):

                    background.board_move[chr(ord(ch3) - 2)][str(k3 + 1)] = True
                    background.board_move[ch3][str(k3)] = False
                    knight.white_knight_position[N][0] = chr(ord(ch3) - 2)
                    knight.white_knight_position[N][1] += 1
                    knight.white_knight_rects[N].x -= 2 * knight.defaut_rect
                    knight.white_knight_rects[N].y -= knight.defaut_rect
                    queen.black_queen_death = eliminate_killed_piece(N, knight.white_knight_position[N], pawn.black_pawn_position,
                                           knight.black_knight_position, bishop.black_bishop_position,
                                           rook.black_rook_position, queen.black_queen_position,
                                           pawn.black_pawn_death, knight.black_knight_death,
                                           bishop.black_bishop_death,
                                           rook.black_rook_death, queen.black_queen_death,
                                           pawn.black_pawn_rects, knight.black_knight_rects,
                                           bishop.black_bishop_rects,
                                           rook.black_rook_rects, queen.black_queen_rect,
                                           pawn, knight, bishop, rook, queen)
                    stats.white_turn = False
                    stats.black_turn = True

            if (knight.white_knight_position[N][0] > "a") and (
                    knight.white_knight_position[N][1] > 2) and (
                    knight.white_big_knight_rects[N].collidepoint(
                        knight.white_knight_rects[N].x - knight.defaut_rect,
                        knight.white_knight_rects[N].y + (2 * knight.defaut_rect))):

                ch4 = knight.white_knight_position[N][0]
                k4 = knight.white_knight_position[N][1]
                if (not background.board_move[chr(ord(ch4) - 1)][str(k4 - 2)]) or (
                        verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position,
                                                rook.black_rook_position, bishop.black_bishop_position,
                                                queen.black_queen_position,
                                                pawn.black_pawn_death, knight.black_knight_death, rook.black_rook_death,
                                                bishop.black_bishop_death, queen.black_queen_death,
                                                knight.white_knight_position[N], -2, -1)):

                    background.board_move[chr(ord(ch4) - 1)][str(k4 - 2)] = True
                    background.board_move[ch4][str(k4)] = False
                    knight.white_knight_position[N][0] = chr(ord(ch4) - 1)
                    knight.white_knight_position[N][1] -= 2
                    knight.white_knight_rects[N].x -= knight.defaut_rect
                    knight.white_knight_rects[N].y += 2 * knight.defaut_rect
                    queen.black_queen_death = eliminate_killed_piece(N, knight.white_knight_position[N], pawn.black_pawn_position,
                                           knight.black_knight_position, bishop.black_bishop_position,
                                           rook.black_rook_position, queen.black_queen_position,
                                           pawn.black_pawn_death, knight.black_knight_death,
                                           bishop.black_bishop_death,
                                           rook.black_rook_death, queen.black_queen_death,
                                           pawn.black_pawn_rects, knight.black_knight_rects,
                                           bishop.black_bishop_rects,
                                           rook.black_rook_rects, queen.black_queen_rect,
                                           pawn, knight, bishop, rook, queen)
                    stats.white_turn = False
                    stats.black_turn = True

            if (knight.white_knight_position[N][0] > "a") and (
                    knight.white_knight_position[N][1] < 7) and (
                    knight.white_big_knight_rects[N].collidepoint(
                        knight.white_knight_rects[N].x - knight.defaut_rect,
                        knight.white_knight_rects[N].y - (2 * knight.defaut_rect))):

                ch5 = knight.white_knight_position[N][0]
                k5 = knight.white_knight_position[N][1]
                if (not background.board_move[chr(ord(ch5) - 1)][str(k5 + 2)]) or (
                        verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position,
                                                rook.black_rook_position, bishop.black_bishop_position,
                                                queen.black_queen_position,
                                                pawn.black_pawn_death, knight.black_knight_death, rook.black_rook_death,
                                                bishop.black_bishop_death, queen.black_queen_death,
                                                knight.white_knight_position[N], 2, -1)):

                    background.board_move[chr(ord(ch5) - 1)][str(k5 + 2)] = True
                    background.board_move[ch5][str(k5)] = False
                    knight.white_knight_position[N][0] = chr(ord(ch5) - 1)
                    knight.white_knight_position[N][1] += 2
                    knight.white_knight_rects[N].x -= knight.defaut_rect
                    knight.white_knight_rects[N].y -= 2 * knight.defaut_rect
                    queen.black_queen_death = eliminate_killed_piece(N, knight.white_knight_position[N], pawn.black_pawn_position,
                                           knight.black_knight_position, bishop.black_bishop_position,
                                           rook.black_rook_position, queen.black_queen_position,
                                           pawn.black_pawn_death, knight.black_knight_death,
                                           bishop.black_bishop_death,
                                           rook.black_rook_death, queen.black_queen_death,
                                           pawn.black_pawn_rects, knight.black_knight_rects,
                                           bishop.black_bishop_rects,
                                           rook.black_rook_rects, queen.black_queen_rect,
                                           pawn, knight, bishop, rook, queen)
                    stats.white_turn = False
                    stats.black_turn = True

            if (knight.white_knight_position[N][0] < "h") and (
                    knight.white_knight_position[N][1] > 2) and (
                    knight.white_big_knight_rects[N].collidepoint(
                        knight.white_knight_rects[N].x + knight.defaut_rect,
                        knight.white_knight_rects[N].y + (2 * knight.defaut_rect))):

                ch6 = knight.white_knight_position[N][0]
                k6 = knight.white_knight_position[N][1]
                if (not background.board_move[chr(ord(ch6) + 1)][str(k6 - 2)]) or (
                        verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position,
                                                rook.black_rook_position, bishop.black_bishop_position,
                                                queen.black_queen_position,
                                                pawn.black_pawn_death, knight.black_knight_death, rook.black_rook_death,
                                                bishop.black_bishop_death, queen.black_queen_death,
                                                knight.white_knight_position[N], -2, 1)):

                    background.board_move[chr(ord(ch6) + 1)][str(k6 - 2)] = True
                    background.board_move[ch6][str(k6)] = False
                    knight.white_knight_position[N][0] = chr(ord(ch6) + 1)
                    knight.white_knight_position[N][1] -= 2
                    knight.white_knight_rects[N].x += knight.defaut_rect
                    knight.white_knight_rects[N].y += 2 * knight.defaut_rect
                    queen.black_queen_death = eliminate_killed_piece(N, knight.white_knight_position[N], pawn.black_pawn_position,
                                           knight.black_knight_position, bishop.black_bishop_position,
                                           rook.black_rook_position, queen.black_queen_position,
                                           pawn.black_pawn_death, knight.black_knight_death,
                                           bishop.black_bishop_death,
                                           rook.black_rook_death, queen.black_queen_death,
                                           pawn.black_pawn_rects, knight.black_knight_rects,
                                           bishop.black_bishop_rects,
                                           rook.black_rook_rects, queen.black_queen_rect,
                                           pawn, knight, bishop, rook, queen)
                    stats.white_turn = False
                    stats.black_turn = True

            if (knight.white_knight_position[N][0] < "h") and (
                    knight.white_knight_position[N][1] < 7) and (
                    knight.white_big_knight_rects[N].collidepoint(
                        knight.white_knight_rects[N].x + knight.defaut_rect,
                        knight.white_knight_rects[N].y - (2 * knight.defaut_rect))):

                ch7 = knight.white_knight_position[N][0]
                k7 = knight.white_knight_position[N][1]
                if (not background.board_move[chr(ord(ch7) + 1)][str(k7 + 2)]) or (
                        verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position,
                                                rook.black_rook_position, bishop.black_bishop_position,
                                                queen.black_queen_position,
                                                pawn.black_pawn_death, knight.black_knight_death, rook.black_rook_death,
                                                bishop.black_bishop_death, queen.black_queen_death,
                                                knight.white_knight_position[N], 2, 1)):

                    background.board_move[chr(ord(ch7) + 1)][str(k7 + 2)] = True
                    background.board_move[ch7][str(k7)] = False
                    knight.white_knight_position[N][0] = chr(ord(ch7) + 1)
                    knight.white_knight_position[N][1] += 2
                    knight.white_knight_rects[N].x += knight.defaut_rect
                    knight.white_knight_rects[N].y -= 2 * knight.defaut_rect
                    queen.black_queen_death = eliminate_killed_piece(N, knight.white_knight_position[N], pawn.black_pawn_position,
                                           knight.black_knight_position, bishop.black_bishop_position,
                                           rook.black_rook_position, queen.black_queen_position,
                                           pawn.black_pawn_death, knight.black_knight_death,
                                           bishop.black_bishop_death,
                                           rook.black_rook_death, queen.black_queen_death,
                                           pawn.black_pawn_rects, knight.black_knight_rects,
                                           bishop.black_bishop_rects,
                                           rook.black_rook_rects, queen.black_queen_rect,
                                           pawn, knight, bishop, rook, queen)
                    stats.white_turn = False
                    stats.black_turn = True

def update_black_knight(stats, background, rook, pawn, knight, bishop, queen):

    for N, click in knight.black_knight_clicked.items():
        if not click:

            if (knight.black_knight_position[N][0] < "g") and (
                    knight.black_knight_position[N][1] > 1) and (
                    knight.black_big_knight_rects[N].collidepoint(
                        knight.black_knight_rects[N].x + (2 * knight.defaut_rect),
                        knight.black_knight_rects[N].y + knight.defaut_rect)):

                ch = knight.black_knight_position[N][0]
                k = knight.black_knight_position[N][1]
                if (not background.board_move[chr(ord(ch) + 2)][str(k - 1)]) or (
                        verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position,
                                                rook.white_rook_position,
                                                bishop.white_bishop_position, queen.white_queen_position,
                                                pawn.white_pawn_death,
                                                knight.white_knight_death, rook.white_rook_death,
                                                bishop.white_bishop_death,
                                                queen.white_queen_death, knight.black_knight_position[N], -1, 2)):

                    background.board_move[chr(ord(ch) + 2)][str(k - 1)] = True
                    background.board_move[ch][str(k)] = False
                    knight.black_knight_position[N][0] = chr(ord(ch) + 2)
                    knight.black_knight_position[N][1] -= 1
                    knight.black_knight_rects[N].x += 2 * knight.defaut_rect
                    knight.black_knight_rects[N].y += knight.defaut_rect
                    queen.white_queen_death = eliminate_killed_piece(N, knight.black_knight_position[N], pawn.white_pawn_position,
                                           knight.white_knight_position, bishop.white_bishop_position,
                                           rook.white_rook_position, queen.white_queen_position,
                                           pawn.white_pawn_death, knight.white_knight_death,
                                           bishop.white_bishop_death,
                                           rook.white_rook_death, queen.white_queen_death,
                                           pawn.white_pawn_rects, knight.white_knight_rects,
                                           bishop.white_bishop_rects,
                                           rook.white_rook_rects, queen.white_queen_rect,
                                           pawn, knight, bishop, rook, queen)
                    stats.black_turn = False
                    stats.white_turn = True

            if (knight.black_knight_position[N][0] < "g") and (
                    knight.black_knight_position[N][1] < 8) and (
                    knight.black_big_knight_rects[N].collidepoint(
                        knight.black_knight_rects[N].x + (2 * knight.defaut_rect),
                        knight.black_knight_rects[N].y - knight.defaut_rect)):

                ch1 = knight.black_knight_position[N][0]
                k1 = knight.black_knight_position[N][1]
                if (not background.board_move[chr(ord(ch1) + 2)][str(k1 + 1)]) or (
                        verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position,
                                                rook.white_rook_position,
                                                bishop.white_bishop_position, queen.white_queen_position,
                                                pawn.white_pawn_death,
                                                knight.white_knight_death, rook.white_rook_death,
                                                bishop.white_bishop_death,
                                                queen.white_queen_death, knight.black_knight_position[N], 1, 2)):

                    background.board_move[chr(ord(ch1) + 2)][str(k1 + 1)] = True
                    background.board_move[ch1][str(k1)] = False
                    knight.black_knight_position[N][0] = chr(ord(ch1) + 2)
                    knight.black_knight_position[N][1] += 1
                    knight.black_knight_rects[N].x += 2 * knight.defaut_rect
                    knight.black_knight_rects[N].y -= knight.defaut_rect
                    queen.white_queen_death = eliminate_killed_piece(N, knight.black_knight_position[N], pawn.white_pawn_position,
                                           knight.white_knight_position, bishop.white_bishop_position,
                                           rook.white_rook_position, queen.white_queen_position,
                                           pawn.white_pawn_death, knight.white_knight_death,
                                           bishop.white_bishop_death,
                                           rook.white_rook_death, queen.white_queen_death,
                                           pawn.white_pawn_rects, knight.white_knight_rects,
                                           bishop.white_bishop_rects,
                                           rook.white_rook_rects, queen.white_queen_rect,
                                           pawn, knight, bishop, rook, queen)
                    stats.black_turn = False
                    stats.white_turn = True

            if (knight.black_knight_position[N][0] > "b") and (
                    knight.black_knight_position[N][1] > 1) and (
                    knight.black_big_knight_rects[N].collidepoint(
                        knight.black_knight_rects[N].x - (2 * knight.defaut_rect),
                        knight.black_knight_rects[N].y + knight.defaut_rect)):

                ch2 = knight.black_knight_position[N][0]
                k2 = knight.black_knight_position[N][1]
                if (not background.board_move[chr(ord(ch2) - 2)][str(k2 - 1)]) or (
                        verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position,
                                                rook.white_rook_position,
                                                bishop.white_bishop_position, queen.white_queen_position,
                                                pawn.white_pawn_death,
                                                knight.white_knight_death, rook.white_rook_death,
                                                bishop.white_bishop_death,
                                                queen.white_queen_death, knight.black_knight_position[N], -1, -2)):

                    background.board_move[chr(ord(ch2) - 2)][str(k2 - 1)] = True
                    background.board_move[ch2][str(k2)] = False
                    knight.black_knight_position[N][0] = chr(ord(ch2) - 2)
                    knight.black_knight_position[N][1] -= 1
                    knight.black_knight_rects[N].x -= 2 * knight.defaut_rect
                    knight.black_knight_rects[N].y += knight.defaut_rect
                    queen.white_queen_death = eliminate_killed_piece(N, knight.black_knight_position[N], pawn.white_pawn_position,
                                           knight.white_knight_position, bishop.white_bishop_position,
                                           rook.white_rook_position, queen.white_queen_position,
                                           pawn.white_pawn_death, knight.white_knight_death,
                                           bishop.white_bishop_death,
                                           rook.white_rook_death, queen.white_queen_death,
                                           pawn.white_pawn_rects, knight.white_knight_rects,
                                           bishop.white_bishop_rects,
                                           rook.white_rook_rects, queen.white_queen_rect,
                                           pawn, knight, bishop, rook, queen)
                    stats.black_turn = False
                    stats.white_turn = True

            if (knight.black_knight_position[N][0] > "b") and (
                    knight.black_knight_position[N][1] < 8) and (
                    knight.black_big_knight_rects[N].collidepoint(
                        knight.black_knight_rects[N].x - (2 * knight.defaut_rect),
                        knight.black_knight_rects[N].y - knight.defaut_rect)):

                ch3 = knight.black_knight_position[N][0]
                k3 = knight.black_knight_position[N][1]
                if (not background.board_move[chr(ord(ch3) - 2)][str(k3 + 1)]) or (
                        verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position,
                                                rook.white_rook_position,
                                                bishop.white_bishop_position, queen.white_queen_position,
                                                pawn.white_pawn_death,
                                                knight.white_knight_death, rook.white_rook_death,
                                                bishop.white_bishop_death,
                                                queen.white_queen_death, knight.black_knight_position[N], 1, -2)):

                    background.board_move[chr(ord(ch3) - 2)][str(k3 + 1)] = True
                    background.board_move[ch3][str(k3)] = False
                    knight.black_knight_position[N][0] = chr(ord(ch3) - 2)
                    knight.black_knight_position[N][1] += 1
                    knight.black_knight_rects[N].x -= 2 * knight.defaut_rect
                    knight.black_knight_rects[N].y -= knight.defaut_rect
                    queen.white_queen_death = eliminate_killed_piece(N, knight.black_knight_position[N], pawn.white_pawn_position,
                                           knight.white_knight_position, bishop.white_bishop_position,
                                           rook.white_rook_position, queen.white_queen_position,
                                           pawn.white_pawn_death, knight.white_knight_death,
                                           bishop.white_bishop_death,
                                           rook.white_rook_death, queen.white_queen_death,
                                           pawn.white_pawn_rects, knight.white_knight_rects,
                                           bishop.white_bishop_rects,
                                           rook.white_rook_rects, queen.white_queen_rect,
                                           pawn, knight, bishop, rook, queen)
                    stats.black_turn = False
                    stats.white_turn = True

            if (knight.black_knight_position[N][0] > "a") and (
                    knight.black_knight_position[N][1] > 2) and (
                    knight.black_big_knight_rects[N].collidepoint(
                        knight.black_knight_rects[N].x - knight.defaut_rect,
                        knight.black_knight_rects[N].y + (2 * knight.defaut_rect))):

                ch4 = knight.black_knight_position[N][0]
                k4 = knight.black_knight_position[N][1]
                if (not background.board_move[chr(ord(ch4) - 1)][str(k4 - 2)]) or (
                        verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position,
                                                rook.white_rook_position,
                                                bishop.white_bishop_position, queen.white_queen_position,
                                                pawn.white_pawn_death,
                                                knight.white_knight_death, rook.white_rook_death,
                                                bishop.white_bishop_death,
                                                queen.white_queen_death, knight.black_knight_position[N], -2, -1)):

                    background.board_move[chr(ord(ch4) - 1)][str(k4 - 2)] = True
                    background.board_move[ch4][str(k4)] = False
                    knight.black_knight_position[N][0] = chr(ord(ch4) - 1)
                    knight.black_knight_position[N][1] -= 2
                    knight.black_knight_rects[N].x -= knight.defaut_rect
                    knight.black_knight_rects[N].y += 2 * knight.defaut_rect
                    queen.white_queen_death = eliminate_killed_piece(N, knight.black_knight_position[N], pawn.white_pawn_position,
                                           knight.white_knight_position, bishop.white_bishop_position,
                                           rook.white_rook_position, queen.white_queen_position,
                                           pawn.white_pawn_death, knight.white_knight_death,
                                           bishop.white_bishop_death,
                                           rook.white_rook_death, queen.white_queen_death,
                                           pawn.white_pawn_rects, knight.white_knight_rects,
                                           bishop.white_bishop_rects,
                                           rook.white_rook_rects, queen.white_queen_rect,
                                           pawn, knight, bishop, rook, queen)
                    stats.black_turn = False
                    stats.white_turn = True

            if (knight.black_knight_position[N][0] > "a") and (
                    knight.black_knight_position[N][1] < 7) and (
                    knight.black_big_knight_rects[N].collidepoint(
                        knight.black_knight_rects[N].x - knight.defaut_rect,
                        knight.black_knight_rects[N].y - (2 * knight.defaut_rect))):

                ch5 = knight.black_knight_position[N][0]
                k5 = knight.black_knight_position[N][1]
                if (not background.board_move[chr(ord(ch5) - 1)][str(k5 + 2)]) or (
                        verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position,
                                                rook.white_rook_position,
                                                bishop.white_bishop_position, queen.white_queen_position,
                                                pawn.white_pawn_death,
                                                knight.white_knight_death, rook.white_rook_death,
                                                bishop.white_bishop_death,
                                                queen.white_queen_death, knight.black_knight_position[N], 2, -1)):

                    background.board_move[chr(ord(ch5) - 1)][str(k5 + 2)] = True
                    background.board_move[ch5][str(k5)] = False
                    knight.black_knight_position[N][0] = chr(ord(ch5) - 1)
                    knight.black_knight_position[N][1] += 2
                    knight.black_knight_rects[N].x -= knight.defaut_rect
                    knight.black_knight_rects[N].y -= 2 * knight.defaut_rect
                    queen.white_queen_death = eliminate_killed_piece(N, knight.black_knight_position[N], pawn.white_pawn_position,
                                           knight.white_knight_position, bishop.white_bishop_position,
                                           rook.white_rook_position, queen.white_queen_position,
                                           pawn.white_pawn_death, knight.white_knight_death,
                                           bishop.white_bishop_death,
                                           rook.white_rook_death, queen.white_queen_death,
                                           pawn.white_pawn_rects, knight.white_knight_rects,
                                           bishop.white_bishop_rects,
                                           rook.white_rook_rects, queen.white_queen_rect,
                                           pawn, knight, bishop, rook, queen)
                    stats.black_turn = False
                    stats.white_turn = True

            if (knight.black_knight_position[N][0] < "h") and (
                    knight.black_knight_position[N][1] > 2) and (
                    knight.black_big_knight_rects[N].collidepoint(
                        knight.black_knight_rects[N].x + knight.defaut_rect,
                        knight.black_knight_rects[N].y + (2 * knight.defaut_rect))):

                ch6 = knight.black_knight_position[N][0]
                k6 = knight.black_knight_position[N][1]
                if (not background.board_move[chr(ord(ch6) + 1)][str(k6 - 2)]) or (
                        verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position,
                                                rook.white_rook_position,
                                                bishop.white_bishop_position, queen.white_queen_position,
                                                pawn.white_pawn_death,
                                                knight.white_knight_death, rook.white_rook_death,
                                                bishop.white_bishop_death,
                                                queen.white_queen_death, knight.black_knight_position[N], -2, 1)):

                    background.board_move[chr(ord(ch6) + 1)][str(k6 - 2)] = True
                    background.board_move[ch6][str(k6)] = False
                    knight.black_knight_position[N][0] = chr(ord(ch6) + 1)
                    knight.black_knight_position[N][1] -= 2
                    knight.black_knight_rects[N].x += knight.defaut_rect
                    knight.black_knight_rects[N].y += 2 * knight.defaut_rect
                    queen.white_queen_death = eliminate_killed_piece(N, knight.black_knight_position[N], pawn.white_pawn_position,
                                           knight.white_knight_position, bishop.white_bishop_position,
                                           rook.white_rook_position, queen.white_queen_position,
                                           pawn.white_pawn_death, knight.white_knight_death,
                                           bishop.white_bishop_death,
                                           rook.white_rook_death, queen.white_queen_death,
                                           pawn.white_pawn_rects, knight.white_knight_rects,
                                           bishop.white_bishop_rects,
                                           rook.white_rook_rects, queen.white_queen_rect,
                                           pawn, knight, bishop, rook, queen)
                    stats.black_turn = False
                    stats.white_turn = True

            if (knight.black_knight_position[N][0] < "h") and (
                    knight.black_knight_position[N][1] < 7) and (
                    knight.black_big_knight_rects[N].collidepoint(
                        knight.black_knight_rects[N].x + knight.defaut_rect,
                        knight.black_knight_rects[N].y - (2 * knight.defaut_rect))):

                ch7 = knight.black_knight_position[N][0]
                k7 = knight.black_knight_position[N][1]
                if (not background.board_move[chr(ord(ch7) + 1)][str(k7 + 2)]) or (
                        verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position,
                                                rook.white_rook_position,
                                                bishop.white_bishop_position, queen.white_queen_position,
                                                pawn.white_pawn_death,
                                                knight.white_knight_death, rook.white_rook_death,
                                                bishop.white_bishop_death,
                                                queen.white_queen_death, knight.black_knight_position[N], 2, 1)):

                    background.board_move[chr(ord(ch7) + 1)][str(k7 + 2)] = True
                    background.board_move[ch7][str(k7)] = False
                    knight.black_knight_position[N][0] = chr(ord(ch7) + 1)
                    knight.black_knight_position[N][1] += 2
                    knight.black_knight_rects[N].x += knight.defaut_rect
                    knight.black_knight_rects[N].y -= 2 * knight.defaut_rect
                    queen.white_queen_death = eliminate_killed_piece(N, knight.black_knight_position[N], pawn.white_pawn_position,
                                           knight.white_knight_position, bishop.white_bishop_position,
                                           rook.white_rook_position, queen.white_queen_position,
                                           pawn.white_pawn_death, knight.white_knight_death,
                                           bishop.white_bishop_death,
                                           rook.white_rook_death, queen.white_queen_death,
                                           pawn.white_pawn_rects, knight.white_knight_rects,
                                           bishop.white_bishop_rects,
                                           rook.white_rook_rects, queen.white_queen_rect,
                                           pawn, knight, bishop, rook, queen)
                    stats.black_turn = False
                    stats.white_turn = True

def update_white_bishop(stats, background, rook, pawn, knight, bishop, queen):

    for bishop0, click in bishop.white_bishop_clicked.items():
        if not click:

            key0 = bishop.white_bishop_position[bishop0][1] + 1
            ch0 = chr(ord(bishop.white_bishop_position[bishop0][0]) + 1)

            key1 = bishop.white_bishop_position[bishop0][1] - 1
            ch1 = chr(ord(bishop.white_bishop_position[bishop0][0]) - 1)

            if (bishop.white_bishop_position[bishop0][0]) < 'h' and (bishop.white_bishop_position[bishop0][1] < 8):
                while (ch0 <= "h") and (key0 <= 8) and (not background.board_move[ch0][str(key0)]):

                    if (bishop.white_big_bishop_rects[bishop0].collidepoint(bishop.white_bishop_rects[bishop0].x + (
                       bishop.defaut_rect * (ord(ch0) - ord(bishop.white_bishop_position[bishop0][0]))),
                       bishop.white_bishop_rects[bishop0].y - (
                       bishop.defaut_rect * (key0 - bishop.white_bishop_position[bishop0][1])))):

                        stats.white_turn = False
                        stats.black_turn = True

                        background.board_move[bishop.white_bishop_position[bishop0][0]][str(bishop.white_bishop_position[bishop0][1])] = False
                        background.board_move[ch0][str(key0)] = True

                        bishop.white_bishop_rects[bishop0].x += bishop.defaut_rect * (ord(ch0) - ord(bishop.white_bishop_position[bishop0][0]))
                        bishop.white_bishop_rects[bishop0].y -= bishop.defaut_rect * (key0 - bishop.white_bishop_position[bishop0][1])

                        bishop.white_bishop_position[bishop0][0] = ch0
                        bishop.white_bishop_position[bishop0][1] = key0
                        pawn.pieces_move.append(bishop0 + bishop.white_bishop_position[bishop0][0] + str(bishop.white_bishop_position[bishop0][1]))
                        print(pawn.pieces_move)
                        break

                    ch0 = chr(ord(ch0) + 1)
                    key0 += 1

                if (bishop.white_big_bishop_rects[bishop0].collidepoint(bishop.white_bishop_rects[bishop0].x + (
                        bishop.defaut_rect * (ord(ch0) - ord(bishop.white_bishop_position[bishop0][0]))),
                        bishop.white_bishop_rects[bishop0].y - (bishop.defaut_rect * (key0 - bishop.white_bishop_position[bishop0][1])))):

                    aux0 = bishop.white_bishop_position[bishop0][0]
                    aux1 = bishop.white_bishop_position[bishop0][1]
                    bishop.white_bishop_position[bishop0][0] = ch0
                    bishop.white_bishop_position[bishop0][1] = key0

                    if verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position, rook.black_rook_position,
                                            bishop.black_bishop_position, queen.black_queen_position, pawn.black_pawn_death,
                                            knight.black_knight_death, rook.black_rook_death, bishop.black_bishop_death,
                                            queen.black_queen_death, bishop.white_bishop_position[bishop0], 0, 0):

                        stats.white_turn = False
                        stats.black_turn = True

                        background.board_move[aux0][str(aux1)] = False
                        background.board_move[bishop.white_bishop_position[bishop0][0]][str(bishop.white_bishop_position[bishop0][1])] = True

                        bishop.white_bishop_rects[bishop0].x += bishop.defaut_rect * (ord(ch0) - ord(aux0))
                        bishop.white_bishop_rects[bishop0].y -= bishop.defaut_rect * (key0 - aux1)

                        queen.black_queen_death = eliminate_killed_piece(bishop0, bishop.white_bishop_position[bishop0], pawn.black_pawn_position,
                                               knight.black_knight_position, bishop.black_bishop_position,
                                               rook.black_rook_position, queen.black_queen_position,
                                               pawn.black_pawn_death, knight.black_knight_death,
                                               bishop.black_bishop_death,
                                               rook.black_rook_death, queen.black_queen_death,
                                               pawn.black_pawn_rects, knight.black_knight_rects,
                                               bishop.black_bishop_rects,
                                               rook.black_rook_rects, queen.black_queen_rect,
                                               pawn, knight, bishop, rook, queen)

                    else:
                        bishop.white_bishop_position[bishop0][0] = aux0
                        bishop.white_bishop_position[bishop0][1] = aux1

            if (bishop.white_bishop_position[bishop0][0] > 'a') and (bishop.white_bishop_position[bishop0][1] > 1):
                while (ch1 >= "a") and (key1 >= 1) and (not background.board_move[ch1][str(key1)]):

                    if (bishop.white_big_bishop_rects[bishop0].collidepoint(bishop.white_bishop_rects[bishop0].x - (
                        bishop.defaut_rect * (ord(bishop.white_bishop_position[bishop0][0]) - ord(ch1))),
                        bishop.white_bishop_rects[bishop0].y + (
                        bishop.defaut_rect * (bishop.white_bishop_position[bishop0][1] - key1)))):

                        stats.white_turn = False
                        stats.black_turn = True

                        background.board_move[bishop.white_bishop_position[bishop0][0]][str(bishop.white_bishop_position[bishop0][1])] = False
                        background.board_move[ch1][str(key1)] = True

                        bishop.white_bishop_rects[bishop0].x -= bishop.defaut_rect * (ord(bishop.white_bishop_position[bishop0][0]) - ord(ch1))
                        bishop.white_bishop_rects[bishop0].y += bishop.defaut_rect * (bishop.white_bishop_position[bishop0][1] - key1)

                        bishop.white_bishop_position[bishop0][0] = ch1
                        bishop.white_bishop_position[bishop0][1] = key1
                        pawn.pieces_move.append(bishop0 + bishop.white_bishop_position[bishop0][0] + str(bishop.white_bishop_position[bishop0][1]))
                        print(pawn.pieces_move)
                        break

                    ch1 = chr(ord(ch1) - 1)
                    key1 -= 1

                if (bishop.white_big_bishop_rects[bishop0].collidepoint(bishop.white_bishop_rects[bishop0].x - (
                        bishop.defaut_rect * (ord(bishop.white_bishop_position[bishop0][0]) - ord(ch1))),
                        bishop.white_bishop_rects[bishop0].y + (bishop.defaut_rect * (
                        bishop.white_bishop_position[bishop0][1] - key1)))):

                    aux2 = bishop.white_bishop_position[bishop0][0]
                    aux3 = bishop.white_bishop_position[bishop0][1]
                    bishop.white_bishop_position[bishop0][0] = ch1
                    bishop.white_bishop_position[bishop0][1] = key1

                    if verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position, rook.black_rook_position,
                                            bishop.black_bishop_position, queen.black_queen_position, pawn.black_pawn_death,
                                            knight.black_knight_death, rook.black_rook_death, bishop.black_bishop_death,
                                            queen.black_queen_death, bishop.white_bishop_position[bishop0], 0, 0):

                        stats.white_turn = False
                        stats.black_turn = True

                        background.board_move[aux2][str(aux3)] = False
                        background.board_move[bishop.white_bishop_position[bishop0][0]][str(bishop.white_bishop_position[bishop0][1])] = True

                        bishop.white_bishop_rects[bishop0].x -= bishop.defaut_rect * (ord(aux2) - ord(ch1))
                        bishop.white_bishop_rects[bishop0].y += bishop.defaut_rect * (aux3 - key1)

                        queen.black_queen_death = eliminate_killed_piece(bishop0, bishop.white_bishop_position[bishop0], pawn.black_pawn_position,
                                               knight.black_knight_position, bishop.black_bishop_position,
                                               rook.black_rook_position, queen.black_queen_position,
                                               pawn.black_pawn_death, knight.black_knight_death,
                                               bishop.black_bishop_death,
                                               rook.black_rook_death, queen.black_queen_death,
                                               pawn.black_pawn_rects, knight.black_knight_rects,
                                               bishop.black_bishop_rects,
                                               rook.black_rook_rects, queen.black_queen_rect,
                                               pawn, knight, bishop, rook, queen)

                    else:
                        bishop.white_bishop_position[bishop0][0] = aux2
                        bishop.white_bishop_position[bishop0][1] = aux3

            ch2 = chr(ord(bishop.white_bishop_position[bishop0][0]) - 1)
            key2 = bishop.white_bishop_position[bishop0][1] + 1
            if (bishop.white_bishop_position[bishop0][0] > 'a') and (bishop.white_bishop_position[bishop0][1] < 8):
                while (ch2 >= "a") and (key2 <= 8) and (not background.board_move[ch2][str(key2)]):

                    if (bishop.white_big_bishop_rects[bishop0].collidepoint(bishop.white_bishop_rects[bishop0].x - (
                        bishop.defaut_rect * (ord(bishop.white_bishop_position[bishop0][0]) - ord(ch2))),
                        bishop.white_bishop_rects[bishop0].y - (
                        bishop.defaut_rect * (key2 - bishop.white_bishop_position[bishop0][1])))):

                        stats.white_turn = False
                        stats.black_turn = True

                        background.board_move[bishop.white_bishop_position[bishop0][0]][str(bishop.white_bishop_position[bishop0][1])] = False
                        background.board_move[ch2][str(key2)] = True

                        bishop.white_bishop_rects[bishop0].x -= bishop.defaut_rect * (ord(bishop.white_bishop_position[bishop0][0]) - ord(ch2))
                        bishop.white_bishop_rects[bishop0].y -= bishop.defaut_rect * (key2 - bishop.white_bishop_position[bishop0][1])

                        bishop.white_bishop_position[bishop0][0] = ch2
                        bishop.white_bishop_position[bishop0][1] = key2
                        pawn.pieces_move.append(bishop0 + bishop.white_bishop_position[bishop0][0] + str(bishop.white_bishop_position[bishop0][1]))
                        print(pawn.pieces_move)
                        break

                    ch2 = chr(ord(ch2) - 1)
                    key2 += 1

                if (bishop.white_big_bishop_rects[bishop0].collidepoint(bishop.white_bishop_rects[bishop0].x - (
                        bishop.defaut_rect * (ord(bishop.white_bishop_position[bishop0][0]) - ord(ch2))),
                        bishop.white_bishop_rects[bishop0].y - (bishop.defaut_rect * (key2 -
                        bishop.white_bishop_position[bishop0][1])))):

                    aux4 = bishop.white_bishop_position[bishop0][0]
                    aux5 = bishop.white_bishop_position[bishop0][1]
                    bishop.white_bishop_position[bishop0][0] = ch2
                    bishop.white_bishop_position[bishop0][1] = key2

                    if verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position, rook.black_rook_position,
                                            bishop.black_bishop_position, queen.black_queen_position, pawn.black_pawn_death,
                                            knight.black_knight_death, rook.black_rook_death, bishop.black_bishop_death,
                                            queen.black_queen_death, bishop.white_bishop_position[bishop0], 0, 0):

                        stats.white_turn = False
                        stats.black_turn = True

                        background.board_move[aux4][str(aux5)] = False
                        background.board_move[bishop.white_bishop_position[bishop0][0]][str(bishop.white_bishop_position[bishop0][1])] = True

                        bishop.white_bishop_rects[bishop0].x -= bishop.defaut_rect * (ord(aux4) - ord(ch2))
                        bishop.white_bishop_rects[bishop0].y -= bishop.defaut_rect * (key2 - aux5)

                        queen.black_queen_death = eliminate_killed_piece(bishop0, bishop.white_bishop_position[bishop0], pawn.black_pawn_position,
                                               knight.black_knight_position, bishop.black_bishop_position,
                                               rook.black_rook_position, queen.black_queen_position,
                                               pawn.black_pawn_death, knight.black_knight_death,
                                               bishop.black_bishop_death,
                                               rook.black_rook_death, queen.black_queen_death,
                                               pawn.black_pawn_rects, knight.black_knight_rects,
                                               bishop.black_bishop_rects,
                                               rook.black_rook_rects, queen.black_queen_rect,
                                               pawn, knight, bishop, rook, queen)

                    else:
                        bishop.white_bishop_position[bishop0][0] = aux4
                        bishop.white_bishop_position[bishop0][1] = aux5

            ch3 = chr(ord(bishop.white_bishop_position[bishop0][0]) + 1)
            key3 = bishop.white_bishop_position[bishop0][1] - 1
            if (bishop.white_bishop_position[bishop0][0] < 'h') and (bishop.white_bishop_position[bishop0][1] > 1):
                while (ch3 <= "h") and (key3 >= 1) and (not background.board_move[ch3][str(key3)]):

                    if (bishop.white_big_bishop_rects[bishop0].collidepoint(bishop.white_bishop_rects[bishop0].x + (
                        bishop.defaut_rect * (ord(ch3) - ord(bishop.white_bishop_position[bishop0][0]))),
                        bishop.white_bishop_rects[bishop0].y + (
                        bishop.defaut_rect * (bishop.white_bishop_position[bishop0][1] - key3)))):

                        stats.white_turn = False
                        stats.black_turn = True

                        background.board_move[bishop.white_bishop_position[bishop0][0]][str(bishop.white_bishop_position[bishop0][1])] = False
                        background.board_move[ch3][str(key3)] = True

                        bishop.white_bishop_rects[bishop0].x += bishop.defaut_rect * (ord(ch3) - ord(bishop.white_bishop_position[bishop0][0]))
                        bishop.white_bishop_rects[bishop0].y += bishop.defaut_rect * (bishop.white_bishop_position[bishop0][1] - key3)

                        bishop.white_bishop_position[bishop0][0] = ch3
                        bishop.white_bishop_position[bishop0][1] = key3
                        pawn.pieces_move.append(bishop0 + bishop.white_bishop_position[bishop0][0] + str(bishop.white_bishop_position[bishop0][1]))
                        print(pawn.pieces_move)
                        break

                    ch3 = chr(ord(ch3) + 1)
                    key3 -= 1

                if (bishop.white_big_bishop_rects[bishop0].collidepoint(bishop.white_bishop_rects[bishop0].x + (
                    bishop.defaut_rect * (ord(ch3) - ord(bishop.white_bishop_position[bishop0][0]))),
                    bishop.white_bishop_rects[bishop0].y + (bishop.defaut_rect * (bishop.white_bishop_position[bishop0][1] - key3)))):

                    aux6 = bishop.white_bishop_position[bishop0][0]
                    aux7 = bishop.white_bishop_position[bishop0][1]
                    bishop.white_bishop_position[bishop0][0] = ch3
                    bishop.white_bishop_position[bishop0][1] = key3

                    if verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position, rook.black_rook_position,
                                            bishop.black_bishop_position, queen.black_queen_position, pawn.black_pawn_death,
                                            knight.black_knight_death, rook.black_rook_death, bishop.black_bishop_death,
                                            queen.black_queen_death, bishop.white_bishop_position[bishop0], 0, 0):

                        stats.white_turn = False
                        stats.black_turn = True

                        background.board_move[aux6][str(aux7)] = False
                        background.board_move[bishop.white_bishop_position[bishop0][0]][str(bishop.white_bishop_position[bishop0][1])] = True

                        bishop.white_bishop_rects[bishop0].x += bishop.defaut_rect * (ord(ch3) - ord(aux6))
                        bishop.white_bishop_rects[bishop0].y += bishop.defaut_rect * (aux7 - key3)

                        queen.black_queen_death = eliminate_killed_piece(bishop0, bishop.white_bishop_position[bishop0], pawn.black_pawn_position,
                                               knight.black_knight_position, bishop.black_bishop_position,
                                               rook.black_rook_position, queen.black_queen_position,
                                               pawn.black_pawn_death, knight.black_knight_death,
                                               bishop.black_bishop_death,
                                               rook.black_rook_death, queen.black_queen_death,
                                               pawn.black_pawn_rects, knight.black_knight_rects,
                                               bishop.black_bishop_rects,
                                               rook.black_rook_rects, queen.black_queen_rect,
                                               pawn, knight, bishop, rook, queen)

                    else:
                        bishop.white_bishop_position[bishop0][0] = aux6
                        bishop.white_bishop_position[bishop0][1] = aux7

def update_black_bishop(stats, background, rook, pawn, knight, bishop, queen):

    for bishop0, click in bishop.black_bishop_clicked.items():
        if not click:

            key0 = bishop.black_bishop_position[bishop0][1] + 1
            ch0 = chr(ord(bishop.black_bishop_position[bishop0][0]) + 1)

            key1 = bishop.black_bishop_position[bishop0][1] - 1
            ch1 = chr(ord(bishop.black_bishop_position[bishop0][0]) - 1)

            if (bishop.black_bishop_position[bishop0][0]) < 'h' and (bishop.black_bishop_position[bishop0][1] < 8):
                while (ch0 <= "h") and (key0 <= 8) and (not background.board_move[ch0][str(key0)]):

                    if (bishop.black_big_bishop_rects[bishop0].collidepoint(bishop.black_bishop_rects[bishop0].x + (
                       bishop.defaut_rect * (ord(ch0) - ord(bishop.black_bishop_position[bishop0][0]))),
                       bishop.black_bishop_rects[bishop0].y - (
                       bishop.defaut_rect * (key0 - bishop.black_bishop_position[bishop0][1])))):

                        stats.black_turn = False
                        stats.white_turn = True

                        background.board_move[bishop.black_bishop_position[bishop0][0]][str(bishop.black_bishop_position[bishop0][1])] = False
                        background.board_move[ch0][str(key0)] = True

                        bishop.black_bishop_rects[bishop0].x += bishop.defaut_rect * (ord(ch0) - ord(bishop.black_bishop_position[bishop0][0]))
                        bishop.black_bishop_rects[bishop0].y -= bishop.defaut_rect * (key0 - bishop.black_bishop_position[bishop0][1])

                        bishop.black_bishop_position[bishop0][0] = ch0
                        bishop.black_bishop_position[bishop0][1] = key0
                        pawn.pieces_move.append(bishop0 + bishop.black_bishop_position[bishop0][0] + str(bishop.black_bishop_position[bishop0][1]))
                        print(pawn.pieces_move)
                        break

                    ch0 = chr(ord(ch0) + 1)
                    key0 += 1

                if (bishop.black_big_bishop_rects[bishop0].collidepoint(bishop.black_bishop_rects[bishop0].x + (
                        bishop.defaut_rect * (ord(ch0) - ord(bishop.black_bishop_position[bishop0][0]))),
                        bishop.black_bishop_rects[bishop0].y - (bishop.defaut_rect * (key0 - bishop.black_bishop_position[bishop0][1])))):

                    aux0 = bishop.black_bishop_position[bishop0][0]
                    aux1 = bishop.black_bishop_position[bishop0][1]
                    bishop.black_bishop_position[bishop0][0] = ch0
                    bishop.black_bishop_position[bishop0][1] = key0

                    if verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position, rook.white_rook_position,
                                           bishop.white_bishop_position, queen.white_queen_position, pawn.white_pawn_death,
                                           knight.white_knight_death, rook.white_rook_death, bishop.white_bishop_death,
                                           queen.white_queen_death, bishop.black_bishop_position[bishop0], 0, 0):

                        stats.black_turn = False
                        stats.white_turn = True

                        background.board_move[aux0][str(aux1)] = False
                        background.board_move[bishop.black_bishop_position[bishop0][0]][str(bishop.black_bishop_position[bishop0][1])] = True

                        bishop.black_bishop_rects[bishop0].x += bishop.defaut_rect * (ord(ch0) - ord(aux0))
                        bishop.black_bishop_rects[bishop0].y -= bishop.defaut_rect * (key0 - aux1)

                        queen.white_queen_death = eliminate_killed_piece(bishop0, bishop.black_bishop_position[bishop0], pawn.white_pawn_position,
                                               knight.white_knight_position, bishop.white_bishop_position,
                                               rook.white_rook_position, queen.white_queen_position,
                                               pawn.white_pawn_death, knight.white_knight_death,
                                               bishop.white_bishop_death,
                                               rook.white_rook_death, queen.white_queen_death,
                                               pawn.white_pawn_rects, knight.white_knight_rects,
                                               bishop.white_bishop_rects,
                                               rook.white_rook_rects, queen.white_queen_rect,
                                               pawn, knight, bishop, rook, queen)

                    else:
                        bishop.black_bishop_position[bishop0][0] = aux0
                        bishop.black_bishop_position[bishop0][1] = aux1

            if (bishop.black_bishop_position[bishop0][0] > 'a') and (bishop.black_bishop_position[bishop0][1] > 1):
                while (ch1 >= "a") and (key1 >= 1) and (not background.board_move[ch1][str(key1)]):

                    if (bishop.black_big_bishop_rects[bishop0].collidepoint(bishop.black_bishop_rects[bishop0].x - (
                        bishop.defaut_rect * (ord(bishop.black_bishop_position[bishop0][0]) - ord(ch1))),
                        bishop.black_bishop_rects[bishop0].y + (
                        bishop.defaut_rect * (bishop.black_bishop_position[bishop0][1] - key1)))):

                        stats.black_turn = False
                        stats.white_turn = True

                        background.board_move[bishop.black_bishop_position[bishop0][0]][str(bishop.black_bishop_position[bishop0][1])] = False
                        background.board_move[ch1][str(key1)] = True

                        bishop.black_bishop_rects[bishop0].x -= bishop.defaut_rect * (ord(bishop.black_bishop_position[bishop0][0]) - ord(ch1))
                        bishop.black_bishop_rects[bishop0].y += bishop.defaut_rect * (bishop.black_bishop_position[bishop0][1] - key1)

                        bishop.black_bishop_position[bishop0][0] = ch1
                        bishop.black_bishop_position[bishop0][1] = key1
                        pawn.pieces_move.append(bishop0 + bishop.black_bishop_position[bishop0][0] + str(bishop.black_bishop_position[bishop0][1]))
                        print(pawn.pieces_move)
                        break

                    ch1 = chr(ord(ch1) - 1)
                    key1 -= 1

                if (bishop.black_big_bishop_rects[bishop0].collidepoint(bishop.black_bishop_rects[bishop0].x - (
                        bishop.defaut_rect * (ord(bishop.black_bishop_position[bishop0][0]) - ord(ch1))),
                        bishop.black_bishop_rects[bishop0].y + (bishop.defaut_rect * (
                        bishop.black_bishop_position[bishop0][1] - key1)))):

                    aux2 = bishop.black_bishop_position[bishop0][0]
                    aux3 = bishop.black_bishop_position[bishop0][1]
                    bishop.black_bishop_position[bishop0][0] = ch1
                    bishop.black_bishop_position[bishop0][1] = key1

                    if verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position, rook.white_rook_position,
                                           bishop.white_bishop_position, queen.white_queen_position, pawn.white_pawn_death,
                                           knight.white_knight_death, rook.white_rook_death, bishop.white_bishop_death,
                                           queen.white_queen_death, bishop.black_bishop_position[bishop0], 0, 0):

                        stats.black_turn = False
                        stats.white_turn = True

                        background.board_move[aux2][str(aux3)] = False
                        background.board_move[bishop.black_bishop_position[bishop0][0]][str(bishop.black_bishop_position[bishop0][1])] = True

                        bishop.black_bishop_rects[bishop0].x -= bishop.defaut_rect * (ord(aux2) - ord(ch1))
                        bishop.black_bishop_rects[bishop0].y += bishop.defaut_rect * (aux3 - key1)

                        queen.white_queen_death = eliminate_killed_piece(bishop0, bishop.black_bishop_position[bishop0], pawn.white_pawn_position,
                                               knight.white_knight_position, bishop.white_bishop_position,
                                               rook.white_rook_position, queen.white_queen_position,
                                               pawn.white_pawn_death, knight.white_knight_death,
                                               bishop.white_bishop_death,
                                               rook.white_rook_death, queen.white_queen_death,
                                               pawn.white_pawn_rects, knight.white_knight_rects,
                                               bishop.white_bishop_rects,
                                               rook.white_rook_rects, queen.white_queen_rect,
                                               pawn, knight, bishop, rook, queen)

                    else:
                        bishop.black_bishop_position[bishop0][0] = aux2
                        bishop.black_bishop_position[bishop0][1] = aux3

            ch2 = chr(ord(bishop.black_bishop_position[bishop0][0]) - 1)
            key2 = bishop.black_bishop_position[bishop0][1] + 1
            if (bishop.black_bishop_position[bishop0][0] > 'a') and (bishop.black_bishop_position[bishop0][1] < 8):
                while (ch2 >= "a") and (key2 <= 8) and (not background.board_move[ch2][str(key2)]):

                    if (bishop.black_big_bishop_rects[bishop0].collidepoint(bishop.black_bishop_rects[bishop0].x - (
                        bishop.defaut_rect * (ord(bishop.black_bishop_position[bishop0][0]) - ord(ch2))),
                        bishop.black_bishop_rects[bishop0].y - (
                        bishop.defaut_rect * (key2 - bishop.black_bishop_position[bishop0][1])))):

                        stats.black_turn = False
                        stats.white_turn = True

                        background.board_move[bishop.black_bishop_position[bishop0][0]][str(bishop.black_bishop_position[bishop0][1])] = False
                        background.board_move[ch2][str(key2)] = True

                        bishop.black_bishop_rects[bishop0].x -= bishop.defaut_rect * (ord(bishop.black_bishop_position[bishop0][0]) - ord(ch2))
                        bishop.black_bishop_rects[bishop0].y -= bishop.defaut_rect * (key2 - bishop.black_bishop_position[bishop0][1])

                        bishop.black_bishop_position[bishop0][0] = ch2
                        bishop.black_bishop_position[bishop0][1] = key2
                        pawn.pieces_move.append(bishop0 + bishop.black_bishop_position[bishop0][0] + str(bishop.black_bishop_position[bishop0][1]))
                        print(pawn.pieces_move)
                        break

                    ch2 = chr(ord(ch2) - 1)
                    key2 += 1

                if (bishop.black_big_bishop_rects[bishop0].collidepoint(bishop.black_bishop_rects[bishop0].x - (
                        bishop.defaut_rect * (ord(bishop.black_bishop_position[bishop0][0]) - ord(ch2))),
                        bishop.black_bishop_rects[bishop0].y - (bishop.defaut_rect * (key2 -
                        bishop.black_bishop_position[bishop0][1])))):

                    aux4 = bishop.black_bishop_position[bishop0][0]
                    aux5 = bishop.black_bishop_position[bishop0][1]
                    bishop.black_bishop_position[bishop0][0] = ch2
                    bishop.black_bishop_position[bishop0][1] = key2

                    if verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position, rook.white_rook_position,
                                           bishop.white_bishop_position, queen.white_queen_position, pawn.white_pawn_death,
                                           knight.white_knight_death, rook.white_rook_death, bishop.white_bishop_death,
                                           queen.white_queen_death, bishop.black_bishop_position[bishop0], 0, 0):

                        stats.black_turn = False
                        stats.white_turn = True

                        background.board_move[aux4][str(aux5)] = False
                        background.board_move[bishop.black_bishop_position[bishop0][0]][str(bishop.black_bishop_position[bishop0][1])] = True

                        bishop.black_bishop_rects[bishop0].x -= bishop.defaut_rect * (ord(aux4) - ord(ch2))
                        bishop.black_bishop_rects[bishop0].y -= bishop.defaut_rect * (key2 - aux5)

                        queen.white_queen_death = eliminate_killed_piece(bishop0, bishop.black_bishop_position[bishop0], pawn.white_pawn_position,
                                               knight.white_knight_position, bishop.white_bishop_position,
                                               rook.white_rook_position, queen.white_queen_position,
                                               pawn.white_pawn_death, knight.white_knight_death,
                                               bishop.white_bishop_death,
                                               rook.white_rook_death, queen.white_queen_death,
                                               pawn.white_pawn_rects, knight.white_knight_rects,
                                               bishop.white_bishop_rects,
                                               rook.white_rook_rects, queen.white_queen_rect,
                                               pawn, knight, bishop, rook, queen)

                    else:
                        bishop.black_bishop_position[bishop0][0] = aux4
                        bishop.black_bishop_position[bishop0][1] = aux5

            ch3 = chr(ord(bishop.black_bishop_position[bishop0][0]) + 1)
            key3 = bishop.black_bishop_position[bishop0][1] - 1
            if (bishop.black_bishop_position[bishop0][0] < 'h') and (bishop.black_bishop_position[bishop0][1] > 1):
                while (ch3 <= "h") and (key3 >= 1) and (not background.board_move[ch3][str(key3)]):

                    if (bishop.black_big_bishop_rects[bishop0].collidepoint(bishop.black_bishop_rects[bishop0].x + (
                        bishop.defaut_rect * (ord(ch3) - ord(bishop.black_bishop_position[bishop0][0]))),
                        bishop.black_bishop_rects[bishop0].y + (
                        bishop.defaut_rect * (bishop.black_bishop_position[bishop0][1] - key3)))):

                        stats.black_turn = False
                        stats.white_turn = True

                        background.board_move[bishop.black_bishop_position[bishop0][0]][str(bishop.black_bishop_position[bishop0][1])] = False
                        background.board_move[ch3][str(key3)] = True

                        bishop.black_bishop_rects[bishop0].x += bishop.defaut_rect * (ord(ch3) - ord(bishop.black_bishop_position[bishop0][0]))
                        bishop.black_bishop_rects[bishop0].y += bishop.defaut_rect * (bishop.black_bishop_position[bishop0][1] - key3)

                        bishop.black_bishop_position[bishop0][0] = ch3
                        bishop.black_bishop_position[bishop0][1] = key3
                        pawn.pieces_move.append(bishop0 + bishop.black_bishop_position[bishop0][0] + str(bishop.black_bishop_position[bishop0][1]))
                        print(pawn.pieces_move)
                        break

                    ch3 = chr(ord(ch3) + 1)
                    key3 -= 1

                if (bishop.black_big_bishop_rects[bishop0].collidepoint(bishop.black_bishop_rects[bishop0].x + (
                    bishop.defaut_rect * (ord(ch3) - ord(bishop.black_bishop_position[bishop0][0]))),
                    bishop.black_bishop_rects[bishop0].y + (bishop.defaut_rect * (bishop.black_bishop_position[bishop0][1] - key3)))):

                    aux6 = bishop.black_bishop_position[bishop0][0]
                    aux7 = bishop.black_bishop_position[bishop0][1]
                    bishop.black_bishop_position[bishop0][0] = ch3
                    bishop.black_bishop_position[bishop0][1] = key3

                    if verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position, rook.white_rook_position,
                                           bishop.white_bishop_position, queen.white_queen_position, pawn.white_pawn_death,
                                           knight.white_knight_death, rook.white_rook_death, bishop.white_bishop_death,
                                           queen.white_queen_death, bishop.black_bishop_position[bishop0], 0, 0):

                        stats.black_turn = False
                        stats.white_turn = True

                        background.board_move[aux6][str(aux7)] = False
                        background.board_move[bishop.black_bishop_position[bishop0][0]][str(bishop.black_bishop_position[bishop0][1])] = True

                        bishop.black_bishop_rects[bishop0].x += bishop.defaut_rect * (ord(ch3) - ord(aux6))
                        bishop.black_bishop_rects[bishop0].y += bishop.defaut_rect * (aux7 - key3)

                        queen.white_queen_death = eliminate_killed_piece(bishop0, bishop.black_bishop_position[bishop0], pawn.white_pawn_position,
                                               knight.white_knight_position, bishop.white_bishop_position,
                                               rook.white_rook_position, queen.white_queen_position,
                                               pawn.white_pawn_death, knight.white_knight_death,
                                               bishop.white_bishop_death,
                                               rook.white_rook_death, queen.white_queen_death,
                                               pawn.white_pawn_rects, knight.white_knight_rects,
                                               bishop.white_bishop_rects,
                                               rook.white_rook_rects, queen.white_queen_rect,
                                               pawn, knight, bishop, rook, queen)

                    else:
                        bishop.black_bishop_position[bishop0][0] = aux6
                        bishop.black_bishop_position[bishop0][1] = aux7

def update_white_queen(stats, background, rook, pawn, knight, bishop, queen):

    if not queen.white_queen_clicked:

        key0 = queen.white_queen_position[1] + 1
        ch0 = chr(ord(queen.white_queen_position[0]) + 1)

        key1 = queen.white_queen_position[1] - 1
        ch1 = chr(ord(queen.white_queen_position[0]) - 1)

        if (queen.white_queen_position[0]) < 'h' and (queen.white_queen_position[1] < 8):
            while (ch0 <= "h") and (key0 <= 8) and (not background.board_move[ch0][str(key0)]):

                if (queen.white_big_queen_rect.collidepoint(queen.white_queen_rect.x + (
                    queen.defaut_rect * (ord(ch0) - ord(queen.white_queen_position[0]))),
                    queen.white_queen_rect.y - (queen.defaut_rect * (key0 - queen.white_queen_position[1])))):

                    stats.white_turn = False
                    stats.black_turn = True

                    background.board_move[queen.white_queen_position[0]][str(queen.white_queen_position[1])] = False
                    background.board_move[ch0][str(key0)] = True

                    queen.white_queen_rect.x += queen.defaut_rect * (ord(ch0) - ord(queen.white_queen_position[0]))
                    queen.white_queen_rect.y -= queen.defaut_rect * (key0 - queen.white_queen_position[1])

                    queen.white_queen_position[0] = ch0
                    queen.white_queen_position[1] = key0
                    pawn.pieces_move.append('Q' + queen.white_queen_position[0] + str(queen.white_queen_position[1]))
                    print(pawn.pieces_move)
                    break

                ch0 = chr(ord(ch0) + 1)
                key0 += 1

            if (queen.white_big_queen_rect.collidepoint(queen.white_queen_rect.x + (
                    queen.defaut_rect * (ord(ch0) - ord(queen.white_queen_position[0]))),
                    queen.white_queen_rect.y - (queen.defaut_rect * (key0 - queen.white_queen_position[1])))):

                aux0 = queen.white_queen_position[0]
                aux1 = queen.white_queen_position[1]
                queen.white_queen_position[0] = ch0
                queen.white_queen_position[1] = key0

                if verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position, rook.black_rook_position,
                                            bishop.black_bishop_position, queen.black_queen_position, pawn.black_pawn_death,
                                            knight.black_knight_death, rook.black_rook_death, bishop.black_bishop_death,
                                            queen.black_queen_death, queen.white_queen_position, 0, 0):

                    stats.white_turn = False
                    stats.black_turn = True

                    background.board_move[aux0][str(aux1)] = False
                    background.board_move[queen.white_queen_position[0]][str(queen.white_queen_position[1])] = True

                    queen.white_queen_rect.x += queen.defaut_rect * (ord(ch0) - ord(aux0))
                    queen.white_queen_rect.y -= queen.defaut_rect * (key0 - aux1)

                    queen.black_queen_death = eliminate_killed_piece("Q", queen.white_queen_position, pawn.black_pawn_position,
                                           knight.black_knight_position, bishop.black_bishop_position,
                                           rook.black_rook_position, queen.black_queen_position,
                                           pawn.black_pawn_death, knight.black_knight_death, bishop.black_bishop_death,
                                           rook.black_rook_death, queen.black_queen_death,
                                           pawn.black_pawn_rects, knight.black_knight_rects, bishop.black_bishop_rects,
                                           rook.black_rook_rects, queen.black_queen_rect,
                                           pawn, knight, bishop, rook, queen)

                else:
                    queen.white_queen_position[0] = aux0
                    queen.white_queen_position[1] = aux1

        if (queen.white_queen_position[0] > 'a') and (queen.white_queen_position[1] > 1):
            while (ch1 >= "a") and (key1 >= 1) and (not background.board_move[ch1][str(key1)]):

                if (queen.white_big_queen_rect.collidepoint(queen.white_queen_rect.x - (
                        queen.defaut_rect * (ord(queen.white_queen_position[0]) - ord(ch1))),
                        queen.white_queen_rect.y + (queen.defaut_rect * (queen.white_queen_position[1] - key1)))):

                    stats.white_turn = False
                    stats.black_turn = True

                    background.board_move[queen.white_queen_position[0]][str(queen.white_queen_position[1])] = False
                    background.board_move[ch1][str(key1)] = True

                    queen.white_queen_rect.x -= queen.defaut_rect * (ord(queen.white_queen_position[0]) - ord(ch1))
                    queen.white_queen_rect.y += queen.defaut_rect * (queen.white_queen_position[1] - key1)

                    queen.white_queen_position[0] = ch1
                    queen.white_queen_position[1] = key1
                    pawn.pieces_move.append("Q" + queen.white_queen_position[0] + str(queen.white_queen_position[1]))
                    print(pawn.pieces_move)
                    break

                ch1 = chr(ord(ch1) - 1)
                key1 -= 1

            if (queen.white_big_queen_rect.collidepoint(queen.white_queen_rect.x - (
                    queen.defaut_rect * (ord(queen.white_queen_position[0]) - ord(ch1))),
                    queen.white_queen_rect.y + (queen.defaut_rect * (queen.white_queen_position[1] - key1)))):

                aux2 = queen.white_queen_position[0]
                aux3 = queen.white_queen_position[1]
                queen.white_queen_position[0] = ch1
                queen.white_queen_position[1] = key1

                if verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position, rook.black_rook_position,
                                            bishop.black_bishop_position, queen.black_queen_position, pawn.black_pawn_death,
                                            knight.black_knight_death, rook.black_rook_death, bishop.black_bishop_death,
                                            queen.black_queen_death, queen.white_queen_position, 0, 0):

                    stats.white_turn = False
                    stats.black_turn = True

                    background.board_move[aux2][str(aux3)] = False
                    background.board_move[queen.white_queen_position[0]][str(queen.white_queen_position[1])] = True

                    queen.white_queen_rect.x -= queen.defaut_rect * (ord(aux2) - ord(ch1))
                    queen.white_queen_rect.y += queen.defaut_rect * (aux3 - key1)

                    queen.black_queen_death = eliminate_killed_piece("Q", queen.white_queen_position, pawn.black_pawn_position,
                                           knight.black_knight_position, bishop.black_bishop_position,
                                           rook.black_rook_position, queen.black_queen_position,
                                           pawn.black_pawn_death, knight.black_knight_death, bishop.black_bishop_death,
                                           rook.black_rook_death, queen.black_queen_death,
                                           pawn.black_pawn_rects, knight.black_knight_rects, bishop.black_bishop_rects,
                                           rook.black_rook_rects, queen.black_queen_rect,
                                           pawn, knight, bishop, rook, queen)

                else:
                    queen.white_queen_position[0] = aux2
                    queen.white_queen_position[1] = aux3

        ch2 = chr(ord(queen.white_queen_position[0]) - 1)
        key2 = queen.white_queen_position[1] + 1
        if (queen.white_queen_position[0] > 'a') and (queen.white_queen_position[1] < 8):
            while (ch2 >= "a") and (key2 <= 8) and (not background.board_move[ch2][str(key2)]):

                if (queen.white_big_queen_rect.collidepoint(queen.white_queen_rect.x - (
                        queen.defaut_rect * (ord(queen.white_queen_position[0]) - ord(ch2))),
                        queen.white_queen_rect.y - (queen.defaut_rect * (key2 - queen.white_queen_position[1])))):

                    stats.white_turn = False
                    stats.black_turn = True

                    background.board_move[queen.white_queen_position[0]][str(queen.white_queen_position[1])] = False
                    background.board_move[ch2][str(key2)] = True

                    queen.white_queen_rect.x -= queen.defaut_rect * (ord(queen.white_queen_position[0]) - ord(ch2))
                    queen.white_queen_rect.y -= queen.defaut_rect * (key2 - queen.white_queen_position[1])

                    queen.white_queen_position[0] = ch2
                    queen.white_queen_position[1] = key2
                    pawn.pieces_move.append("Q" + queen.white_queen_position[0] + str(queen.white_queen_position[1]))
                    print(pawn.pieces_move)
                    break

                ch2 = chr(ord(ch2) - 1)
                key2 += 1

            if (queen.white_big_queen_rect.collidepoint(queen.white_queen_rect.x - (
                    queen.defaut_rect * (ord(queen.white_queen_position[0]) - ord(ch2))),
                    queen.white_queen_rect.y - (queen.defaut_rect * (key2 - queen.white_queen_position[1])))):

                aux4 = queen.white_queen_position[0]
                aux5 = queen.white_queen_position[1]
                queen.white_queen_position[0] = ch2
                queen.white_queen_position[1] = key2
                if verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position, rook.black_rook_position,
                                            bishop.black_bishop_position, queen.black_queen_position, pawn.black_pawn_death,
                                            knight.black_knight_death, rook.black_rook_death, bishop.black_bishop_death,
                                            queen.black_queen_death, queen.white_queen_position, 0, 0):

                    stats.white_turn = False
                    stats.black_turn = True

                    background.board_move[aux4][str(aux5)] = False
                    background.board_move[queen.white_queen_position[0]][str(queen.white_queen_position[1])] = True

                    queen.white_queen_rect.x -= queen.defaut_rect * (ord(aux4) - ord(ch2))
                    queen.white_queen_rect.y -= queen.defaut_rect * (key2 - aux5)

                    queen.black_queen_death = eliminate_killed_piece("Q", queen.white_queen_position, pawn.black_pawn_position,
                                           knight.black_knight_position, bishop.black_bishop_position,
                                           rook.black_rook_position, queen.black_queen_position,
                                           pawn.black_pawn_death, knight.black_knight_death, bishop.black_bishop_death,
                                           rook.black_rook_death, queen.black_queen_death,
                                           pawn.black_pawn_rects, knight.black_knight_rects, bishop.black_bishop_rects,
                                           rook.black_rook_rects, queen.black_queen_rect,
                                           pawn, knight, bishop, rook, queen)

                else:
                    queen.white_queen_position[0] = aux4
                    queen.white_queen_position[1] = aux5

        ch3 = chr(ord(queen.white_queen_position[0]) + 1)
        key3 = queen.white_queen_position[1] - 1
        if (queen.white_queen_position[0] < 'h') and (queen.white_queen_position[1] > 1):
            while (ch3 <= "h") and (key3 >= 1) and (not background.board_move[ch3][str(key3)]):

                if (queen.white_big_queen_rect.collidepoint(queen.white_queen_rect.x + (
                        queen.defaut_rect * (ord(ch3) - ord(queen.white_queen_position[0]))),
                        queen.white_queen_rect.y + (queen.defaut_rect * (queen.white_queen_position[1] - key3)))):

                    stats.white_turn = False
                    stats.black_turn = True

                    background.board_move[queen.white_queen_position[0]][str(queen.white_queen_position[1])] = False
                    background.board_move[ch3][str(key3)] = True

                    queen.white_queen_rect.x += queen.defaut_rect * (ord(ch3) - ord(queen.white_queen_position[0]))
                    queen.white_queen_rect.y += queen.defaut_rect * (queen.white_queen_position[1] - key3)

                    queen.white_queen_position[0] = ch3
                    queen.white_queen_position[1] = key3
                    pawn.pieces_move.append("Q" + queen.white_queen_position[0] + str(queen.white_queen_position[1]))
                    print(pawn.pieces_move)
                    break

                ch3 = chr(ord(ch3) + 1)
                key3 -= 1

            if (queen.white_big_queen_rect.collidepoint(queen.white_queen_rect.x + (
                    queen.defaut_rect * (ord(ch3) - ord(queen.white_queen_position[0]))),
                    queen.white_queen_rect.y + (queen.defaut_rect * (queen.white_queen_position[1] - key3)))):

                aux6 = queen.white_queen_position[0]
                aux7 = queen.white_queen_position[1]
                queen.white_queen_position[0] = ch3
                queen.white_queen_position[1] = key3
                if verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position, rook.black_rook_position,
                                            bishop.black_bishop_position, queen.black_queen_position, pawn.black_pawn_death,
                                            knight.black_knight_death, rook.black_rook_death, bishop.black_bishop_death,
                                            queen.black_queen_death, queen.white_queen_position, 0, 0):

                    stats.white_turn = False
                    stats.black_turn = True

                    background.board_move[aux6][str(aux7)] = False
                    background.board_move[queen.white_queen_position[0]][str(queen.white_queen_position[1])] = True

                    queen.white_queen_rect.x += queen.defaut_rect * (ord(ch3) - ord(aux6))
                    queen.white_queen_rect.y += queen.defaut_rect * (aux7 - key3)

                    queen.black_queen_death = eliminate_killed_piece("Q", queen.white_queen_position, pawn.black_pawn_position,
                                           knight.black_knight_position, bishop.black_bishop_position,
                                           rook.black_rook_position, queen.black_queen_position,
                                           pawn.black_pawn_death, knight.black_knight_death, bishop.black_bishop_death,
                                           rook.black_rook_death, queen.black_queen_death,
                                           pawn.black_pawn_rects, knight.black_knight_rects, bishop.black_bishop_rects,
                                           rook.black_rook_rects, queen.black_queen_rect,
                                           pawn, knight, bishop, rook, queen)

                else:
                    queen.white_queen_position[0] = aux6
                    queen.white_queen_position[1] = aux7

        key4 = queen.white_queen_position[1] + 1
        key5 = queen.white_queen_position[1] - 1
        ch4 = chr(ord(queen.white_queen_position[0]) + 1)
        ch5 = chr(ord(queen.white_queen_position[0]) - 1)
        if queen.white_queen_position[0] < 'h':
            while (ch4 <= "h") and (
                    not background.board_move[ch4][str(queen.white_queen_position[1])]):

                if (queen.white_big_queen_rect.collidepoint(queen.white_queen_rect.x + (
                    queen.defaut_rect * (ord(ch4) - ord(queen.white_queen_position[0]))), queen.white_queen_rect.y)):

                    stats.white_turn = False
                    stats.black_turn = True

                    background.board_move[queen.white_queen_position[0]][str(queen.white_queen_position[1])] = False
                    background.board_move[ch4][str(queen.white_queen_position[1])] = True

                    queen.white_queen_rect.x += queen.defaut_rect * (ord(ch4) - ord(queen.white_queen_position[0]))

                    queen.white_queen_position[0] = ch4
                    pawn.pieces_move.append(
                        "Q" + queen.white_queen_position[0] + str(queen.white_queen_position[1]))
                    print(pawn.pieces_move)
                    break

                ch4 = chr(ord(ch4) + 1)

            if (queen.white_big_queen_rect.collidepoint(queen.white_queen_rect.x + (
                        queen.defaut_rect * (ord(ch4) - ord(queen.white_queen_position[0]))), queen.white_queen_rect.y)):

                aux8 = queen.white_queen_position[0]
                queen.white_queen_position[0] = ch4

                if verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position, rook.black_rook_position,
                                            bishop.black_bishop_position, queen.black_queen_position, pawn.black_pawn_death,
                                            knight.black_knight_death, rook.black_rook_death, bishop.black_bishop_death,
                                            queen.black_queen_death, queen.white_queen_position, 0, 0):

                    stats.white_turn = False
                    stats.black_turn = True

                    background.board_move[aux8][str(queen.white_queen_position[1])] = False
                    background.board_move[queen.white_queen_position[0]][str(queen.white_queen_position[1])] = True

                    queen.white_queen_rect.x += queen.defaut_rect * (ord(ch4) - ord(aux8))

                    queen.black_queen_death = eliminate_killed_piece("Q", queen.white_queen_position, pawn.black_pawn_position,
                                           knight.black_knight_position, bishop.black_bishop_position,
                                           rook.black_rook_position, queen.black_queen_position,
                                           pawn.black_pawn_death, knight.black_knight_death, bishop.black_bishop_death,
                                           rook.black_rook_death, queen.black_queen_death,
                                           pawn.black_pawn_rects, knight.black_knight_rects, bishop.black_bishop_rects,
                                           rook.black_rook_rects, queen.black_queen_rect,
                                           pawn, knight, bishop, rook, queen)

                else:
                    queen.white_queen_position[0] = aux8

        if queen.white_queen_position[0] > 'a':
            while (ch5 >= 'a') and (not background.board_move[ch5][str(queen.white_queen_position[1])]):

                if (queen.white_big_queen_rect.collidepoint(queen.white_queen_rect.x - (
                        queen.defaut_rect * (ord(queen.white_queen_position[0]) - ord(ch5))),
                                                                   queen.white_queen_rect.y)):
                    stats.white_turn = False
                    stats.black_turn = True

                    background.board_move[queen.white_queen_position[0]][str(queen.white_queen_position[1])] = False
                    background.board_move[ch5][str(queen.white_queen_position[1])] = True

                    queen.white_queen_rect.x -= queen.defaut_rect * (ord(queen.white_queen_position[0]) - ord(ch5))

                    queen.white_queen_position[0] = ch5
                    pawn.pieces_move.append(
                        "Q" + queen.white_queen_position[0] + str(queen.white_queen_position[1]))
                    print(pawn.pieces_move)
                    break
                ch5 = chr(ord(ch5) - 1)

            if (queen.white_big_queen_rect.collidepoint(queen.white_queen_rect.x - (
                    queen.defaut_rect * (ord(queen.white_queen_position[0]) - ord(ch5))),
                                                        queen.white_queen_rect.y)):

                aux9 = queen.white_queen_position[0]
                queen.white_queen_position[0] = ch5

                if verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position, rook.black_rook_position,
                                            bishop.black_bishop_position, queen.black_queen_position, pawn.black_pawn_death,
                                            knight.black_knight_death, rook.black_rook_death, bishop.black_bishop_death,
                                            queen.black_queen_death, queen.white_queen_position, 0, 0):

                    stats.white_turn = False
                    stats.black_turn = True

                    background.board_move[aux9][str(queen.white_queen_position[1])] = False
                    background.board_move[queen.white_queen_position[0]][str(queen.white_queen_position[1])] = True

                    queen.white_queen_rect.x -= queen.defaut_rect * (ord(aux9) - ord(ch5))

                    queen.black_queen_death = eliminate_killed_piece("Q", queen.white_queen_position, pawn.black_pawn_position,
                                           knight.black_knight_position, bishop.black_bishop_position,
                                           rook.black_rook_position, queen.black_queen_position,
                                           pawn.black_pawn_death, knight.black_knight_death, bishop.black_bishop_death,
                                           rook.black_rook_death, queen.black_queen_death,
                                           pawn.black_pawn_rects, knight.black_knight_rects, bishop.black_bishop_rects,
                                           rook.black_rook_rects, queen.black_queen_rect,
                                           pawn, knight, bishop, rook, queen)

                else:
                    queen.white_queen_position[0] = aux9

        if queen.white_queen_position[1] < 8:
            while (key4 <= 8) and (not background.board_move[queen.white_queen_position[0]][str(key4)]):

                if (queen.white_big_queen_rect.collidepoint(queen.white_queen_rect.x,
                     queen.white_queen_rect.y - (queen.defaut_rect * (key4 - queen.white_queen_position[1])))):

                    stats.white_turn = False
                    stats.black_turn = True

                    background.board_move[queen.white_queen_position[0]][str(queen.white_queen_position[1])] = False
                    background.board_move[queen.white_queen_position[0]][str(key4)] = True

                    queen.white_queen_rect.y -= queen.defaut_rect * (key4 - queen.white_queen_position[1])

                    queen.white_queen_position[1] = key4
                    pawn.pieces_move.append(
                        "Q" + queen.white_queen_position[0] + str(queen.white_queen_position[1]))
                    print(pawn.pieces_move)
                    break
                key4 += 1

            if (queen.white_big_queen_rect.collidepoint(queen.white_queen_rect.x,
                                                        queen.white_queen_rect.y - (queen.defaut_rect * (
                                                                key4 - queen.white_queen_position[1])))):

                aux10 = queen.white_queen_position[1]
                queen.white_queen_position[1] = key4
                if verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position, rook.black_rook_position,
                                            bishop.black_bishop_position, queen.black_queen_position, pawn.black_pawn_death,
                                            knight.black_knight_death, rook.black_rook_death, bishop.black_bishop_death,
                                            queen.black_queen_death, queen.white_queen_position, 0, 0):

                    stats.white_turn = False
                    stats.black_turn = True

                    background.board_move[queen.white_queen_position[0]][str(aux10)] = False
                    background.board_move[queen.white_queen_position[0]][str(queen.white_queen_position[1])] = True

                    queen.white_queen_rect.y -= queen.defaut_rect * (key4 - aux10)

                    queen.black_queen_death = eliminate_killed_piece("Q", queen.white_queen_position, pawn.black_pawn_position,
                                           knight.black_knight_position, bishop.black_bishop_position,
                                           rook.black_rook_position, queen.black_queen_position,
                                           pawn.black_pawn_death, knight.black_knight_death, bishop.black_bishop_death,
                                           rook.black_rook_death, queen.black_queen_death,
                                           pawn.black_pawn_rects, knight.black_knight_rects, bishop.black_bishop_rects,
                                           rook.black_rook_rects, queen.black_queen_rect,
                                           pawn, knight, bishop, rook, queen)

                else:
                    queen.white_queen_position[1] = aux10

        if queen.white_queen_position[1] > 1:
            while (key5 >= 1) and (not background.board_move[queen.white_queen_position[0]][str(key5)]):

                if (queen.white_big_queen_rect.collidepoint(queen.white_queen_rect.x,
                    queen.white_queen_rect.y + (queen.defaut_rect * (queen.white_queen_position[1] - key5)))):

                    stats.white_turn = False
                    stats.black_turn = True

                    background.board_move[queen.white_queen_position[0]][str(queen.white_queen_position[1])] = False
                    background.board_move[queen.white_queen_position[0]][str(key5)] = True

                    queen.white_queen_rect.y += queen.defaut_rect * (queen.white_queen_position[1] - key5)

                    queen.white_queen_position[1] = key5
                    pawn.pieces_move.append(
                        "Q" + queen.white_queen_position[0] + str(queen.white_queen_position[1]))
                    print(pawn.pieces_move)
                    break
                key5 -= 1

            if (queen.white_big_queen_rect.collidepoint(queen.white_queen_rect.x,
                queen.white_queen_rect.y + (queen.defaut_rect * (queen.white_queen_position[1] - key5)))):

                aux11 = queen.white_queen_position[1]
                queen.white_queen_position[1] = key5
                if verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position, rook.black_rook_position,
                                            bishop.black_bishop_position, queen.black_queen_position, pawn.black_pawn_death,
                                            knight.black_knight_death, rook.black_rook_death, bishop.black_bishop_death,
                                            queen.black_queen_death, queen.white_queen_position, 0, 0):

                    stats.white_turn = False
                    stats.black_turn = True

                    background.board_move[queen.white_queen_position[0]][str(aux11)] = False
                    background.board_move[queen.white_queen_position[0]][str(queen.white_queen_position[1])] = True

                    queen.white_queen_rect.y += queen.defaut_rect * (aux11 - key5)

                    queen.black_queen_death = eliminate_killed_piece("Q", queen.white_queen_position, pawn.black_pawn_position,
                                           knight.black_knight_position, bishop.black_bishop_position,
                                           rook.black_rook_position, queen.black_queen_position,
                                           pawn.black_pawn_death, knight.black_knight_death, bishop.black_bishop_death,
                                           rook.black_rook_death, queen.black_queen_death,
                                           pawn.black_pawn_rects, knight.black_knight_rects, bishop.black_bishop_rects,
                                           rook.black_rook_rects, queen.black_queen_rect,
                                           pawn, knight, bishop, rook, queen)

                else:
                    queen.white_queen_position[1] = aux11

def update_black_queen(stats, background, rook, pawn, knight, bishop, queen):

    if not queen.black_queen_clicked:

        key0 = queen.black_queen_position[1] + 1
        ch0 = chr(ord(queen.black_queen_position[0]) + 1)

        key1 = queen.black_queen_position[1] - 1
        ch1 = chr(ord(queen.black_queen_position[0]) - 1)

        if (queen.black_queen_position[0]) < 'h' and (queen.black_queen_position[1] < 8):
            while (ch0 <= "h") and (key0 <= 8) and (not background.board_move[ch0][str(key0)]):

                if (queen.black_big_queen_rect.collidepoint(queen.black_queen_rect.x + (
                    queen.defaut_rect * (ord(ch0) - ord(queen.black_queen_position[0]))),
                    queen.black_queen_rect.y - (queen.defaut_rect * (key0 - queen.black_queen_position[1])))):

                    stats.black_turn = False
                    stats.white_turn = True

                    background.board_move[queen.black_queen_position[0]][str(queen.black_queen_position[1])] = False
                    background.board_move[ch0][str(key0)] = True

                    queen.black_queen_rect.x += queen.defaut_rect * (ord(ch0) - ord(queen.black_queen_position[0]))
                    queen.black_queen_rect.y -= queen.defaut_rect * (key0 - queen.black_queen_position[1])

                    queen.black_queen_position[0] = ch0
                    queen.black_queen_position[1] = key0
                    pawn.pieces_move.append('Q' + queen.black_queen_position[0] + str(queen.black_queen_position[1]))
                    print(pawn.pieces_move)
                    break

                ch0 = chr(ord(ch0) + 1)
                key0 += 1

            if (queen.black_big_queen_rect.collidepoint(queen.black_queen_rect.x + (
                    queen.defaut_rect * (ord(ch0) - ord(queen.black_queen_position[0]))),
                    queen.black_queen_rect.y - (queen.defaut_rect * (key0 - queen.black_queen_position[1])))):

                aux0 = queen.black_queen_position[0]
                aux1 = queen.black_queen_position[1]
                queen.black_queen_position[0] = ch0
                queen.black_queen_position[1] = key0

                if verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position, rook.white_rook_position,
                                           bishop.white_bishop_position, queen.white_queen_position, pawn.white_pawn_death,
                                           knight.white_knight_death, rook.white_rook_death, bishop.white_bishop_death,
                                           queen.white_queen_death, queen.black_queen_position, 0, 0):

                    stats.black_turn = False
                    stats.white_turn = True

                    background.board_move[aux0][str(aux1)] = False
                    background.board_move[queen.black_queen_position[0]][str(queen.black_queen_position[1])] = True

                    queen.black_queen_rect.x += queen.defaut_rect * (ord(ch0) - ord(aux0))
                    queen.black_queen_rect.y -= queen.defaut_rect * (key0 - aux1)

                    queen.white_queen_death = eliminate_killed_piece("Q", queen.black_queen_position, pawn.white_pawn_position,
                                           knight.white_knight_position, bishop.white_bishop_position,
                                           rook.white_rook_position, queen.white_queen_position,
                                           pawn.white_pawn_death, knight.white_knight_death, bishop.white_bishop_death,
                                           rook.white_rook_death, queen.white_queen_death,
                                           pawn.white_pawn_rects, knight.white_knight_rects, bishop.white_bishop_rects,
                                           rook.white_rook_rects, queen.white_queen_rect,
                                           pawn, knight, bishop, rook, queen)

                else:
                    queen.black_queen_position[0] = aux0
                    queen.black_queen_position[1] = aux1

        if (queen.black_queen_position[0] > 'a') and (queen.black_queen_position[1] > 1):
            while (ch1 >= "a") and (key1 >= 1) and (not background.board_move[ch1][str(key1)]):

                if (queen.black_big_queen_rect.collidepoint(queen.black_queen_rect.x - (
                        queen.defaut_rect * (ord(queen.black_queen_position[0]) - ord(ch1))),
                        queen.black_queen_rect.y + (queen.defaut_rect * (queen.black_queen_position[1] - key1)))):

                    stats.black_turn = False
                    stats.white_turn = True

                    background.board_move[queen.black_queen_position[0]][str(queen.black_queen_position[1])] = False
                    background.board_move[ch1][str(key1)] = True

                    queen.black_queen_rect.x -= queen.defaut_rect * (ord(queen.black_queen_position[0]) - ord(ch1))
                    queen.black_queen_rect.y += queen.defaut_rect * (queen.black_queen_position[1] - key1)

                    queen.black_queen_position[0] = ch1
                    queen.black_queen_position[1] = key1
                    pawn.pieces_move.append("Q" + queen.black_queen_position[0] + str(queen.black_queen_position[1]))
                    print(pawn.pieces_move)
                    break

                ch1 = chr(ord(ch1) - 1)
                key1 -= 1

            if (queen.black_big_queen_rect.collidepoint(queen.black_queen_rect.x - (
                    queen.defaut_rect * (ord(queen.black_queen_position[0]) - ord(ch1))),
                    queen.black_queen_rect.y + (queen.defaut_rect * (queen.black_queen_position[1] - key1)))):

                aux2 = queen.black_queen_position[0]
                aux3 = queen.black_queen_position[1]
                queen.black_queen_position[0] = ch1
                queen.black_queen_position[1] = key1

                if verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position, rook.white_rook_position,
                                           bishop.white_bishop_position, queen.white_queen_position, pawn.white_pawn_death,
                                           knight.white_knight_death, rook.white_rook_death, bishop.white_bishop_death,
                                           queen.white_queen_death, queen.black_queen_position, 0, 0):

                    stats.black_turn = False
                    stats.white_turn = True

                    background.board_move[aux2][str(aux3)] = False
                    background.board_move[queen.black_queen_position[0]][str(queen.black_queen_position[1])] = True

                    queen.black_queen_rect.x -= queen.defaut_rect * (ord(aux2) - ord(ch1))
                    queen.black_queen_rect.y += queen.defaut_rect * (aux3 - key1)

                    queen.white_queen_death = eliminate_killed_piece("Q", queen.black_queen_position, pawn.white_pawn_position,
                                           knight.white_knight_position, bishop.white_bishop_position,
                                           rook.white_rook_position, queen.white_queen_position,
                                           pawn.white_pawn_death, knight.white_knight_death, bishop.white_bishop_death,
                                           rook.white_rook_death, queen.white_queen_death,
                                           pawn.white_pawn_rects, knight.white_knight_rects, bishop.white_bishop_rects,
                                           rook.white_rook_rects, queen.white_queen_rect,
                                           pawn, knight, bishop, rook, queen)

                else:
                    queen.black_queen_position[0] = aux2
                    queen.black_queen_position[1] = aux3

        ch2 = chr(ord(queen.black_queen_position[0]) - 1)
        key2 = queen.black_queen_position[1] + 1
        if (queen.black_queen_position[0] > 'a') and (queen.black_queen_position[1] < 8):
            while (ch2 >= "a") and (key2 <= 8) and (not background.board_move[ch2][str(key2)]):

                if (queen.black_big_queen_rect.collidepoint(queen.black_queen_rect.x - (
                        queen.defaut_rect * (ord(queen.black_queen_position[0]) - ord(ch2))),
                        queen.black_queen_rect.y - (queen.defaut_rect * (key2 - queen.black_queen_position[1])))):

                    stats.black_turn = False
                    stats.white_turn = True

                    background.board_move[queen.black_queen_position[0]][str(queen.black_queen_position[1])] = False
                    background.board_move[ch2][str(key2)] = True

                    queen.black_queen_rect.x -= queen.defaut_rect * (ord(queen.black_queen_position[0]) - ord(ch2))
                    queen.black_queen_rect.y -= queen.defaut_rect * (key2 - queen.black_queen_position[1])

                    queen.black_queen_position[0] = ch2
                    queen.black_queen_position[1] = key2
                    pawn.pieces_move.append("Q" + queen.black_queen_position[0] + str(queen.black_queen_position[1]))
                    print(pawn.pieces_move)
                    break

                ch2 = chr(ord(ch2) - 1)
                key2 += 1

            if (queen.black_big_queen_rect.collidepoint(queen.black_queen_rect.x - (
                    queen.defaut_rect * (ord(queen.black_queen_position[0]) - ord(ch2))),
                    queen.black_queen_rect.y - (queen.defaut_rect * (key2 - queen.black_queen_position[1])))):

                aux4 = queen.black_queen_position[0]
                aux5 = queen.black_queen_position[1]
                queen.black_queen_position[0] = ch2
                queen.black_queen_position[1] = key2

                if verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position, rook.white_rook_position,
                                           bishop.white_bishop_position, queen.white_queen_position, pawn.white_pawn_death,
                                           knight.white_knight_death, rook.white_rook_death, bishop.white_bishop_death,
                                           queen.white_queen_death, queen.black_queen_position, 0, 0):

                    stats.black_turn = False
                    stats.white_turn = True

                    background.board_move[aux4][str(aux5)] = False
                    background.board_move[queen.black_queen_position[0]][str(queen.black_queen_position[1])] = True

                    queen.black_queen_rect.x -= queen.defaut_rect * (ord(aux4) - ord(ch2))
                    queen.black_queen_rect.y -= queen.defaut_rect * (key2 - aux5)

                    queen.white_queen_death = eliminate_killed_piece("Q", queen.black_queen_position, pawn.white_pawn_position,
                                           knight.white_knight_position, bishop.white_bishop_position,
                                           rook.white_rook_position, queen.white_queen_position,
                                           pawn.white_pawn_death, knight.white_knight_death, bishop.white_bishop_death,
                                           rook.white_rook_death, queen.white_queen_death,
                                           pawn.white_pawn_rects, knight.white_knight_rects, bishop.white_bishop_rects,
                                           rook.white_rook_rects, queen.white_queen_rect,
                                           pawn, knight, bishop, rook, queen)

                else:
                    queen.black_queen_position[0] = aux4
                    queen.black_queen_position[1] = aux5

        ch3 = chr(ord(queen.black_queen_position[0]) + 1)
        key3 = queen.black_queen_position[1] - 1
        if (queen.black_queen_position[0] < 'h') and (queen.black_queen_position[1] > 1):
            while (ch3 <= "h") and (key3 >= 1) and (not background.board_move[ch3][str(key3)]):

                if (queen.black_big_queen_rect.collidepoint(queen.black_queen_rect.x + (
                        queen.defaut_rect * (ord(ch3) - ord(queen.black_queen_position[0]))),
                        queen.black_queen_rect.y + (queen.defaut_rect * (queen.black_queen_position[1] - key3)))):

                    stats.black_turn = False
                    stats.white_turn = True

                    background.board_move[queen.black_queen_position[0]][str(queen.black_queen_position[1])] = False
                    background.board_move[ch3][str(key3)] = True

                    queen.black_queen_rect.x += queen.defaut_rect * (ord(ch3) - ord(queen.black_queen_position[0]))
                    queen.black_queen_rect.y += queen.defaut_rect * (queen.black_queen_position[1] - key3)

                    queen.black_queen_position[0] = ch3
                    queen.black_queen_position[1] = key3
                    pawn.pieces_move.append("Q" + queen.black_queen_position[0] + str(queen.black_queen_position[1]))
                    print(pawn.pieces_move)
                    break

                ch3 = chr(ord(ch3) + 1)
                key3 -= 1

            if (queen.black_big_queen_rect.collidepoint(queen.black_queen_rect.x + (
                    queen.defaut_rect * (ord(ch3) - ord(queen.black_queen_position[0]))),
                    queen.black_queen_rect.y + (queen.defaut_rect * (queen.black_queen_position[1] - key3)))):

                aux6 = queen.black_queen_position[0]
                aux7 = queen.black_queen_position[1]
                queen.black_queen_position[0] = ch3
                queen.black_queen_position[1] = key3

                if verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position, rook.white_rook_position,
                                           bishop.white_bishop_position, queen.white_queen_position, pawn.white_pawn_death,
                                           knight.white_knight_death, rook.white_rook_death, bishop.white_bishop_death,
                                           queen.white_queen_death, queen.black_queen_position, 0, 0):

                    stats.black_turn = False
                    stats.white_turn = True

                    background.board_move[aux6][str(aux7)] = False
                    background.board_move[queen.black_queen_position[0]][str(queen.black_queen_position[1])] = True

                    queen.black_queen_rect.x += queen.defaut_rect * (ord(ch3) - ord(aux6))
                    queen.black_queen_rect.y += queen.defaut_rect * (aux7 - key3)

                    queen.white_queen_death = eliminate_killed_piece("Q", queen.black_queen_position, pawn.white_pawn_position,
                                           knight.white_knight_position, bishop.white_bishop_position,
                                           rook.white_rook_position, queen.white_queen_position,
                                           pawn.white_pawn_death, knight.white_knight_death, bishop.white_bishop_death,
                                           rook.white_rook_death, queen.white_queen_death,
                                           pawn.white_pawn_rects, knight.white_knight_rects, bishop.white_bishop_rects,
                                           rook.white_rook_rects, queen.white_queen_rect,
                                           pawn, knight, bishop, rook, queen)

                else:
                    queen.black_queen_position[0] = aux6
                    queen.black_queen_position[1] = aux7

        key4 = queen.black_queen_position[1] + 1
        key5 = queen.black_queen_position[1] - 1
        ch4 = chr(ord(queen.black_queen_position[0]) + 1)
        ch5 = chr(ord(queen.black_queen_position[0]) - 1)

        if queen.black_queen_position[0] < 'h':
            while (ch4 <= "h") and (
                    not background.board_move[ch4][str(queen.black_queen_position[1])]):

                if (queen.black_big_queen_rect.collidepoint(queen.black_queen_rect.x + (
                    queen.defaut_rect * (ord(ch4) - ord(queen.black_queen_position[0]))), queen.black_queen_rect.y)):

                    stats.black_turn = False
                    stats.white_turn = True

                    background.board_move[queen.black_queen_position[0]][str(queen.black_queen_position[1])] = False
                    background.board_move[ch4][str(queen.black_queen_position[1])] = True

                    queen.black_queen_rect.x += queen.defaut_rect * (ord(ch4) - ord(queen.black_queen_position[0]))

                    queen.black_queen_position[0] = ch4
                    pawn.pieces_move.append(
                        "Q" + queen.black_queen_position[0] + str(queen.black_queen_position[1]))
                    print(pawn.pieces_move)
                    break

                ch4 = chr(ord(ch4) + 1)

            if (queen.black_big_queen_rect.collidepoint(queen.black_queen_rect.x + (
                queen.defaut_rect * (ord(ch4) - ord(queen.black_queen_position[0]))), queen.black_queen_rect.y)):

                aux = queen.black_queen_position[0]
                queen.black_queen_position[0] = ch4

                if verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position, rook.white_rook_position,
                                           bishop.white_bishop_position, queen.white_queen_position, pawn.white_pawn_death,
                                           knight.white_knight_death, rook.white_rook_death, bishop.white_bishop_death,
                                           queen.white_queen_death, queen.black_queen_position, 0, 0):

                    stats.black_turn = False
                    stats.white_turn = True

                    background.board_move[aux][str(queen.black_queen_position[1])] = False
                    background.board_move[queen.black_queen_position[0]][str(queen.black_queen_position[1])] = True

                    queen.black_queen_rect.x += queen.defaut_rect * (ord(ch4) - ord(aux))

                    queen.white_queen_death = eliminate_killed_piece("Q", queen.black_queen_position, pawn.white_pawn_position,
                                           knight.white_knight_position, bishop.white_bishop_position,
                                           rook.white_rook_position, queen.white_queen_position,
                                           pawn.white_pawn_death, knight.white_knight_death, bishop.white_bishop_death,
                                           rook.white_rook_death, queen.white_queen_death,
                                           pawn.white_pawn_rects, knight.white_knight_rects, bishop.white_bishop_rects,
                                           rook.white_rook_rects, queen.white_queen_rect,
                                           pawn, knight, bishop, rook, queen)

                else:
                    queen.black_queen_position[0] = aux

        if queen.black_queen_position[0] > 'a':
            while (ch5 >= 'a') and (not background.board_move[ch5][str(queen.black_queen_position[1])]):

                if (queen.black_big_queen_rect.collidepoint(queen.black_queen_rect.x - (
                    queen.defaut_rect * (ord(queen.black_queen_position[0]) - ord(ch5))), queen.black_queen_rect.y)):

                    stats.black_turn = False
                    stats.white_turn = True

                    background.board_move[queen.black_queen_position[0]][str(queen.black_queen_position[1])] = False
                    background.board_move[ch5][str(queen.black_queen_position[1])] = True

                    queen.black_queen_rect.x -= queen.defaut_rect * (ord(queen.black_queen_position[0]) - ord(ch5))

                    queen.black_queen_position[0] = ch5
                    pawn.pieces_move.append(
                        "Q" + queen.black_queen_position[0] + str(queen.black_queen_position[1]))
                    print(pawn.pieces_move)
                    break
                ch5 = chr(ord(ch5) - 1)

            if (queen.black_big_queen_rect.collidepoint(queen.black_queen_rect.x - (
                queen.defaut_rect * (ord(queen.black_queen_position[0]) - ord(ch5))), queen.black_queen_rect.y)):

                aux1 = queen.black_queen_position[0]
                queen.black_queen_position[0] = ch5

                if verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position, rook.white_rook_position,
                                           bishop.white_bishop_position, queen.white_queen_position, pawn.white_pawn_death,
                                           knight.white_knight_death, rook.white_rook_death, bishop.white_bishop_death,
                                           queen.white_queen_death, queen.black_queen_position, 0, 0):

                    stats.black_turn = False
                    stats.white_turn = True

                    background.board_move[aux1][str(queen.black_queen_position[1])] = False
                    background.board_move[queen.black_queen_position[0]][str(queen.black_queen_position[1])] = True

                    queen.black_queen_rect.x -= queen.defaut_rect * (ord(aux1) - ord(ch5))

                    queen.white_queen_death = eliminate_killed_piece("Q", queen.black_queen_position, pawn.white_pawn_position,
                                           knight.white_knight_position, bishop.white_bishop_position,
                                           rook.white_rook_position, queen.white_queen_position,
                                           pawn.white_pawn_death, knight.white_knight_death, bishop.white_bishop_death,
                                           rook.white_rook_death, queen.white_queen_death,
                                           pawn.white_pawn_rects, knight.white_knight_rects, bishop.white_bishop_rects,
                                           rook.white_rook_rects, queen.white_queen_rect,
                                           pawn, knight, bishop, rook, queen)
                else:
                    queen.black_queen_position[0] = aux1

        if queen.black_queen_position[1] < 8:
            while (key4 <= 8) and (not background.board_move[queen.black_queen_position[0]][str(key4)]):

                if (queen.black_big_queen_rect.collidepoint(queen.black_queen_rect.x,
                     queen.black_queen_rect.y - (queen.defaut_rect * (key4 - queen.black_queen_position[1])))):

                    stats.black_turn = False
                    stats.white_turn = True

                    background.board_move[queen.black_queen_position[0]][str(queen.black_queen_position[1])] = False
                    background.board_move[queen.black_queen_position[0]][str(key4)] = True

                    queen.black_queen_rect.y -= queen.defaut_rect * (key4 - queen.black_queen_position[1])

                    queen.black_queen_position[1] = key4
                    pawn.pieces_move.append(
                        "Q" + queen.black_queen_position[0] + str(queen.black_queen_position[1]))
                    print(pawn.pieces_move)
                    break
                key4 += 1

            if (queen.black_big_queen_rect.collidepoint(queen.black_queen_rect.x,
                queen.black_queen_rect.y - (queen.defaut_rect * (key4 - queen.black_queen_position[1])))):

                aux2 = queen.black_queen_position[1]
                queen.black_queen_position[1] = key4
                if verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position, rook.white_rook_position,
                                           bishop.white_bishop_position, queen.white_queen_position, pawn.white_pawn_death,
                                           knight.white_knight_death, rook.white_rook_death, bishop.white_bishop_death,
                                           queen.white_queen_death, queen.black_queen_position, 0, 0):

                    stats.black_turn = False
                    stats.white_turn = True

                    background.board_move[queen.black_queen_position[0]][str(aux2)] = False
                    background.board_move[queen.black_queen_position[0]][str(queen.black_queen_position[1])] = True

                    queen.black_queen_rect.y -= queen.defaut_rect * (key4 - aux2)

                    queen.white_queen_death = eliminate_killed_piece("Q", queen.black_queen_position, pawn.white_pawn_position,
                                           knight.white_knight_position, bishop.white_bishop_position,
                                           rook.white_rook_position, queen.white_queen_position,
                                           pawn.white_pawn_death, knight.white_knight_death, bishop.white_bishop_death,
                                           rook.white_rook_death, queen.white_queen_death,
                                           pawn.white_pawn_rects, knight.white_knight_rects, bishop.white_bishop_rects,
                                           rook.white_rook_rects, queen.white_queen_rect,
                                           pawn, knight, bishop, rook, queen)

                else:
                    queen.black_queen_position[1] = aux2

        if queen.black_queen_position[1] > 1:
            while (key5 >= 1) and (not background.board_move[queen.black_queen_position[0]][str(key5)]):

                if (queen.black_big_queen_rect.collidepoint(queen.black_queen_rect.x,
                    queen.black_queen_rect.y + (queen.defaut_rect * (queen.black_queen_position[1] - key5)))):

                    stats.black_turn = False
                    stats.white_turn = True

                    background.board_move[queen.black_queen_position[0]][str(queen.black_queen_position[1])] = False
                    background.board_move[queen.black_queen_position[0]][str(key5)] = True

                    queen.black_queen_rect.y += queen.defaut_rect * (queen.black_queen_position[1] - key5)

                    queen.black_queen_position[1] = key5
                    pawn.pieces_move.append(
                        "Q" + queen.black_queen_position[0] + str(queen.black_queen_position[1]))
                    print(pawn.pieces_move)
                    break
                key5 -= 1

            if (queen.black_big_queen_rect.collidepoint(queen.black_queen_rect.x,
                queen.black_queen_rect.y + (queen.defaut_rect * (queen.black_queen_position[1] - key5)))):

                aux3 = queen.black_queen_position[1]
                queen.black_queen_position[1] = key5
                if verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position, rook.white_rook_position,
                                           bishop.white_bishop_position, queen.white_queen_position, pawn.white_pawn_death,
                                           knight.white_knight_death, rook.white_rook_death, bishop.white_bishop_death,
                                           queen.white_queen_death, queen.black_queen_position, 0, 0):

                    stats.black_turn = False
                    stats.white_turn = True

                    background.board_move[queen.black_queen_position[0]][str(aux3)] = False
                    background.board_move[queen.black_queen_position[0]][str(queen.black_queen_position[1])] = True

                    queen.black_queen_rect.y += queen.defaut_rect * (aux3 - key5)

                    queen.white_queen_death = eliminate_killed_piece("Q", queen.black_queen_position, pawn.white_pawn_position, knight.white_knight_position, bishop.white_bishop_position,
                                           rook.white_rook_position, queen.white_queen_position,
                                           pawn.white_pawn_death, knight.white_knight_death, bishop.white_bishop_death, rook.white_rook_death, queen.white_queen_death,
                                           pawn.white_pawn_rects, knight.white_knight_rects, bishop.white_bishop_rects, rook.white_rook_rects, queen.white_queen_rect,
                                           pawn, knight, bishop, rook, queen)

                else:
                    queen.black_queen_position[1] = aux3

def undo_check(stats, king):
    if stats.white_turn:
        king.bk = [False, False, False, False, False]
        king.black_check_mvt = []
        king.black_check = False
        king.bpc = None

    if stats.black_turn:
        king.wk = [False, False, False, False, False]
        king.white_check_mvt = []
        king.white_check = False
        king.wpc = None

def king_check(stats, background, rook, pawn, knight, bishop, queen, king):

    if stats.white_turn:
        if (not queen.black_queen_death):
            wking_queen(background, king, queen)

        for key in rook.black_rook_clicked.keys():
            if (not rook.black_rook_death[key]):
                wking_rook(background, king, rook, key)

        for key in bishop.black_bishop_clicked.keys():
            if (not bishop.black_bishop_death[key]):
                wking_bishop(background, king, bishop, key)

        for key in pawn.black_pawn_clicked.keys():
            if (not pawn.black_pawn_death[key]):
                wking_pawn(background, king, pawn, key)

        for key in knight.black_knight_clicked.keys():
            if (not knight.black_knight_death[key]):
                wking_knight(background, king, knight, key)

    if stats.black_turn:
        if (not queen.white_queen_death):
            bking_queen(background, king, queen)

        for key in rook.white_rook_clicked.keys():
            if (not rook.white_rook_death[key]):
                bking_rook(background, king, rook, key)

        for key in bishop.white_bishop_clicked.keys():
            if (not bishop.white_bishop_death[key]):
                bking_bishop(background, king, bishop, key)

        for key in pawn.white_pawn_clicked.keys():
            if (not pawn.white_pawn_death[key]):
                bking_pawn(background, king, pawn, key)

        for key in knight.white_knight_clicked.keys():
            if (not knight.white_knight_death[key]):
                bking_knight(background, king, knight, key)

def wking_rook(background, king, rook, key):

    ch0 = chr(ord(rook.black_rook_position[key][0]) + 1)
    ch1 = chr(ord(rook.black_rook_position[key][0]) - 1)
    index0 = rook.black_rook_position[key][1] + 1
    index1 = rook.black_rook_position[key][1] - 1
    if rook.black_rook_position[key][0] < 'h':
        while (ch0 <= 'h') and (not background.board_move[ch0][str(rook.black_rook_position[key][1])]):
            ch0 = chr(ord(ch0) + 1)

        if (king.white_king_position[0] == ch0) and (king.white_king_position[1] == rook.black_rook_position[key][1]):
            king.white_check_mvt = []
            king.white_check_mvt.append(background.board_rect[ch0][str(rook.black_rook_position[key][1])])
            king.white_check_mvt.append(background.board_rect[rook.black_rook_position[key][0]][str(rook.black_rook_position[key][1])])
            king.white_check = True
            king.wk[0] = True
            king.wpc = key

    if rook.black_rook_position[key][0] > 'a':
        while (ch1 >= 'a') and (not background.board_move[ch1][str(rook.black_rook_position[key][1])]):
            ch1 = chr(ord(ch1) - 1)

        if (king.white_king_position[0] == ch1) and (king.white_king_position[1] == rook.black_rook_position[key][1]):
            king.white_check_mvt = []
            king.white_check_mvt.append(background.board_rect[ch1][str(rook.black_rook_position[key][1])])
            king.white_check_mvt.append(background.board_rect[rook.black_rook_position[key][0]][str(rook.black_rook_position[key][1])])
            king.white_check = True
            king.wk[0] = True
            king.wpc = key

    if rook.black_rook_position[key][1] < 8:
        while (index0 <= 8) and (not background.board_move[rook.black_rook_position[key][0]][str(index0)]):
            index0 += 1

        if (king.white_king_position[0] == rook.black_rook_position[key][0]) and (king.white_king_position[1] == index0):
            king.white_check_mvt = []
            king.white_check_mvt.append(background.board_rect[rook.black_rook_position[key][0]][str(index0)])
            king.white_check_mvt.append(background.board_rect[rook.black_rook_position[key][0]][str(rook.black_rook_position[key][1])])
            king.white_check = True
            king.wk[0] = True
            king.wpc = key

    if rook.black_rook_position[key][1] > 1:
        while (index1 >= 1) and (not background.board_move[rook.black_rook_position[key][0]][str(index1)]):
            index1 -= 1

        if (king.white_king_position[0] == rook.black_rook_position[key][0]) and (king.white_king_position[1] == index1):
            king.white_check_mvt = []
            king.white_check_mvt.append(background.board_rect[rook.black_rook_position[key][0]][str(index1)])
            king.white_check_mvt.append(background.board_rect[rook.black_rook_position[key][0]][str(rook.black_rook_position[key][1])])
            king.white_check = True
            king.wk[0] = True
            king.wpc = key

def bking_rook(background, king, rook, key):

    ch0 = chr(ord(rook.white_rook_position[key][0]) + 1)
    ch1 = chr(ord(rook.white_rook_position[key][0]) - 1)
    index0 = rook.white_rook_position[key][1] + 1
    index1 = rook.white_rook_position[key][1] - 1
    if rook.white_rook_position[key][0] < 'h':
        while (ch0 <= 'h') and (not background.board_move[ch0][str(rook.white_rook_position[key][1])]):
            ch0 = chr(ord(ch0) + 1)

        if (king.black_king_position[0] == ch0) and (king.black_king_position[1] == rook.white_rook_position[key][1]):
            king.black_check_mvt = []
            king.black_check_mvt.append(background.board_rect[ch0][str(rook.white_rook_position[key][1])])
            king.black_check_mvt.append(background.board_rect[rook.white_rook_position[key][0]][str(rook.white_rook_position[key][1])])
            king.black_check = True
            king.bk[0] = True
            king.bpc = key

    if rook.white_rook_position[key][0] > 'a':
        while (ch1 >= 'a') and (not background.board_move[ch1][str(rook.white_rook_position[key][1])]):
            ch1 = chr(ord(ch1) - 1)

        if (king.black_king_position[0] == ch1) and (king.black_king_position[1] == rook.white_rook_position[key][1]):
            king.black_check_mvt = []
            king.black_check_mvt.append(background.board_rect[ch1][str(rook.white_rook_position[key][1])])
            king.black_check_mvt.append(background.board_rect[rook.white_rook_position[key][0]][str(rook.white_rook_position[key][1])])
            king.black_check = True
            king.bk[0] = True
            king.bpc = key

    if rook.white_rook_position[key][1] < 8:
        while (index0 <= 8) and (not background.board_move[rook.white_rook_position[key][0]][str(index0)]):
            index0 += 1

        if (king.black_king_position[0] == rook.white_rook_position[key][0]) and (king.black_king_position[1] == index0):
            king.black_check_mvt = []
            king.black_check_mvt.append(background.board_rect[rook.white_rook_position[key][0]][str(index0)])
            king.black_check_mvt.append(background.board_rect[rook.white_rook_position[key][0]][str(rook.white_rook_position[key][1])])
            king.black_check = True
            king.bk[0] = True
            king.bpc = key

    if rook.white_rook_position[key][1] > 1:
        while (index1 >= 1) and (not background.board_move[rook.white_rook_position[key][0]][str(index1)]):
            index1 -= 1

        if (king.black_king_position[0] == rook.white_rook_position[key][0]) and (king.black_king_position[1] == index1):
            king.black_check_mvt = []
            king.black_check_mvt.append(background.board_rect[rook.white_rook_position[key][0]][str(index1)])
            king.black_check_mvt.append(background.board_rect[rook.white_rook_position[key][0]][str(rook.white_rook_position[key][1])])
            king.black_check = True
            king.bk[0] = True
            king.bpc = key

def wking_bishop(background, king, bishop, key):

    key0 = bishop.black_bishop_position[key][1] + 1
    ch0 = chr(ord(bishop.black_bishop_position[key][0]) + 1)
    key1 = bishop.black_bishop_position[key][1] - 1
    ch1 = chr(ord(bishop.black_bishop_position[key][0]) - 1)
    if (bishop.black_bishop_position[key][0]) < 'h' and (bishop.black_bishop_position[key][1] < 8):
        while (ch0 <= "h") and (key0 <= 8) and (not background.board_move[ch0][str(key0)]):
            ch0 = chr(ord(ch0) + 1)
            key0 += 1

        if (king.white_king_position[0] == ch0) and (king.white_king_position[1] == key0):
            king.white_check_mvt = []
            king.white_check_mvt.append(background.board_rect[ch0][str(key0)])
            king.white_check_mvt.append(background.board_rect[bishop.black_bishop_position[key][0]][str(
                bishop.black_bishop_position[key][1])])
            king.white_check = True
            king.wk[1] = True
            king.wpc = key

    if (bishop.black_bishop_position[key][0] > 'a') and (bishop.black_bishop_position[key][1] > 1):
        while (ch1 >= "a") and (key1 >= 1) and (not background.board_move[ch1][str(key1)]):
            ch1 = chr(ord(ch1) - 1)
            key1 -= 1

        if (king.white_king_position[0] == ch1) and (king.white_king_position[1] == key1):
            king.white_check_mvt = []
            king.white_check_mvt.append(background.board_rect[ch1][str(key1)])
            king.white_check_mvt.append(background.board_rect[bishop.black_bishop_position[key][0]][str(
                bishop.black_bishop_position[key][1])])
            king.white_check = True
            king.wk[1] = True
            king.wpc = key

    ch2 = chr(ord(bishop.black_bishop_position[key][0]) - 1)
    key2 = bishop.black_bishop_position[key][1] + 1
    if (bishop.black_bishop_position[key][0] > 'a') and (bishop.black_bishop_position[key][1] < 8):
        while (ch2 >= "a") and (key2 <= 8) and (not background.board_move[ch2][str(key2)]):
            ch2 = chr(ord(ch2) - 1)
            key2 += 1

        if (king.white_king_position[0] == ch2) and (king.white_king_position[1] == key2):
            king.white_check_mvt = []
            king.white_check_mvt.append(background.board_rect[ch2][str(key2)])
            king.white_check_mvt.append(background.board_rect[bishop.black_bishop_position[key][0]][str(
                bishop.black_bishop_position[key][1])])
            king.white_check = True
            king.wk[1] = True
            king.wpc = key

    ch3 = chr(ord(bishop.black_bishop_position[key][0]) + 1)
    key3 = bishop.black_bishop_position[key][1] - 1
    if (bishop.black_bishop_position[key][0] < 'h') and (bishop.black_bishop_position[key][1] > 1):
        while (ch3 <= "h") and (key3 >= 1) and (not background.board_move[ch3][str(key3)]):
            ch3 = chr(ord(ch3) + 1)
            key3 -= 1

        if (king.white_king_position[0] == ch3) and (king.white_king_position[1] == key3):
            king.white_check_mvt = []
            king.white_check_mvt.append(background.board_rect[ch3][str(key3)])
            king.white_check_mvt.append(background.board_rect[bishop.black_bishop_position[key][0]][str(
                bishop.black_bishop_position[key][1])])
            king.white_check = True
            king.wk[1] = True
            king.wpc = key

def bking_bishop(background, king, bishop, key):

    key0 = bishop.white_bishop_position[key][1] + 1
    ch0 = chr(ord(bishop.white_bishop_position[key][0]) + 1)
    key1 = bishop.white_bishop_position[key][1] - 1
    ch1 = chr(ord(bishop.white_bishop_position[key][0]) - 1)
    if (bishop.white_bishop_position[key][0]) < 'h' and (bishop.white_bishop_position[key][1] < 8):
        while (ch0 <= "h") and (key0 <= 8) and (not background.board_move[ch0][str(key0)]):
            ch0 = chr(ord(ch0) + 1)
            key0 += 1

        if (king.black_king_position[0] == ch0) and (king.black_king_position[1] == key0):
            king.black_check_mvt = []
            king.black_check_mvt.append(background.board_rect[ch0][str(key0)])
            king.black_check_mvt.append(background.board_rect[bishop.white_bishop_position[key][0]][str(
                bishop.white_bishop_position[key][1])])
            king.black_check = True
            king.bk[1] = True
            king.bpc = key

    if (bishop.white_bishop_position[key][0] > 'a') and (bishop.white_bishop_position[key][1] > 1):
        while (ch1 >= "a") and (key1 >= 1) and (not background.board_move[ch1][str(key1)]):
            ch1 = chr(ord(ch1) - 1)
            key1 -= 1

        if (king.black_king_position[0] == ch1) and (king.black_king_position[1] == key1):
            king.black_check_mvt = []
            king.black_check_mvt.append(background.board_rect[ch1][str(key1)])
            king.black_check_mvt.append(background.board_rect[bishop.white_bishop_position[key][0]][str(
                bishop.white_bishop_position[key][1])])
            king.black_check = True
            king.bk[1] = True
            king.bpc = key

    ch2 = chr(ord(bishop.white_bishop_position[key][0]) - 1)
    key2 = bishop.white_bishop_position[key][1] + 1
    if (bishop.white_bishop_position[key][0] > 'a') and (bishop.white_bishop_position[key][1] < 8):
        while (ch2 >= "a") and (key2 <= 8) and (not background.board_move[ch2][str(key2)]):
            ch2 = chr(ord(ch2) - 1)
            key2 += 1

        if (king.black_king_position[0] == ch2) and (king.black_king_position[1] == key2):
            king.black_check_mvt = []
            king.black_check_mvt.append(background.board_rect[ch2][str(key2)])
            king.black_check_mvt.append(
                background.board_rect[bishop.white_bishop_position[key][0]][str(bishop.white_bishop_position[key][1])])
            king.black_check = True
            king.bk[1] = True
            king.bpc = key

    ch3 = chr(ord(bishop.white_bishop_position[key][0]) + 1)
    key3 = bishop.white_bishop_position[key][1] - 1
    if (bishop.white_bishop_position[key][0] < 'h') and (bishop.white_bishop_position[key][1] > 1):
        while (ch3 <= "h") and (key3 >= 1) and (not background.board_move[ch3][str(key3)]):
            ch3 = chr(ord(ch3) + 1)
            key3 -= 1

        if (king.black_king_position[0] == ch3) and (king.black_king_position[1] == key3):
            king.black_check_mvt = []
            king.black_check_mvt.append(background.board_rect[ch3][str(key3)])
            king.black_check_mvt.append(
                background.board_rect[bishop.white_bishop_position[key][0]][str(bishop.white_bishop_position[key][1])])
            king.black_check = True
            king.bk[1] = True
            king.bpc = key

def wking_queen(background, king, queen):

    ch0 = chr(ord(queen.black_queen_position[0]) + 1)
    ch1 = chr(ord(queen.black_queen_position[0]) - 1)
    index0 = queen.black_queen_position[1] + 1
    index1 = queen.black_queen_position[1] - 1
    if queen.black_queen_position[0] < 'h':
        while (ch0 <= 'h') and (not background.board_move[ch0][str(queen.black_queen_position[1])]):
            ch0 = chr(ord(ch0) + 1)

        if (king.white_king_position[0] == ch0) and (king.white_king_position[1] == queen.black_queen_position[1]):
            king.white_check_mvt = []
            king.white_check_mvt.append(background.board_rect[ch0][str(queen.black_queen_position[1])])
            king.white_check_mvt.append(background.board_rect[queen.black_queen_position[0]][str(
                queen.black_queen_position[1])])
            king.white_check = True
            king.wk[2] = True
            king.wpc = 'Q'

    if queen.black_queen_position[0] > 'a':
        while (ch1 >= 'a') and (not background.board_move[ch1][str(queen.black_queen_position[1])]):
            ch1 = chr(ord(ch1) - 1)

        if (king.white_king_position[0] == ch1) and (king.white_king_position[1] == queen.black_queen_position[1]):
            king.white_check_mvt = []
            king.white_check_mvt.append(background.board_rect[ch1][str(queen.black_queen_position[1])])
            king.white_check_mvt.append(background.board_rect[queen.black_queen_position[0]][str(
                queen.black_queen_position[1])])
            king.white_check = True
            king.wk[2] = True
            king.wpc = 'Q'

    if queen.black_queen_position[1] < 8:
        while (index0 <= 8) and (not background.board_move[queen.black_queen_position[0]][str(index0)]):
            index0 += 1

        if (king.white_king_position[0] == queen.black_queen_position[0]) and (king.white_king_position[1] == index0):
            king.white_check_mvt = []
            king.white_check_mvt.append(background.board_rect[queen.black_queen_position[0]][str(index0)])
            king.white_check_mvt.append(background.board_rect[queen.black_queen_position[0]][str(
                queen.black_queen_position[1])])
            king.white_check = True
            king.wk[2] = True
            king.wpc = 'Q'

    if queen.black_queen_position[1] > 1:
        while (index1 >= 1) and (not background.board_move[queen.black_queen_position[0]][str(index1)]):
            index1 -= 1

        if (king.white_king_position[0] == queen.black_queen_position[0]) and (king.white_king_position[1] == index1):
            king.white_check_mvt = []
            king.white_check_mvt.append(background.board_rect[queen.black_queen_position[0]][str(index1)])
            king.white_check_mvt.append(background.board_rect[queen.black_queen_position[0]][str(
                queen.black_queen_position[1])])
            king.white_check = True
            king.wk[2] = True
            king.wpc = 'Q'

    key2 = queen.black_queen_position[1] + 1
    ch2 = chr(ord(queen.black_queen_position[0]) + 1)
    key3 = queen.black_queen_position[1] - 1
    ch3 = chr(ord(queen.black_queen_position[0]) - 1)
    if (queen.black_queen_position[0]) < 'h' and (queen.black_queen_position[1] < 8):
        while (ch2 <= "h") and (key2 <= 8) and (not background.board_move[ch2][str(key2)]):
            ch2 = chr(ord(ch2) + 1)
            key2 += 1

        if (king.white_king_position[0] == ch2) and (king.white_king_position[1] == key2):
            king.white_check_mvt = []
            king.white_check_mvt.append(background.board_rect[ch2][str(key2)])
            king.white_check_mvt.append(background.board_rect[queen.black_queen_position[0]][str(
                queen.black_queen_position[1])])
            king.white_check = True
            king.wk[2] = True
            king.wpc = 'Q'

    if (queen.black_queen_position[0] > 'a') and (queen.black_queen_position[1] > 1):
        while (ch3 >= "a") and (key3 >= 1) and (not background.board_move[ch3][str(key3)]):
            ch3 = chr(ord(ch3) - 1)
            key3 -= 1

        if (king.white_king_position[0] == ch3) and (king.white_king_position[1] == key3):
            king.white_check_mvt = []
            king.white_check_mvt.append(background.board_rect[ch3][str(key3)])
            king.white_check_mvt.append(background.board_rect[queen.black_queen_position[0]][str(
                queen.black_queen_position[1])])
            king.white_check = True
            king.wk[2] = True
            king.wpc = 'Q'

    ch4 = chr(ord(queen.black_queen_position[0]) - 1)
    key4 = queen.black_queen_position[1] + 1
    if (queen.black_queen_position[0] > 'a') and (queen.black_queen_position[1] < 8):
        while (ch4 >= "a") and (key4 <= 8) and (not background.board_move[ch4][str(key4)]):
            ch4 = chr(ord(ch4) - 1)
            key4 += 1

        if (king.white_king_position[0] == ch4) and (king.white_king_position[1] == key4):
            king.white_check_mvt = []
            king.white_check_mvt.append(background.board_rect[ch4][str(key4)])
            king.white_check_mvt.append(background.board_rect[queen.black_queen_position[0]][str(
                queen.black_queen_position[1])])
            king.white_check = True
            king.wk[2] = True
            king.wpc = 'Q'

    ch5 = chr(ord(queen.black_queen_position[0]) + 1)
    key5 = queen.black_queen_position[1] - 1
    if (queen.black_queen_position[0] < 'h') and (queen.black_queen_position[1] > 1):
        while (ch5 <= "h") and (key5 >= 1) and (not background.board_move[ch5][str(key5)]):
            ch5 = chr(ord(ch5) + 1)
            key5 -= 1

        if (king.white_king_position[0] == ch5) and (king.white_king_position[1] == key5):
            king.white_check_mvt = []
            king.white_check_mvt.append(background.board_rect[ch5][str(key5)])
            king.white_check_mvt.append(background.board_rect[queen.black_queen_position[0]][str(
                queen.black_queen_position[1])])
            king.white_check = True
            king.wk[2] = True
            king.wpc = 'Q'

def bking_queen(background, king, queen):

    ch0 = chr(ord(queen.white_queen_position[0]) + 1)
    ch1 = chr(ord(queen.white_queen_position[0]) - 1)
    index0 = queen.white_queen_position[1] + 1
    index1 = queen.white_queen_position[1] - 1
    if queen.white_queen_position[0] < 'h':
        while (ch0 <= 'h') and (not background.board_move[ch0][str(queen.white_queen_position[1])]):
            ch0 = chr(ord(ch0) + 1)

        if (king.black_king_position[0] == ch0) and (king.black_king_position[1] == queen.white_queen_position[1]):
            king.black_check_mvt = []
            king.black_check_mvt.append(background.board_rect[ch0][str(queen.white_queen_position[1])])
            king.black_check_mvt.append(background.board_rect[queen.white_queen_position[0]][str(
                queen.white_queen_position[1])])
            king.black_check = True
            king.bk[2] = True
            king.bpc = 'Q'

    if queen.white_queen_position[0] > 'a':
        while (ch1 >= 'a') and (not background.board_move[ch1][str(queen.white_queen_position[1])]):
            ch1 = chr(ord(ch1) - 1)

        if (king.black_king_position[0] == ch1) and (king.black_king_position[1] == queen.white_queen_position[1]):
            king.black_check_mvt = []
            king.black_check_mvt.append(background.board_rect[ch1][str(queen.white_queen_position[1])])
            king.black_check_mvt.append(background.board_rect[queen.white_queen_position[0]][str(
                queen.white_queen_position[1])])
            king.black_check = True
            king.bk[2] = True
            king.bpc = 'Q'

    if queen.white_queen_position[1] < 8:
        while (index0 <= 8) and (not background.board_move[queen.white_queen_position[0]][str(index0)]):
            index0 += 1

        if (king.black_king_position[0] == queen.white_queen_position[0]) and (king.black_king_position[1] == index0):
            king.black_check_mvt = []
            king.black_check_mvt.append(background.board_rect[queen.white_queen_position[0]][str(index0)])
            king.black_check_mvt.append(background.board_rect[queen.white_queen_position[0]][str(
                queen.white_queen_position[1])])
            king.black_check = True
            king.bk[2] = True
            king.bpc = 'Q'

    if queen.white_queen_position[1] > 1:
        while (index1 >= 1) and (not background.board_move[queen.white_queen_position[0]][str(index1)]):
            index1 -= 1

        if (king.black_king_position[0] == queen.white_queen_position[0]) and (king.black_king_position[1] == index1):
            king.black_check_mvt = []
            king.black_check_mvt.append(background.board_rect[queen.white_queen_position[0]][str(index1)])
            king.black_check_mvt.append(background.board_rect[queen.white_queen_position[0]][str(
                queen.white_queen_position[1])])
            king.black_check = True
            king.bk[2] = True
            king.bpc = 'Q'

    key2 = queen.white_queen_position[1] + 1
    ch2 = chr(ord(queen.white_queen_position[0]) + 1)
    key3 = queen.white_queen_position[1] - 1
    ch3 = chr(ord(queen.white_queen_position[0]) - 1)
    if (queen.white_queen_position[0]) < 'h' and (queen.white_queen_position[1] < 8):
        while (ch2 <= "h") and (key2 <= 8) and (not background.board_move[ch2][str(key2)]):
            ch2 = chr(ord(ch2) + 1)
            key2 += 1

        if (king.black_king_position[0] == ch2) and (king.black_king_position[1] == key2):
            king.black_check_mvt = []
            king.black_check_mvt.append(background.board_rect[ch2][str(key2)])
            king.black_check_mvt.append(background.board_rect[queen.white_queen_position[0]][str(
                queen.white_queen_position[1])])
            king.black_check = True
            king.bk[2] = True
            king.bpc = 'Q'

    if (queen.white_queen_position[0] > 'a') and (queen.white_queen_position[1] > 1):
        while (ch3 >= "a") and (key3 >= 1) and (not background.board_move[ch3][str(key3)]):
            ch3 = chr(ord(ch3) - 1)
            key3 -= 1

        if (king.black_king_position[0] == ch3) and (king.black_king_position[1] == key3):
            king.black_check_mvt = []
            king.black_check_mvt.append(background.board_rect[ch3][str(key3)])
            king.black_check_mvt.append(background.board_rect[queen.white_queen_position[0]][str(
                queen.white_queen_position[1])])
            king.black_check = True
            king.bk[2] = True
            king.bpc = 'Q'

    ch4 = chr(ord(queen.white_queen_position[0]) - 1)
    key4 = queen.white_queen_position[1] + 1
    if (queen.white_queen_position[0] > 'a') and (queen.white_queen_position[1] < 8):
        while (ch4 >= "a") and (key4 <= 8) and (not background.board_move[ch4][str(key4)]):
            ch4 = chr(ord(ch4) - 1)
            key4 += 1

        if (king.black_king_position[0] == ch4) and (king.black_king_position[1] == key4):
            king.black_check_mvt = []
            king.black_check_mvt.append(background.board_rect[ch4][str(key4)])
            king.black_check_mvt.append(background.board_rect[queen.white_queen_position[0]][str(
                queen.white_queen_position[1])])
            king.black_check = True
            king.bk[2] = True
            king.bpc = 'Q'

    ch5 = chr(ord(queen.white_queen_position[0]) + 1)
    key5 = queen.white_queen_position[1] - 1
    if (queen.white_queen_position[0] < 'h') and (queen.white_queen_position[1] > 1):
        while (ch5 <= "h") and (key5 >= 1) and (not background.board_move[ch5][str(key5)]):
            ch5 = chr(ord(ch5) + 1)
            key5 -= 1

        if (king.black_king_position[0] == ch5) and (king.black_king_position[1] == key5):
            king.black_check_mvt = []
            king.black_check_mvt.append(background.board_rect[ch5][str(key5)])
            king.black_check_mvt.append(background.board_rect[queen.white_queen_position[0]][str(
                queen.white_queen_position[1])])
            king.black_check = True
            king.bk[2] = True
            king.bpc = 'Q'

def wking_knight(background, king, knight, key):

    ch = knight.black_knight_position[key][0]
    k = knight.black_knight_position[key][1]
    if (ch < "g") and (k > 1):
        if (king.white_king_position[0] == chr(ord(ch) + 2)) and (king.white_king_position[1] == k - 1):
            king.white_check_mvt = []
            king.white_check_mvt.append(background.board_rect[chr(ord(ch) + 2)][str(k - 1)])
            king.white_check_mvt.append(background.board_rect[ch][str(k)])
            king.white_check = True
            king.wk[3] = True
            king.wpc = key

    if (ch < "g") and (k < 8):
        if (king.white_king_position[0] == chr(ord(ch) + 2)) and (king.white_king_position[1] == k + 1):
            king.white_check_mvt = []
            king.white_check_mvt.append(background.board_rect[chr(ord(ch) + 2)][str(k + 1)])
            king.white_check_mvt.append(background.board_rect[ch][str(k)])
            king.white_check = True
            king.wk[3] = True
            king.wpc = key

    if (ch > "b") and (k > 1):
        if (king.white_king_position[0] == chr(ord(ch) - 2)) and (king.white_king_position[1] == k - 1):
            king.white_check_mvt = []
            king.white_check_mvt.append(background.board_rect[chr(ord(ch) - 2)][str(k - 1)])
            king.white_check_mvt.append(background.board_rect[ch][str(k)])
            king.white_check = True
            king.wk[3] = True
            king.wpc = key

    if (ch > "b") and (k < 8):
        if (king.white_king_position[0] == chr(ord(ch) - 2)) and (king.white_king_position[1] == k + 1):
            king.white_check_mvt = []
            king.white_check_mvt.append(background.board_rect[chr(ord(ch) - 2)][str(k + 1)])
            king.white_check_mvt.append(background.board_rect[ch][str(k)])
            king.white_check = True
            king.wk[3] = True
            king.wpc = key

    if (ch > "a") and (k > 2):
        if (king.white_king_position[0] == chr(ord(ch) - 1)) and (king.white_king_position[1] == k - 2):
            king.white_check_mvt = []
            king.white_check_mvt.append(background.board_rect[chr(ord(ch) - 1)][str(k - 2)])
            king.white_check_mvt.append(background.board_rect[ch][str(k)])
            king.white_check = True
            king.wk[3] = True
            king.wpc = key

    if (ch > "a") and (k < 7):
        if (king.white_king_position[0] == chr(ord(ch) - 1)) and (king.white_king_position[1] == k + 2):
            king.white_check_mvt.append(background.board_rect[chr(ord(ch) - 1)][str(k + 2)])
            king.white_check_mvt.append(background.board_rect[ch][str(k)])
            king.white_check = True
            king.wk[3] = True
            king.wpc = key

    if (ch < "h") and (k > 2):
        if (king.white_king_position[0] == chr(ord(ch) + 1)) and (king.white_king_position[1] == k - 2):
            king.white_check_mvt = []
            king.white_check_mvt.append(background.board_rect[chr(ord(ch) + 1)][str(k - 2)])
            king.white_check_mvt.append(background.board_rect[ch][str(k)])
            king.white_check = True
            king.wk[3] = True
            king.wpc = key

    if (ch < "h") and (k < 7):
        if (king.white_king_position[0] == chr(ord(ch) + 1)) and (king.white_king_position[1] == k + 2):
            king.white_check_mvt = []
            king.white_check_mvt.append(background.board_rect[chr(ord(ch) + 1)][str(k + 2)])
            king.white_check_mvt.append(background.board_rect[ch][str(k)])
            king.white_check = True
            king.wk[3] = True
            king.wpc = key

def bking_knight(background, king, knight, key):
    king.bk[3] = False
    ch = knight.white_knight_position[key][0]
    k = knight.white_knight_position[key][1]
    if (ch < "g") and (k > 1):
        if (king.black_king_position[0] == chr(ord(ch) + 2)) and (king.black_king_position[1] == k - 1):
            king.black_check_mvt = []
            king.black_check_mvt.append(background.board_rect[chr(ord(ch) + 2)][str(k - 1)])
            king.black_check_mvt.append(background.board_rect[ch][str(k)])
            king.black_check = True
            king.bk[3] = True
            king.bpc = key

    if (ch < "g") and (k < 8):
        if (king.black_king_position[0] == chr(ord(ch) + 2)) and (king.black_king_position[1] == k + 1):
            king.black_check_mvt = []
            king.black_check_mvt.append(background.board_rect[chr(ord(ch) + 2)][str(k + 1)])
            king.black_check_mvt.append(background.board_rect[ch][str(k)])
            king.black_check = True
            king.bk[3] = True
            king.bpc = key

    if (ch > "b") and (k > 1):
        if (king.black_king_position[0] == chr(ord(ch) - 2)) and (king.black_king_position[1] == k - 1):
            king.black_check_mvt = []
            king.black_check_mvt.append(background.board_rect[chr(ord(ch) - 2)][str(k - 1)])
            king.black_check_mvt.append(background.board_rect[ch][str(k)])
            king.black_check = True
            king.bk[3] = True
            king.bpc = key

    if (ch > "b") and (k < 8):
        if (king.black_king_position[0] == chr(ord(ch) - 2)) and (king.black_king_position[1] == k + 1):
            king.black_check_mvt = []
            king.black_check_mvt.append(background.board_rect[chr(ord(ch) - 2)][str(k + 1)])
            king.black_check_mvt.append(background.board_rect[ch][str(k)])
            king.black_check = True
            king.bk[3] = True
            king.bpc = key

    if (ch > "a") and (k > 2):
        if (king.black_king_position[0] == chr(ord(ch) - 1)) and (king.black_king_position[1] == k - 2):
            king.black_check_mvt = []
            king.black_check_mvt.append(background.board_rect[chr(ord(ch) - 1)][str(k - 2)])
            king.black_check_mvt.append(background.board_rect[ch][str(k)])
            king.black_check = True
            king.bk[3] = True
            king.bpc = key

    if (ch > "a") and (k < 7):
        if (king.black_king_position[0] == chr(ord(ch) - 1)) and (king.black_king_position[1] == k + 2):
            king.black_check_mvt = []
            king.black_check_mvt.append(background.board_rect[chr(ord(ch) - 1)][str(k + 2)])
            king.black_check_mvt.append(background.board_rect[ch][str(k)])
            king.black_check = True
            king.bk[3] = True
            king.bpc = key

    if (ch < "h") and (k > 2):
        if (king.black_king_position[0] == chr(ord(ch) + 1)) and (king.black_king_position[1] == k - 2):
            king.black_check_mvt = []
            king.black_check_mvt.append(background.board_rect[chr(ord(ch) + 1)][str(k - 2)])
            king.black_check_mvt.append(background.board_rect[ch][str(k)])
            king.black_check = True
            king.bk[3] = True
            king.bpc = key

    if (ch < "h") and (k < 7):
        if (king.black_king_position[0] == chr(ord(ch) + 1)) and (king.black_king_position[1] == k + 2):
            king.black_check_mvt = []
            king.black_check_mvt.append(background.board_rect[chr(ord(ch) + 1)][str(k + 2)])
            king.black_check_mvt.append(background.board_rect[ch][str(k)])
            king.black_check = True
            king.bk[3] = True
            king.bpc = key

def wking_pawn(background, king, pawn, key):

    ch = pawn.black_pawn_position[key][0]
    k = pawn.black_pawn_position[key][1]
    if ch > "a" and k > 1:
        if (king.white_king_position[0] == chr(ord(ch) - 1)) and (king.white_king_position[1] == k - 1):
            king.white_check_mvt = []
            king.white_check_mvt.append(background.board_rect[chr(ord(ch) - 1)][str(k - 1)])
            king.white_check_mvt.append(background.board_rect[ch][str(k)])
            king.white_check = True
            king.wk[4] = True
            king.wpc = key

    if ch < "h" and k > 1:
        if (king.white_king_position[0] == chr(ord(ch) + 1)) and (king.white_king_position[1] == k - 1):
            king.white_check_mvt = []
            king.white_check_mvt.append(background.board_rect[chr(ord(ch) + 1)][str(k - 1)])
            king.white_check_mvt.append(background.board_rect[ch][str(k)])
            king.white_check = True
            king.wk[4] = True
            king.wpc = key

def bking_pawn(background, king, pawn, key):

    ch = pawn.white_pawn_position[key][0]
    k = pawn.white_pawn_position[key][1]
    if k < 8 and ch > "a":
        if (king.black_king_position[0] == chr(ord(ch) - 1)) and (king.black_king_position[1] == k + 1):
            king.black_check_mvt = []
            king.black_check_mvt.append(background.board_rect[chr(ord(ch) - 1)][str(k + 1)])
            king.black_check_mvt.append(background.board_rect[ch][str(k)])
            king.black_check = True
            king.bk[4] = True
            king.bpc = key

    if ch < "h" and k < 8:
        if (king.black_king_position[0] == chr(ord(ch) + 1)) and (king.black_king_position[1] == k + 1):
            king.black_check_mvt = []
            king.black_check_mvt.append(background.board_rect[chr(ord(ch) + 1)][str(k + 1)])
            king.black_check_mvt.append(background.board_rect[ch][str(k)])
            king.black_check = True
            king.bk[4] = True
            king.bpc = key

def update_white_king(stats, background, rook, pawn, knight, bishop, queen, king):

    if not king.white_king_clicked:
        if (king.white_king_position[0] > 'a'):

            if (king.white_big_king_rect.collidepoint(
                    king.white_king_rect.x - king.defaut_rect, king.white_king_rect.y)):

                ch = king.white_king_position[0]
                k = king.white_king_position[1]
                if (not background.board_move[chr(ord(ch) - 1)][str(k)]) or (
                        verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position,
                                                rook.black_rook_position, bishop.black_bishop_position,
                                                queen.black_queen_position,
                                                pawn.black_pawn_death, knight.black_knight_death, rook.black_rook_death,
                                                bishop.black_bishop_death, queen.black_queen_death,
                                                king.white_king_position, 0, -1)):

                    background.board_move[chr(ord(ch) - 1)][str(k)] = True
                    background.board_move[ch][str(k)] = False
                    king.white_king_position[0] = chr(ord(ch) - 1)
                    king.white_king_rect.x -= king.defaut_rect
                    queen.black_queen_death = eliminate_killed_piece("K", king.white_king_position, pawn.black_pawn_position,
                                           knight.black_knight_position, bishop.black_bishop_position,
                                           rook.black_rook_position, queen.black_queen_position,
                                           pawn.black_pawn_death, knight.black_knight_death,
                                           bishop.black_bishop_death,
                                           rook.black_rook_death, queen.black_queen_death,
                                           pawn.black_pawn_rects, knight.black_knight_rects,
                                           bishop.black_bishop_rects,
                                           rook.black_rook_rects, queen.black_queen_rect,
                                           pawn, knight, bishop, rook, queen)
                    stats.white_turn = False
                    stats.black_turn = True
                    king.white_king_no_move = False

            if (king.white_king_position[1] > 1) and (king.white_big_king_rect.collidepoint(
                    king.white_king_rect.x - king.defaut_rect, king.white_king_rect.y + king.defaut_rect)):

                ch1 = king.white_king_position[0]
                k1 = king.white_king_position[1]
                if (not background.board_move[chr(ord(ch1) - 1)][str(k1 - 1)]) or (
                        verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position,
                                                rook.black_rook_position, bishop.black_bishop_position,
                                                queen.black_queen_position,
                                                pawn.black_pawn_death, knight.black_knight_death, rook.black_rook_death,
                                                bishop.black_bishop_death, queen.black_queen_death,
                                                king.white_king_position, -1, -1)):

                    background.board_move[chr(ord(ch1) - 1)][str(k1 - 1)] = True
                    background.board_move[ch1][str(k1)] = False
                    king.white_king_position[0] = chr(ord(ch1) - 1)
                    king.white_king_position[1] -= 1
                    king.white_king_rect.x -= king.defaut_rect
                    king.white_king_rect.y += king.defaut_rect
                    queen.black_queen_death = eliminate_killed_piece("K", king.white_king_position, pawn.black_pawn_position,
                                           knight.black_knight_position, bishop.black_bishop_position,
                                           rook.black_rook_position, queen.black_queen_position,
                                           pawn.black_pawn_death, knight.black_knight_death,
                                           bishop.black_bishop_death,
                                           rook.black_rook_death, queen.black_queen_death,
                                           pawn.black_pawn_rects, knight.black_knight_rects,
                                           bishop.black_bishop_rects,
                                           rook.black_rook_rects, queen.black_queen_rect,
                                           pawn, knight, bishop, rook, queen)
                    stats.white_turn = False
                    stats.black_turn = True
                    king.white_king_no_move = False

            if (king.white_king_position[1] < 8) and (king.white_big_king_rect.collidepoint(
                    king.white_king_rect.x - king.defaut_rect, king.white_king_rect.y - king.defaut_rect)):

                ch2 = king.white_king_position[0]
                k2 = king.white_king_position[1]
                if (not background.board_move[chr(ord(ch2) - 1)][str(k2 + 1)]) or (
                        verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position,
                                                rook.black_rook_position, bishop.black_bishop_position,
                                                queen.black_queen_position,
                                                pawn.black_pawn_death, knight.black_knight_death, rook.black_rook_death,
                                                bishop.black_bishop_death, queen.black_queen_death,
                                                king.white_king_position, 1, -1)):

                    background.board_move[chr(ord(ch2) - 1)][str(k2 + 1)] = True
                    background.board_move[ch2][str(k2)] = False
                    king.white_king_position[0] = chr(ord(ch2) - 1)
                    king.white_king_position[1] += 1
                    king.white_king_rect.x -= king.defaut_rect
                    king.white_king_rect.y -= king.defaut_rect
                    queen.black_queen_death = eliminate_killed_piece("K", king.white_king_position, pawn.black_pawn_position,
                                           knight.black_knight_position, bishop.black_bishop_position,
                                           rook.black_rook_position, queen.black_queen_position,
                                           pawn.black_pawn_death, knight.black_knight_death,
                                           bishop.black_bishop_death,
                                           rook.black_rook_death, queen.black_queen_death,
                                           pawn.black_pawn_rects, knight.black_knight_rects,
                                           bishop.black_bishop_rects,
                                           rook.black_rook_rects, queen.black_queen_rect,
                                           pawn, knight, bishop, rook, queen)
                    stats.white_turn = False
                    stats.black_turn = True
                    king.white_king_no_move = False

        if (king.white_king_position[0] < 'h'):
            if (king.white_big_king_rect.collidepoint(
                    king.white_king_rect.x + king.defaut_rect, king.white_king_rect.y)):

                ch3 = king.white_king_position[0]
                k3 = king.white_king_position[1]
                if (not background.board_move[chr(ord(ch3) + 1)][str(k3)]) or (
                        verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position,
                                                rook.black_rook_position, bishop.black_bishop_position,
                                                queen.black_queen_position,
                                                pawn.black_pawn_death, knight.black_knight_death, rook.black_rook_death,
                                                bishop.black_bishop_death, queen.black_queen_death,
                                                king.white_king_position, 0, 1)):

                    background.board_move[chr(ord(ch3) + 1)][str(k3)] = True
                    background.board_move[ch3][str(k3)] = False
                    king.white_king_position[0] = chr(ord(ch3) + 1)
                    king.white_king_rect.x += king.defaut_rect
                    queen.black_queen_death = eliminate_killed_piece("K", king.white_king_position, pawn.black_pawn_position,
                                           knight.black_knight_position, bishop.black_bishop_position,
                                           rook.black_rook_position, queen.black_queen_position,
                                           pawn.black_pawn_death, knight.black_knight_death,
                                           bishop.black_bishop_death,
                                           rook.black_rook_death, queen.black_queen_death,
                                           pawn.black_pawn_rects, knight.black_knight_rects,
                                           bishop.black_bishop_rects,
                                           rook.black_rook_rects, queen.black_queen_rect,
                                           pawn, knight, bishop, rook, queen)
                    stats.white_turn = False
                    stats.black_turn = True
                    king.white_king_no_move = False

            if (king.white_king_position[1] > 1) and (king.white_big_king_rect.collidepoint(
                    king.white_king_rect.x + king.defaut_rect, king.white_king_rect.y + king.defaut_rect)):

                ch4 = king.white_king_position[0]
                k4 = king.white_king_position[1]
                if (not background.board_move[chr(ord(ch4) + 1)][str(k4 - 1)]) or (
                        verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position,
                                                rook.black_rook_position, bishop.black_bishop_position,
                                                queen.black_queen_position,
                                                pawn.black_pawn_death, knight.black_knight_death, rook.black_rook_death,
                                                bishop.black_bishop_death, queen.black_queen_death,
                                                king.white_king_position, -1, 1)):

                    background.board_move[chr(ord(ch4) + 1)][str(k4 - 1)] = True
                    background.board_move[ch4][str(k4)] = False
                    king.white_king_position[0] = chr(ord(ch4) + 1)
                    king.white_king_position[1] -= 1
                    king.white_king_rect.x += king.defaut_rect
                    king.white_king_rect.y += king.defaut_rect
                    queen.black_queen_death = eliminate_killed_piece("K", king.white_king_position, pawn.black_pawn_position,
                                           knight.black_knight_position, bishop.black_bishop_position,
                                           rook.black_rook_position, queen.black_queen_position,
                                           pawn.black_pawn_death, knight.black_knight_death,
                                           bishop.black_bishop_death,
                                           rook.black_rook_death, queen.black_queen_death,
                                           pawn.black_pawn_rects, knight.black_knight_rects,
                                           bishop.black_bishop_rects,
                                           rook.black_rook_rects, queen.black_queen_rect,
                                           pawn, knight, bishop, rook, queen)
                    stats.white_turn = False
                    stats.black_turn = True
                    king.white_king_no_move = False

            if (king.white_king_position[1] < 8) and (king.white_big_king_rect.collidepoint(
                    king.white_king_rect.x + king.defaut_rect, king.white_king_rect.y - king.defaut_rect)):

                ch5 = king.white_king_position[0]
                k5 = king.white_king_position[1]
                if (not background.board_move[chr(ord(ch5) + 1)][str(k5 + 1)]) or (
                        verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position,
                                                rook.black_rook_position, bishop.black_bishop_position,
                                                queen.black_queen_position,
                                                pawn.black_pawn_death, knight.black_knight_death, rook.black_rook_death,
                                                bishop.black_bishop_death, queen.black_queen_death,
                                                king.white_king_position, 1, 1)):

                    background.board_move[chr(ord(ch5) + 1)][str(k5 + 1)] = True
                    background.board_move[ch5][str(k5)] = False
                    king.white_king_position[0] = chr(ord(ch5) + 1)
                    king.white_king_position[1] += 1
                    king.white_king_rect.x += king.defaut_rect
                    king.white_king_rect.y -= king.defaut_rect
                    queen.black_queen_death = eliminate_killed_piece("K", king.white_king_position, pawn.black_pawn_position,
                                           knight.black_knight_position, bishop.black_bishop_position,
                                           rook.black_rook_position, queen.black_queen_position,
                                           pawn.black_pawn_death, knight.black_knight_death,
                                           bishop.black_bishop_death,
                                           rook.black_rook_death, queen.black_queen_death,
                                           pawn.black_pawn_rects, knight.black_knight_rects,
                                           bishop.black_bishop_rects,
                                           rook.black_rook_rects, queen.black_queen_rect,
                                           pawn, knight, bishop, rook, queen)
                    stats.white_turn = False
                    stats.black_turn = True
                    king.white_king_no_move = False

        if (king.white_king_position[1] < 8) and (king.white_big_king_rect.collidepoint(
                king.white_king_rect.x, king.white_king_rect.y - king.defaut_rect)):

            ch6 = king.white_king_position[0]
            k6 = king.white_king_position[1]
            if (not background.board_move[ch6][str(k6 + 1)]) or (
                    verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position,
                                            rook.black_rook_position, bishop.black_bishop_position,
                                            queen.black_queen_position,
                                            pawn.black_pawn_death, knight.black_knight_death, rook.black_rook_death,
                                            bishop.black_bishop_death, queen.black_queen_death,
                                            king.white_king_position, 1, 0)):

                background.board_move[ch6][str(k6 + 1)] = True
                background.board_move[ch6][str(k6)] = False
                king.white_king_position[1] += 1
                king.white_king_rect.y -= king.defaut_rect
                queen.black_queen_death = eliminate_killed_piece("K", king.white_king_position, pawn.black_pawn_position,
                                       knight.black_knight_position, bishop.black_bishop_position,
                                       rook.black_rook_position, queen.black_queen_position,
                                       pawn.black_pawn_death, knight.black_knight_death,
                                       bishop.black_bishop_death,
                                       rook.black_rook_death, queen.black_queen_death,
                                       pawn.black_pawn_rects, knight.black_knight_rects,
                                       bishop.black_bishop_rects,
                                       rook.black_rook_rects, queen.black_queen_rect,
                                       pawn, knight, bishop, rook, queen)
                stats.white_turn = False
                stats.black_turn = True
                king.white_king_no_move = False

        if (king.white_king_position[1] > 1) and (king.white_big_king_rect.collidepoint(
                king.white_king_rect.x, king.white_king_rect.y + king.defaut_rect)):

            ch7 = king.white_king_position[0]
            k7 = king.white_king_position[1]
            if (not background.board_move[ch7][str(k7 - 1)]) or (
                    verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position,
                                            rook.black_rook_position, bishop.black_bishop_position,
                                            queen.black_queen_position,
                                            pawn.black_pawn_death, knight.black_knight_death, rook.black_rook_death,
                                            bishop.black_bishop_death, queen.black_queen_death,
                                            king.white_king_position, -1, 0)):

                background.board_move[ch7][str(k7 - 1)] = True
                background.board_move[ch7][str(k7)] = False
                king.white_king_position[1] -= 1
                king.white_king_rect.y += king.defaut_rect
                queen.black_queen_death = eliminate_killed_piece("K", king.white_king_position, pawn.black_pawn_position,
                                       knight.black_knight_position, bishop.black_bishop_position,
                                       rook.black_rook_position, queen.black_queen_position,
                                       pawn.black_pawn_death, knight.black_knight_death,
                                       bishop.black_bishop_death,
                                       rook.black_rook_death, queen.black_queen_death,
                                       pawn.black_pawn_rects, knight.black_knight_rects,
                                       bishop.black_bishop_rects,
                                       rook.black_rook_rects, queen.black_queen_rect,
                                       pawn, knight, bishop, rook, queen)
                stats.white_turn = False
                stats.black_turn = True
                king.white_king_no_move = False

        if (king.white_king_no_move) and rook.white_rook_no_move['R1'] and (
            king.white_big_king_rect.collidepoint(king.white_king_rect.x - (2 * king.defaut_rect) , king.white_king_rect.y)):

            ch8 = king.white_king_position[0]
            k8 = king.white_king_position[1]
            if (not background.board_move[chr(ord(ch8) - 1)][str(k8)]) and (not background.board_move[chr(ord(ch8) - 2)][str(k8)]) and (
                not background.board_move[chr(ord(ch8) - 3)][str(k8)]):

                background.board_move[chr(ord(ch8) - 2)][str(k8)] = True
                background.board_move[chr(ord(ch8) - 1)][str(k8)] = True
                background.board_move[chr(ord(ch8) - 4)][str(k8)] = False
                background.board_move[ch8][str(k8)] = False
                king.white_king_position[0] = chr(ord(ch8) - 2)
                rook.white_rook_position['R1'][0] = chr(ord(ch8) - 1)
                king.white_king_rect.x -= 2 * king.defaut_rect
                rook.white_rook_rects['R1'].x += 3 * king.defaut_rect
                stats.white_turn = False
                stats.black_turn = True
                king.white_king_no_move = False
                rook.white_rook_no_move['R1'] = False
                pawn.pieces_move.append('K/R1')

        if (king.white_king_no_move) and rook.white_rook_no_move['R2'] and (
            king.white_big_king_rect.collidepoint(king.white_king_rect.x + (2 * king.defaut_rect) , king.white_king_rect.y)):

            ch9 = king.white_king_position[0]
            k9 = king.white_king_position[1]
            if (not background.board_move[chr(ord(ch9) + 1)][str(k9)]) and (not background.board_move[chr(ord(ch9) + 2)][str(k9)]):

                background.board_move[chr(ord(ch9) + 2)][str(k9)] = True
                background.board_move[chr(ord(ch9) + 1)][str(k9)] = True
                background.board_move[chr(ord(ch9) + 3)][str(k9)] = False
                background.board_move[ch9][str(k9)] = False
                king.white_king_position[0] = chr(ord(ch9) + 2)
                rook.white_rook_position['R2'][0] = chr(ord(ch9) + 1)
                king.white_king_rect.x += 2 * king.defaut_rect
                rook.white_rook_rects['R2'].x -= 2 * king.defaut_rect
                stats.white_turn = False
                stats.black_turn = True
                king.white_king_no_move = False
                rook.white_rook_no_move['R2'] = False
                pawn.pieces_move.append('K/R2')

def update_black_king(stats, background, rook, pawn, knight, bishop, queen, king):

    if not king.black_king_clicked:
        if (king.black_king_position[0] > 'a'):

            if (king.black_big_king_rect.collidepoint(
                    king.black_king_rect.x - king.defaut_rect, king.black_king_rect.y)):

                ch = king.black_king_position[0]
                k = king.black_king_position[1]
                if (not background.board_move[chr(ord(ch) - 1)][str(k)]) or (
                        verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position,
                                                rook.white_rook_position,
                                                bishop.white_bishop_position, queen.white_queen_position,
                                                pawn.white_pawn_death,
                                                knight.white_knight_death, rook.white_rook_death,
                                                bishop.white_bishop_death,
                                                queen.white_queen_death, king.black_king_position, 0, -1)):

                    background.board_move[chr(ord(ch) - 1)][str(k)] = True
                    background.board_move[ch][str(k)] = False
                    king.black_king_position[0] = chr(ord(ch) - 1)
                    king.black_king_rect.x -= king.defaut_rect
                    queen.white_queen_death = eliminate_killed_piece("K", king.black_king_position, pawn.white_pawn_position,
                                           knight.white_knight_position, bishop.white_bishop_position,
                                           rook.white_rook_position, queen.white_queen_position,
                                           pawn.white_pawn_death, knight.white_knight_death, bishop.white_bishop_death,
                                           rook.white_rook_death, queen.white_queen_death,
                                           pawn.white_pawn_rects, knight.white_knight_rects, bishop.white_bishop_rects,
                                           rook.white_rook_rects, queen.white_queen_rect,
                                           pawn, knight, bishop, rook, queen)
                    stats.black_turn = False
                    stats.white_turn = True
                    king.black_king_no_move = False

            if (king.black_king_position[1] > 1) and (king.black_big_king_rect.collidepoint(
                    king.black_king_rect.x - king.defaut_rect, king.black_king_rect.y + king.defaut_rect)):

                ch1 = king.black_king_position[0]
                k1 = king.black_king_position[1]
                if (not background.board_move[chr(ord(ch1) - 1)][str(k1 - 1)]) or (
                        verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position,
                                                rook.white_rook_position,
                                                bishop.white_bishop_position, queen.white_queen_position,
                                                pawn.white_pawn_death,
                                                knight.white_knight_death, rook.white_rook_death,
                                                bishop.white_bishop_death,
                                                queen.white_queen_death, king.black_king_position, -1, -1)):

                    background.board_move[chr(ord(ch1) - 1)][str(k1 - 1)] = True
                    background.board_move[ch1][str(k1)] = False
                    king.black_king_position[0] = chr(ord(ch1) - 1)
                    king.black_king_position[1] -= 1
                    king.black_king_rect.x -= king.defaut_rect
                    king.black_king_rect.y += king.defaut_rect
                    queen.white_queen_death = eliminate_killed_piece("K", king.black_king_position, pawn.white_pawn_position,
                                           knight.white_knight_position, bishop.white_bishop_position,
                                           rook.white_rook_position, queen.white_queen_position,
                                           pawn.white_pawn_death, knight.white_knight_death, bishop.white_bishop_death,
                                           rook.white_rook_death, queen.white_queen_death,
                                           pawn.white_pawn_rects, knight.white_knight_rects, bishop.white_bishop_rects,
                                           rook.white_rook_rects, queen.white_queen_rect,
                                           pawn, knight, bishop, rook, queen)
                    stats.black_turn = False
                    stats.white_turn = True
                    king.black_king_no_move = False

            if (king.black_king_position[1] < 8) and (king.black_big_king_rect.collidepoint(
                    king.black_king_rect.x - king.defaut_rect, king.black_king_rect.y - king.defaut_rect)):

                ch2 = king.black_king_position[0]
                k2 = king.black_king_position[1]
                if (not background.board_move[chr(ord(ch2) - 1)][str(k2 + 1)]) or (
                        verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position,
                                                rook.white_rook_position,
                                                bishop.white_bishop_position, queen.white_queen_position,
                                                pawn.white_pawn_death,
                                                knight.white_knight_death, rook.white_rook_death,
                                                bishop.white_bishop_death,
                                                queen.white_queen_death, king.black_king_position, 1, -1)):

                    background.board_move[chr(ord(ch2) - 1)][str(k2 + 1)] = True
                    background.board_move[ch2][str(k2)] = False
                    king.black_king_position[0] = chr(ord(ch2) - 1)
                    king.black_king_position[1] += 1
                    king.black_king_rect.x -= king.defaut_rect
                    king.black_king_rect.y -= king.defaut_rect
                    queen.white_queen_death = eliminate_killed_piece("K", king.black_king_position, pawn.white_pawn_position,
                                           knight.white_knight_position, bishop.white_bishop_position,
                                           rook.white_rook_position, queen.white_queen_position,
                                           pawn.white_pawn_death, knight.white_knight_death, bishop.white_bishop_death,
                                           rook.white_rook_death, queen.white_queen_death,
                                           pawn.white_pawn_rects, knight.white_knight_rects, bishop.white_bishop_rects,
                                           rook.white_rook_rects, queen.white_queen_rect,
                                           pawn, knight, bishop, rook, queen)
                    stats.black_turn = False
                    stats.white_turn = True
                    king.black_king_no_move = False

        if (king.black_king_position[0] < 'h'):
            if (king.black_big_king_rect.collidepoint(
                    king.black_king_rect.x + king.defaut_rect, king.black_king_rect.y)):

                ch3 = king.black_king_position[0]
                k3 = king.black_king_position[1]
                if (not background.board_move[chr(ord(ch3) + 1)][str(k3)]) or (
                        verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position,
                                                rook.white_rook_position,
                                                bishop.white_bishop_position, queen.white_queen_position,
                                                pawn.white_pawn_death,
                                                knight.white_knight_death, rook.white_rook_death,
                                                bishop.white_bishop_death,
                                                queen.white_queen_death, king.black_king_position, 0, 1)):

                    background.board_move[chr(ord(ch3) + 1)][str(k3)] = True
                    background.board_move[ch3][str(k3)] = False
                    king.black_king_position[0] = chr(ord(ch3) + 1)
                    king.black_king_rect.x += king.defaut_rect
                    queen.white_queen_death = eliminate_killed_piece("K", king.black_king_position, pawn.white_pawn_position,
                                           knight.white_knight_position, bishop.white_bishop_position,
                                           rook.white_rook_position, queen.white_queen_position,
                                           pawn.white_pawn_death, knight.white_knight_death, bishop.white_bishop_death,
                                           rook.white_rook_death, queen.white_queen_death,
                                           pawn.white_pawn_rects, knight.white_knight_rects, bishop.white_bishop_rects,
                                           rook.white_rook_rects, queen.white_queen_rect,
                                           pawn, knight, bishop, rook, queen)
                    stats.black_turn = False
                    stats.white_turn = True
                    king.black_king_no_move = False

            if (king.black_king_position[1] > 1) and (king.black_big_king_rect.collidepoint(
                    king.black_king_rect.x + king.defaut_rect, king.black_king_rect.y + king.defaut_rect)):

                ch4 = king.black_king_position[0]
                k4 = king.black_king_position[1]
                if (not background.board_move[chr(ord(ch4) + 1)][str(k4 - 1)]) or (
                        verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position,
                                                rook.white_rook_position,
                                                bishop.white_bishop_position, queen.white_queen_position,
                                                pawn.white_pawn_death,
                                                knight.white_knight_death, rook.white_rook_death,
                                                bishop.white_bishop_death,
                                                queen.white_queen_death, king.black_king_position, -1, 1)):

                    background.board_move[chr(ord(ch4) + 1)][str(k4 - 1)] = True
                    background.board_move[ch4][str(k4)] = False
                    king.black_king_position[0] = chr(ord(ch4) + 1)
                    king.black_king_position[1] -= 1
                    king.black_king_rect.x += king.defaut_rect
                    king.black_king_rect.y += king.defaut_rect
                    queen.white_queen_death = eliminate_killed_piece("K", king.black_king_position, pawn.white_pawn_position,
                                           knight.white_knight_position, bishop.white_bishop_position,
                                           rook.white_rook_position, queen.white_queen_position,
                                           pawn.white_pawn_death, knight.white_knight_death, bishop.white_bishop_death,
                                           rook.white_rook_death, queen.white_queen_death,
                                           pawn.white_pawn_rects, knight.white_knight_rects, bishop.white_bishop_rects,
                                           rook.white_rook_rects, queen.white_queen_rect,
                                           pawn, knight, bishop, rook, queen)
                    stats.black_turn = False
                    stats.white_turn = True
                    king.black_king_no_move = False

            if (king.black_king_position[1] < 8) and (king.black_big_king_rect.collidepoint(
                    king.black_king_rect.x + king.defaut_rect, king.black_king_rect.y - king.defaut_rect)):

                ch5 = king.black_king_position[0]
                k5 = king.black_king_position[1]
                if (not background.board_move[chr(ord(ch5) + 1)][str(k5 + 1)]) or (
                        verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position,
                                                rook.white_rook_position,
                                                bishop.white_bishop_position, queen.white_queen_position,
                                                pawn.white_pawn_death,
                                                knight.white_knight_death, rook.white_rook_death,
                                                bishop.white_bishop_death,
                                                queen.white_queen_death, king.black_king_position, 1, 1)):

                    background.board_move[chr(ord(ch5) + 1)][str(k5 + 1)] = True
                    background.board_move[ch5][str(k5)] = False
                    king.black_king_position[0] = chr(ord(ch5) + 1)
                    king.black_king_position[1] += 1
                    king.black_king_rect.x += king.defaut_rect
                    king.black_king_rect.y -= king.defaut_rect
                    queen.white_queen_death = eliminate_killed_piece("K", king.black_king_position, pawn.white_pawn_position,
                                           knight.white_knight_position, bishop.white_bishop_position,
                                           rook.white_rook_position, queen.white_queen_position,
                                           pawn.white_pawn_death, knight.white_knight_death, bishop.white_bishop_death,
                                           rook.white_rook_death, queen.white_queen_death,
                                           pawn.white_pawn_rects, knight.white_knight_rects, bishop.white_bishop_rects,
                                           rook.white_rook_rects, queen.white_queen_rect,
                                           pawn, knight, bishop, rook, queen)
                    stats.black_turn = False
                    stats.white_turn = True
                    king.black_king_no_move = False

        if (king.black_king_position[1] < 8) and (king.black_big_king_rect.collidepoint(
                king.black_king_rect.x, king.black_king_rect.y - king.defaut_rect)):

            ch6 = king.black_king_position[0]
            k6 = king.black_king_position[1]
            if (not background.board_move[ch6][str(k6 + 1)]) or (
                    verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position,
                                            rook.white_rook_position,
                                            bishop.white_bishop_position, queen.white_queen_position,
                                            pawn.white_pawn_death,
                                            knight.white_knight_death, rook.white_rook_death,
                                            bishop.white_bishop_death,
                                            queen.white_queen_death, king.black_king_position, 1, 0)):

                background.board_move[ch6][str(k6 + 1)] = True
                background.board_move[ch6][str(k6)] = False
                king.black_king_position[1] += 1
                king.black_king_rect.y -= king.defaut_rect
                queen.white_queen_death = eliminate_killed_piece("K", king.black_king_position, pawn.white_pawn_position,
                                       knight.white_knight_position, bishop.white_bishop_position,
                                       rook.white_rook_position, queen.white_queen_position,
                                       pawn.white_pawn_death, knight.white_knight_death, bishop.white_bishop_death,
                                       rook.white_rook_death, queen.white_queen_death,
                                       pawn.white_pawn_rects, knight.white_knight_rects, bishop.white_bishop_rects,
                                       rook.white_rook_rects, queen.white_queen_rect,
                                       pawn, knight, bishop, rook, queen)
                stats.black_turn = False
                stats.white_turn = True
                king.black_king_no_move = False

        if (king.black_king_position[1] > 1) and (king.black_big_king_rect.collidepoint(
                king.black_king_rect.x, king.black_king_rect.y + king.defaut_rect)):

            ch6 = king.black_king_position[0]
            k6 = king.black_king_position[1]
            if (not background.board_move[ch6][str(k6 - 1)]) or (
                    verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position,
                                            rook.white_rook_position,
                                            bishop.white_bishop_position, queen.white_queen_position,
                                            pawn.white_pawn_death,
                                            knight.white_knight_death, rook.white_rook_death,
                                            bishop.white_bishop_death,
                                            queen.white_queen_death, king.black_king_position, -1, 0)):

                background.board_move[ch6][str(k6 - 1)] = True
                background.board_move[ch6][str(k6)] = False
                king.black_king_position[1] -= 1
                king.black_king_rect.y += king.defaut_rect
                queen.white_queen_death = eliminate_killed_piece("K", king.black_king_position, pawn.white_pawn_position,
                                       knight.white_knight_position, bishop.white_bishop_position,
                                       rook.white_rook_position, queen.white_queen_position,
                                       pawn.white_pawn_death, knight.white_knight_death, bishop.white_bishop_death,
                                       rook.white_rook_death, queen.white_queen_death,
                                       pawn.white_pawn_rects, knight.white_knight_rects, bishop.white_bishop_rects,
                                       rook.white_rook_rects, queen.white_queen_rect,
                                       pawn, knight, bishop, rook, queen)
                stats.black_turn = False
                stats.white_turn = True
                king.black_king_no_move = False

        if (king.black_king_no_move) and rook.black_rook_no_move['R1'] and (
            king.black_big_king_rect.collidepoint(king.black_king_rect.x - (2 * king.defaut_rect) , king.black_king_rect.y)):

            ch7 = king.black_king_position[0]
            k7 = king.black_king_position[1]
            if (not background.board_move[chr(ord(ch7) - 1)][str(k7)]) and (not background.board_move[chr(ord(ch7) - 2)][str(k7)]) and (
                not background.board_move[chr(ord(ch7) - 3)][str(k7)]):

                background.board_move[chr(ord(ch7) - 2)][str(k7)] = True
                background.board_move[chr(ord(ch7) - 1)][str(k7)] = True
                background.board_move[chr(ord(ch7) - 4)][str(k7)] = False
                background.board_move[ch7][str(k7)] = False
                king.black_king_position[0] = chr(ord(ch7) - 2)
                rook.black_rook_position['R1'][0] = chr(ord(ch7) - 1)
                king.black_king_rect.x -= 2 * king.defaut_rect
                rook.black_rook_rects['R1'].x += 3 * king.defaut_rect
                stats.black_turn = False
                stats.white_turn = True
                king.black_king_no_move = False
                rook.black_rook_no_move['R1'] = False
                pawn.pieces_move.append('K/R1')

        if (king.black_king_no_move) and rook.black_rook_no_move['R2'] and (
            king.black_big_king_rect.collidepoint(king.black_king_rect.x + (2 * king.defaut_rect) , king.black_king_rect.y)):

            ch8 = king.black_king_position[0]
            k8 = king.black_king_position[1]
            if (not background.board_move[chr(ord(ch8) + 1)][str(k8)]) and (not background.board_move[chr(ord(ch8) + 2)][str(k8)]):

                background.board_move[chr(ord(ch8) + 2)][str(k8)] = True
                background.board_move[chr(ord(ch8) + 1)][str(k8)] = True
                background.board_move[chr(ord(ch8) + 3)][str(k8)] = False
                background.board_move[ch8][str(k8)] = False
                king.black_king_position[0] = chr(ord(ch8) + 2)
                rook.black_rook_position['R2'][0] = chr(ord(ch8) + 1)
                king.black_king_rect.x += 2 * king.defaut_rect
                rook.black_rook_rects['R2'].x -= 2 * king.defaut_rect
                stats.black_turn = False
                stats.white_turn = True
                king.black_king_no_move = False
                rook.black_rook_no_move['R2'] = False
                pawn.pieces_move.append('K/R2')

def white_pawn_move(background, pawn, knight, rook, bishop, queen, king, key):

    pawn.white_movements[2] = background.board_rect[pawn.white_pawn_position[key][0]][str(pawn.white_pawn_position[key][1])]

    if pawn.white_pawn_position[key][1] < 8 and pawn.white_pawn_position[key][0] != "a":
        if (verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position, rook.black_rook_position,
                    bishop.black_bishop_position, queen.black_queen_position, pawn.black_pawn_death,
                    knight.black_knight_death, rook.black_rook_death, bishop.black_bishop_death,
                    queen.black_queen_death, pawn.white_pawn_position[key], 1, -1)):

            pawn.white_movements[4] = (background.board_rect[chr(ord(pawn.white_pawn_position[key][0]) - 1)][str(pawn.white_pawn_position[key][1] + 1)])

    if pawn.white_pawn_position[key][0] != "h" and pawn.white_pawn_position[key][1] != 8:
        if (verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position, rook.black_rook_position,
                    bishop.black_bishop_position, queen.black_queen_position, pawn.black_pawn_death,
                    knight.black_knight_death, rook.black_rook_death, bishop.black_bishop_death,
                    queen.black_queen_death, pawn.white_pawn_position[key], 1, 1)):

            pawn.white_movements[3] = (background.board_rect[chr(ord(pawn.white_pawn_position[key][0]) + 1)][str(pawn.white_pawn_position[key][1] + 1)])

    if pawn.white_pawn_position[key][1] == 5:
        if pawn.white_pawn_position[key][0] != "h":
            for key0, black_pawn in pawn.black_pawn_position.items():
                if pawn.white_pawn_position[key][1] == black_pawn[1] and pawn.black_pawns_mv2[key0] and (
                        pawn.white_pawn_position[key][0] == chr(ord(black_pawn[0]) + 1)) and (
                        pawn.pieces_move[len(pawn.pieces_move) - 1] == key0 + black_pawn[0] + str(black_pawn[1])) and (
                        pawn.black_pawns_mv2[key0]):

                    pawn.white_movements[5] = (background.board_rect[chr(ord(pawn.white_pawn_position[key][0]) - 1
                                                        )][str(pawn.white_pawn_position[key][1] + 1)])

        if pawn.white_pawn_position[key][0] != "a":
            for key0, black_pawn in pawn.black_pawn_position.items():
                if pawn.white_pawn_position[key][1] == black_pawn[1] and pawn.black_pawns_mv2[key0] and \
                        pawn.white_pawn_position[key][0] == chr(ord(black_pawn[0]) - 1) and (
                        pawn.pieces_move[len(pawn.pieces_move) - 1] == key0 + black_pawn[0] + str(black_pawn[1])) and (
                        pawn.black_pawns_mv2[key0]):

                    pawn.white_movements[6] = (background.board_rect[chr(ord(pawn.white_pawn_position[key][0]) + 1
                                                        )][str(pawn.white_pawn_position[key][1] + 1)])

    if (pawn.white_pawn_position[key][1] < 8) and (not verify_piece_collisions(
            pawn.white_pawn_position, knight.white_knight_position, rook.white_rook_position,
            bishop.white_bishop_position, queen.white_queen_position, pawn.white_pawn_death,
            knight.white_knight_death, rook.white_rook_death, bishop.white_bishop_death,
            queen.white_queen_death, pawn.white_pawn_position[key], 1, 0)) and (

            not verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position, rook.black_rook_position,
                    bishop.black_bishop_position, queen.black_queen_position, pawn.black_pawn_death,
                    knight.black_knight_death, rook.black_rook_death, bishop.black_bishop_death,
                    queen.black_queen_death, pawn.white_pawn_position[key], 1, 0)) and not (

            (pawn.white_pawn_position[key][0] == king.white_king_position[0] and pawn.white_pawn_position[key][1] + 1 == king.white_king_position[1]
            ) or (pawn.white_pawn_position[key][0] == king.black_king_position[0] and pawn.white_pawn_position[key][1] + 1 == king.black_king_position[1])):

        pawn.white_movements[0] = background.board_rect[pawn.white_pawn_position[key][0]][str(pawn.white_pawn_position[key][1] + 1)]

        if pawn.white_pawn_position[key][1] == 2 and (not verify_piece_collisions(
                pawn.white_pawn_position, knight.white_knight_position, rook.white_rook_position,
               bishop.white_bishop_position, queen.white_queen_position, pawn.white_pawn_death,
               knight.white_knight_death, rook.white_rook_death, bishop.white_bishop_death,
               queen.white_queen_death, pawn.white_pawn_position[key], 2, 0)) and (

            not verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position, rook.black_rook_position,
                    bishop.black_bishop_position, queen.black_queen_position, pawn.black_pawn_death,
                    knight.black_knight_death, rook.black_rook_death, bishop.black_bishop_death,
                    queen.black_queen_death, pawn.white_pawn_position[key], 2, 0)) and not (

                (pawn.white_pawn_position[key][0] == king.white_king_position[0]\
            and pawn.white_pawn_position[key][1] + 2 == king.white_king_position[1]) or (pawn.white_pawn_position[key][0] == king.black_king_position[0]\
            and pawn.white_pawn_position[key][1] + 2 == king.black_king_position[1])):

            pawn.white_movements[1] = (background.board_rect[pawn.white_pawn_position[key][0]][str(pawn.white_pawn_position[key][1] + 2)])

        if (pawn.white_pawn_position[key][1] > 2):

            pawn.white_second_move[key] = False

def black_pawn_move(background, pawn, knight, rook, bishop, queen, king, key):

    pawn.black_movements[2] = (background.board_rect[pawn.black_pawn_position[key][0]][str(pawn.black_pawn_position[key][1])])

    if pawn.black_pawn_position[key][0] != "a" and pawn.black_pawn_position[key][1] > 1:
        if (verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position, rook.white_rook_position,
               bishop.white_bishop_position, queen.white_queen_position, pawn.white_pawn_death,
               knight.white_knight_death, rook.white_rook_death, bishop.white_bishop_death,
               queen.white_queen_death, pawn.black_pawn_position[key], -1, -1)):

            pawn.black_movements[4] = (background.board_rect[chr(ord(pawn.black_pawn_position[key][0]) - 1)][str(pawn.black_pawn_position[key][1] - 1)])

    if pawn.black_pawn_position[key][0] != "h" and pawn.black_pawn_position[key][1] > 1:
        if (verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position, rook.white_rook_position,
               bishop.white_bishop_position, queen.white_queen_position, pawn.white_pawn_death,
               knight.white_knight_death, rook.white_rook_death, bishop.white_bishop_death,
               queen.white_queen_death, pawn.black_pawn_position[key], -1, 1)):

            pawn.black_movements[3] = (background.board_rect[chr(ord(pawn.black_pawn_position[key][0]) + 1)][str(pawn.black_pawn_position[key][1] - 1)])

    if pawn.black_pawn_position[key][1] == 4:
        if pawn.black_pawn_position[key][0] != "h":
            for key0, white_pawn in pawn.white_pawn_position.items():
                if pawn.black_pawn_position[key][1] == white_pawn[1] and pawn.white_pawns_mv2[key0] and (
                   pawn.black_pawn_position[key][0] == chr(ord(white_pawn[0]) + 1)) and (
                   pawn.pieces_move[len(pawn.pieces_move) - 1] == key0 + white_pawn[0] + str(white_pawn[1])) and (
                   pawn.white_pawns_mv2[key0]):

                    pawn.black_movements[5] = (background.board_rect[chr(ord(pawn.black_pawn_position[key][0]) - 1)][str(pawn.black_pawn_position[key][1] - 1)])

        if pawn.black_pawn_position[key][0] != "a":
            for key0, white_pawn in pawn.white_pawn_position.items():
                if pawn.black_pawn_position[key][1] == white_pawn[1] and pawn.white_pawns_mv2[key0] and \
                   pawn.black_pawn_position[key][0] == chr(ord(white_pawn[0]) - 1) and (
                   pawn.pieces_move[len(pawn.pieces_move) - 1] == key0 + white_pawn[0] + str(white_pawn[1])) and (
                   pawn.white_pawns_mv2[key0]):

                    pawn.black_movements[6] = (background.board_rect[chr(ord(pawn.black_pawn_position[key][0]) + 1)][str(pawn.black_pawn_position[key][1] - 1)])

    if (pawn.black_pawn_position[key][1] > 1) and (not verify_piece_collisions(
                    pawn.black_pawn_position, knight.black_knight_position, rook.black_rook_position,
                    bishop.black_bishop_position, queen.black_queen_position, pawn.black_pawn_death,
                    knight.black_knight_death, rook.black_rook_death, bishop.black_bishop_death,
                    queen.black_queen_death, pawn.black_pawn_position[key], -1, 0)) and (

            not verify_piece_collisions(
                   pawn.white_pawn_position, knight.white_knight_position, rook.white_rook_position,
                   bishop.white_bishop_position, queen.white_queen_position, pawn.white_pawn_death,
                   knight.white_knight_death, rook.white_rook_death, bishop.white_bishop_death,
                   queen.white_queen_death, pawn.black_pawn_position[key], -1, 0)) and not (

            (pawn.black_pawn_position[key][0] == king.white_king_position[0]\
            and pawn.black_pawn_position[key][1] - 1 == king.white_king_position[1]) or (pawn.black_pawn_position[key][0] == king.black_king_position[0]\
            and pawn.black_pawn_position[key][1] - 1 == king.black_king_position[1])):

        pawn.black_movements[0] = (background.board_rect[pawn.black_pawn_position[key][0]][str(pawn.black_pawn_position[key][1] - 1)])

        if pawn.black_pawn_position[key][1] == 7 and (not verify_piece_collisions(
                    pawn.black_pawn_position, knight.black_knight_position, rook.black_rook_position,
                    bishop.black_bishop_position, queen.black_queen_position, pawn.black_pawn_death,
                    knight.black_knight_death, rook.black_rook_death, bishop.black_bishop_death,
                    queen.black_queen_death, pawn.black_pawn_position[key], -2, 0)) and (

            not verify_piece_collisions(pawn.white_pawn_position,
                   knight.white_knight_position, rook.white_rook_position,
                   bishop.white_bishop_position, queen.white_queen_position, pawn.white_pawn_death,
                   knight.white_knight_death, rook.white_rook_death, bishop.white_bishop_death,
                   queen.white_queen_death, pawn.black_pawn_position[key], -2, 0)) and not (

            (pawn.black_pawn_position[key][0] == king.white_king_position[0]\
            and pawn.black_pawn_position[key][1] - 2 == king.white_king_position[1]) or (pawn.black_pawn_position[key][0] == king.black_king_position[0]\
            and pawn.black_pawn_position[key][1] - 2 == king.black_king_position[1])):

            pawn.black_movements[1] = (background.board_rect[pawn.black_pawn_position[key][0]][str(pawn.black_pawn_position[key][1] - 2)])

        if pawn.black_pawn_position[key][1] < 7:
            pawn.black_second_move[key] = False

def white_pawn_attack(background, stats, pawn, knight, rook, bishop, queen):

    for pawn0, click in pawn.white_pawn_clicked.items():
        if not click:

            if (pawn.white_big_pawn_rects[pawn0].collidepoint(pawn.white_pawn_rects[pawn0].x - pawn.defaut_rect,
                pawn.white_pawn_rects[pawn0].y - pawn.defaut_rect)) and pawn.white_pawn_position[pawn0][1] < 8 and (
                     pawn.white_pawn_position[pawn0][0] != "a"):

                pawn.white_pawn_position[pawn0][1] += 1
                pawn.white_pawn_position[pawn0][0] = chr(ord(pawn.white_pawn_position[pawn0][0]) - 1)
                if (verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position, rook.black_rook_position,
                            bishop.black_bishop_position, queen.black_queen_position, pawn.black_pawn_death,
                            knight.black_knight_death, rook.black_rook_death, bishop.black_bishop_death,
                            queen.black_queen_death, pawn.white_pawn_position[pawn0], 0, 0)):

                    background.board_move[pawn.white_pawn_position[pawn0][0]][str(pawn.white_pawn_position[pawn0][1])] = True
                    background.board_move[chr(ord(pawn.white_pawn_position[pawn0][0]) + 1)][str(pawn.white_pawn_position[pawn0][1] - 1)] = False
                    pawn.white_pawn_attack[pawn0][0] = True
                    pawn.white_pawn_attack[pawn0][1] = False
                    stats.black_turn = True
                    stats.white_turn = False

                    for key, black_knight in knight.black_knight_position.items():
                        if black_knight[0] == pawn.white_pawn_position[pawn0][0] and black_knight[1] == pawn.white_pawn_position[pawn0][1]:
                            knight.black_knight_death[key] = True
                            knight.black_knight_rects[key].center = (knight.screen_rect.right - 500, knight.screen_rect.top)
                            pawn.pieces_move.append(pawn0 + chr(ord(pawn.white_pawn_position[pawn0][0]) + 1) + str(
                                pawn.white_pawn_position[pawn0][1] - 1) + 'x' + key + pawn.white_pawn_position[pawn0][0] + str(
                                pawn.white_pawn_position[pawn0][1]))
                            break

                    for key, black_bishop in bishop.black_bishop_position.items():
                        if black_bishop[0] == pawn.white_pawn_position[pawn0][0] and black_bishop[1] == pawn.white_pawn_position[pawn0][1]:
                            bishop.black_bishop_death[key] = True
                            bishop.black_bishop_rects[key].center = (bishop.screen_rect.right - 500, bishop.screen_rect.top)
                            pawn.pieces_move.append(pawn0 + chr(ord(pawn.white_pawn_position[pawn0][0]) + 1) + str(
                                pawn.white_pawn_position[pawn0][1] - 1) + 'x' + key + pawn.white_pawn_position[pawn0][0] + str(
                                pawn.white_pawn_position[pawn0][1]))
                            break

                    for key, black_rook in rook.black_rook_position.items():
                        if black_rook[0] == pawn.white_pawn_position[pawn0][0] and black_rook[1] == pawn.white_pawn_position[pawn0][1]:
                            rook.black_rook_death[key] = True
                            rook.black_rook_rects[key].center = (rook.screen_rect.right - 500, rook.screen_rect.top)
                            pawn.pieces_move.append(pawn0 + chr(ord(pawn.white_pawn_position[pawn0][0]) + 1) + str(
                                pawn.white_pawn_position[pawn0][1] - 1) + 'x' + key + pawn.white_pawn_position[pawn0][0] + str(
                                pawn.white_pawn_position[pawn0][1]))
                            break

                    if queen.black_queen_position[0] == pawn.white_pawn_position[pawn0][0] and (
                              queen.black_queen_position[1] == pawn.white_pawn_position[pawn0][1]):
                        queen.black_queen_death = True
                        queen.black_queen_rect.center = (queen.screen_rect.right - 500, queen.screen_rect.top)
                        pawn.pieces_move.append(pawn0 + chr(ord(pawn.white_pawn_position[pawn0][0]) + 1) + str(
                                pawn.white_pawn_position[pawn0][1] - 1) + 'xQ' + pawn.white_pawn_position[pawn0][0] + str(
                                pawn.white_pawn_position[pawn0][1]))

                else:
                    pawn.white_pawn_position[pawn0][1] -= 1
                    pawn.white_pawn_position[pawn0][0] = chr(ord(pawn.white_pawn_position[pawn0][0]) + 1)

            elif (pawn.white_big_pawn_rects[pawn0].collidepoint(pawn.white_pawn_rects[pawn0].x + pawn.defaut_rect,
                  pawn.white_pawn_rects[pawn0].y - pawn.defaut_rect)) and pawn.white_pawn_position[
                  pawn0][1] < 8 and pawn.white_pawn_position[pawn0][0] != "h":

                pawn.white_pawn_position[pawn0][1] += 1
                pawn.white_pawn_position[pawn0][0] = chr(ord(pawn.white_pawn_position[pawn0][0]) + 1)
                if verify_piece_collisions(pawn.black_pawn_position, knight.black_knight_position, rook.black_rook_position,
                    bishop.black_bishop_position, queen.black_queen_position, pawn.black_pawn_death,
                    knight.black_knight_death, rook.black_rook_death, bishop.black_bishop_death,
                    queen.black_queen_death, pawn.white_pawn_position[pawn0], 0, 0):

                    background.board_move[pawn.white_pawn_position[pawn0][0]][str(pawn.white_pawn_position[pawn0][1])] = True
                    background.board_move[chr(ord(pawn.white_pawn_position[pawn0][0]) - 1)][str(pawn.white_pawn_position[pawn0][1] - 1)] = False
                    pawn.white_pawn_attack[pawn0][0] = True
                    pawn.white_pawn_attack[pawn0][1] = True
                    stats.black_turn = True
                    stats.white_turn = False

                    for key, black_knight in knight.black_knight_position.items():
                        if black_knight[0] == pawn.white_pawn_position[pawn0][0] and black_knight[1] == pawn.white_pawn_position[pawn0][1]:
                            knight.black_knight_death[key] = True
                            knight.black_knight_rects[key].center = (knight.screen_rect.right - 500, knight.screen_rect.top)
                            pawn.pieces_move.append(pawn0 + chr(ord(pawn.white_pawn_position[pawn0][0]) - 1) + str(
                                pawn.white_pawn_position[pawn0][1] - 1) + 'x' + key + pawn.white_pawn_position[pawn0][0] + str(
                                pawn.white_pawn_position[pawn0][1]))
                            break

                    for key, black_bishop in bishop.black_bishop_position.items():
                        if black_bishop[0] == pawn.white_pawn_position[pawn0][0] and black_bishop[1] == pawn.white_pawn_position[pawn0][1]:
                            bishop.black_bishop_death[key] = True
                            bishop.black_bishop_rects[key].center = (bishop.screen_rect.right - 500, bishop.screen_rect.top)
                            pawn.pieces_move.append(pawn0 + chr(ord(pawn.white_pawn_position[pawn0][0]) - 1) + str(
                                pawn.white_pawn_position[pawn0][1] - 1) + 'x' + key + pawn.white_pawn_position[pawn0][0] + str(
                                pawn.white_pawn_position[pawn0][1]))
                            break

                    for key, black_rook in rook.black_rook_position.items():
                        if black_rook[0] == pawn.white_pawn_position[pawn0][0] and black_rook[1] == pawn.white_pawn_position[pawn0][1]:
                            rook.black_rook_death[key] = True
                            rook.black_rook_rects[key].center = (rook.screen_rect.right - 500, rook.screen_rect.top)
                            pawn.pieces_move.append(pawn0 + chr(ord(pawn.white_pawn_position[pawn0][0]) - 1) + str(
                                pawn.white_pawn_position[pawn0][1] - 1) + 'x' + key + pawn.white_pawn_position[pawn0][0] + str(
                                pawn.white_pawn_position[pawn0][1]))
                            break

                    if queen.black_queen_position[0] == pawn.white_pawn_position[pawn0][0] and \
                            queen.black_queen_position[1] == pawn.white_pawn_position[pawn0][1]:
                        queen.black_queen_death = True
                        queen.black_queen_rect.center = (queen.screen_rect.right - 500, queen.screen_rect.top)
                        pawn.pieces_move.append(pawn0 + chr(ord(pawn.white_pawn_position[pawn0][0]) - 1) + str(
                            pawn.white_pawn_position[pawn0][1] - 1) + 'xQ' + pawn.white_pawn_position[pawn0][0] + str(
                            pawn.white_pawn_position[pawn0][1]))

                else:
                    pawn.white_pawn_position[pawn0][0] = chr(ord(pawn.white_pawn_position[pawn0][0]) - 1)
                    pawn.white_pawn_position[pawn0][1] -= 1

            elif (pawn.white_big_pawn_rects[pawn0].collidepoint(pawn.white_pawn_rects[pawn0].x,
                    pawn.white_pawn_rects[pawn0].y - pawn.defaut_rect)) and (
                    pawn.white_pawn_rects[pawn0].y > pawn.white_rect_y - (pawn.defaut_rect * 6)):

                pawn.white_pawn_position[pawn0][1] += 1
                if not background.board_move[pawn.white_pawn_position[pawn0][0]][str(pawn.white_pawn_position[pawn0][1])]:

                    background.board_move[pawn.white_pawn_position[pawn0][0]][str(pawn.white_pawn_position[pawn0][1])] = True
                    background.board_move[pawn.white_pawn_position[pawn0][0]][str(pawn.white_pawn_position[pawn0][1] - 1)] = False
                    pawn.white_pawn_mvs[pawn0][0] = True
                    stats.black_turn = True
                    stats.white_turn = False

                else:
                    pawn.white_pawn_position[pawn0][1] -= 1

            elif pawn.white_big_pawn_rects[pawn0].collidepoint(pawn.white_pawn_rects[pawn0].x,
                    pawn.white_pawn_rects[pawn0].y - pawn.defaut_rect * 2) and pawn.white_second_move[pawn0]:

                pawn.white_pawn_position[pawn0][1] += 2
                if not background.board_move[pawn.white_pawn_position[pawn0][0]][str(pawn.white_pawn_position[pawn0][1])] and (
                   not background.board_move[pawn.white_pawn_position[pawn0][0]][str(pawn.white_pawn_position[pawn0][1] - 1)]):

                    background.board_move[pawn.white_pawn_position[pawn0][0]][str(pawn.white_pawn_position[pawn0][1])] = True
                    background.board_move[pawn.white_pawn_position[pawn0][0]][str(pawn.white_pawn_position[pawn0][1] - 2)] = False
                    pawn.white_pawn_mvs[pawn0][1] = True
                    stats.black_turn = True
                    stats.white_turn = False

                else:
                    pawn.white_pawn_position[pawn0][1] -= 2

            elif pawn.white_pawn_mvs[pawn0][2]:

                background.board_move[pawn.white_pawn_position[pawn0][0]][str(pawn.white_pawn_position[pawn0][1])] = True
                background.board_move[chr(ord(pawn.white_pawn_position[pawn0][0]) - 1)][str(pawn.white_pawn_position[pawn0][1] - 1)] = False
                background.board_move[pawn.white_pawn_position[pawn0][0]][str(pawn.white_pawn_position[pawn0][1] - 1)] = False
                pawn.white_pawn_mvs[pawn0][2] = False
                stats.black_turn = True
                stats.white_turn = False

            elif pawn.white_pawn_mvs[pawn0][3]:

                background.board_move[pawn.white_pawn_position[pawn0][0]][str(pawn.white_pawn_position[pawn0][1])] = True
                background.board_move[chr(ord(pawn.white_pawn_position[pawn0][0]) + 1)][str(pawn.white_pawn_position[pawn0][1] - 1)] = False
                background.board_move[pawn.white_pawn_position[pawn0][0]][str(pawn.white_pawn_position[pawn0][1] - 1)] = False
                pawn.white_pawn_mvs[pawn0][3] = False
                stats.black_turn = True
                stats.white_turn = False

def black_pawn_attack(background, stats, pawn, knight, rook, bishop, queen):

    for pawn0, click in pawn.black_pawn_clicked.items():
        if not click:

            if (pawn.black_big_pawn_rects[pawn0].collidepoint(pawn.black_pawn_rects[pawn0].x - pawn.defaut_rect,
                pawn.black_pawn_rects[pawn0].y + pawn.defaut_rect)) and (pawn.black_pawn_position[pawn0][1] > 1
                    ) and (pawn.black_pawn_position[pawn0][0] != "a"):

                pawn.black_pawn_position[pawn0][1] -= 1
                pawn.black_pawn_position[pawn0][0] = chr(ord(pawn.black_pawn_position[pawn0][0]) - 1)
                if verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position, rook.white_rook_position,
                                           bishop.white_bishop_position, queen.white_queen_position, pawn.white_pawn_death,
                                           knight.white_knight_death, rook.white_rook_death, bishop.white_bishop_death,
                                           queen.white_queen_death, pawn.black_pawn_position[pawn0], 0, 0):

                    background.board_move[pawn.black_pawn_position[pawn0][0]][str(pawn.black_pawn_position[pawn0][1])] = True
                    background.board_move[chr(ord(pawn.black_pawn_position[pawn0][0]) + 1)][str(pawn.black_pawn_position[pawn0][1] + 1)] = False
                    pawn.black_pawn_attack[pawn0][0] = True
                    pawn.black_pawn_attack[pawn0][1] = False
                    stats.white_turn = True
                    stats.black_turn = False

                    for key, white_knight in knight.white_knight_position.items():
                        if white_knight[0] == pawn.black_pawn_position[pawn0][0] and white_knight[1] == \
                                pawn.black_pawn_position[pawn0][1]:
                            knight.white_knight_death[key] = True
                            knight.white_knight_rects[key].center = (
                            knight.screen_rect.right - 500, knight.screen_rect.top)
                            pawn.pieces_move.append(pawn0 + chr(ord(pawn.black_pawn_position[pawn0][0]) + 1) + str(
                                pawn.black_pawn_position[pawn0][1] + 1) + 'x' + key + pawn.black_pawn_position[pawn0][0] + str(
                                pawn.black_pawn_position[pawn0][1]))
                            break

                    for key, white_bishop in bishop.white_bishop_position.items():
                        if white_bishop[0] == pawn.black_pawn_position[pawn0][0] and white_bishop[1] == \
                                pawn.black_pawn_position[pawn0][1]:
                            bishop.white_bishop_death[key] = True
                            bishop.white_bishop_rects[key].center = (
                            bishop.screen_rect.right - 500, bishop.screen_rect.top)
                            pawn.pieces_move.append(pawn0 + chr(ord(pawn.black_pawn_position[pawn0][0]) + 1) + str(
                                pawn.black_pawn_position[pawn0][1] + 1) + 'x' + key + pawn.black_pawn_position[pawn0][0] + str(
                                pawn.black_pawn_position[pawn0][1]))
                            break

                    for key, white_rook in rook.white_rook_position.items():
                        if white_rook[0] == pawn.black_pawn_position[pawn0][0] and white_rook[1] == \
                                pawn.black_pawn_position[pawn0][1]:
                            rook.white_rook_death[key] = True
                            rook.white_rook_rects[key].center = (rook.screen_rect.right - 500, rook.screen_rect.top)
                            pawn.pieces_move.append(pawn0 + chr(ord(pawn.black_pawn_position[pawn0][0]) + 1) + str(
                                pawn.black_pawn_position[pawn0][1] + 1) + 'x' + key + pawn.black_pawn_position[pawn0][0] + str(
                                pawn.black_pawn_position[pawn0][1]))
                            break

                    if queen.white_queen_position[0] == pawn.black_pawn_position[pawn0][0] and \
                            queen.white_queen_position[1] == pawn.black_pawn_position[pawn0][1]:
                        queen.white_queen_death = True
                        queen.white_queen_rect.center = (queen.screen_rect.right - 500, queen.screen_rect.top)
                        pawn.pieces_move.append(pawn0 + chr(ord(pawn.black_pawn_position[pawn0][0]) + 1) + str(
                            pawn.black_pawn_position[pawn0][1] + 1) + 'xQ' + pawn.black_pawn_position[pawn0][0] + str(
                            pawn.black_pawn_position[pawn0][1]))

                else:
                    pawn.black_pawn_position[pawn0][1] += 1
                    pawn.black_pawn_position[pawn0][0] = chr(ord(pawn.black_pawn_position[pawn0][0]) + 1)

            elif (pawn.black_big_pawn_rects[pawn0].collidepoint(pawn.black_pawn_rects[pawn0].x + pawn.defaut_rect,
                  pawn.black_pawn_rects[pawn0].y + pawn.defaut_rect)) and (pawn.black_pawn_position[pawn0][1] > 1) and (
                    pawn.black_pawn_position[pawn0][0] != "h"):

                pawn.black_pawn_position[pawn0][1] -= 1
                pawn.black_pawn_position[pawn0][0] = chr(ord(pawn.black_pawn_position[pawn0][0]) + 1)
                if verify_piece_collisions(pawn.white_pawn_position, knight.white_knight_position, rook.white_rook_position,
                                           bishop.white_bishop_position, queen.white_queen_position, pawn.white_pawn_death,
                                           knight.white_knight_death, rook.white_rook_death, bishop.white_bishop_death,
                                           queen.white_queen_death, pawn.black_pawn_position[pawn0], 0, 0):

                    background.board_move[pawn.black_pawn_position[pawn0][0]][str(pawn.black_pawn_position[pawn0][1])] = True
                    background.board_move[chr(ord(pawn.black_pawn_position[pawn0][0]) - 1)][str(pawn.black_pawn_position[pawn0][1] + 1)] = False
                    pawn.black_pawn_attack[pawn0][0] = True
                    pawn.black_pawn_attack[pawn0][1] = True
                    stats.white_turn = True
                    stats.black_turn = False

                    for key, white_knight in knight.white_knight_position.items():
                        if white_knight[0] == pawn.black_pawn_position[pawn0][0] and white_knight[1] == \
                                pawn.black_pawn_position[pawn0][1]:
                            knight.white_knight_death[key] = True
                            knight.white_knight_rects[key].center = (
                            knight.screen_rect.right - 500, knight.screen_rect.top)
                            pawn.pieces_move.append(pawn0 + chr(ord(pawn.black_pawn_position[pawn0][0]) - 1) + str(
                                pawn.black_pawn_position[pawn0][1] + 1) + 'x' + key + pawn.black_pawn_position[pawn0][0] + str(
                                pawn.black_pawn_position[pawn0][1]))
                            break

                    for key, white_bishop in bishop.white_bishop_position.items():
                        if white_bishop[0] == pawn.black_pawn_position[pawn0][0] and white_bishop[1] == \
                                pawn.black_pawn_position[pawn0][1]:
                            bishop.white_bishop_death[key] = True
                            bishop.white_bishop_rects[key].center = (
                            bishop.screen_rect.right - 500, bishop.screen_rect.top)
                            pawn.pieces_move.append(pawn0 + chr(ord(pawn.black_pawn_position[pawn0][0]) - 1) + str(
                                pawn.black_pawn_position[pawn0][1] + 1) + 'x' + key + pawn.black_pawn_position[pawn0][0] + str(
                                pawn.black_pawn_position[pawn0][1]))
                            break

                    for key, white_rook in rook.white_rook_position.items():
                        if white_rook[0] == pawn.black_pawn_position[pawn0][0] and white_rook[1] == \
                                pawn.black_pawn_position[pawn0][1]:
                            rook.white_rook_death[key] = True
                            rook.white_rook_rects[key].center = (rook.screen_rect.right - 500, rook.screen_rect.top)
                            pawn.pieces_move.append(pawn0 + chr(ord(pawn.black_pawn_position[pawn0][0]) - 1) + str(
                                pawn.black_pawn_position[pawn0][1] + 1) + 'x' + key + pawn.black_pawn_position[pawn0][0] + str(
                                pawn.black_pawn_position[pawn0][1]))
                            break

                    if queen.white_queen_position[0] == pawn.black_pawn_position[pawn0][0] and \
                            queen.white_queen_position[1] == pawn.black_pawn_position[pawn0][1]:

                        queen.white_queen_death = True
                        queen.white_queen_rect.center = (queen.screen_rect.right - 500, queen.screen_rect.top)
                        pawn.pieces_move.append(pawn0 + chr(ord(pawn.black_pawn_position[pawn0][0]) - 1) + str(
                            pawn.black_pawn_position[pawn0][1] + 1) + 'xQ' + pawn.black_pawn_position[pawn0][0] + str(
                            pawn.black_pawn_position[pawn0][1]))

                else:
                    pawn.black_pawn_position[pawn0][1] += 1
                    pawn.black_pawn_position[pawn0][0] = chr(ord(pawn.black_pawn_position[pawn0][0]) - 1)

            elif pawn.black_big_pawn_rects[pawn0].collidepoint(pawn.black_pawn_rects[pawn0].x,
                    pawn.black_pawn_rects[pawn0].y + pawn.defaut_rect) and \
                    pawn.black_pawn_rects[pawn0].y < pawn.white_rect_y:

                pawn.black_pawn_position[pawn0][1] -= 1
                if not background.board_move[pawn.black_pawn_position[pawn0][0]][str(pawn.black_pawn_position[pawn0][1])]:

                    background.board_move[pawn.black_pawn_position[pawn0][0]][str(pawn.black_pawn_position[pawn0][1])] = True
                    background.board_move[pawn.black_pawn_position[pawn0][0]][str(pawn.black_pawn_position[pawn0][1] + 1)] = False
                    pawn.black_pawn_mvs[pawn0][0] = True
                    stats.white_turn = True
                    stats.black_turn = False

                else:
                    pawn.black_pawn_position[pawn0][1] += 1

            elif pawn.black_big_pawn_rects[pawn0].collidepoint(pawn.black_pawn_rects[pawn0].x,
                 pawn.black_pawn_rects[pawn0].y + pawn.defaut_rect * 2) and pawn.black_second_move[pawn0]:

                pawn.black_pawn_position[pawn0][1] -= 2
                if not background.board_move[pawn.black_pawn_position[pawn0][0]][str(pawn.black_pawn_position[pawn0][1])] and (
                   not background.board_move[pawn.black_pawn_position[pawn0][0]][str(pawn.black_pawn_position[pawn0][1] + 1)]):

                    background.board_move[pawn.black_pawn_position[pawn0][0]][str(pawn.black_pawn_position[pawn0][1])] = True
                    background.board_move[pawn.black_pawn_position[pawn0][0]][str(pawn.black_pawn_position[pawn0][1] + 2)] = False
                    pawn.black_pawn_mvs[pawn0][1] = True
                    stats.white_turn = True
                    stats.black_turn = False

                else:
                    pawn.black_pawn_position[pawn0][1] += 2

            elif pawn.black_pawn_mvs[pawn0][2]:
                background.board_move[pawn.black_pawn_position[pawn0][0]][str(pawn.black_pawn_position[pawn0][1])] = True
                background.board_move[chr(ord(pawn.black_pawn_position[pawn0][0]) - 1)][str(pawn.black_pawn_position[pawn0][1] + 1)] = False
                background.board_move[pawn.black_pawn_position[pawn0][0]][str(pawn.black_pawn_position[pawn0][1] + 1)] = False
                pawn.black_pawn_mvs[pawn0][2] = False
                stats.white_turn = True
                stats.black_turn = False

            elif pawn.black_pawn_mvs[pawn0][3]:
                background.board_move[pawn.black_pawn_position[pawn0][0]][str(pawn.black_pawn_position[pawn0][1])] = True
                background.board_move[chr(ord(pawn.black_pawn_position[pawn0][0]) + 1)][str(pawn.black_pawn_position[pawn0][1] + 1)] = False
                background.board_move[pawn.black_pawn_position[pawn0][0]][str(pawn.black_pawn_position[pawn0][1] + 1)] = False
                pawn.black_pawn_mvs[pawn0][3] = False
                stats.white_turn = True
                stats.black_turn = False

def verify_piece_collisions(pawn_position, knight_position, rook_position, bishop_position, queen_position,
                            pawn_death, knight_death, rook_death, bishop_death, queen_death, piece_position, i, j):
    piece_moves = [False, False, False, False, False]
    pms = False

    for key0, pawn0 in pawn_position.items():
        if piece_position[1] + i == pawn0[1] and chr(ord(
                piece_position[0]) + j) == pawn0[0] and not pawn_death[key0]:
            piece_moves[0] = True
            break

    for key0, knight0 in knight_position.items():
        if piece_position[1] + i == knight0[1] and chr(ord(
                piece_position[0]) + j) == knight0[0] and not knight_death[key0]:
            piece_moves[1] = True
            break

    for key0, rook0 in rook_position.items():
        if piece_position[1] + i == rook0[1] and chr(ord(
                piece_position[0]) + j) == rook0[0] and not rook_death[key0]:
            piece_moves[2] = True
            break

    for key0, bishop0 in bishop_position.items():
        if piece_position[1] + i == bishop0[1] and chr(ord(
                piece_position[0]) + j) == bishop0[0] and not bishop_death[key0]:
            piece_moves[3] = True
            break

    if piece_position[1] + i == queen_position[1] and chr(ord(
            piece_position[0]) + j) == queen_position[0] and not queen_death:
        piece_moves[4] = True

    for pm in piece_moves:
        if pm == True:
            pms = True
            break

    return (pms)

def eliminate_killed_piece(piece, piece_position, pawn_position, knight_position, bishop_position, rook_position, queen_position,
                            pawn_death, knight_death, bishop_death, rook_death, queen_death,
                            pawn_rect, knight_rect, bishop_rect, rook_rect, queen_rect,
                            pawn, knight, bishop, rook, queen):

    if piece == "Q":
        for key, pawn1 in pawn_position.items():
            if pawn1[0] == piece_position[0] and pawn1[1] == piece_position[1]:
                pawn_death[key] = True
                pawn_rect[key].center = (
                    pawn.screen_rect.right - 1000, pawn.screen_rect.top)
                pawn.pieces_move.append("Qx" + key + pawn1[0] + str(pawn1[1]))
                print(pawn.pieces_move)
                break

        for key, knight1 in knight_position.items():
            if knight1[1] == piece_position[1] and knight1[0] == piece_position[0]:
                knight_death[key] = True
                knight_rect[key].center = (
                    knight.screen_rect.right - 1000, knight.screen_rect.top)
                pawn.pieces_move.append("Qx" + key + knight1[0] + str(knight1[1]))
                print(pawn.pieces_move)
                break

        for key, bishop1 in bishop_position.items():

            if bishop1[1] == piece_position[1] and bishop1[0] == piece_position[0]:
                bishop_death[key] = True
                bishop_rect[key].center = (
                    bishop.screen_rect.right - 1000, bishop.screen_rect.top)
                pawn.pieces_move.append("Qx" + key + bishop1[0] + str(bishop1[1]))
                print(pawn.pieces_move)
                break

        for key, rook1 in rook_position.items():
            if rook1[1] == piece_position[1] and rook1[0] == piece_position[0]:
                rook_death[key] = True
                rook_rect[key].center = (
                    rook.screen_rect.right - 1000, rook.screen_rect.top)
                pawn.pieces_move.append("Qx" + key + rook1[0] + str(rook1[1]))
                print(pawn.pieces_move)
                break

        if piece_position[1] == queen_position[1] and (piece_position[0] == queen_position[0]):
            queen_death = True
            queen_rect.center = (queen.screen_rect.right - 1000, queen.screen_rect.top)
            pawn.pieces_move.append("QxQ" + queen_position[0]
                                    + str(queen_position[1]))
            print(pawn.pieces_move)

    elif piece == "K":
        for key, pawn1 in pawn_position.items():
            if pawn1[0] == piece_position[0] and pawn1[1] == piece_position[1]:
                pawn_death[key] = True
                pawn_rect[key].center = (
                    pawn.screen_rect.right - 1000, pawn.screen_rect.top)
                pawn.pieces_move.append("Kx" + key + pawn1[0] + str(pawn1[1]))
                print(pawn.pieces_move)
                break

        for key, knight1 in knight_position.items():
            if knight1[1] == piece_position[1] and knight1[0] == piece_position[0]:
                knight_death[key] = True
                knight_rect[key].center = (
                    knight.screen_rect.right - 1000, knight.screen_rect.top)
                pawn.pieces_move.append("Kx" + key + knight1[0] + str(knight1[1]))
                print(pawn.pieces_move)
                break

        for key, bishop1 in bishop_position.items():

            if bishop1[1] == piece_position[1] and bishop1[0] == piece_position[0]:
                bishop_death[key] = True
                bishop_rect[key].center = (
                    bishop.screen_rect.right - 1000, bishop.screen_rect.top)
                pawn.pieces_move.append("Kx" + key + bishop1[0] + str(bishop1[1]))
                print(pawn.pieces_move)
                break

        for key, rook1 in rook_position.items():
            if rook1[1] == piece_position[1] and rook1[0] == piece_position[0]:
                rook_death[key] = True
                rook_rect[key].center = (
                    rook.screen_rect.right - 1000, rook.screen_rect.top)
                pawn.pieces_move.append("Kx" + key + rook1[0] + str(rook1[1]))
                print(pawn.pieces_move)
                break

        if piece_position[1] == queen_position[1] and (piece_position[0] == queen_position[0]):
            queen_death = True
            queen_rect.center = (queen.screen_rect.right - 1000, queen.screen_rect.top)
            pawn.pieces_move.append("KxQ" + queen_position[0] + str(queen_position[1]))
            print(pawn.pieces_move)

    else:
        for key, pawn1 in pawn_position.items():
            if pawn1[0] == piece_position[0] and pawn1[1] == piece_position[1]:
                pawn_death[key] = True
                pawn_rect[key].center = (
                    pawn.screen_rect.right - 1000, pawn.screen_rect.top)
                pawn.pieces_move.append(piece + "x" + key + pawn1[0] + str(pawn1[1]))
                print(pawn.pieces_move)
                break

        for key, knight1 in knight_position.items():
            if knight1[1] == piece_position[1] and knight1[0] == piece_position[0]:
                knight_death[key] = True
                knight_rect[key].center = (
                    knight.screen_rect.right - 1000, knight.screen_rect.top)
                pawn.pieces_move.append(piece + "x" + key + knight1[0] + str(knight1[1]))
                print(pawn.pieces_move)
                break

        for key, bishop1 in bishop_position.items():

            if bishop1[1] == piece_position[1] and bishop1[0] == piece_position[0]:
                bishop_death[key] = True
                bishop_rect[key].center = (
                    bishop.screen_rect.right - 1000, bishop.screen_rect.top)
                pawn.pieces_move.append(piece + "x" + key + bishop1[0] + str(bishop1[1]))
                print(pawn.pieces_move)
                break

        for key, rook1 in rook_position.items():
            if rook1[1] == piece_position[1] and rook1[0] == piece_position[0]:
                rook_death[key] = True
                rook_rect[key].center = (
                    rook.screen_rect.right - 1000, rook.screen_rect.top)
                pawn.pieces_move.append(piece + "x" + key + rook1[0] + str(rook1[1]))
                print(pawn.pieces_move)
                break

        if piece_position[1] == queen_position[1] and (piece_position[0] == queen_position[0]):
            queen_death = True
            queen_rect.center = (queen.screen_rect.right - 1000, queen.screen_rect.top)
            pawn.pieces_move.append(piece + "xQ" + queen_position[0] + str(queen_position[1]))
            print(pawn.pieces_move)
    return (queen_death)

def verify_king_free(p, background, rook, pawn, knight, bishop, queen, king, king_color):

    if king_color == 'w':
        if p == 0:
            for key in rook.black_rook_clicked.keys():
                wking_rook(background, king, rook, key)
        if p == 1:
            for key in bishop.black_bishop_clicked.keys():
                wking_bishop(background, king, bishop, key)
        if p == 2:
            wking_queen(background, king, queen)
        if p == 3:
            for key in knight.black_knight_clicked.keys():
                wking_knight(background, king, knight, key)
        if p == 4:
            for key in pawn.black_pawn_clicked.keys():
                wking_pawn(background, king, pawn, key)
    elif king_color == 'b':
        if p == 0:
            for key in rook.white_rook_clicked.keys():
                bking_rook(background, king, rook, key)
        if p == 1:
            for key in bishop.white_bishop_clicked.keys():
                bking_bishop(background, king, bishop, key)
        if p == 2:
            bking_queen(background, king, queen)
        if p == 3:
            for key in knight.white_knight_clicked.keys():
                bking_knight(background, king, knight, key)
        if p == 4:
            for key in pawn.white_pawn_clicked.keys():
                bking_pawn(background, king, pawn, key)

def piece_check(pieces):
    p = None
    for i in range(len(pieces)):
        if pieces[i]:
            p = i
            break
    return(p)

def verify_king_collision(position, rook_position, pawn_position, knight_position, bishop_position, queen_position):

    if (position == queen_position):
        piece = 'Q'

    for key, rook in rook_position.items():
        if (position == rook):
            piece = key
            break
    for key, pawn in pawn_position.items():
        if (position == pawn):
            piece = key
            break
    for key, knight in knight_position.items():
        if (position == knight):
            piece = key
            break
    for key, bishop in bishop_position.items():
        if (position == bishop):
            piece = key
            break

    return(piece)

def verify_king_safe(piece1_position, check_piece, rook_position, pawn_position, knight_position, bishop_position, queen_position):
    b = False
    if check_piece == 'Q':
        b = check_position(piece1_position, queen_position)

    for key, pawn in pawn_position.items():
        if key == check_piece:
            b = check_position(piece1_position, pawn)

    for key, knight in knight_position.items():
        if key == check_piece:
            b = check_position(piece1_position, knight)

    for key, bishop in bishop_position.items():
        if key == check_piece:
            b = check_position(piece1_position, bishop)

    for key, rook in rook_position.items():
        if key == check_piece:
            b = check_position(piece1_position, rook)

    return(b)

def check_position(piece1_position, piece2_position):
    b = False
    if (piece1_position == piece2_position):
        b = True
    return(b)

def eliminate_check_piece(piece ,check_piece, rook, pawn, knight, bishop, queen, piece_color):
    if piece_color == 'w':

        if check_piece == 'Q':
            queen.white_queen_death = True
            queen.white_queen_rect.center = (queen.screen_rect.right - 1000, queen.screen_rect.top)
            pawn.pieces_move.append(piece + "xQ" + queen.white_queen_position[0] + str(queen.white_queen_position[1]))
            print(pawn.pieces_move)

        for key, pawn0 in pawn.white_pawn_position.items():
            if key == check_piece:
                pawn.white_pawn_death[key] = True
                pawn.white_pawn_rects[key].center = (pawn.screen_rect.right - 1000, pawn.screen_rect.top)
                pawn.pieces_move.append(piece + "x" + key + pawn0[0] + str(pawn0[1]))
                break

        for key, knight0 in knight.white_knight_position.items():
            if key == check_piece:
                knight.white_knight_death[key] = True
                knight.white_knight_rects[key].center = (knight.screen_rect.right - 1000, knight.screen_rect.top)
                pawn.pieces_move.append(piece + "x" + key + knight0[0] + str(knight0[1]))
                break

        for key, bishop0 in bishop.white_bishop_position.items():
            if key == check_piece:
                bishop.white_bishop_death[key] = True
                bishop.white_bishop_rects[key].center = (bishop.screen_rect.right - 1000, bishop.screen_rect.top)
                pawn.pieces_move.append(piece + "x" + key + bishop0[0] + str(bishop0[1]))
                break

        for key, rook0 in rook.white_rook_position.items():
            if key == check_piece:
                rook.white_rook_death[key] = True
                rook.white_rook_rects[key].center = (rook.screen_rect.right - 1000, rook.screen_rect.top)
                pawn.pieces_move.append(piece + "x" + key + rook0[0] + str(rook0[1]))
                break

    elif piece_color == 'b':
        if check_piece == 'Q':
            queen.black_queen_death = True
            queen.black_queen_rect.center = (queen.screen_rect.right - 1000, queen.screen_rect.top)
            pawn.pieces_move.append(piece + "xQ" + queen.black_queen_position[0] + str(queen.black_queen_position[1]))
            print(pawn.pieces_move)

        for key, pawn0 in pawn.black_pawn_position.items():
            if key == check_piece:
                pawn.black_pawn_death[key] = True
                pawn.black_pawn_rects[key].center = (pawn.screen_rect.right - 1000, pawn.screen_rect.top)
                pawn.pieces_move.append(piece + "x" + key + pawn0[0] + str(pawn0[1]))
                break

        for key, knight0 in knight.black_knight_position.items():
            if key == check_piece:
                knight.black_knight_death[key] = True
                knight.black_knight_rects[key].center = (knight.screen_rect.right - 1000, knight.screen_rect.top)
                pawn.pieces_move.append(piece + "x" + key + knight0[0] + str(knight0[1]))
                break

        for key, bishop0 in bishop.black_bishop_position.items():
            if key == check_piece:
                bishop.black_bishop_death[key] = True
                bishop.black_bishop_rects[key].center = (bishop.screen_rect.right - 1000, bishop.screen_rect.top)
                pawn.pieces_move.append(piece + "x" + key + bishop0[0] + str(bishop0[1]))
                break

        for key, rook0 in rook.black_rook_position.items():
            if key == check_piece:
                rook.black_rook_death[key] = True
                rook.black_rook_rects[key].center = (rook.screen_rect.right - 1000, rook.screen_rect.top)
                pawn.pieces_move.append(piece + "x" + key + rook0[0] + str(rook0[1]))
                break





































