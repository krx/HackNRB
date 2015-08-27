import sys, pygame, math, time, serial
from serial import SerialException
from World import *
import threading
# current_milli_time = lambda: int(round(time.time() * 1000))


def display_bordered_text(screen, msg, pos):
    fobj = pygame.font.SysFont('Lucida Console', 18)
    kpos = fobj.size(msg)
    pygame.draw.line(screen, (255, 255, 255), [pos[0], pos[1]], [pos[0] + kpos[0], pos[1]])
    pygame.draw.line(screen, (255, 255, 255), [pos[0], pos[1]], [pos[0], pos[1] + kpos[1]])
    pygame.draw.line(screen, (255, 255, 255), [pos[0], pos[1] + kpos[1]], [pos[0] + kpos[0], pos[1] + kpos[1]])
    pygame.draw.line(screen, (255, 255, 255), [pos[0] + kpos[0], pos[1]], [pos[0] + kpos[0], pos[1] + kpos[1]])
    if len(msg) != 0:
        screen.blit(fobj.render(msg, 1, (255, 255, 255)), pos)
    pygame.display.flip()


def display_text(screen, msg, pos):
    fobj = pygame.font.SysFont('Lucida Console', 18)
    kpos = fobj.size(msg)
    if len(msg) != 0:
        screen.blit(fobj.render(msg, 1, (255, 255, 255)), pos)


def display_center_text(screen, msg, dims, offs):
    fobj = pygame.font.SysFont('Lucida Console', 18)
    kpos = fobj.size(msg)
    if len(msg) != 0:
        screen.blit(fobj.render(msg, 1, (255, 255, 255)), [dims[0] / 2 - kpos[0] / 2, dims[1] / 2 - kpos[1] / 2 + offs])


def draw_game_borders(screen, dims):
    pygame.draw.line(screen, (255, 255, 255), [200, 10], [200, dims[1] - 10])
    pygame.draw.line(screen, (255, 255, 255), [200, 10], [dims[0] - 10, 10])
    pygame.draw.line(screen, (255, 255, 255), [200, dims[1] - 10], [dims[0] - 10, dims[1] - 10])
    pygame.draw.line(screen, (255, 255, 255), [dims[0] - 10, 10], [dims[0] - 10, dims[1] - 10])
    pygame.draw.line(screen, (255, 255, 255), [10, 10], [190, 10])
    pygame.draw.line(screen, (255, 255, 255), [10, 10], [10, 30])
    pygame.draw.line(screen, (255, 255, 255), [10, 30], [190, 30])
    pygame.draw.line(screen, (255, 255, 255), [190, 10], [190, 30])



def serialRead(ser, bytes=1):
    return ser.read(bytes).decode() if ser else 0


def serialWrite(ser, bytes):
    if ser:
        ser.write(bytes.encode())


pygame.init()
dims = width, height = 800, 600
speed = [2, 2]
black = 0, 0, 0
white = 255, 255, 255
score = 0
gameStage = 2
starfield = [[706, 326, 0, 3], [388, 112, 0, 6], [136, 366, 0, 5], [408, 68, 0, 5], [516, 229, 0, 4], [772, 493, 0, 3],
             [368, 568, 0, 7], [487, 533, 0, 6], [396, 532, 0, 3], [493, 10, 0, 2]]
ticks = pygame.time.get_ticks()
last_ticks = pygame.time.get_ticks()
sineticks = pygame.time.get_ticks()
pi = 4.0 * math.atan(1.0)
lastExplosion = 0
isExploding = 0
lastScore = 0

s = None
try:
    s = serial.Serial('COM6', 9600, timeout=.001)
except SerialException:
    print("Failed to connect to serial")

q = ''
running = True
def serialThread():
    global q
    while running:
        q = serialRead(s)

threading.Thread(target=serialThread).start()

screen = pygame.display.set_mode(dims)

world = World(pygame.Rect(201, 11, 579, 579), 49, 48)
snake = world.snake

