import pygame, os
import time
import random
os.environ['SDL_VIDEO_CENTERED'] = '1'          # centrowanie okna
pygame.init()


screen_size = width, height = 1920, 1080
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Labirynt')
clock = pygame.time.Clock()
pygame.font.init()

#poziomy

level1 = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,1,1,1,1,0,0,0,0,1,1,1,1,0,0,0,0,0],
    [0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,1,1,1],
    [0,0,1,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0],
    [0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
    [0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,1,1,1,1,0,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
]
level2 = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,0,0,0,0,1,1,1,1,1,0,0],
    [0,0,1,1,1,1,1,1,1,0,0,1,0,0,0,0,0,0],
    [0,0,0,0,1,0,0,0,1,1,1,1,0,0,0,0,0,0],
    [0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0],
    [1,1,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
]

level3 = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
    [1,1,1,1,1,0,0,0,1,1,1,1,0,0,0,0,0,0],
    [0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,1,0,0,0,1,0,0,0,0,0,1,1,1,1],
    [0,0,0,0,1,0,0,0,1,1,1,1,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
]

levels = [level1,level2,level3]
level = random.choice(levels)

class Player(pygame.sprite.Sprite):
    def __init__(self, file_image):
        super().__init__()
        self.image = file_image
        self.rect = self.image.get_rect()
        
        self.movement_x = 0
        self.movement_y = 0

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def go_right(self):
        self.movement_x = 60
    
    def go_left(self):
        self.movement_x = -60

    def go_up(self):
        self.movement_y = -60

    def go_down(self):
        self.movement_y = 60

    def stop(self):
        self.movement_x = 0
        self.movement_y = 0

    def update(self):
        self.rect.x += self.movement_x
        self.rect.y += self.movement_y

        if self.rect.colliderect(0,0,390,1000):
            self.rect.x = first_room_x
            self.rect.y = first_room_y

        if self.rect.colliderect(1470,0,1800,1000):
            self.rect.x = 1410
            self.rect.y = last_room_y
            

        #zmiana grafiki przy ruchu

        if self.movement_x > 0:
            self.image = pygame.image.load(os.path.join('game2', 'player_1.png'))

        if self.movement_x < 0:
            self.image = pygame.image.load(os.path.join('game2', 'player_3.png'))

        if self.movement_y > 0:
            self.image = pygame.image.load(os.path.join('game2', 'player_2.png'))

        if self.movement_y < 0:
            self.image = pygame.image.load(os.path.join('game2', 'player_4.png'))

        # wykrywanie kolizji

        for rock in rocks:
            if self.rect.colliderect(rock.rect):
                if self.movement_x > 0: 
                    self.rect.right = rock.rect.left
                if self.movement_x < 0: 
                    self.rect.left = rock.rect.right
                if self.movement_y > 0: 
                    self.rect.bottom = rock.rect.top
                if self.movement_y < 0: 
                    self.rect.top = rock.rect.bottom

    def get_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                self.go_right()
            if event.key == pygame.K_a:
                self.go_left()
            if event.key == pygame.K_w:
                self.go_up()
            if event.key == pygame.K_s:
                self.go_down()

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d and self.movement_x > 0:
                self.stop()
            if event.key == pygame.K_a and self.movement_x < 0:
                self.stop()
            if event.key == pygame.K_w and self.movement_y < 0:
                self.stop()
            if event.key == pygame.K_s and self.movement_y > 0:
                self.stop()


class Text(pygame.sprite.Sprite):
    def __init__(self,text):
        self.text = text
        self.my_font = pygame.font.SysFont('Arial Black', 80)
        self.textsurface = self.my_font.render(self.text, False, (255, 255, 255))
        screen.blit(self.textsurface,(750,70))




rocks = []

class Wall:
    def __init__(self, pos):
        rocks.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 60, 60)

start_x, start_y = 390, 190
    
for y in level:
    for x in y:

        if x == 0:
            Wall((start_x,start_y))
        start_x += 60

    start_x = 390
    start_y += 60

hidden_blocks = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
]

#klasa elementów labiryntu

class Plate(pygame.sprite.Sprite):

    def __init__(self,plate_type,x,y,player,hidden):
        self.plate_type = plate_type
        self.hidden = hidden

        #sprawdzanie czy blok jest ukryty czy nie

        if (player.rect.x == x-60 and player.rect.y == y) or (player.rect.x == x+60 and player.rect.y == y) or (player.rect.x == x and player.rect.y == y+60) or (player.rect.x == x and player.rect.y == y-60) or (player.rect.x == x and player.rect.y == y) or (self.hidden == 1):
            if self.plate_type == 0:
                self.image = pygame.image.load(os.path.join('game2', 'rock.png'))
                self.hidden = 1
            elif self.plate_type == 1:
                self.image = pygame.image.load(os.path.join('game2', 'yellow.png'))
                self.hidden = 1
        else:
            self.image = pygame.image.load(os.path.join('game2', 'black.png'))
            hidden = 0

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self,surface):
        surface.blit(self.image, self.rect)

# konkretyzacja obiektów
player = Player(pygame.image.load(os.path.join('game2', 'player_2.png')))


first, last = True, True
# głowna pętla gry
window_open = True
while window_open:
    screen.blit(pygame.image.load(os.path.join('game2', 'maze.png')), [0,0])
    # pętla zdarzeń
    for event in pygame.event.get():
        player.get_event(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                window_open = False
        elif event.type == pygame.QUIT:
            window_open = False

    # rysowanie i aktualizacja obiektów

    start_x, start_y = 390, 190
    
    hidden_x, hidden_y = 0, 0


    #rysowanie labiryntu
    for y in level:
        for x in y:

            if first == True and y[0] == 1:
                first_room_x = start_x
                first_room_y = start_y
                player.rect.x, player.rect.y = first_room_x, first_room_y
                first = False

            if last == True and y[17] == 1:
                last_room_y = start_y
                last = False
            
            plate = Plate(x,start_x,start_y,player,hidden_blocks[hidden_y][hidden_x])
            plate.draw(screen)
            
            #zapisywanie które bloki zostały pokazane
            hidden_blocks[hidden_y][hidden_x] = plate.hidden

            start_x += 60
            hidden_x += 1

        start_x = 390
        start_y += 60
        hidden_x = 0
        hidden_y += 1

    player.update()
    player.draw(screen)
    if player.rect.x == 1410 and player.rect.y == last_room_y:
        text = Text("Wygrałeś!")
    
    

    # aktualizacja okna pygame
    pygame.display.flip()
    clock.tick(15)

pygame.quit()