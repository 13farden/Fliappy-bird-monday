from pygame import *
from random import randint

init()
window_size = 800, 600 #!! кортеж
window = display.set_mode(window_size)
display.set_caption("Flappy Bird")

clock = time.Clock()
FPS = 60
#!!!                x    y    w    h
player_rect = Rect(150, 200, 100, 100)

def generate_tubes(count, 
                   tube_width = 140, 
                   gap = 240, 
                   min_height = 50,
                   max_height = 320,
                   distance = 650):
    tubes = []
    start_x = window_size[0]
    for i in range(count):
        height = randint(min_height, max_height) # 120, 250
        top_tube = Rect(start_x, 0, tube_width, height)
        bottom_tube = Rect(start_x, 
                           height + gap, 
                           tube_width, 
                           window_size[1] - height - gap)
        tubes.extend([top_tube, bottom_tube])
        start_x += distance

    return tubes


tubes = generate_tubes(150)

gravity = 0.4 #!!!!!!!!!!!!!!!!
y_vel = 0.0 #!!!!!!!!!!!!!!!!
IMPULSE = -7.0 #!!!!!!!!!!!!!!!!

lose = False
score = 0
my_font = font.Font(None, 50)

while 1:
    for e in event.get():
        if e.type == QUIT:
            quit()
    if not lose:
        y_vel += gravity 
        player_rect.y += int(y_vel)

    keys = key.get_pressed()
    if keys[K_UP] or keys[K_w]:
        if not lose:
            y_vel = IMPULSE 
    #if keys[K_DOWN] or keys[K_s]: y_vel = 5

    if player_rect.bottom >= window_size[1]: #!!!!!!!!!
        player_rect.bottom = window_size[1]#!!!!!!!!!
        lose = True
        y_vel = 0

    if player_rect.top <= 0:#!!!!!!!!!
        player_rect.top = 0#!!!!!!!!!
        lose = True
        y_vel = 0
    
    
    window.fill("sky blue")
    for tube in tubes[:]: 
        if not lose:
            tube.x -= 5
        if tube.right < 0:
            tubes.remove(tube)
            score += 0.5
            continue
        draw.rect(window, (0, 255, 0), tube)
        if player_rect.colliderect(tube):
            lose = True
            y_vel = 0
    if len(tubes) < 8:
        tubes += generate_tubes(150)
    
    draw.rect(window, (0, 255, 0), player_rect) #!!!!! 0 - 255

    score_text = my_font.render(f"Score: {int(score)}", True, "black")
    window.blit(score_text, (20, 20))
    display.update()
    clock.tick(FPS)