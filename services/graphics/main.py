from io import BytesIO

import matplotlib.dates as mdates
from matplotlib import pyplot as plt


class Graphic:
    def __init__(self, graphic: plt) -> None:
        self.gr = graphic

    def config_graphic(
        self,
        x_label: str,
        y_label: str,
        title: str,
        is_legend: bool = True,
        is_tight: bool = True,
    ) -> None:
        self.gr.title(title, fontsize=20, pad=20)
        self.gr.xlabel(x_label)
        self.gr.ylabel(y_label)
        if is_legend:
            self.gr.legend()
        if is_tight:
            self.gr.tight_layout()
        return self

    def draw_graphics(
        self, x_values: list[list], y_values: list[list], lines: list
    ) -> None:
        self.gr.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        self.gr.gca().xaxis.set_major_locator(
            mdates.DayLocator(interval=self.__count_shift(len(x_values)))
        )
        for i in range(len(lines)):
            self.gr.plot(x_values, y_values[i], label=lines[i])
        self.gr.gcf().autofmt_xdate()

        return self

    def graphic_pic_to_bytes(self) -> bytes:
        img = BytesIO()
        self.gr.savefig(img, format="png")
        img.seek(0)
        self.gr.close()
        return img.getvalue()

    def __count_shift(self, length: int) -> int:
        if length >= 12:
            return length // 12
        return 1
