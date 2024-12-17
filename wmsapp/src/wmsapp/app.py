"""
WMS application for android scanners to work together with Dynamics GP
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, BOTTOM


class WMSApp(toga.App):
    MENU_FONT_SIZE = 20

    def startup(self):
        self.main_box = toga.Box(style=Pack(direction=COLUMN))
        self.create_helpers()
        self.create_windows()
        self.add_main_menu()

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = self.main_box
        self.main_window.show()

    def create_windows(self):
        self.create_receiving_window()
        self.create_picking_window()
        self.create_putaway_window()

    def create_receiving_window(self):
        self.receiving_box = toga.Box(style=Pack(direction=COLUMN))
        self.r_header = toga.TextInput()
        self.r_label_box = toga.Box(style=Pack(padding=5,
                                               direction=COLUMN))
        self.r_label_box.add(self.r_header)
        self.receiving_box.add(self.r_label_box)

    def create_putaway_window(self):
        self.putaway_box = toga.Box(style=Pack(direction=COLUMN))
        self.pa_header = toga.Label("Putaway")
        self.pa_label_box = toga.Box(style=Pack(direction=COLUMN))
        self.pa_label_box.add(self.pa_header)
        self.putaway_box.add(self.pa_label_box)

    def create_picking_window(self):
        self.picking_box = toga.Box(style=Pack(direction=COLUMN))
        self.p_header = toga.Label("Picking")
        self.p_label_box = toga.Box(style=Pack(direction=COLUMN))
        self.p_label_box.add(self.p_header)
        self.picking_box.add(self.p_label_box)

    def create_helpers(self):
        self.back_button = toga.Button(
            "Back",
            on_press=self.back,
            style=Pack(padding=5, font_size=self.MENU_FONT_SIZE, alignment=BOTTOM)
        )

        self.spacer = toga.Box(
            id="spacer",
            style=Pack(flex=1),
        )

    def add_main_menu(self):
        self.receiving_button = toga.Button(
            "Receiving",
            on_press=self.receiving,
            style=Pack(padding=5, font_size=self.MENU_FONT_SIZE),
        )

        self.putaway_button = toga.Button(
            "Put away",
            on_press=self.putaway,
            style=Pack(padding=5, font_size=self.MENU_FONT_SIZE)
        )

        self.picking_button = toga.Button(
            "Picking",
            on_press=self.picking,
            style=Pack(padding=5, font_size=self.MENU_FONT_SIZE),
        )

        self.main_box.add(self.receiving_button)
        self.main_box.add(self.putaway_button)
        self.main_box.add(self.picking_button)

    def receiving(self, widget):
        self.receiving_box.add(self.spacer)
        self.receiving_box.add(self.back_button)
        self.main_window.content = self.receiving_box

    def putaway(self, widget):
        self.putaway_box.add(self.spacer)
        self.putaway_box.add(self.back_button)
        self.main_window.content = self.putaway_box

    def picking(self, widget):
        self.picking_box.add(self.spacer)
        self.picking_box.add(self.back_button)
        self.main_window.content = self.picking_box

    def back(self, widget):
        self.main_window.content = self.main_box


def main():
    return WMSApp()
