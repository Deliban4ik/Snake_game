import pygame as pg
from random import randint

clock=pg.time.Clock()

pg.init()
field_x=608
field_y=608
screen=pg.display.set_mode((field_x,field_y),pg.RESIZABLE)
pg.display.set_caption("SNAKE GAME")
icon=pg.image.load("images/snake_icon.png")
pg.display.set_icon(icon)
running=True

field=pg.image.load("images/snake_field.png")
head=[pg.image.load("images/sprites/head_vert.png"),
    pg.image.load("images/sprites/head_right.png"),
    pg.image.load("images/sprites/head_down.png"),
    pg.image.load("images/sprites/head_left.png")
]
body=[pg.image.load("images/sprites/long_vert.png"),
    pg.image.load("images/sprites/long_gor.png")
]
side=pg.image.load("images/sprites/up-right.png")
apple=pg.image.load("images/apple.png")

font_game=pg.font.Font("fonts/mainfont.ttf",30)
points=0


head_position,body_position=0,0


snake_speed=76

snake_y,body_y=0,76
snake_x,body_x=0,0
bg_y=0
apple_x=randint(0,7)
apple_y=randint(0,7)
print((apple_x,apple_y))
while running:
    counter=font_game.render(f"{points}",True,"Black")
    keys=pg.key.get_pressed()
    
    
    screen.blit(field,(0,0))
    screen.blit(field,(0,-608))
    screen.blit(counter,(0,0))
    screen.blit(apple,(apple_x*76,apple_y*76))
    screen.blit(head[head_position],(snake_x,snake_y))
    screen.blit(body[body_position],(body_x,body_y))
    
    if snake_x == apple_x*76 and snake_y==apple_y*76:
        apple_x=randint(0,7)
        apple_y=randint(0,7)
        points+=1

    if keys[pg.K_RIGHT]:
        if head_position!=3:
            head_position=1
        

    elif keys[pg.K_LEFT]:
        if head_position!=1:
            head_position=3
        

    elif keys[pg.K_UP]:
        if head_position!=2:
            head_position=0
        
        

    elif keys[pg.K_DOWN]:
        if head_position!=0:
            head_position=2

        
    print(head_position)

    if snake_y<=-snake_speed:
        snake_y=field_y-snake_speed

    elif snake_y>=field_y:
        snake_y=0

    elif snake_x<=-snake_speed:
        snake_x=field_x-snake_speed

    elif snake_x>=field_x:
        snake_x=0

    if head_position==0:
        body_position=0
        snake_y-=snake_speed
        body_y=snake_y+snake_speed
        body_x=snake_x+18

    elif head_position==2:
        body_position=0
        snake_y+=snake_speed
        body_y=snake_y-snake_speed
        body_x=snake_x+18

    elif head_position==1:
        body_position=1
        snake_x+=snake_speed
        body_x=snake_x-snake_speed
        body_y=snake_y+18
        

    elif head_position==3:
        body_position=1
        snake_x-=snake_speed
        body_x=snake_x+snake_speed
        body_y=snake_y+18
        

    pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running=False
            pg.quit()
            
    clock.tick(5)
    