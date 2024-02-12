import pygame
import pygame.mixer
import time
import sys

current_level_no = 0

screen_with = 800
screen_height = 600

pygame.mixer.init()

pygame.mixer.music.load('files/Хэллоуин-Brawl-Stars.wav')

pygame.mixer.music.play(-1)

bg = pygame.image.load('files/фон2.jpg')


def death():
    pygame.init()

    screen_with1 = 800
    screen_height1 = 600
    screen = pygame.display.set_mode((screen_with1, screen_height1))

    background_image = pygame.image.load('files/фон (1).jpg').convert()

    font = pygame.font.Font(None, 36)
    button_width = 200
    button_height = 50
    button_color = (100, 100, 100)

    button_restart = pygame.Rect((screen_with1 - button_width) // 2, 200, button_width, button_height)

    button_exit = pygame.Rect((screen_with1 - button_width) // 2, 300, button_width, button_height)

    button_menu = pygame.Rect((screen_with1 - button_width) // 2, 400, button_width, button_height)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_restart.collidepoint(event.pos):
                    main()

                elif button_exit.collidepoint(event.pos):

                    running = False
                    pygame.quit()
                    sys.exit()

                elif button_menu.collidepoint(event.pos):
                    press_window()

        screen.blit(background_image, (0, 0))

        pygame.draw.rect(screen, button_color, button_restart)
        pygame.draw.rect(screen, button_color, button_exit)
        pygame.draw.rect(screen, button_color, button_menu)

        text_surface = font.render('Главное меню', True, (255, 255, 255))
        screen.blit(text_surface, (button_menu.x + 20, button_menu.y + 15))
        text_surface = font.render('Выход', True, (255, 255, 255))
        screen.blit(text_surface, (button_exit.x + 55, button_exit.y + 15))
        text_surface = font.render('Заново', True, (255, 255, 255))
        screen.blit(text_surface, (button_restart.x + 60, button_restart.y + 15))

        pygame.display.flip()


def perehod():
    global money_game, current_level_no
    pygame.init()
    file = open("money_game.txt", "w")
    file.write("coins: " + str(k_money))
    file.close()

    screen_with2 = 800
    screen_height2 = 600
    screen = pygame.display.set_mode((screen_with2, screen_height2))

    background_image = pygame.image.load('files/winner.jpg').convert()

    font = pygame.font.Font(None, 36)
    button_width = 200
    button_height = 50
    button_color = (100, 100, 100)

    button_restart = pygame.Rect((screen_with2 - button_width) // 2, 200, button_width, button_height)

    button_exit = pygame.Rect((screen_with2 - button_width) // 2, 300, button_width, button_height)

    button_next = pygame.Rect((screen_with2 - 277) // 2, 400, 255, button_height)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_next.collidepoint(event.pos):
                    current_level_no += 1
                    if current_level_no > 2:
                        final()
                    main()

                elif button_exit.collidepoint(event.pos):

                    running = False
                    pygame.quit()
                    sys.exit()

                elif button_restart.collidepoint(event.pos):
                    press_window()

        screen.blit(background_image, (0, 0))

        pygame.draw.rect(screen, button_color, button_restart)
        pygame.draw.rect(screen, button_color, button_exit)
        pygame.draw.rect(screen, button_color, button_next)

        text_surface = font.render('Главное меню', True, (255, 255, 255))
        screen.blit(text_surface, (button_restart.x + 10, button_restart.y + 15))
        text_surface = font.render('Выход', True, (255, 255, 255))
        screen.blit(text_surface, (button_exit.x + 55, button_exit.y + 15))
        text_surface = font.render('Следующий уровень', True, (255, 255, 255))
        screen.blit(text_surface, (button_next.x -2 , button_next.y + 20))

        f1 = pygame.font.Font(None, 46)
        text1 = f1.render('Монеты за раунд: ' + str(tek_money), 5, (255, 102, 10))
        screen.blit(text1, (250, 150))

        pygame.display.flip()


def final():
    pygame.init()

    # Установка размеров экрана
    screen_with3 = 800
    screen_height3 = 600
    screen = pygame.display.set_mode((screen_with3, screen_height3))

    # Загрузка изображения фона
    background_image = pygame.image.load('files/1 (1).jpg').convert()

    # Создание кнопок
    font = pygame.font.Font(None, 36)
    button_width = 400
    button_height = 100
    button_color = (100, 100, 100)

    button_exit = pygame.Rect((screen_with3 - button_width) // 2, 300, button_width, button_height)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:

                if button_exit.collidepoint(event.pos):
                    running = False
                    pygame.quit()
                    sys.exit()

        screen.blit(background_image, (0, 0))

        pygame.draw.rect(screen, button_color, button_exit)

        text_surface = font.render('Выход', True, (255, 255, 255))
        screen.blit(text_surface, (button_exit.x + 150, button_exit.y + 40))

        pygame.display.flip()


money_game = []
k_money = 0
tek_money = 0


class Player(pygame.sprite.Sprite):
    global money_game, k_money
    right = True

    def __init__(self):

        super().__init__()

        self.image = pygame.image.load('files/project_prizrak .png')

        self.rect = self.image.get_rect()

        self.change_x = 0
        self.change_y = 0
        self.k_money = 0

    def update(self):
        global k_money, tek_money

        self.calc_grav()

        self.rect.x += self.change_x

        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)

        for block in block_hit_list:

            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:

                self.rect.left = block.rect.right

        self.rect.y += self.change_y

        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:

            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            self.change_y = 0

        smoke_hit_list = pygame.sprite.spritecollide(self, self.level.smoke_list, False)

        for _ in smoke_hit_list:
            k_money = 0
            death()

        finish_hit_list = pygame.sprite.spritecollide(self, self.level.finish_list, False)

        for _ in finish_hit_list:
            perehod()

        money_hit_list = pygame.sprite.spritecollide(self, self.level.money_list,
                                                     True)

        for _ in money_hit_list:
            self.k_money += 1

            money_game.append(self.k_money)
            k_money += 1
            money_game.append(k_money)

            tek_money = self.k_money

    def calc_grav(self):

        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .95

        if self.rect.y >= screen_height - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = screen_height - self.rect.height

    def jump(self):

        self.rect.y += 10
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 10

        if len(platform_hit_list) > 0 or self.rect.bottom >= screen_height:
            self.change_y = -14.5

    def go_left(self):

        self.change_x = -9
        if self.right:
            self.flip()
            self.right = False

    def go_right(self):

        self.change_x = 9
        if not self.right:
            self.flip()
            self.right = True

    def stop(self):

        self.change_x = 0

    def flip(self):

        self.image = pygame.transform.flip(self.image, True, False)


class Smoke(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.images = [pygame.image.load('files/smoke_game1 (1).png').convert_alpha(),
                       pygame.image.load('files/smoke_game3 (1).png').convert_alpha(),
                       pygame.image.load('files/smoke_game4 (1).png').convert_alpha(),
                       pygame.image.load('files/smoke_game5 (1).png').convert_alpha(),
                       pygame.image.load('files/smoke_game6 (1).png').convert_alpha(),
                       pygame.image.load('files/smoke_game7 (1).png').convert_alpha()]

        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.image.set_colorkey((255, 255, 255))
        self.image.set_colorkey((255, 255, 255))
        self.image.set_colorkey((255, 255, 255))
        self.image.set_colorkey((255, 255, 255))
        self.image.set_colorkey((255, 255, 255))
        self.image.set_colorkey((255, 255, 255))
        self.image.set_colorkey((255, 255, 255))

        self.animation_speed = 0.005
        self.current_time = 0

        self.smoke_speed = 1
        self.start_time = time.time()

    def update(self):
        self.current_time += 1
        if self.current_time >= self.animation_speed * 1000:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

        elapsed_time = time.time() - self.start_time
        if elapsed_time > 7:
            self.rect.y -= self.smoke_speed


class Platform(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()

        self.image = pygame.image.load('files/платфор-transformed.png')

        self.rect = self.image.get_rect()


class Finish(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()

        self.image = pygame.image.load('files/original_flag (1).png')

        self.rect = self.image.get_rect()


class Money(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.images = [pygame.image.load('files/pngwing.com (1) (1).png').convert_alpha(),
                       pygame.image.load('files/pngwing.com (2) (1).png').convert_alpha(),
                       pygame.image.load('files/pngwing.com (3) (1).png').convert_alpha(),
                       pygame.image.load('files/pngwing.com (4) (1).png').convert_alpha(),
                       pygame.image.load('files/pngwing.com (5) (1).png').convert_alpha(),
                       pygame.image.load('files/pngwing.com (6) (1).png').convert_alpha()]
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()

        self.animation_speed = 0.005
        self.current_time = 0

    def update(self):
        self.current_time += 1
        if self.current_time >= self.animation_speed * 1000:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]


class Level(object):
    def __init__(self, player):
        self.platform_list = pygame.sprite.Group()

        self.smoke_list = pygame.sprite.Group()
        self.finish_list = pygame.sprite.Group()
        self.money_list = pygame.sprite.Group()
        self.player = player

    def update(self):
        self.platform_list.update()
        self.smoke_list.update()
        self.finish_list.update()
        self.money_list.update()

    def draw(self, screen):
        screen.blit(bg, (0, 0))

        self.platform_list.draw(screen)
        self.smoke_list.draw(screen)
        self.finish_list.draw(screen)
        self.money_list.draw(screen)


class Level01(Level):
    def __init__(self, player):

        Level.__init__(self, player)

        level = [
            [210, 32, 10, 570],
            [210, 32, 100, 470],
            [210, 32, 10, 370],
            [210, 32, 250, 470],
            [210, 32, 350, 370],
            [210, 32, 700, 430],
            [210, 32, 800, 500],
            [210, 32, 500, 400],
            [210, 32, 750, 350],
            [210, 32, 600, 250],
            [210, 32, 450, 200],
            [210, 32, 270, 200],
            [210, 32, 100, 265],
            [210, 32, 450, 550],
            [210, 32, 350, 100], ]

        smoke_level = [
            [30, 30, 0, 650],
            [30, 30, 30, 650],
            [30, 30, 60, 650],
            [30, 30, 90, 650],
            [30, 30, 120, 650],
            [30, 30, 150, 650],
            [30, 30, 180, 650],
            [30, 30, 210, 650],
            [30, 30, 240, 650],
            [30, 30, 270, 650],
            [30, 30, 300, 650],
            [30, 30, 330, 650],
            [30, 30, 360, 650],
            [30, 30, 390, 650],
            [30, 30, 420, 650],
            [30, 30, 450, 650], [30, 30, 480, 650], [30, 30, 510, 650], [30, 30, 540, 650], [30, 30, 570, 650],
            [30, 30, 600, 650], [30, 30, 630, 650], [30, 30, 660, 650], [30, 30, 690, 650], [30, 30, 720, 650],
            [30, 30, 750, 650], [30, 30, 780, 650], [30, 30, 810, 650],

        ]

        finish = [[75, 75, 340, 45]]

        money_level = [[30, 30, 10, 345],
                       [30, 30, 700, 400],

                       [30, 30, 120, 550],
                       [30, 30, 105, 235],
                       [30, 30, 255, 440],
                       [30, 30, 210, 550],
                       [30, 30, 455, 520],
                       [30, 30, 500, 370],
                       [30, 30, 755, 320]]

        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        for platform in smoke_level:
            block1 = Smoke(platform[0], platform[1])
            block1.rect.x = platform[2]
            block1.rect.y = platform[3]
            block1.player = self.player
            self.smoke_list.add(block1)

        for platform in finish:
            block1 = Finish(platform[0], platform[1])
            block1.rect.x = platform[2]
            block1.rect.y = platform[3]
            block1.player = self.player
            self.finish_list.add(block1)

        for platform in money_level:
            block2 = Money(platform[0], platform[1])
            block2.rect.x = platform[2]
            block2.rect.y = platform[3]
            block2.player = self.player
            self.money_list.add(block2)


class Level02(Level):
    def __init__(self, player):

        Level.__init__(self, player)

        smoke_level = [
            [30, 30, 0, 650],
            [30, 30, 30, 650],
            [30, 30, 60, 650],
            [30, 30, 90, 650],
            [30, 30, 120, 650],
            [30, 30, 150, 650],
            [30, 30, 180, 650],
            [30, 30, 210, 650],
            [30, 30, 240, 650],
            [30, 30, 270, 650],
            [30, 30, 300, 650],
            [30, 30, 330, 650],
            [30, 30, 360, 650],
            [30, 30, 390, 650],
            [30, 30, 420, 650],
            [30, 30, 450, 650], [30, 30, 480, 650], [30, 30, 510, 650], [30, 30, 540, 650], [30, 30, 570, 650],
            [30, 30, 600, 650], [30, 30, 630, 650], [30, 30, 660, 650], [30, 30, 690, 650], [30, 30, 720, 650],
            [30, 30, 750, 650], [30, 30, 780, 650], [30, 30, 810, 650]

        ]

        level = [
            [210, 32, 250, 550],
            [210, 32, 100, 500],
            [210, 32, 10, 450],
            [210, 32, 150, 350],
            [210, 32, 250, 400],
            [210, 32, 350, 450],
            [210, 32, 450, 500],
            [210, 32, 550, 550],
            [210, 32, 770, 500],
            [210, 32, 600, 400],
            [210, 32, 500, 300],
            [210, 32, 400, 200],
            [210, 32, 300, 100],
            [210, 32, 200, 50],
            [210, 32, 600, 200]

        ]

        money_level = [
            [75, 75, 50, 500],
            [75, 75, 100, 400],
            [75, 75, 200, 300],
            [75, 75, 300, 300],
            [75, 75, 450, 200],
            [75, 75, 600, 100],

            [75, 75, 550, 520],
            [75, 75, 350, 150],
            [75, 75, 250, 250],
            [75, 75, 700, 50],
            [75, 75, 760, 470]
        ]

        finish = [[75, 75, 190, -5]]

        for platform in money_level:
            block2 = Money(platform[0], platform[1])
            block2.rect.x = platform[2]
            block2.rect.y = platform[3]
            block2.player = self.player
            self.money_list.add(block2)

        for platform in finish:
            block1 = Finish(platform[0], platform[1])
            block1.rect.x = platform[2]
            block1.rect.y = platform[3]
            block1.player = self.player
            self.finish_list.add(block1)

        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        for platform in smoke_level:
            block1 = Smoke(platform[0], platform[1])
            block1.rect.x = platform[2]
            block1.rect.y = platform[3]
            block1.player = self.player
            self.smoke_list.add(block1)


class Level03(Level):
    def __init__(self, player):

        Level.__init__(self, player)

        level = [
            [210, 32, 600, 550],
            [210, 32, 750, 500],
            [210, 32, 600, 450],
            [210, 32, 450, 400],
            [210, 32, 300, 350],
            [210, 32, 150, 300],
            [210, 32, 10, 250],
            [210, 32, 150, 150],
            [210, 32, 300, 100],
            [210, 32, 450, 100],
            [210, 32, 700, 100],
            [210, 32, 600, 250],
            [210, 32, 700, 300]

        ]
        smoke_level = [
            [30, 30, 0, 650],
            [30, 30, 30, 650],
            [30, 30, 60, 650],
            [30, 30, 90, 650],
            [30, 30, 120, 650],
            [30, 30, 150, 650],
            [30, 30, 180, 650],
            [30, 30, 210, 650],
            [30, 30, 240, 650],
            [30, 30, 270, 650],
            [30, 30, 300, 650],
            [30, 30, 330, 650],
            [30, 30, 360, 650],
            [30, 30, 390, 650],
            [30, 30, 420, 650],
            [30, 30, 450, 650], [30, 30, 480, 650], [30, 30, 510, 650], [30, 30, 540, 650], [30, 30, 570, 650],
            [30, 30, 600, 650], [30, 30, 630, 650], [30, 30, 660, 650], [30, 30, 690, 650], [30, 30, 720, 650],
            [30, 30, 750, 650], [30, 30, 780, 650], [30, 30, 810, 650],

        ]

        finish = [[75, 75, 440, 45]]

        money_level = [[30, 30, 0, 600],
                       [30, 30, 30, 550],
                       [30, 30, 60, 550],
                       [30, 30, 90, 550],
                       [30, 30, 120, 550],
                       [30, 30, 150, 550],
                       [30, 30, 180, 550],
                       [30, 30, 210, 550],
                       [30, 30, 240, 550],
                       [30, 30, 750, 470],
                       [30, 30, 15, 220],
                       [30, 30, 305, 320],
                       [30, 30, 155, 120],
                       ]

        for platform in money_level:
            block2 = Money(platform[0], platform[1])
            block2.rect.x = platform[2]
            block2.rect.y = platform[3]
            block2.player = self.player
            self.money_list.add(block2)

        for platform in finish:
            block1 = Finish(platform[0], platform[1])
            block1.rect.x = platform[2]
            block1.rect.y = platform[3]
            block1.player = self.player
            self.finish_list.add(block1)

        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        for platform in smoke_level:
            block1 = Smoke(platform[0], platform[1])
            block1.rect.x = platform[2]
            block1.rect.y = platform[3]
            block1.player = self.player
            self.smoke_list.add(block1)


# Основная функция прогарммы
def main():
    global current_level_no

    pygame.init()

    size = [screen_with, screen_height]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Ghost Hunting")

    player = Player()

    level_list = list()
    level_list.append(Level03(player))
    level_list.append(Level01(player))
    level_list.append(Level02(player))

    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    player.rect.x = 340
    player.rect.y = screen_height - player.rect.height
    active_sprite_list.add(player)

    done = False

    clock = pygame.time.Clock()

    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()

        active_sprite_list.update()

        current_level.update()

        if player.rect.right > screen_with:
            player.rect.right = screen_with

        if player.rect.left < 0:
            player.rect.left = 0

        current_level.draw(screen)
        active_sprite_list.draw(screen)

        clock.tick(45)

        pygame.display.flip()

    sys.exit()


def press_window():
    global current_level_no

    pygame.init()
    bg1 = pygame.image.load('files/превью (1).jpg')

    window_size = (800, 540)
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Ghost Hunting")

    white = (255, 255, 255)
    button_color = (117, 117, 117)

    font = pygame.font.Font(None, 36)

    text1 = font.render('level 1', True, white)
    text2 = font.render('level 2', True, white)
    text3 = font.render('level 3', True, white)

    # Размеры кнопок
    button_width = 150
    button_height = 100

    button_x1 = 100
    button_x2 = 300
    button_x3 = 500
    button_y = (window_size[1] - button_height) / 2

    text_x1 = button_x1 + (button_width - text1.get_width()) / 2
    text_x2 = button_x2 + (button_width - text2.get_width()) / 2
    text_x3 = button_x3 + (button_width - text3.get_width()) / 2
    text_y = button_y + (button_height - text1.get_height()) / 2

    screen.blit(bg1, (1, 0))

    pygame.draw.rect(screen, button_color, (button_x1, button_y, button_width, button_height))
    screen.blit(text1, (text_x1, text_y))

    pygame.draw.rect(screen, button_color, (button_x2, button_y, button_width, button_height))
    screen.blit(text2, (text_x2, text_y))

    pygame.draw.rect(screen, button_color, (button_x3, button_y, button_width, button_height))
    screen.blit(text3, (text_x3, text_y))

    # Основной игровой цикл
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                if button_x1 <= mouse_pos[0] <= button_x1 + button_width and button_y <= mouse_pos[1] \
                        <= button_y + button_height:
                    current_level_no = 0
                    main()

                if button_x2 <= mouse_pos[0] <= button_x2 + button_width and button_y <= mouse_pos[1] \
                        <= button_y + button_height:
                    current_level_no = 1
                    main()
                if button_x3 <= mouse_pos[0] <= button_x3 + button_width and button_y <= mouse_pos[1] \
                        <= button_y + button_height:
                    current_level_no = 2
                    main()
        pygame.display.flip()

    pygame.quit()


press_window()
