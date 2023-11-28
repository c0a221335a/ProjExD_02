import random
import sys
import pygame as pg


WIDTH, HEIGHT = 1600, 900
delta = {  #練習3
    pg.K_UP: (0, -5),
    pg.K_DOWN: (0, +5),
    pg.K_LEFT: (-5, 0),
    pg.K_RIGHT: (+5, 0)
}

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_rect = kk_img.get_rect()  #練習3
    kk_rect.center = 900, 400  #練習3
    bb_img = pg.Surface((20, 20))  #練習1
    bb_img.set_colorkey((0, 0, 0))
    pg.draw.circle(bb_img, (255, 0, 0), (10, 10), 10)  #練習1
    bb_rect = bb_img.get_rect()  #練習1
    bb_rect.centerx = random.randint(0, WIDTH)  #練習1
    bb_rect.centery = random.randint(0, HEIGHT)  #練習1
    vx, vy = +5, +5  #練習2

    clock = pg.time.Clock()
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        key_lst = pg.key.get_pressed()  #練習3
        sum_mv = [0, 0]  #練習3
        for k, tpl in delta.items():  #練習3
            if key_lst[k]:
                sum_mv[0] += tpl[0]
                sum_mv[1] += tpl[1]

        
        screen.blit(bg_img, [0, 0])
        kk_rect.move_ip(sum_mv[0], sum_mv[1])  #練習3
        screen.blit(kk_img, kk_rect)  #練習3
        bb_rect.move_ip(vx, vy)  #練習2
        screen.blit(bb_img, bb_rect)
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()