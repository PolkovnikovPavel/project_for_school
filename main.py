import time
#from __future__ import print_function

from data.main_cycle import *
from data.objects import *


def move_oval(event):
    global c
    c.destroy()
    c = tkinter.Canvas(master, width=20, height=20, bg="red", cursor="pencil")
    c.pack()


print('Primary screen resolution: {}x{}'.format(
        *ScreenRes.get()
        ))
print(ScreenRes.get_modes())
#ScreenRes.set(1280, 720)
#ScreenRes.set() # Set defaults


master = tkinter.Tk()
master.attributes('-fullscreen', True)
master.protocol("WM_DELETE_WINDOW", close_window)
screen_w = master.winfo_screenwidth()
screen_h = master.winfo_screenheight()
teak_w_and_h(screen_w, screen_h)
canvas = tkinter.Canvas(master, bg='#000000', height=screen_h, width=screen_w)
canvas.pack(fill=tkinter.BOTH, expand=1)
print(screen_w, screen_h)



all_gropes = []

main_grope = Group()
grope_2 = Group()
grope_2.container = [0]
all_levels = []

all_gropes.append(main_grope)
all_gropes.append(grope_2)

obj1 = Object(pw(-50), 0, pw(200), ph(100), 'background.png', canvas)
btn1 = Button(pw(15), ph(50), pw(10), pw(10), 'tabl_left.png', canvas, 'tabl_left_2.png', function=go_to_menu_1)
main_grope.add_objects(obj1)
main_grope.add_objects(btn1)


obj1 = Object(pw(-50), ph(-250), pw(200), ph(350), 'background_2.png', canvas)
btn2 = Button(pw(75), ph(50), pw(10), pw(10), 'tabl_right.png', canvas, 'tabl_right_2.png', function=go_to_menu_2)
level_1 = Level(pw(50), ph(50), canvas, 1, get_running, grope_2, get_mouse)
btn3 = Button(pw(50), ph(50), pw(4), pw(4), 'blast.png', canvas, 'tank_blue.png', level_1.start, [grope_2])
btn4 = Button(pw(30), ph(-30), pw(4), pw(4), 'blast.png', canvas, 'tank_blue.png', level_1.start, [grope_2])
grope_2.add_objects(obj1, btn2, btn3, btn4)

all_levels.append(level_1)
grope_2.hide_all()


master.bind('<Motion>', move)
master.bind('<Button-1>', click)
master.bind('<ButtonRelease-1>', click_out)
master.bind('<MouseWheel>', mouse_wheel)

main_cycle(canvas, all_gropes, all_levels)

ScreenRes.set() # Set defaults



