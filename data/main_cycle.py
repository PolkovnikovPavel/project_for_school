import asyncio, time
from data.functions import pw, ph


mous_x = 0
mous_y = 0


def get_running():
    return running


def get_mouse():
    return mous_x, mous_y


def create_all_gropes():
    global main_grope, grope_2
    main_grope, grope_2 = all_gropes


def close_window(*args):
    global running
    running = False


def mouse_wheel(event, *args):
    if type_menu == 'menu_2':
        dy = event.delta // 3
        timer = time.time()
        for i in range(int(event.delta / dy)):
            menu_y = grope_2.all_objects[0].y + dy
            if menu_y > ph(-250) and menu_y < 0:
                grope_2.all_move_on(0, dy)
            else:
                break
            canvas.update()
            dt = time.time() - timer
            dt = (1 / 60) - dt
            if dt > 0:
                time.sleep(dt)

            timer = time.time()


def move(event, *args):
    global mous_x, mous_y
    mous_x = event.x
    mous_y = event.y

    if type_menu == 'menu_2':
        if is_click:
            menu_y = grope_2.all_objects[0].y + (mous_y - grope_2.container[0])
            if menu_y > ph(-250) and menu_y < 0:
                grope_2.all_move_on(0, mous_y - grope_2.container[0])
            grope_2.container[0] = mous_y


def click(event, *args):
    global is_click, old_mous_x, old_mous_y
    is_click = True
    old_mous_x = mous_x
    old_mous_y = mous_y
    for grope in all_gropes:
        grope.check(mous_x, mous_y, is_clik=True)
    for level in all_levels:
        level.check(mous_x, mous_y, is_clik=True)

    if type_menu == 'menu_2':
        grope_2.container[0] = mous_y


def click_out(event, *args):
    global is_click, is_ended

    is_click = False
    for grope in all_gropes:
        grope.check(mous_x, mous_y, is_clik=False)
    for level in all_levels:
        level.check(mous_x, mous_y, is_clik=False)


def start_main_menu(*args):
    global type_menu
    type_menu = 'main_menu'
    main_grope.show_all()



def main_cycle(canvas_, all_gropes_, all_levels_):
    global canvas, running, all_gropes, my_id, type_menu, all_levels
    type_menu = 'main_menu'
    canvas = canvas_
    all_levels = all_levels_
    all_gropes = all_gropes_
    create_all_gropes()


    timer = time.time()
    running = True

    while running:

        canvas.update()
        dt = time.time() - timer
        dt = (1 / 120) - dt
        if dt > 0:
            time.sleep(dt)

        timer = time.time()


def start_animation_to_right(start_group, end_group, speed=4):
    dx = 0
    way = 0
    timer = time.time()
    while running:
        dx += speed
        way += dx
        start_group.all_move_on(dx, 0)
        if way > pw(150):
            break
        canvas.update()
        dt = time.time() - timer
        dt = (1 / 60) - dt
        if dt > 0:
            time.sleep(dt)
        timer = time.time()
    start_group.hide_all()
    end_group.show_all()
    end_group.all_move_on(-1 * way, 0)
    start_group.all_move_on(-1 * way, 0)
    print(way)
    way = 0
    way += dx
    end_group.all_move_on(dx, 0)
    while running:
        dx -= speed
        way += dx
        end_group.all_move_on(dx, 0)
        if dx == 0:
            break
        canvas.update()
        dt = time.time() - timer
        dt = (1 / 60) - dt
        if dt > 0:
            time.sleep(dt)
        timer = time.time()
    print(way)


def start_animation_to_left(start_group, end_group, speed=4):
    dx = 0
    way = 0
    timer = time.time()
    while running:
        dx -= speed
        way -= dx
        start_group.all_move_on(dx, 0)
        if way > pw(150):
            break
        canvas.update()
        dt = time.time() - timer
        dt = (1 / 60) - dt
        if dt > 0:
            time.sleep(dt)
        timer = time.time()
    start_group.hide_all()
    end_group.show_all()
    end_group.all_move_on(way, 0)
    start_group.all_move_on(way, 0)
    print(way)
    way = 0
    way -= dx
    end_group.all_move_on(dx, 0)
    while running:
        dx += speed
        way -= dx
        end_group.all_move_on(dx, 0)
        if dx == 0:
            break
        canvas.update()
        dt = time.time() - timer
        dt = (1 / 60) - dt
        if dt > 0:
            time.sleep(dt)
        timer = time.time()
    print(way)


def go_to_menu_1(*args):
    global type_menu
    start_animation_to_right(main_grope, grope_2)
    type_menu = 'menu_2'


def go_to_menu_2(*args):
    global type_menu
    start_animation_to_left(grope_2, main_grope)
    type_menu = 'main_menu'

