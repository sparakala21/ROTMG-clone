import pygame
from settings import *

class Game_Over:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE+30)

    def create(self):
        width = self.display_surface.get_width()
        height = self.display_surface.get_height()
        l = width //4
        t = (height * 4)//6
        w = width // 2
        h = height // 9.5
        retry_rect = pygame.rect.Rect(l, t, w, h)
        (mouseX, mouseY) = pygame.mouse.get_pos()
        color = TEXT_COLOR_SELECTED if retry_rect.collidepoint((mouseX, mouseY)) else TEXT_COLOR
        rect = self.display_surface.get_rect()
        pygame.draw.rect(self.display_surface, 'black', rect)
        title_surf = self.font.render('Game Over', False, TEXT_COLOR)
        title_rect= title_surf.get_rect(midtop = self.display_surface.get_rect().midtop + pygame.math.Vector2(0,60))
        self.display_surface.blit(title_surf, title_rect)

        retry_surf = self.font.render('   Try Again?', False, TEXT_COLOR)
        
        
        pygame.draw.rect(self.display_surface, BAR_COLOR, retry_rect, 4)
        self.display_surface.blit(retry_surf, retry_rect)
        return retry_rect.collidepoint((mouseX, mouseY))

    def display(self):
        if self.create():
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]==True:
                        print('i dont know how to do this yet')
                        

    

