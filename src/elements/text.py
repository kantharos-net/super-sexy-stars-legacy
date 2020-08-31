import pygame.font
from typing import Tuple

class Text():
    text: str = ""
    width: int = 0
    height: int = 0
    text_font: str = ""
    text_size: int = 0
    position_x: int = 0
    position_y: int = 0
    screen: pygame.Surface = None
    text_color: Tuple[int, int, int] = (0, 0, 0)

    def __init__(self,
        text: str = text,
        width: int = width,
        height: int = height,
        position_x: int = position_x,
        position_y: int = position_y,
        text_font: str = text_font,
        text_size: int = text_size,
        screen: pygame.Surface = screen,
        text_color: Tuple[int, int, int] = text_color

    ):
        self.text = text
        self.screen = screen
        self.width = width
        self.height = height
        self.text_color = text_color
        self.position_x = position_x
        self.position_y = position_y

        self.font = pygame.font.SysFont(text_font, text_size)
        self.text_rect = pygame.Rect(
            (self.position_x, self.position_y),
            (self.width, self.height)
        )
    
    def create_text_render(self) -> Tuple[pygame.Surface, pygame.Rect]:
        msg_image: pygame.Surface = self.font.render(
            self.text, 
            True, 
            self.text_color
        )
        msg_image_rect: pygame.Rect = msg_image.get_rect()
        msg_image_rect.center = self.text_rect.center

        return msg_image, msg_image_rect

    def draw_text(self) -> None:
        msg_image, msg_image_rect = self.create_text_render()
        self.screen.blit(
            source = msg_image,
            dest = msg_image_rect
        )