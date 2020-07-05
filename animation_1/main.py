import time
#from __future__ import print_function

from data.main_cycle import *
from data.objects import *


def press_1(*args):
    dx = 0
    timer = time.time()
    while True:
        dx += 3
        obj.go_to(obj.x + dx, 0)
        if obj.x > -1:
            break
        canvas.update()
        dt = time.time() - timer
        dt = (1 / 60) - dt
        if dt > 0:
            time.sleep(dt)
        print(1 / (time.time() - timer))
        timer = time.time()
    obj.go_to(pw(-200), 0)
    while True:
        dx -= 3
        if dx == 0:
            dx = 3
        obj.go_to(obj.x + dx, 0)
        if obj.x > pw(-100):
            break
        canvas.update()
        dt = time.time() - timer
        dt = (1 / 60) - dt
        if dt > 0:
            time.sleep(dt)
        print(1 / (time.time() - timer))
        timer = time.time()
    obj.go_to(pw(-100), 0)


def press_2(*args):
    dx = 0
    timer = time.time()
    while True:
        dx -= 3
        obj.go_to(obj.x + dx, 0)
        if obj.x < pw(-200):
            break
        canvas.update()
        dt = time.time() - timer
        dt = (1 / 60) - dt
        if dt > 0:
            time.sleep(dt)
        print(1 / (time.time() - timer))
        timer = time.time()
    obj.go_to(0, 0)
    while True:
        dx += 3
        if dx == 0:
            dx = -3
        obj.go_to(obj.x + dx, 0)
        if obj.x < pw(-100):
            break
        canvas.update()
        dt = time.time() - timer
        dt = (1 / 60) - dt
        if dt > 0:
            time.sleep(dt)
        print(1 / (time.time() - timer))
        timer = time.time()
    obj.go_to(pw(-100), 0)


def move_oval(event):
    global c
    c.destroy()
    c = tkinter.Canvas(master, width=20, height=20, bg="red", cursor="pencil")
    c.pack()


print('Primary screen resolution: {}x{}'.format(
        *ScreenRes.get()
        ))
print(ScreenRes.get_modes())
ScreenRes.set(1280, 720)
#ScreenRes.set() # Set defaults


master = tkinter.Tk()
master.attributes('-fullscreen', True)
screen_w = master.winfo_screenwidth()
screen_h = master.winfo_screenheight()
teak_w_and_h(screen_w, screen_h)
canvas = tkinter.Canvas(master, bg='#CCCCCC', height=screen_h, width=screen_w)
canvas.pack(fill=tkinter.BOTH, expand=1)
print(screen_w, screen_h)

obj = Object(pw(-100), 0, pw(300), ph(100), 'background.png', canvas)

btn1 = Button(0, 0, pw(5), pw(5), 'tank_blue.png', canvas, 'tank_blue_d.png', function=press_1)
btn3 = Button(pw(5), 0, pw(5), pw(5), 'tank_blue.png', canvas, 'tank_blue_d.png', function=press_2)
btn2 = Button(pw(95), 0, pw(5), pw(5), 'tank_red.png', canvas, function=out)



master.bind('<Motion>', move)
master.bind('<Button-1>', click)
master.bind('<ButtonRelease-1>', clik_out)

loop = asyncio.get_event_loop()
loop.run_until_complete(main_cycle(master, screen_w, screen_h, obj, btn1, btn2, btn3))

ScreenRes.set() # Set defaults
