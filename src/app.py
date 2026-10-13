import tkinter

from .models.animation_model import Model
from .renderers.renderer import Renderer

TITLE = 'Простая анимация "Система частиц"'
SIZE = "700x700"
BACKGROUND_COLOR = 'black'
WIDTH = 650
HEIGHT = 650


class App:

    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title(TITLE)
        self.root.geometry(SIZE)

        self.canvas = tkinter.Canvas(bg=BACKGROUND_COLOR, width=WIDTH,
                                     height=HEIGHT)
        self.canvas.pack(anchor=tkinter.CENTER, expand=1)
        self.model = Model(WIDTH, HEIGHT)
        self.renderer = Renderer(self.canvas, BACKGROUND_COLOR)

    def run(self):
        self.root.mainloop()
