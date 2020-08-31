import pygame.font
from typing import Tuple

class LogScreen():
    width: int = 0
    height: int = 0
    position_x: int = 0
    position_y: int = 0
    log_text: str = ""
    text_font: str = ""
    text_size: int = 0
    screen: pygame.Surface = None
    log_screen_color: Tuple[int, int, int] = (0, 0, 0)
    log_screen_text_color: Tuple[int, int, int] = (0, 0, 0)

    def __init__(self,
        width: int = width,
        height: int = height,
        position_x: int = position_x,
        position_y: int = position_y,
        log_text: str = log_text,
        text_font: str = text_font,
        text_size: int = text_size,
        screen: pygame.Surface = screen,
        log_screen_color: Tuple[int, int, int] = log_screen_color,
        log_screen_text_color: Tuple[int, int, int] = log_screen_text_color
    ):
        self.screen = screen
        self.width = width
        self.height = height
        self.log_text = log_text
        self.log_screen_color = log_screen_color
        self.log_screen_text_color = log_screen_text_color

        self.font = pygame.font.SysFont(text_font, text_size)
        self.log_screen_rect = pygame.Rect(
            (self.position_x, self.position_y),
            (self.width, self.height)
        )
    
    def create_log_image_text_render(self) -> None:
        msg_image = self.font.render(
            self.log_text, 
            True, 
            self.log_screen_text_color, 
            self.log_screen_color
        )
        msg_image_rect = msg_image.get_rect()
        msg_image_rect.topright = self.log_screen_rect.topright

        return msg_image, msg_image_rect

    def draw_log_screen(self) -> None:
        self.screen.fill(
            color = self.log_screen_color,
            rect = self.log_screen_rect
        )

        msg_image, msg_image_rect = self.create_log_image_text_render()
        self.screen.blit(
            source = msg_image,
            dest = msg_image_rect
        )