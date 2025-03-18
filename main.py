#Github: https://github.com/indr3kk/Ylessane4Pall/blob/a2191c7db4c49e0c7d81914b7ec00c3b3da9654e/main.py#L1
import pygame, sys , random

#pygame.init()


# värvid
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
lGreen = [153, 255, 153]
lBlue = [153, 204, 255]

# ekraani seaded
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Animeerimine")
screen.fill(lBlue)
clock = pygame.time.Clock()

# graafika laadimine
ball = pygame.image.load("ball.png")

#koordinaatide loomine ja lisamine massiivi
coords = []
for i in range (10):
    posX = random.randint(1,screenX)
    posY = random.randint(1,screenY)
    speed = random.randint(1,5)
    coords.append([posX, posY, speed])

# kiirus ja asukoht
posX, posY = 0, 0
speedX, speedY = 3, 4

gameover = False
while not gameover:

    # fps
    clock.tick(60)
    # mängu sulgemine ristist
    events = pygame.event.get()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    # pildi lisamine ekraanile
    screen.blit(ball, (posX, posY))

    posX += speedX
    posY += speedY

    # loendist koordinaadid
    for i in range(len(coords)):
        pygame.draw.rect(screen, red, [coords[i][0], coords[i][1], 20, 20])
        coords[i][1] += coords[i][2]
        # kui jõuab alla, siis muudame ruduu alguspunkti
        if coords[i][1] > screenY:
            coords[i][1] = random.randint(-40, -10)
            coords[i][0] = random.randint(0, screenX)
    # kui puudub ääri, siis muudab suunda
    if posX > screenX - ball.get_rect().width or posX < 0:
        speedX = -speedX

    if posY > screenY - ball.get_rect().height or posY < 0:
        speedY = -speedY

    # graafika kuvamine ekraanil
    pygame.display.flip()
    screen.fill(lBlue)

pygame.quit()