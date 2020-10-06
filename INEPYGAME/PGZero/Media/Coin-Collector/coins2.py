#Game Coins Collector
import pgzrun
from random import randint
# define windows size
WIDTH = 800
HEIGHT = 600

#define variable
score = 0
game_over = False
# Create object
fox = Actor('fox')
fox.pos = 100, 100
coin = Actor('coin')


def draw():
    screen.fill('sky blue')
    fox.draw()
    coin.draw()
    screen.draw.text('Score : '+str(score), color='white', topleft=(10, 10))
    if game_over:
        screen.fill('black')
        if score < 5000:
            message = 'You are very NOOB!!!!!! Final Score : '+str(score)
        else:
            message = 'Final Score : '+str(score)
        screen.draw.text(message, topleft=(10, 10), fontsize=50)



def place_coin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))


def update():
    global score
    if keyboard.left:
        fox.x = fox.x - 100
        if fox.x <= 20:
            fox.x = 780
    elif keyboard.right:
        fox.x = fox.x + 100
        if fox.x >= 780:
            fox.x = 20
    elif keyboard.up:
        fox.y = fox.y - 100
        if fox.y <= 30:
            fox.y = 560
    elif keyboard.down:
        fox.y = fox.y + 16
        if fox.y >= 560:
            fox.y = 20

    coin_collected = fox.colliderect(coin)
    if coin_collected:
        place_coin()
        score += 1

def time_up():
    global game_over
    game_over = True

clock.schedule(time_up, 5.0)
place_coin()
pgzrun.go()