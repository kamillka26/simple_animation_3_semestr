class Renderer:
    def __init__(self, canvas, background):
        self.canvas = canvas
        self.background = background
        self._items = {}

    def render(self, model):
        active = set()

        for system in model.systems:
            for p in system.particles:
                active.add(p)
                self._draw(p)

        for p in list(self._items.keys()):
            if p not in active:
                self.canvas.delete(self._items.pop(p))

    def clear(self):
        for item in self._items.values():
            self.canvas.delete(item)
        self._items.clear()

    def _draw(self, p):
        color = self._blend(p.color, p.alpha)
        coords = (p.x - p.radius, p.y - p.radius,
                  p.x + p.radius, p.y + p.radius)

        item = self._items.get(p)
        if item is None:
            item = self.canvas.create_oval(*coords, fill=color, outline=color)
            self._items[p] = item
        else:
            self.canvas.coords(item, *coords)
            self.canvas.itemconfig(item, fill=color, outline=color)

    def _blend(self, color, alpha):
        r = int(color[0] * alpha + self.background[0] * (1 - alpha))
        g = int(color[1] * alpha + self.background[1] * (1 - alpha))
        b = int(color[2] * alpha + self.background[2] * (1 - alpha))
        return f"#{r:02x}{g:02x}{b:02x}"
