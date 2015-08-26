import sys,pygame


def display_bordered_text(screen, msg, pos):
    fobj = pygame.font.SysFont('Lucida Console', 18)
    kpos = fobj.size(msg)
    pygame.draw.line(screen, (255, 255, 255), [pos[0], pos[1]], [pos[0]+kpos[0], pos[1]])
    pygame.draw.line(screen, (255, 255, 255), [pos[0], pos[1]], [pos[0], pos[1]+kpos[1]])
    pygame.draw.line(screen, (255, 255, 255), [pos[0], pos[1]+kpos[1]], [pos[0]+kpos[0], pos[1]+kpos[1]])
    pygame.draw.line(screen, (255, 255, 255), [pos[0]+kpos[0], pos[1]], [pos[0]+kpos[0], pos[1]+kpos[1]])
    if len(msg) != 0:
        screen.blit(fobj.render(msg, 1, (255,255,255)), pos)
    pygame.display.flip()

def display_text(screen, msg, pos):
    fobj = pygame.font.SysFont('Lucida Console', 18)
    kpos = fobj.size(msg)
    if len(msg) != 0:
        screen.blit(fobj.render(msg, 1, (255,255,255)), pos)
    pygame.display.flip()

def draw_game_borders(screen, dims):
    pygame.draw.line(screen, (255, 255, 255), [200, 10], [200, dims[1]-10])
    pygame.draw.line(screen, (255, 255, 255), [200, 10], [dims[0]-10, 10])
    pygame.draw.line(screen, (255, 255, 255), [200, dims[1]-10], [dims[0]-10, dims[1]-10])
    pygame.draw.line(screen, (255, 255, 255), [dims[0]-10, 10], [dims[0]-10, dims[1]-10])
    pygame.draw.line(screen, (255, 255, 255), [10, 10], [190, 10])
    pygame.draw.line(screen, (255, 255, 255), [10, 10], [10, 30])
    pygame.draw.line(screen, (255, 255, 255), [10, 30], [190, 30])
    pygame.draw.line(screen, (255, 255, 255), [190, 10], [190, 30])
    
pygame.init()
dims = width,height = 800,600
speed = [2,2]
black = 0,0,0
white = 255,255,255
score = 0
cWorld = World()

screen = pygame.display.set_mode(dims)
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYUP:
            key = pygame.key.get_pressed()
            if key[pygame.key.K_w]:
                
        screen.fill(black)
        draw_game_borders(screen, dims)
        display_text(screen, 'Score: ' + str(score), [10, 10])
        pygame.display.flip()
        
