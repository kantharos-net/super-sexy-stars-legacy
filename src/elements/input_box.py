from typing import Tuple

import pygame


class InputBox():
    standard_text: str = ""
    width: int = 0
    height: int = 0
    text: str = ""
    text_font: str = ""
    text_size: int = 0
    max_character: int = 0
    position_x: int = 0
    position_y: int = 0
    border_size: int = 0
    screen: pygame.Surface = None
    background_color: Tuple[int, int, int] = (0, 0, 0)
    border_color: Tuple[int, int, int] = (0, 0, 0)
    active_color: Tuple[int, int, int] = (0, 0, 0)
    inactive_color: Tuple[int, int, int] = (0, 0, 0)
    text_color: Tuple[int, int, int] = (0, 0, 0)
    active: bool = False
    m_hover: bool = False
    m_hover_active: bool = False
    name_assigned: bool = False

    def __init__(self,
                 standard_text: str = standard_text,
                 text: str = text,
                 width: int = width,
                 height: int = height,
                 position_x: int = position_x,
                 position_y: int = position_y,
                 text_font: str = text_font,
                 text_size: int = text_size,
                 max_character: int = max_character,
                 border_size: int = border_size,
                 border_color: Tuple[int, int, int] = border_color,
                 screen: pygame.Surface = screen,
                 active_color: Tuple[int, int, int] = active_color,
                 inactive_color: Tuple[int, int, int] = inactive_color,
                 text_color: Tuple[int, int, int] = text_color
                 ):

        self.standard_text = standard_text
        self.text = text
        self.screen = screen
        self.width = width
        self.height = height
        self.max_character = max_character
        self.border_size = border_size
        self.background_color = inactive_color
        self.active_color = active_color
        self.inactive_color = inactive_color
        self.text_color = text_color
        self.border_color = border_color
        self.position_x = position_x
        self.position_y = position_y
        self.active = False
        self.m_hover = False
        self.m_hover_active = False

        self.font = pygame.font.SysFont(text_font, text_size)

        self.inputbox_border_rect = pygame.Rect(
            (self.position_x, self.position_y),
            (self.width, self.height)
        )

        self.inputbox_rect = pygame.Rect(
            (self.position_x+self.border_size, self.position_y+self.border_size),
            (self.width-2*self.border_size, self.height-2*self.border_size)
        )

    def create_inputbox_render(self) -> Tuple[pygame.Surface, pygame.Rect]:
        if (self.text == "" or self.text == self.standard_text) and not self.active:
            self.text = self.standard_text

        msg_image: pygame.Surface = self.font.render(
            self.text,
            True,
            self.text_color,
            self.background_color
        )
        msg_image_rect: pygame.Rect = msg_image.get_rect()
        msg_image_rect.center = self.inputbox_rect.center

        return msg_image, msg_image_rect

    def mouse_hover(self, mouse_x: int, mouse_y: int) -> bool:
        return self.inputbox_rect.collidepoint(mouse_x, mouse_y)

    def draw_inputbox(self) -> None:

        self.screen.fill(
            color=self.border_color,
            rect=self.inputbox_border_rect
        )

        self.screen.fill(
            color=self.background_color,
            rect=self.inputbox_rect
        )

        msg_image, msg_image_rect = self.create_inputbox_render()
        self.screen.blit(
            source=msg_image,
            dest=msg_image_rect
        )

    def update_inputbox(self, mouse_x: int, mouse_y: int, event: pygame.event) -> str:
        self.m_hover = self.mouse_hover(mouse_x, mouse_y)

        if self.m_hover and not self.m_hover_active and not self.active:
            self.background_color = self.active_color
            self.m_hover_active = True
            self.draw_inputbox()
            pygame.display.flip()
        elif not self.m_hover and self.m_hover_active and not self.active:
            self.background_color = self.inactive_color
            self.m_hover_active = False
            self.draw_inputbox()
            pygame.display.flip()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.m_hover and not self.active:
                self.active = True
                self.text = ''
            elif not self.m_hover and self.active:
                self.active = False

        if event.type == pygame.KEYDOWN:
            if self.active:
                if  event.key == pygame.K_RETURN:
                    self.name_assigned = True
                    print(self.text)
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if len(self.text) < self.max_character:
                        self.text += event.unicode
            self.draw_inputbox()
            pygame.display.flip()

        return self.text
