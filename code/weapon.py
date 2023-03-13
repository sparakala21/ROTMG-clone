import pygame

class Weapon(pygame.sprite.Sprite):
    def __init__(self, player, groups):
        super().__init__(groups)
        self.sprite_type = 'weapon'
        self.direction = player.status.split('_')[0]

        #graphic
        full_path = f'../graphics/weapons/{player.weapon}/{self.direction}.png'
        self.image = pygame.image.load(full_path).convert_alpha()

        self.rect = self.image.get_rect(center = player.rect.center)
        #placement
        if self.direction== 'right':
            self.rect = self.image.get_rect(center = player.rect.midright + pygame.math.Vector2(0,16))
        elif self.direction== 'left':
            self.rect = self.image.get_rect(center = player.rect.midleft + pygame.math.Vector2(0,16))
        elif self.direction== 'down':
            self.rect = self.image.get_rect(center = player.rect.midbottom + pygame.math.Vector2(-10,0))
        else:
            self.rect = self.image.get_rect(center = player.rect.midtop + pygame.math.Vector2(-10,0))
        
