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


def check_bound(rct: pg.Rect) -> tuple[bool, bool]:  #練習4
    """
    オブジェクトが画面外かを判定し,真理値タプルを返す
    引数2 rct : オブジェクトSurfaceのRect
    戻り値 : 横方向,縦方向のはみだし判定結果（画面内:True / 画面外:False
    """
    yoko, tate = True, True
    if rct.left < 0 or WIDTH < rct.right:
        yoko = False
    if rct.top < 0 or HEIGHT < rct.bottom:
        tate = False
    return yoko, tate


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_img_dic = {  #演習1：回転したこうかとんの辞書
        (0, -5): pg.transform.rotozoom(kk_img, -90, 1.0),
        (+5, -5): pg.transform.rotozoom(pg.transform.flip(kk_img, True, False), 45, 1.0),
        (+5, 0): pg.transform.rotozoom(pg.transform.flip(kk_img, True, False), 0, 1.0),
        (+5, +5): pg.transform.rotozoom(pg.transform.flip(kk_img, True, False), -45, 1.0),
        (0, +5): pg.transform.rotozoom(kk_img, 90, 1.0),
        (-5, +5): pg.transform.rotozoom(kk_img, 45, 1.0),
        (-5, 0): pg.transform.rotozoom(kk_img, 0, 1.0),
        (-5, -5): pg.transform.rotozoom(kk_img, -45, 1.0),
        (0, 0): kk_img
    }
    kk_rect = kk_img.get_rect()  #練習3
    kk_rect.center = 900, 400  #練習3
    bb_img = pg.Surface((20, 20))  #練習1
    bb_img.set_colorkey((0, 0, 0))
    pg.draw.circle(bb_img, (255, 0, 0), (10, 10), 10)  #練習1
    bb_rect = bb_img.get_rect()  #練習1
    bb_rect.centerx = random.randint(0, WIDTH)  #練習1
    bb_rect.centery = random.randint(0, HEIGHT)  #練習1
    vx, vy = +5, +5  #練習2
    accs = [a for a in range(1, 11)]  #演習2：加速度リスト
    #Issue1 空行の削除
    clock = pg.time.Clock()
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
            
        if kk_rect.colliderect(bb_rect):  #練習5
            screen.blit(bg_img, [0, 0])  #演習3：背景を描画
            kk_img = pg.image.load("ex02/fig/8.png")  #演習3：泣いている画像を読み込み
            kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)  #演習３：画像を拡大
            screen.blit(kk_img, kk_rect)  #演習３：画像を描写
            pg.display.update()
            clock.tick(0.5)
            print("Game Over")
            return

        key_lst = pg.key.get_pressed()  #練習3
        sum_mv = [0, 0]  #練習3
        for k, tpl in delta.items():  #練習3
            if key_lst[k]:
                sum_mv[0] += tpl[0]
                sum_mv[1] += tpl[1]
                kk_img = kk_img_dic[tuple(sum_mv)]  #演習1：向きの変更
        
        screen.blit(bg_img, [0, 0])
        kk_rect.move_ip(sum_mv[0], sum_mv[1])  #練習4
        if check_bound(kk_rect) != (True, True):  #練習4
            kk_rect.move_ip(-sum_mv[0], -sum_mv[1])
        screen.blit(kk_img, kk_rect)  #練習3
        avx, avy = vx*accs[min(tmr//500, 9)], vy*accs[min(tmr//500, 9)]  #演習2：tmrに応じて速度を上げる
        bb_rect.move_ip(avx, avy)  #練習2
        yoko, tate = check_bound(bb_rect)  #練習4
        if not yoko:
            vx *= -1
            avx *= -1
        if not tate:
            vy *= -1
            avy *= -1
        bb_rect.move_ip(avx, avy)
        screen.blit(bb_img, bb_rect)
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()