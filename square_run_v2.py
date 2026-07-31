import pygame
import random
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Square Escape")
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()
player = pygame.Rect(375, 275, 40, 40)
enemies = [pygame.Rect(100, 100, 40, 30)]
bullet = pygame.Rect(0, 0, 8, 15)
apple = pygame.Rect(random.randint(50, 700), random.randint(80, 500), 30, 30)
score = 0
lives = 3
gameOver = False
running = True
appleStreak = 0
bulletReady = False
bulletActive = False
showRules = True

def moveEnemy():
    for enemy in enemies:
        if enemy.x < player.x:
            enemy.x += 2
        if enemy.x > player.x:
            enemy.x -= 2
        if enemy.y < player.y:
            enemy.y += 2
        if enemy.y > player.y:
            enemy.y -= 2
def resetGame():
    player.topleft = (375, 375)
    bullet.topleft = (0, 0)
    return 0, 3, False, [pygame.Rect(100, 100, 30, 30)], 0, False, False
while showRules:
    screen.fill("black")
    titleText = font.render("SQUARE ESCAPE", True, "blue")
    rule1 = font.render("5 apples: + 1 Life", True, "green")
    rule2 = font.render("10 apples: + 1 Enemy & + 1 Bullet", True, "red")
    rule3 = font.render("Press SPACE to Shoot", True, "white")
    startText = font.render("Press Any Key to Begin!", True, "yellow")
    screen.blit(titleText, (280, 140))
    screen.blit(rule1, (205, 220))
    screen.blit(rule2, (180, 270))
    screen.blit(rule3, (220, 320))
    screen.blit(startText, (225, 430))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            showRules = False
            running = False
        if event.type == pygame.KEYDOWN:
            showRules = False
    clock.tick(60)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if gameOver and event.key == pygame.K_SPACE:
                score, lives, gameOver, enemies, appleStreak, bulletReady, bulletActive = resetGame()
            elif not gameOver and event.key == pygame.K_SPACE and bulletReady and not bulletActive:
                bullet.x = player.x + 16
                bullet.y = player.y 
                bulletActive = True
                bulletReady = False
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
        player.clamp_ip(pygame.Rect(0, 60, 800, 540))
        moveEnemy()
        for i in range(len(enemies)):
            for x in range(i + 1, len(enemies)):
                if enemies[i].colliderect(enemies[x]):
                    enemies[x].x += 20
                    enemies[x].y += 20
        if bulletActive: 
            bullet.y -= 8
            if bullet.y < 60:
                bulletActive = False
        for enemy in enemies:
            if bulletActive and bullet.colliderect(enemy):
                enemy.x = random.choice([50, 700])
                enemy.y = random.choice([100, 700])
                bulletActive = False
                break
        if player.colliderect(apple):
            score += 1
            appleStreak += 1
            apple.x = random.randint(30, 740)
            apple.y = random.randint(80, 540)
            if score % 5 == 0:
                lives += 1
            if appleStreak == 10:
                bulletReady = True
                appleStreak = 0
                enemies.append(pygame.Rect(random.randint(50, 700), random.randint(100, 500), 40, 30))
        for enemy in enemies:    
            if player.colliderect(enemy):
                lives -= 1
                appleStreak = 0
                player.topleft = (375, 275)
                enemy.x = random.choice([50, 700])
                enemy.y = random.choice([100, 500])
                pygame.time.delay(500)
        if lives <= 0:
            gameOver = True
    screen.fill("black")
    pygame.draw.line(screen, "white", (0, 60), (800, 60), 2)
    scoreText = font.render(f"Score: {score}", True, "white")
    livesText = font.render(f"Lives: {lives}", True, "red")
    if bulletReady:
        bulletText = font.render("Bullet: Ready!", True, "yellow")
    else:
        bulletText = font.render(f"Bullet: {appleStreak}/10", True, "yellow")
    screen.blit(scoreText, (20, 20))
    screen.blit(bulletText, (300, 20))
    screen.blit(livesText, (650, 20))
    if not gameOver:
        pygame.draw.rect(screen, "green", player)
        pygame.draw.ellipse(screen, "red", apple)
        for enemy in enemies:
            pygame.draw.rect(screen, "purple", enemy)
        if bulletActive:
            pygame.draw.rect(screen, "yellow", bullet)
    else:
        gameText = font.render("GAME OVER", True, "red")
        restartText = font.render("Press SPACE to restart", True, "white")
        screen.blit(gameText, (320, 250))
        screen.blit(restartText, (270, 300))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
