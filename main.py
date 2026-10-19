from pygame import *
from random import randint

init()
window_size = 800, 600
window = display.set_mode(window_size)
display.set_caption("Flappy Bird")

clock = time.Clock()
FPS = 60

player_rect = Rect(150, 200, 100, 100)
def generate_tudes(count,
                    tube_width = 140,
                    gap = 240,
                    min_height = 50,
                    max_height = 320,
                    distance = 650):
    tubes = []
    start_x = window_size[0]
    for i in range(count):
        height = randint(min_height, max_height)
        tor_tude = Rect(start_x, 0, tube_width, height)
        botton_tube = Rect(start_x, height + gap, tube_width, window_size[1] - height - gap)
        tubes.extend([tor_tude, botton_tube])
        start_x += distance

    return tubes
while 1:
    for e in event.get():
        if e.type == QUIT:
            quit()
    keys = key.get_pressed()
    if keys[K_w]: player_rect.y -= 15
    if keys[K_s]: player_rect.y += 15
    window.fill("sky blue")
    draw.rect(window, (0, 0, 0), player_rect)
    display.update()
    clock.tick(FPS)