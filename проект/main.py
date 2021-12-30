import pygame
import sqlite3

from Player import Player
from Enemy1 import Enemy1
from Enemy2 import Enemy2
from Room1 import Room1
from Room2 import Room2
from Room3 import Room3
from button import button

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

WIDTH = 800
HEIGHT = 600

# База данных
# ===================================================
conn = sqlite3.connect('rooms.db') #
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS rooms(
   ROOM INT,
   ITERATION INT,
   X INT,
   Y INT,
   WIDTH INT,
   HEIGHT INT);
""")
conn.commit()

# =============================================

def animate(group, game_state):
    group.remove(player)
    if pygame.sprite.spritecollide(player, group, False):
        game_state = 'died'
    group.add(player)
    screen.blit(enemy1.image, enemy1.rect)
    screen.blit(enemy2.image, enemy2.rect)
    return game_state

def menu():
    screen.blit(fon_menu, (0, 0))
    font_menu = pygame.font.SysFont('kristenitc', 55, True)
    name_game = font_menu.render('Tunnels of Despair ', True, pygame.Color('orange'))
    screen.blit(name_game, (110, 120))

    startButton.draw(screen, (0, 0, 0))
    quitButton.draw(screen, (0, 0, 0))
    historyButton.draw(screen, (0, 0, 0))

    pygame.mixer.init()
    pygame.mixer.music.load("anim/3.mp3")
    pygame.mixer.music.play(1)


def redraw_game_window():
    player.groups()
    enemy1.groups()
    enemy2.groups()


def game_over():
    pygame.mixer.music.pause()
    screen.blit(fon_menu, (0, 0))

    saved_font = pygame.font.SysFont('kristenitc', 90)
    game_over_surface = saved_font.render('YOU SAVED', True, RED)
    my_font = pygame.font.SysFont('kristenitc', 50)
    points_surface = my_font.render('DIED:' + str(died_num), True, 'orange')

    time_room1 = my_font.render('time room 1: ' + str(ex1), True, 'RED')
    time_room2 = my_font.render('time room 2: ' + str(ex2), True, 'RED')
    time_room3 = my_font.render('time room 3: ' + str(ex3), True, 'RED')
    sum_time = my_font.render('sum time: ' + str(int(s)), True, 'RED')
    best_time = my_font.render('best time: ' + str(x), True, 'RED')

    game_over_rect = game_over_surface.get_rect()
    points_rect = points_surface.get_rect()

    game_over_rect.midtop = (400, 20)
    points_rect.midleft = (50, 150)
    time_room1_rect = (50, 200)
    time_room2_rect = (50, 250)
    time_room3_rect = (50, 300)
    sum_rect = (50, 350)
    best_rect = (50, 400)

    start_over_Button.draw(screen, (0, 0, 0))
    quitButton.draw(screen, (0, 0, 0))
    screen.blit(game_over_surface, game_over_rect)
    screen.blit(points_surface, points_rect)
    screen.blit(time_room1, time_room1_rect)
    screen.blit(time_room2, time_room2_rect)
    screen.blit(time_room3, time_room3_rect)
    screen.blit(sum_time, sum_rect)
    screen.blit(best_time, best_rect)
    pygame.display.update()


def died():
    pygame.mixer.music.pause()

    screen.blit(fon_menu, (0, 0))
    my_font = pygame.font.SysFont('kristenitc', 90)
    game_over_surface = my_font.render('YOU DIED', True, RED)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (400, 50)
    start_over_Button.draw(screen, (0, 0, 0))
    quitButton.draw(screen, (0, 0, 0))
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.update()


def pause():
    pygame.mixer.music.pause()

    screen.blit(fon_menu, (0, 0))
    my_font = pygame.font.SysFont('kristenitc', 90)
    game_over_surface = my_font.render('PAUSE', True, RED)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (400, 50)
    continueButton.draw(screen, (0, 0, 0))
    quitButton.draw(screen, (0, 0, 0))
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.update()


def history():
    screen.blit(history_fon, (0, 0))
    menuButton.draw(screen, (0, 0, 0))
    pygame.mixer.music.pause()
    pygame.display.update()


pygame.init()
screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption('Tunnels of Despair')
background = pygame.image.load('anim/background.jpg')
fon_menu = pygame.image.load('anim/fon2.png')
history_fon = pygame.image.load('anim/history_fon.jpg')

programIcon = pygame.image.load('anim/icon.png')
pygame.display.set_icon(programIcon)

enemy_group = pygame.sprite.Group()
enemy_image1 = pygame.image.load("anim/medooza.png")
enemy_image2 = pygame.image.load("anim/enemy1.png")
enemy_speed1 = [0, 3]
enemy_speed2 = [0, 4]
player = Player(20, 500)
enemy_group.add(player)

enemy_location1 = [190, 200]
enemy1 = Enemy1(enemy_image1, enemy_location1, enemy_speed1)
enemy_group.add(enemy1)
screen.blit(enemy1.image, enemy1.rect)
enemy_group.add(player)

enemy_location2 = [610, 210]
enemy2 = Enemy2(enemy_image2, enemy_location2, enemy_speed2)
enemy_group.add(enemy2)
screen.blit(enemy2.image, enemy2.rect)
enemy_group.add(player)

rooms = []
room = Room1(cur, conn) #  cur - запросы к БД; conn - соединение с БД;
rooms.append(room)

room = Room2(cur, conn)
rooms.append(room)

room = Room3(cur, conn)
rooms.append(room)

current_room_no = 0
current_room = rooms[current_room_no]

clock = pygame.time.Clock()

startButton = button((0, 100, 80), 50, 250, 250, 100, "Start")
start_over_Button = button((0, 100, 80), 50, 480, 350, 100, "Start over")
quitButton = button((0, 20, 80), 480, 450, 250, 100, "Quit")
continueButton = button((0, 100, 80), 50, 350, 300, 100, "continue")
historyButton = button((0, 100, 80), 50, 400, 250, 100, "story")
menuButton = button((0, 100, 80), 320, 500, 200, 80, "menu")


kol = 1
died_num = 0


def tick(timer_started, start_time):
    timer_started = not timer_started
    if timer_started:
        start_time = pygame.time.get_ticks()
    elif not timer_started:
        results.append(passed_time)
        if len(results) > 10:
            results.pop(0)
    return timer_started, start_time

passed_time = 0
start_time = 0
timer_started = False
results = []

game_state = "menu"
done = False
while not done:

    if game_state == "menu":
        menu()
    elif game_state == "game":
        redraw_game_window()
    elif game_state == "finish":
        game_over()
    elif game_state == "pause":
        pause()
    elif game_state == "died":
        died()
    elif game_state == "history":
        history()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_state = "pause"
                pause()
            if event.key == pygame.K_LEFT:
                player.changespeed(-5, 0)
            if event.key == pygame.K_RIGHT:
                player.changespeed(5, 0)
            if event.key == pygame.K_UP:
                player.changespeed(0, -5)
            if event.key == pygame.K_DOWN:
                player.changespeed(0, 5)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(5, 0)
            if event.key == pygame.K_RIGHT:
                player.changespeed(-5, 0)
            if event.key == pygame.K_UP:
                player.changespeed(0, 5)
            if event.key == pygame.K_DOWN:
                player.changespeed(0, -5)

        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
            quit()
        if game_state == "menu":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if startButton.isover(pos):
                    print("clicked the button")
                    game_state = "game"
                if historyButton.isover(pos):
                    print("clicked the button")
                    game_state = "history"
                if quitButton.isover(pos):
                    print("clicked the 2button")
                    done = True
                    pygame.quit()
                    quit()
            if event.type == pygame.MOUSEMOTION:
                if startButton.isover(pos):
                    startButton.color = (0, 50, 100)
                else:
                    startButton.color = (0, 100, 80)
                if historyButton.isover(pos):
                    historyButton.color = (0, 50, 100)
                else:
                    historyButton.color = (0, 100, 80)
                if quitButton.isover(pos):
                    quitButton.color = (0, 50, 100)
                else:
                    quitButton.color = (0, 20, 80)

        if game_state == "history":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menuButton.isover(pos):
                    print("clicked the button")
                    game_state = "menu"
            pygame.display.update()
            if event.type == pygame.MOUSEMOTION:
                if menuButton.isover(pos):
                    menuButton.color = (0, 50, 100)
                else:
                    menuButton.color = (0, 100, 80)
            pygame.display.update()

        if game_state == "pause":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if continueButton.isover(pos):
                    print("clicked the button")
                    game_state = "game"
                    pygame.mixer.music.unpause()
                if quitButton.isover(pos):
                    print("clicked the 2button")
                    done = True
                    pygame.quit()
                    quit()
            pygame.display.update()
            if event.type == pygame.MOUSEMOTION:
                if continueButton.isover(pos):
                    continueButton.color = (0, 50, 100)
                else:
                    continueButton.color = (0, 100, 80)
                if quitButton.isover(pos):
                    quitButton.color = (0, 50, 100)
                else:
                    quitButton.color = (0, 20, 80)
            pygame.display.update()

        if game_state == "died":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_over_Button.isover(pos):
                    print("clicked the button")
                    game_state = "game"
                    died_num += 1
                    pygame.mixer.music.unpause()
                if quitButton.isover(pos):
                    print("clicked the 2button")
                    done = True
                    pygame.quit()
                    quit()
            pygame.display.update()
            if event.type == pygame.MOUSEMOTION:
                if start_over_Button.isover(pos):
                    start_over_Button.color = (0, 50, 100)
                else:
                    start_over_Button.color = (0, 100, 80)
                if quitButton.isover(pos):
                    quitButton.color = (0, 50, 100)
                else:
                    quitButton.color = (0, 20, 80)
            pygame.display.update()

        if game_state == "finish":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_over_Button.isover(pos):
                    print("clicked the button")
                    game_state = "game"
                    pygame.mixer.music.unpause()
                    died_num = 0
                if quitButton.isover(pos):
                    print("clicked the 2button")
                    done = True
                    pygame.quit()
                    quit()
            pygame.display.update()
            if event.type == pygame.MOUSEMOTION:
                if start_over_Button.isover(pos):
                    start_over_Button.color = (0, 50, 100)
                else:
                    start_over_Button.color = (0, 100, 80)
                if quitButton.isover(pos):
                    quitButton.color = (0, 50, 100)
                else:
                    quitButton.color = (0, 20, 80)
            pygame.display.update()

    player.move(current_room.wall_list)

    # Чтобы игрок спавнился после смерти вначале карты
    # ==========================
    if game_state == "died":
        player.rect.x = 70
        player.rect.y = 500
    if player.rect.x == 50 and player.rect.y == 500:
        timer_started, start_time = tick(timer_started, start_time)
    if player.rect.x == 780:
        timer_started, start_time = tick(timer_started, start_time)

    if player.rect.x > 780:
        if current_room_no == 0:
            current_room_no = 1
            current_room = rooms[current_room_no]
            player.rect.x = 20
            player.rect.y = 500
            kol = 2

        elif current_room_no == 1:
            current_room_no = 2
            current_room = rooms[current_room_no]
            player.rect.x = 20
            player.rect.y = 500
            kol = 3

        else:
            current_room_no = 0
            current_room = rooms[current_room_no]
            player.rect.x = 20
            player.rect.y = 500
            ex1 = float(results[0]/1000)
            ex2 = float(results[1]/1000)
            ex3 = float(results[2]/1000)
            s = ex1 + ex2 + ex3
            x = (min(results)/1000)
            print(x)
            game_state = "finish"

    font_color = pygame.Color(GREEN)
    font = pygame.font.Font('anim/gothic.ttf', 25)
    if timer_started:
        passed_time = pygame.time.get_ticks() - start_time
    for index, result in enumerate(results):
        text = font.render(f'{(result / 1000):.3f}', True, font_color)
        screen.blit(text, (50, 50 + 54 * (len(results) - index)))

    screen.fill(BLACK)
    screen.blit(background, (0, 0))
    font = pygame.font.Font('anim/gothic.ttf', 26)

    game_state = animate(enemy_group, game_state)
    enemy1.move()
    enemy2.move()

    render_score = font.render('УРОВЕНЬ:  ' + str(kol), True, pygame.Color('orange'))
    screen.blit(render_score, (20, 20))
    render_score = font.render('СМЕРТЕЙ:  ' + str(died_num), True, pygame.Color('red'))
    screen.blit(render_score, (20, 45))

    text = font.render(f'{(passed_time / 1000):.3f}', True, font_color)
    screen.blit(text, (20, 70))

    enemy_group.draw(screen)
    current_room.wall_list.draw(screen)
    clock.tick(100)

pygame.quit()
