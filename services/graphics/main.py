from io import BytesIO

import matplotlib.dates as mdates
from matplotlib import pyplot as plt


class Graphic:
    def __init__(self, graphic: plt) -> None:
        self.gr = graphic

    def config_graphic(
        self, x_label: str, y_label: str, title: str, is_legend: bool
    ) -> None:
        self.gr.title(title)
        self.gr.xlabel(x_label)
        self.gr.ylabel(y_label)
        if is_legend:
            self.gr.legend()

    def draw_graphics(
        self, x_values: list[list], y_values: list[list], lines: list
    ) -> None:
        self.gr.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        if len(x_values) >= 12:
            
            shift = len(x_values) // 12
        else: 
            shift = 1
        self.gr.gca().xaxis.set_major_locator(mdates.DayLocator(interval=shift))
        for i in range(len(lines)):
            self.gr.plot(x_values, y_values[i], label=lines[i])
        self.gr.gcf().autofmt_xdate()
        self.gr.legend()
        self.gr.tight_layout()

    def graphic_pic_to_bytes(
        self, x_values: list, y_values: list, lines: list
    ) -> bytes:
        self.draw_graphics(x_values, y_values, lines)
        img = BytesIO()
        self.gr.savefig(img, format="png")
        img.seek(0)
        self.gr.close()
        return img.getvalue()
