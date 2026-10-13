import time
import tkinter

from .widgets.controls import Controls
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
        self.controls = Controls(self.root, self.model, self.reset)

        self._running = True
        self._last_time = time.perf_counter()
        self.canvas.bind("<Button-1>", self._on_click)
        self.root.bind("<space>", lambda e: self.toggle_pause())
        self.root.bind("<r>", lambda e: self.reset())

        self._paused = False

    def run(self):
        self._last_time = time.perf_counter()
        self._tick()
        self.root.mainloop()

    def _tick(self):
        now = time.perf_counter()
        dt = min(now - self._last_time, MAX_DT)
        self._last_time = now
        if not self._paused:
            self.model.update(dt)
            self.renderer.render(self.model)

        if self._running:
            self.root.after(FRAME_DELAY, self._tick)

    def _on_click(self, event):
        self.model.add_system(event.x, event.y)

    def toggle_pause(self):
        self._paused = not self._paused

    def reset(self):
        self.renderer.clear()
        self.model.clear()
