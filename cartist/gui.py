"""
    Cellular Automata GUI ARTIST.
"""

import tkinter as tk
import tkinter.font as tkfont

from cartist import Artist
from cartist.ca import SqrtCA
from cartist.canvas import ResizingCanvas
from cartist.colors import STATE_COLOR
from cartist.rules import DEFAULT_RULE_SET


class GUIArtist(Artist):
    """Cellular Automata artist."""

    def __init__(self, number, rule_set=DEFAULT_RULE_SET):
        self._rule_set = rule_set
        self._ca = SqrtCA(rule_set, number)

    def paint(self):
        self._window = tk.Tk()

        width, height = self._get_start_window_size()
        self._window.geometry(f'{width}x{height}+0+0')

        self._font = tkfont.Font(family='Helvetica', size=16, weight='bold')
        self._window.option_add('*Font', self._font)

        # Key names:
        # https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/key-names.html
        self._window.bind('<Return>', self._on_enter_pressed)
        self._window.bind('<KP_Enter>', self._on_enter_pressed)

        self._add_info_frame(width, height)
        self._add_ca_frame(width, height)

        self._window.mainloop()

    def _add_ca_frame(self, width, height):
        self._ca_frame = tk.Frame(self._window, width=width, height=height)
        self._ca_frame.pack(fill='both', expand=True)
        self._canvas = ResizingCanvas(self._ca_frame, bg='white')
        self._canvas.config(width=width, height=height)
        self._canvas.pack(side=tk.LEFT, fill='both', expand=True)

        self._draw_ca()

    def _draw_ca(self):
        self._canvas.delete('all')
        cell_size = 1
        row = 0
        outline = 'snow' if self._ca.number < 150 else ''

        def draw_row(row):
            for col, state in enumerate(self._ca):
                self._canvas.create_rectangle(
                    col,
                    row,
                    col + cell_size,
                    row + cell_size,
                    fill=STATE_COLOR[state],
                    outline=outline,
                )

        while True:
            draw_row(row)
            row += 1
            self._ca.evolve()
            if not self._ca.has_changed():
                draw_row(row)
                row += 1
                self._canvas.width = len(self._ca) * cell_size
                self._canvas.height = row * cell_size

                self._set_result_text()
                print(f'√{self._ca.number}: {self._ca.sqrt_value}')
                break

        self._canvas.resize_to(
            self._ca_frame.winfo_width(), self._ca_frame.winfo_height()
        )

    def _add_info_frame(self, width, height):
        self._info_frame = tk.Frame(
            self._window,
            width=width,
            height=min(self._window.winfo_screenheight() // 10, 100),
        )
        self._info_frame.pack(side=tk.TOP)
        self._info_frame_label = tk.Label(self._info_frame, text='√')
        self._info_frame_label.pack(side=tk.LEFT, fill='y')
        self._number = tk.StringVar()
        self._number_entry = tk.Entry(
            self._info_frame, textvariable=self._number, width=5
        )
        self._number_entry.pack(side=tk.LEFT, fill='y', padx=10, pady=10)
        self._number.set(str(self._ca.number))
        self._info_frame_result = tk.Label(self._info_frame, text=' = ')
        self._info_frame_result.pack(side=tk.LEFT, fill='y')

    def _set_result_text(self):
        self._info_frame_result.config(text=f'= {self._ca.sqrt_value}')

    def _get_start_window_size(self):
        width = self._window.winfo_screenwidth()
        height = self._window.winfo_screenheight()
        size = min([width, height])
        size = size * 3 // 4
        return size, size

    def _on_enter_pressed(self, event):
        number = self._number.get()
        try:
            number = int(number)
        except ValueError:
            print(f'invalid input: {number}')

        self._ca = SqrtCA(self._rule_set, number)
        self._draw_ca()
