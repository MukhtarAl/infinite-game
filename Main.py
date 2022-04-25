import pygame
Window = pygame.display.set_mode((960, 540))
WHITE = (255,255,255)
Window.fill(WHITE)

Character = pygame.image.load("darkcharacter.png")
Character = pygame.transform.scale(Character, (70,70))
Window.blit(Character, (50,300))
CharacterPosition = (50,300)
pygame.display.update()

def KEYCHECK(KEYS):
    if KEYS[pygame.K_s] or KEYS[pygame.K_DOWN]:
        Character = pygame.image.load("darkjump.png")
    if KEYS[pygame.K_d] or KEYS[pygame.K_RIGHT]:
        Character = CharacterPosition[0] + 1
    if KEYS[pygame.K_a] or KEYS[pygame.K_LEFT]:
        Character = CharacterPosition[0] - 1
    if KEYS[pygame.K_SPACE] or KEYS[pygame.K_UP]:
        Character = CharacterPosition[1] + 1
    #if KEYS[pygame.K_LSHIFT]:
5
running = True
while running == True:
    KEYS = pygame.key.get_pressed()
    KEYCHECK(KEYS)

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False