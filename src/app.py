import time
import tkinter

from .models.animation_model import Model
from .renderers.renderer import Renderer

TITLE = 'Простая анимация "Система частиц"'
SIZE = "700x700"
BACKGROUND_COLOR = 'black'
BACKGROUND_RGB = (0, 0, 0)
WIDTH = 650
HEIGHT = 650
FRAME_DELAY = 16
MAX_DT = 0.1


class App:

    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title(TITLE)
        self.root.geometry(SIZE)

        self.canvas = tkinter.Canvas(bg=BACKGROUND_COLOR, width=WIDTH,
                                     height=HEIGHT)
        self.canvas.pack(anchor=tkinter.CENTER, expand=1)
        self.model = Model(WIDTH, HEIGHT)
        self.renderer = Renderer(self.canvas, BACKGROUND_RGB)

        self._running = True
        self._last_time = time.perf_counter()

    def run(self):
        self._last_time = time.perf_counter()
        self._tick()
        self.root.mainloop()

    def _tick(self):
        now = time.perf_counter()
        dt = min(now - self._last_time, MAX_DT)
        self._last_time = now

        self.model.update(dt)
        self.renderer.render(self.model)

        if self._running:
            self.root.after(FRAME_DELAY, self._tick)
     
