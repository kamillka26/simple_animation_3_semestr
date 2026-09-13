import tkinter

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

        canvas = tkinter.Canvas(bg=BACKGROUND_COLOR, width=WIDTH,
                                height=HEIGHT)
        canvas.pack(anchor=tkinter.CENTER, expand=1)
