import pygame
import random

# START
pygame.init()

# SCREEN
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Square Escape")

# TEXT
font=pygame.font.Font(None,36)
clock=pygame.time.Clock()

# PLAYER
player=pygame.Rect(375,275,25,25)

# ENEMIES
enemies=[pygame.Rect(100,100,40,30)]
enemyTimers=[0]

# BULLET
bullet=pygame.Rect(0,0,8,15)

# APPLE
apple=pygame.Rect(
    random.randint(50,700),
    random.randint(80,500),
    random.randint(30,50),
    random.randint(30,50)
)

# SCORE
score=0
lives=3

# MESSAGES
message=""
messageTimer=0

# SWITCHES
bulletReady=False
bulletActive=False
gameOver=False
running=True
showRules=True


# CHASE
def moveEnemy():
    for i in range(len(enemies)):
        if enemyTimers[i]==0:
            enemy=enemies[i]

            if enemy.x<player.x:
                enemy.x+=2
            if enemy.x>player.x:
                enemy.x-=2
            if enemy.y<player.y:
                enemy.y+=2
            if enemy.y>player.y:
                enemy.y-=2


# RESET
def resetGame():
    player.topleft=(375,275)
    bullet.topleft=(0,0)

    return (
        0,
        3,
        False,
        [pygame.Rect(100,100,40,30)],
        [0],
        False,
        False,
        "",
        0
    )


# RULES
while showRules:
    screen.fill("black")

    titleText=font.render("SQUARE ESCAPE",True,"blue")
    rule1=font.render("5 apples: +1 Life",True,"green")
    rule2=font.render("10 apples: +1 Enemy and Bullet",True,"red")
    rule3=font.render("SPACE removes an enemy for 10 seconds",True,"white")
    startText=font.render("Press Any Key to Begin!",True,"yellow")

    screen.blit(titleText,(280,140))
    screen.blit(rule1,(275,220))
    screen.blit(rule2,(180,270))
    screen.blit(rule3,(125,320))
    screen.blit(startText,(225,430))

    pygame.display.flip()

    # EVENTS
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            showRules=False
            running=False

        if event.type==pygame.KEYDOWN:
            showRules=False

    clock.tick(60)


# LOOP
while running:

    # EVENTS
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        if event.type==pygame.KEYDOWN:

            # RESTART
            if gameOver and event.key==pygame.K_SPACE:
                (
                    score,
                    lives,
                    gameOver,
                    enemies,
                    enemyTimers,
                    bulletReady,
                    bulletActive,
                    message,
                    messageTimer
                )=resetGame()

            # SHOOT
            elif (
                not gameOver
                and event.key==pygame.K_SPACE
                and bulletReady
                and not bulletActive
            ):
                bullet.x=player.x+8
                bullet.y=player.y
                bulletActive=True
                bulletReady=False


    # PLAY
    if not gameOver:

        # KEYS
        keys=pygame.key.get_pressed()

        # MOVE
        if keys[pygame.K_LEFT]:
            player.x-=5
        if keys[pygame.K_RIGHT]:
            player.x+=5
        if keys[pygame.K_UP]:
            player.y-=5
        if keys[pygame.K_DOWN]:
            player.y+=5

        # WALLS
        player.clamp_ip(pygame.Rect(0,60,800,530))

        # HUNT
        moveEnemy()


        # RESPAWN
        for i in range(len(enemies)):
            if enemyTimers[i]>0:
                enemyTimers[i]-=1

                if enemyTimers[i]==0:
                    enemies[i].x=random.choice([50,700])
                    enemies[i].y=random.choice([100,500])


        # SEPARATE
        for i in range(len(enemies)):
            for x in range(i+1,len(enemies)):
                if (
                    enemyTimers[i]==0
                    and enemyTimers[x]==0
                    and enemies[i].colliderect(enemies[x])
                ):
                    enemies[x].x+=20
                    enemies[x].y+=20


        # FLY
        if bulletActive:
            bullet.y-=8

            if bullet.y<60:
                bulletActive=False


        # HIT
        for i in range(len(enemies)):
            if (
                enemyTimers[i]==0
                and bulletActive
                and bullet.colliderect(enemies[i])
            ):
                enemyTimers[i]=600
                bulletActive=False
                break


        # EAT
        if player.colliderect(apple):

            score+=1

            apple.x=random.randint(30,740)
            apple.y=random.randint(80,510)


            # MILESTONES
            if score%10==0:

                messages=[
                    "Level 10! Nice work!",
                    "Level 20! You're cooking!",
                    "Level 30! Okay, you're actually good.",
                    "Level 40! Someone has free time...",
                    "Level 50! Certified try-hard.",
                    "Level 60! Your chair misses sunlight.",
                    "Level 70! The apples fear you.",
                    "Level 80! This is becoming concerning.",
                    "Level 90! Please blink occasionally.",
                    "GO TAKE A SHOWER!"
                ]

                messageNumber=score//10

                if messageNumber<=len(messages):
                    message=messages[messageNumber-1]
                else:
                    message="GO TAKE A SHOWER!"

                messageTimer=180
                bulletReady=True

                enemies.append(
                    pygame.Rect(
                        random.randint(50,700),
                        random.randint(100,500),
                        40,
                        30
                    )
                )

                enemyTimers.append(0)


            # BONUS
            if score%5==0:
                lives+=1


        # DAMAGE
        for i in range(len(enemies)):
            if (
                enemyTimers[i]==0
                and player.colliderect(enemies[i])
            ):
                lives-=1

                player.topleft=(375,275)

                enemies[i].x=random.choice([50,700])
                enemies[i].y=random.choice([100,500])

                pygame.time.delay(500)
                break


        # COOKED
        if lives<=0:
            gameOver=True


    # ERASE
    screen.fill("black")

    # BORDER
    pygame.draw.line(screen,"white",(0,60),(800,60),2)

    # SCOREBOARD
    scoreText=font.render(f"Score: {score}",True,"white")
    livesText=font.render(f"Lives: {lives}",True,"red")

    if bulletReady:
        bulletText=font.render("Bullet: READY!",True,"yellow")
    else:
        bulletText=font.render(f"Bullet: {score%10}/10",True,"yellow")

    screen.blit(scoreText,(20,20))
    screen.blit(bulletText,(300,20))
    screen.blit(livesText,(650,20))


    # TRASH-TALK
    if messageTimer>0:
        messageText=font.render(message,True,"cyan")
        messageRect=messageText.get_rect(center=(400,560))
        screen.blit(messageText,messageRect)

        messageTimer-=1
    else:
        message=""


    # DRAW
    if not gameOver:

        # HERO
        pygame.draw.rect(screen,"green",player)

        # SNACK
        pygame.draw.ellipse(screen,"red",apple)

        # VILLAINS
        for i in range(len(enemies)):
            if enemyTimers[i]==0:
                enemy=enemies[i]

                pygame.draw.polygon(
                    screen,
                    "purple",
                    [
                        (enemy.x+20,enemy.y),
                        (enemy.x,enemy.y+30),
                        (enemy.x+40,enemy.y+30)
                    ]
                )

        # PEW-PEW
        if bulletActive:
            pygame.draw.rect(screen,"yellow",bullet)

    else:

        # DEFEAT
        gameText=font.render("GAME OVER",True,"red")
        restartText=font.render("Press SPACE to restart",True,"white")

        screen.blit(gameText,(320,250))
        screen.blit(restartText,(270,300))


    # UPDATE
    pygame.display.flip()
    clock.tick(60)


# GOODBYE
pygame.quit()
