import pygame.font

class Button:

    def __init__(self, screen, settings):

        self.settings = settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.width, self.height = 100, 75
        self.text_color1 = (255, 255, 255)
        self.text_color2 = (60, 60, 60)
        self.font = pygame.font.SysFont(None, 48)

        self.rect1 = pygame.Rect(0, 0, self.width, self.height)
        self.rect2 = pygame.Rect(0, 0, 495, 90)
        self.player1_rect = pygame.Rect(0, 0, self.width, self.height)
        self.player2_rect = pygame.Rect(0, 0, self.width, self.height)
        self.endgame1_rect = pygame.Rect(0, 0, self.width, self.height)
        self.endgame2_rect = pygame.Rect(0, 0, self.width, self.height)
        self.draw_rect = pygame.Rect(0, 0, self.width, self.height)
        self.replay_rect = pygame.Rect(0, 0, self.width, self.height)
        self.main_menu_rect = pygame.Rect(0, 0, self.width, self.height)


        #QUIT_button_rect coordinates
        self.rect1.left = self.screen_rect.left
        self.rect1.bottom = self.screen_rect.bottom


        #PLAY_button_rect coordinates
        self.rect2.left = self.screen_rect.left + 220
        self.rect2.bottom = self.screen_rect.bottom - 220
        self.rect2.x, self.rect2.y = (self.screen_rect.width/2) - 295, (self.screen_rect.height/2) + 40

        #Replay rect_coordinates
        self.replay_rect.center = self.screen_rect.center

        #Main_Menu rect_coordinates
        self.main_menu_rect.x, self.main_menu_rect.y = self.replay_rect.x, self.replay_rect.y - 100

        self.quit_button_on = False
        self.play_button_on = False

        self.player1_on = True
        self.player2_on = False

        self.menu_button_on = False
        self.replay_button_on = False

    def prep_msg(self):

        if not self.quit_button_on:
            self.button_color1 = self.settings.button_color[0]
        else:
            self.button_color1 = self.settings.button_color[1]

        if self.quit_button_on:
            self.msg1_image = self.font.render("QUIT", True, self.text_color1, self.settings.green)
        else:
            self.msg1_image = self.font.render("QUIT", True, self.text_color1, (255, 132, 132))

        self.msg1_rect = self.msg1_image.get_rect()


        self.msg1_rect.center = self.rect1.center


    def prep_replay_main_menu_msgs(self):

        if not self.replay_button_on:
            self.button_color5 = self.settings.blue
        else:
            self.button_color5 = self.settings.button_color[1]

        if not self.menu_button_on:
            self.button_color6 = self.settings.blue
        else:
            self.button_color6 = self.settings.button_color[1]

        self.replay_msg = self.font.render("REPLAY", True, self.text_color1, self.button_color5)
        self.replay_msg_rect = self.player2_image.get_rect()

        self.main_menu_msg = self.font.render("MENU", True, self.text_color1, self.button_color6)
        self.main_menu_msg_rect = self.player1_image.get_rect()

        self.replay_msg_rect.center = self.replay_rect.center
        self.main_menu_msg_rect.center = self.main_menu_rect.center
        self.main_menu_msg_rect.x = self.main_menu_msg_rect.x + 10


    def prep_draw(self):

        self.draw_msg = self.font.render("Draw", True, self.text_color2, self.settings.bg_color)
        self.draw_msg_rect = self.draw_msg.get_rect()
        self.draw_msg_rect.center = self.draw_rect.center

    def draw_quit_button(self):
        if self.quit_button_on:
            pygame.draw.rect(self.screen, self.settings.green, (self.rect1.x, self.rect1.y, self.width, self.height))
        else:
            pygame.draw.rect(self.screen, (255, 132, 132), (self.rect1.x, self.rect1.y, self.width, self.height))

        self.screen.blit(self.msg1_image, self.msg1_rect)

    def draw_draw_msg(self):
        self.screen.fill(self.settings.bg_color, self.draw_rect)
        self.screen.blit(self.draw_msg, self.draw_msg_rect)

    def draw_main_menu_buttom(self):
        self.screen.fill(self.button_color5, self.main_menu_rect)
        self.screen.blit(self.main_menu_msg, self.main_menu_msg_rect)

    def draw_main_replay_button(self):
        self.screen.fill(self.button_color6, self.replay_rect)
        self.screen.blit(self.replay_msg, self.replay_msg_rect)
