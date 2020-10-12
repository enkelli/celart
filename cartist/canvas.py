"""
    Resizing canvas.
"""

import tkinter as tk


class ResizingCanvas(tk.Canvas):
    """Canvas adaptable to window size."""

    # Based on: https://stackoverflow.com/a/22837522/5601069

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.bind('<Configure>', self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()

    def on_resize(self, event):
        self.resize_to(event.width, event.height)

    def resize_to(self, width, height):
        # Determine the ratio of old width/height to new width/height.
        wscale = width / self.width
        hscale = height / self.height
        self.width = width
        self.height = height
        # Resize the canvas.
        self.config(
            width=self.width, height=self.height, scrollregion=self.bbox(tk.ALL)
        )
        # Rescale all the objects tagged with the "all" tag.
        self.scale(tk.ALL, 0, 0, wscale, hscale)
