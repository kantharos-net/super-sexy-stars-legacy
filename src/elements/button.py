import pygame.font
from typing import List, Tuple

class Button():
    screen: pygame.Surface = None
    message: str = ""
    width: int = 200
    height: int = 50
    button_color: Tuple[int, int, int] = (255, 0, 255)
    text_color: Tuple[int, int, int] = (255, 255, 255)

    def __init__(self,
        screen: pygame.Surface = screen,
        message: str = message,
        width: int = width,
        height: int = height,
        button_color: Tuple[int, int, int] = button_color,
        text_color: Tuple[int, int, int] = text_color
    ):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.width = width
        self.height = height
        self.button_color = button_color
        self.text_color = text_color
        self.font = pygame.font.SysFont('Calibri', 48)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.prep_msg(message)

    # Renders the message displayed in the button.
    def prep_msg(self, message):          
        self.msg_image = self.font.render(message, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    # Draws a button.
    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        