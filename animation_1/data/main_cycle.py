import asyncio, time
from data.functions import pw, ph


mous_x = 0
mous_y = 0


def out(*args):
    global running
    running = False



def move(event):
    global mous_x, mous_y
    mous_x = event.x
    mous_y = event.y


def click(event):
    btn1.check(mous_x, mous_y)
    btn2.check(mous_x, mous_y)
    btn3.check(mous_x, mous_y)


def clik_out(event):
    btn1.check(mous_x, mous_y, False)
    btn2.check(mous_x, mous_y, False)
    btn3.check(mous_x, mous_y, False)



async def main_cycle(canvas_, screen_w, screen_h, obj_, btn1_, btn2_, btn3_):
    global canvas, obj, btn1, btn2, running, btn3
    canvas = canvas_
    obj = obj_
    btn1 = btn1_
    btn2 = btn2_
    btn3 = btn3_
    timer = time.time()
    running = True

    while running:
        canvas.update()
        dt = time.time() - timer
        dt = (1 / 65) - dt
        if dt > 0:
            time.sleep(dt)
        print(1 / (time.time() - timer))
        timer = time.time()

