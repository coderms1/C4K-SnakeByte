# C4K - SNAKE BYTE: Python Dungeon Game


import pygame
import random

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Dungeon")

clock = pygame.time.Clock()

font = pygame.font.Font(None, 36)
bigFont = pygame.font.Font(None, 72)

playerX = 375
playerY = 275

playerSize = 40
playerSpeed = 5

score = 0
lives = 3

appleX = random.randint(50, 700)
appleY = random.randint(80, 500)

enemyX = 100
enemyY = 100

enemySize = 40
enemySpeed = 2

powerX = random.randint(50, 700)
powerY = random.randint(80, 500)

powerSize = 30
powerActive = False
powerTimer = 0

gameOver = False


def resetGame():
    global playerX
    global playerY
    global enemyX
    global enemyY
    global appleX
    global appleY
    global powerX
    global powerY
    global score
    global lives
    global playerSpeed
    global powerActive
    global gameOver

    playerX = 375
    playerY = 275

    enemyX = 100
    enemyY = 100

    appleX = random.randint(50, 700)
    appleY = random.randint(80, 500)

    powerX = random.randint(50, 700)
    powerY = random.randint(80, 500)

    score = 0
    lives = 3

    playerSpeed = 5

    powerActive = False

    gameOver = False


running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if gameOver and event.key == pygame.K_SPACE:
                resetGame()


    if not gameOver:

        keys = pygame.key.get_pressed()


        # PLAYER MOVEMENT

        if keys[pygame.K_LEFT]:
            playerX -= playerSpeed

        if keys[pygame.K_RIGHT]:
            playerX += playerSpeed

        if keys[pygame.K_UP]:
            playerY -= playerSpeed

        if keys[pygame.K_DOWN]:
            playerY += playerSpeed


        # SCREEN BOUNDARIES

        if playerX < 0:
            playerX = 0

        if playerX > WIDTH - playerSize:
            playerX = WIDTH - playerSize

        if playerY < 60:
            playerY = 60

        if playerY > HEIGHT - playerSize:
            playerY = HEIGHT - playerSize


        # ENEMY CHASES PLAYER

        if enemyX < playerX:
            enemyX += enemySpeed

        if enemyX > playerX:
            enemyX -= enemySpeed

        if enemyY < playerY:
            enemyY += enemySpeed

        if enemyY > playerY:
            enemyY -= enemySpeed


        # COLLISION BOXES

        playerRect = pygame.Rect(
            playerX,
            playerY,
            playerSize,
            playerSize
        )

        appleRect = pygame.Rect(
            appleX,
            appleY,
            30,
            30
        )

        enemyRect = pygame.Rect(
            enemyX,
            enemyY,
            enemySize,
            enemySize
        )

        powerRect = pygame.Rect(
            powerX,
            powerY,
            powerSize,
            powerSize
        )


        # APPLE COLLISION

        if playerRect.colliderect(appleRect):

            score += 1

            appleX = random.randint(30, WIDTH - 60)
            appleY = random.randint(80, HEIGHT - 60)


        # POWER-UP COLLISION

        if playerRect.colliderect(powerRect):

            powerActive = True
            playerSpeed = 9

            powerTimer = pygame.time.get_ticks()

            powerX = -100
            powerY = -100


        # POWER-UP TIMER

        if powerActive:

            currentTime = pygame.time.get_ticks()

            if currentTime - powerTimer > 5000:

                playerSpeed = 5
                powerActive = False

                powerX = random.randint(30, WIDTH - 60)
                powerY = random.randint(80, HEIGHT - 60)


        # ENEMY COLLISION

        if playerRect.colliderect(enemyRect):

            lives -= 1

            playerX = 375
            playerY = 275

            enemyX = random.choice([50, 700])
            enemyY = random.choice([100, 500])

            pygame.time.delay(500)


        # GAME OVER

        if lives <= 0:
            gameOver = True


    # BACKGROUND

    screen.fill((20, 25, 35))


    # TOP SCORE BAR

    pygame.draw.rect(
        screen,
        (10, 15, 25),
        (0, 0, WIDTH, 60)
    )


    scoreText = font.render(
        "Score: " + str(score),
        True,
        "white"
    )

    livesText = font.render(
        "Lives: " + str(lives),
        True,
        "red"
    )

    screen.blit(scoreText, (20, 15))
    screen.blit(livesText, (650, 15))


    if not gameOver:

        # APPLE

        pygame.draw.circle(
            screen,
            "red",
            (appleX + 15, appleY + 15),
            15
        )

        pygame.draw.rect(
            screen,
            "green",
            (appleX + 13, appleY - 3, 5, 8)
        )


        # POWER-UP

        if not powerActive:

            pygame.draw.circle(
                screen,
                "yellow",
                (powerX + 15, powerY + 15),
                15
            )

            powerText = font.render(
                "!",
                True,
                "black"
            )

            screen.blit(
                powerText,
                (powerX + 9, powerY - 2)
            )


        # ENEMY

        pygame.draw.rect(
            screen,
            "purple",
            (enemyX, enemyY, enemySize, enemySize),
            border_radius=8
        )

        pygame.draw.circle(
            screen,
            "white",
            (int(enemyX + 12), int(enemyY + 14)),
            6
        )

        pygame.draw.circle(
            screen,
            "white",
            (int(enemyX + 28), int(enemyY + 14)),
            6
        )

        pygame.draw.circle(
            screen,
            "black",
            (int(enemyX + 12), int(enemyY + 14)),
            3
        )

        pygame.draw.circle(
            screen,
            "black",
            (int(enemyX + 28), int(enemyY + 14)),
            3
        )


        # PYTHON SNAKE PLAYER

        pygame.draw.circle(
            screen,
            "green",
            (int(playerX + 18), int(playerY + 22)),
            18
        )

        pygame.draw.circle(
            screen,
            "lime",
            (int(playerX + 28), int(playerY + 16)),
            14
        )

        pygame.draw.circle(
            screen,
            "white",
            (int(playerX + 32), int(playerY + 11)),
            4
        )

        pygame.draw.circle(
            screen,
            "black",
            (int(playerX + 33), int(playerY + 11)),
            2
        )

        pygame.draw.line(
            screen,
            "red",
            (playerX + 40, playerY + 20),
            (playerX + 48, playerY + 20),
            3
        )


        # SPEED MESSAGE

        if powerActive:

            boostText = font.render(
                "SPEED BOOST!",
                True,
                "yellow"
            )

            screen.blit(boostText, (300, 15))


    else:

        gameOverText = bigFont.render(
            "GAME OVER",
            True,
            "red"
        )

        finalScoreText = font.render(
            "Final Score: " + str(score),
            True,
            "white"
        )

        restartText = font.render(
            "Press SPACE to play again",
            True,
            "yellow"
        )

        screen.blit(
            gameOverText,
            (235, 210)
        )

        screen.blit(
            finalScoreText,
            (315, 300)
        )

        screen.blit(
            restartText,
            (245, 350)
        )


    pygame.display.flip()

    clock.tick(60)


pygame.quit()