baseInterval = 100
updateInterval = baseInterval // snake.length
# lastUpdate = current_milli_time()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        if gameStage == 0:
            if event.type == pygame.KEYDOWN:
                key = pygame.key.get_pressed()
                if key[pygame.K_a] or key[pygame.K_LEFT]:
                    snake.turnLeft()
                elif key[pygame.K_d] or key[pygame.K_RIGHT]:
                    snake.turnRight()
                elif key[pygame.K_KP8] and snake.speed != Dir.DOWN:
                    snake.setDirection(Dir.UP)
                elif key[pygame.K_KP6] and snake.speed != Dir.LEFT:
                    snake.setDirection(Dir.RIGHT)
                elif key[pygame.K_KP2] and snake.speed != Dir.UP:
                    snake.setDirection(Dir.DOWN)
                elif key[pygame.K_KP4] and snake.speed != Dir.RIGHT:
                    snake.setDirection(Dir.LEFT)
        if gameStage == 1 or gameStage == 2:
            if event.type == pygame.KEYDOWN:
                score = 0
                gameStage = 0
                world = World(pygame.Rect(201, 11, 579, 579), 49, 48)
                snake = world.snake

    screen.fill(black)
    if gameStage == 0:
        draw_game_borders(screen, dims)
        display_text(screen, 'Score: ' + str(score), [10, 10])
    if gameStage == 1:
        display_center_text(screen, 'You have lost.', dims, -15)
        display_center_text(screen, 'Press ANY KEY to try again.', dims, 15)
    if gameStage == 2:
        display_center_text(screen, 'Welcome to SNAKE.', dims, -15)
        display_center_text(screen, 'Press ANY KEY to begin.', dims, 15)
    if gameStage == 0:
        # q = serialRead(s)
        # print("READ: {}".format(q))
        if q == 'U' and snake.speed != Dir.DOWN:
            snake.setDirection(Dir.UP)
        if q == 'D' and snake.speed != Dir.UP:
            snake.setDirection(Dir.DOWN)
        if q == 'L' and snake.speed != Dir.RIGHT:
            snake.setDirection(Dir.LEFT)
        if q == 'R' and snake.speed != Dir.LEFT:
            snake.setDirection(Dir.RIGHT)

        for particle in world.particles:
            particle.update()
            particle.draw(screen)
            x, y = particle.pos
            if x < 0 or x > width or y < 0 or y > width:
                world.particles.remove(particle)
    last_ticks = pygame.time.get_ticks()
    # if last_ticks - ticks > 100:
    # ticks = last_ticks
    u = 0
    for star in starfield:
        if last_ticks - ticks > 50:
            u = 1
            if gameStage == 0:
                star[1] -= star[3] + int(0.25 * score)
                star[0] += int(5.0 * (score + 1) * 0.5 * math.sin((2.0 * pi) * last_ticks / 5000.0))
            if gameStage == 1 or gameStage == 2:
                star[1] -= star[3]
                star[0] += int(5.0 * math.sin((2.0 * pi) * last_ticks / 5000.0))
            if star[1] > dims[1]:
                star[1] -= dims[1]
            if star[1] < 0:
                star[1] += dims[1]
            if star[0] > dims[0]:
                star[0] -= dims[0]
            if star[0] < 0:
                star[0] += dims[0]
        if gameStage == 1 or gameStage == 2:
            pygame.draw.line(screen, (255, 255, 255), [star[0], star[1]], [star[0], star[1] + 1])
        if gameStage == 0:
            if star[0] < dims[0] - 10 and star[0] > 200 and star[1] < dims[1] - 10 and star[1] > 10:
                pygame.draw.line(screen, (255, 255, 255), [star[0], star[1]], [star[0], star[1] + 1])
    if u == 1:
        ticks = last_ticks
    if gameStage == 0:
        if score != lastScore:
            lastScore = score
            serialWrite(s, 'M')
        if score % 5 == 0 and score > 0 and isExploding == 0:
            lastExplosion = last_ticks
            isExploding = 1
            serialWrite(s, 'A')
            serialWrite(s, 'R')
        if isExploding == 1:
            # for x in range(0, dims[0]):
            #     for y in range(0, dims[1]):
            c = pygame.Color(0)
            c.hsva = ((int(last_ticks)) % 360, 90, 90, 100)
            # pygame.draw.rect(screen, c, pygame.Rect(0, 0, width, height))

            sur = pygame.Surface((width, height))
            sur.set_alpha(128)
            sur.fill(c)
            screen.blit(sur, (0,0))
            if last_ticks - lastExplosion > 1000:
                serialWrite(s, 'B')
                isExploding = 2
        if isExploding == 2 and score % 5 != 0:
            isExploding = 0

        world.draw(screen)
        # if current_milli_time() - lastUpdate >= updateInterval:
        world.update()
        # lastUpdate = current_milli_time()
        if snake.dead:
            serialWrite(s, 'K')
            gameStage = 1
    score = (snake.length - 1) // 2;
    pygame.display.flip()
