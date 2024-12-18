"""
WMS application for android scanners to work together with Dynamics GP
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, BOTTOM, CENTER, RIGHT
from toga.constants import RED


class WMSApp(toga.App):
    MENU_FONT_SIZE = 20
    DEF_PADDING = 5
    TOP_MENU_PADDING = (30, DEF_PADDING, DEF_PADDING, DEF_PADDING)
    LABEL_PADDING = (DEF_PADDING, 1, DEF_PADDING, DEF_PADDING)
    ENTRY_PADDING = (DEF_PADDING, DEF_PADDING, DEF_PADDING, 1)

    def startup(self):
        self.main_box = toga.Box(style=Pack(direction=COLUMN,
                                            padding=self.TOP_MENU_PADDING))
        self.create_helpers()
        self.create_windows()
        self.add_main_menu()

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = self.main_box
        self.main_window.show()

    def create_helpers(self):
        self.spacer = toga.Box(
            id="spacer",
            style=Pack(flex=1,
                       direction=COLUMN),
        )

    def create_windows(self):
        self.__create_receiving_main_window()
        self.create_picking_window()
        self.create_putaway_window()

    def add_main_menu(self):
        self.receiving_button = toga.Button(
            "Receiving",
            on_press=self.enter_receiving_main,
            style=Pack(padding=self.DEF_PADDING,
                       font_size=self.MENU_FONT_SIZE),
        )

        self.putaway_button = toga.Button(
            "Put away",
            on_press=self.enter_putaway_main,
            style=Pack(padding=self.DEF_PADDING,
                       font_size=self.MENU_FONT_SIZE)
        )

        self.picking_button = toga.Button(
            "Picking",
            on_press=self.enter_picking_main,
            style=Pack(padding=self.DEF_PADDING,
                       font_size=self.MENU_FONT_SIZE),
        )

        self.main_box.add(self.receiving_button)
        self.main_box.add(self.putaway_button)
        self.main_box.add(self.picking_button)

    # Receiving

    def __create_receiving_main_window(self):
        self.r_sku_label = toga.Label("SKU:",
                                      style=Pack(padding=self.LABEL_PADDING,
                                                 alignment=RIGHT))

        self.r_sku_entry = toga.TextInput(style=Pack(direction=COLUMN,
                                                     flex=1))

        self.no_sku_found_label = toga.Label("No such SKU found.",
                                             style=Pack(color=RED,
                                                        padding=self.DEF_PADDING,
                                                        flex=1,
                                                        direction=COLUMN,
                                                        ))

        self.r_enter_button = toga.Button(
            "Enter",
            on_press=self.enter_receiving_detail,
            style=Pack(padding=self.DEF_PADDING,
                       font_size=self.MENU_FONT_SIZE,
                       flex=1)
        )

        self.r_back_button = toga.Button(
            "Back",
            on_press=self.back_to_main,
            style=Pack(padding=self.DEF_PADDING,
                       font_size=self.MENU_FONT_SIZE,
                       flex=1)
        )

        self.sku_box = toga.Box(style=Pack(padding=self.DEF_PADDING,
                                           flex=1),
                                children=[self.r_sku_label,
                                          self.r_sku_entry,
                                          ])

        self.r_outer_sku_box = toga.Box(style=Pack(direction=COLUMN,
                                                   alignment=CENTER,
                                                   ),
                                        children=[self.sku_box,
                                                  self.no_sku_found_label,
                                                  ])

        self.lower_menu_box = toga.Box(style=Pack(padding=self.DEF_PADDING,
                                                  direction=ROW),
                                       children=[self.r_enter_button,
                                                 self.r_back_button,
                                                 ]
                                       )

        self.receiving_box = toga.Box(style=Pack(padding=self.DEF_PADDING,
                                                 direction=COLUMN),
                                      children=[self.r_outer_sku_box,
                                                self.lower_menu_box,
                                                ])

    def enter_receiving_main(self, widget):
        self.__clear_receiving_window()
        self.main_window.content = self.receiving_box

    def __clear_receiving_window(self):
        self.r_sku_entry.value = ""
        self.__remove_no_sku_label()

    def enter_receiving_detail(self, widget):
        sku = self.r_sku_entry.value
        if sku == "111":
            self.__clear_receiving_window()
            self.receive_product(sku)
        else:
            self.r_outer_sku_box.insert(1, self.no_sku_label_box)

    def receive_product(self, sku):
        print(f"Received {sku}")

    def __remove_no_sku_label(self):
        self.r_outer_sku_box.remove(self.no_sku_label_box)

    # Putaway

    def create_putaway_window(self):
        pass

    def enter_putaway_main(self, widget):
        pass

    # Picking

    def create_picking_window(self):
        pass

    def enter_picking_main(self, widget):
        pass

    def back_to_main(self, widget):
        self.main_window.content = self.main_box


def main():
    return WMSApp()
