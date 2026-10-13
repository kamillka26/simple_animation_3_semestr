import tkinter as tk


class Controls:
    def __init__(self, parent, model, on_reset):
        self.model = model
        self.on_reset = on_reset
        self.frame = tk.Frame(parent, bg="#202020")
        self.frame.pack(fill=tk.X)

        self._add_slider("Частота", 10, 200, model.systems[0].spawn_rate,
                         lambda v: self._set("spawn_rate", float(v)))
        self._add_slider("Жизнь", 0.5, 5.0, model.systems[0].lifetime,
                         lambda v: self._set("lifetime", float(v)))
        self._add_slider("Скорость", 10, 300, model.systems[0].speed_max,
                         lambda v: self._set("speed_max", float(v)))

        tk.Button(self.frame, text="Сброс",
                  command=on_reset).pack(side=tk.LEFT)

    def _add_slider(self, label, a, b, initial, command):
        tk.Label(self.frame, text=label, bg="#202020",
                 fg="white").pack(side=tk.LEFT)
        scale = tk.Scale(self.frame, from_=a, to=b, resolution=0.1,
                         orient=tk.HORIZONTAL, length=200,
                         bg="#202020", fg="white",
                         command=command)
        scale.set(initial)
        scale.pack(side=tk.LEFT, padx=5)

    def _set(self, key, value):
        for system in self.model.systems:
            setattr(system, key, value)
