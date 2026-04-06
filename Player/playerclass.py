import pygame

FRAMES_PER_ROW = {0: 4, 1: 3, 2: 4, 3: 4}

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sprite_sheet = pygame.image.load("assets/player.png").convert_alpha()
        
        scale = 0.05
        new_w = int(self.sprite_sheet.get_width() * scale)
        new_h = int(self.sprite_sheet.get_height() * scale)
        self.sprite_sheet = pygame.transform.scale(self.sprite_sheet, (new_w, new_h))



        self.frame_width = (self.sprite_sheet.get_width() // 4) 
        self.frame_height = (self.sprite_sheet.get_height() // 4) 
        self.current_frame = 0
        self.direction_row = 0 # down up left right 
        self.animation_speed = 8
        self.frame_timer = 0


        self.update_image()
        self.rect = self.image.get_rect(topleft=(400, 300))
        self.speed = 5

    def handle_input(self,dt):
        keys = pygame.key.get_pressed()
        is_moving = False

        if keys[pygame.K_w]:
            self.rect.y -= self.speed
            self.direction_row = 1
            is_moving = True
        if keys[pygame.K_s]:
            self.rect.y += self.speed
            self.direction_row = 0
            is_moving = True
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
            self.direction_row = 2
            is_moving = True
        if keys[pygame.K_d]:
            self.rect.x += self.speed
            self.direction_row = 3
            is_moving = True

        
        if is_moving:
            max_frames = FRAMES_PER_ROW[self.direction_row]
            self.current_frame += self.animation_speed
            if self.current_frame >= max_frames:
                self.current_frame = 0
        else:
            self.current_frame = 0
        self.update_image()
            

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update_image(self):
        column = int(self.current_frame)
        row = self.direction_row

        crop_x = column * self.frame_width
        crop_y = row * self.frame_height
        self.image = self.sprite_sheet.subsurface(crop_x, crop_y, self.frame_width, self.frame_height)