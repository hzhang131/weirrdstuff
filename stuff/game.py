import pygame
import sys

# --- constants ---

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED = (230, 0, 0)
GREEN = (76, 187, 23)
YELLOW = (255, 191, 0)
GRAY = (128,128,128)

# --- main ---

def driver(red = 20000, yellow = 3000, green = 30000):
    pygame.init()
    fenetre = pygame.display.set_mode((400, 760))
    # time in millisecond from start program 
    current_time = pygame.time.get_ticks()

    # how long to show or hide
    delay = [int(red), int(yellow), int(green), int(yellow)] # 500ms = 0.5s
    lights = [(200, 163), (200, 311), (200, 459), (200, 311)]
    # time of next change 
    background_image = pygame.image.load("a.png").convert_alpha()
    background_image = pygame.transform.scale(background_image, (200, 680))
    tuples = [RED, YELLOW, GREEN, YELLOW]
    counter = 0
    change_time = current_time + delay[counter]
    fenetre.fill(WHITE)
    fenetre.blit(background_image, [100,75])
    pygame.draw.circle(fenetre, tuples[counter], (200, 163), 61)
    pygame.draw.circle(fenetre, GRAY, (200, 311), 61)
    pygame.draw.circle(fenetre, GRAY, (200, 459), 61)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # --- updates ---

        current_time = pygame.time.get_ticks()

        # is time to change ?
        if current_time >= change_time:
            # time of next change 
            # show = not show
            counter = (counter + 1) %4
            change_time = current_time + delay[counter]
            # fenetre.fill(tuples[counter])
            pygame.draw.circle(fenetre, GRAY, (200, 163), 61)
            pygame.draw.circle(fenetre, GRAY, (200, 311), 61)
            pygame.draw.circle(fenetre, GRAY, (200, 459), 61)
            pygame.draw.circle(fenetre, tuples[counter], lights[counter], 61)
        # --- draws ---
        pygame.display.update()

if len(sys.argv) == 1:
    driver()
if len(sys.argv) == 2:
    driver(sys.argv[1])
if len(sys.argv) == 3:
    driver(sys.argv[1], sys.argv[2])
if len(sys.argv) == 4:
    driver(sys.argv[1], sys.argv[2], sys.argv[3])
