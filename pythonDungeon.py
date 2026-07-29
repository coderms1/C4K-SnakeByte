# C4K - SNAKE BYTE: Python Dungeon Game

import pygame
import random
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Python Dungeon")
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()
player = pygame.Rect(375, 275, 40, 40)
enemy = pygame.Rect(100, 100, 40, 40)
apple = pygame.Rect(random.randint(50, 700), random.randint(80, 500), 30, 30)
score = 0
lives = 3
gameOver = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if gameOver and event.key == pygame.K_SPACE:
                player.x = 375
                player.y = 275
                enemy.x = 100
                enemy.y = 100
                score = 0
                lives = 3
                gameOver = False
    if not gameOver:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.x -= 5
        if keys[pygame.K_RIGHT]:
            player.x += 5
        if keys[pygame.K_UP]:
            player.y -= 5
        if keys[pygame.K_DOWN]:
            player.y += 5
        # Keep player on screen
        player.clamp_ip(pygame.Rect(0, 60, 800, 540))
        # Enemy follows player
        if enemy.x < player.x:
            enemy.x += 2
        if enemy.x > player.x:
            enemy.x -= 2
        if enemy.y < player.y:
            enemy.y += 2
        if enemy.y > player.y:
            enemy.y -= 2
        # Apple
        if player.colliderect(apple):
            score += 1
            apple.x = random.randint(30, 740)
            apple.y = random.randint(80, 540)
        # Enemy
        if player.colliderect(enemy):
            lives -= 1
            player.x = 375
            player.y = 275
            enemy.x = random.choice([50, 700])
            enemy.y = random.choice([100, 500])
            pygame.time.delay(500)
        if lives <= 0:
            gameOver = True
    screen.fill("black")
    # Score
    scoreText = font.render("Score: " + str(score), True, "white")
    livesText = font.render("Lives: " + str(lives), True, "red")
    screen.blit(scoreText, (20, 20))
    screen.blit(livesText, (650, 20))
    if not gameOver:
        pygame.draw.rect(screen, "green", player)
        pygame.draw.rect(screen, "purple", enemy)
        pygame.draw.ellipse(screen, "red", apple)
    else:
        gameText = font.render("GAME OVER", True, "red")
        restartText = font.render("Press SPACE to restart", True, "white")
        screen.blit(gameText, (320, 250))
        screen.blit(restartText, (270, 300))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
