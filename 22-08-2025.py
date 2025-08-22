names = ['Амелия', 'Алина', 'Снежа']

# for i in range(3):
#     print(names[i])

# for elem in names:
#     print(elem)

# while True:
#     if условие
import pygame as pg
pg.init()

screen = pg.display.set_mode((700, 700))
# event - событие
is_running = True
clock = pg.time.Clock()
while is_running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False
    clock.tick(60)
    screen.fill((191, 255, 0))
    pg.display.update()
