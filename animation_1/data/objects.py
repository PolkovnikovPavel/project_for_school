import tkinter
from images.images import *


class Object():
    def __init__(self, x, y, w, h, img, canvas, visibility=True):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.angle = 0
        if type(img) == str:
            self.img, self.img_pil = get_image(img, w, h, mode=1)
        else:
            self.img = img
            self.img_pil = None
        self.img_pil_start = self.img_pil
        self.canvas = canvas
        self.visibility = visibility
        if visibility:
            self.obj = self.canvas.create_image((x + 0.5 * self.w, y + 0.5 * self.h), image=self.img)

    def go_to(self, x, y):
        dx = x - self.x
        dy = y - self.y
        self.canvas.move(self.obj, dx, dy)
        self.x += dx
        self.y += dy

    def hide(self):
        self.canvas.delete(self.obj)
        self.visibility = False

    def show(self):
        self.obj = self.canvas.create_image((self.x + 0.5 * self.w, self.y + 0.5 * self.h), image=self.img)
        self.visibility = True

    def rotation_on(self, angle):
        self.angle += angle
        self.rotation(self.angle)

    def rotation(self, angle):
        self.angle = angle
        if self.img_pil is not None:
            self.img_pil = self.img_pil_start.rotate(self.angle)
            self.img = ImageTk.PhotoImage(self.img_pil)

            self.canvas.delete(self.obj)
            self.obj = self.canvas.create_image((self.x + 0.5 * self.w, self.y + 0.5 * self.h), image=self.img)


    def check_point(self, x, y):
        if x >= self.x and x <= self.x + self.w and y >= self.y and y <= self.y + self.h:
            return True
        return False


class Button(Object):
    def __init__(self, x, y, w, h, img, canvas, img2=None, function=None, args=[], visibility=True):
        Object.__init__(self, x, y, w, h, img, canvas, visibility=visibility)
        self.is_clik = False
        if type(img2) == str:
            self.img2 = get_image(img2, w, h)
        else:
            self.img2 = img2
        self.function = function
        self.args = args

    def press(self):
        self.function(self.args)

    def hide(self):
        Object.hide(self)
        self.is_clik = False


    def show(self):
        Object.show(self)
        self.is_clik = False

    def check(self, x, y, is_clik=True):
        if not self.visibility:
            return
        if self.check_point(x, y):
            if is_clik:
                if not self.is_clik:
                    self.is_clik = True
                    if self.img2 is not None:
                        self.canvas.delete(self.obj)
                        self.obj = self.canvas.create_image((self.x + 0.5 * self.w, self.y + 0.5 * self.h), image=self.img2)

            else:
                if self.is_clik:
                    self.is_clik = False
                    if self.img2 is not None:
                        self.canvas.delete(self.obj)
                        self.obj = self.canvas.create_image((self.x + 0.5 * self.w, self.y + 0.5 * self.h), image=self.img)
                    self.press()
        else:
            if self.is_clik:
                self.is_clik = False
                if self.img2 is not None:
                    self.canvas.delete(self.obj)
                    self.obj = self.canvas.create_image((self.x + 0.5 * self.w, self.y + 0.5 * self.h), image=self.img)



class Group():
    def __init__(self):
        self.all_objects = []
        self.visibility = True
        self.container = []

    def add_objects(self, *objects):
        for object in objects:
            self.all_objects.append(object)

    def delete(self, *objects):
        if len(objects) == 0:
            self.all_objects = []
        for object in objects:
            del self.all_objects[self.all_objects.index(object)]

    def hide_all(self):
        for object in self.all_objects:
            object.hide()

    def show_all(self):
        for object in self.all_objects:
            object.show()

    def check(self, x, y, is_clik=True):
        if is_clik:
            for object in self.all_objects:
                if isinstance(object, Button):
                    object.check(x, y, is_clik)
        else:
            for object in self.all_objects:
                if isinstance(object, Button):
                    object.check(x, y, is_clik)

