"""
WMS application for android scanners to work together with Dynamics GP
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, BOTTOM, CENTER
from toga.constants import RED


class WMSApp(toga.App):
    MENU_FONT_SIZE = 20
    DEF_PADDING = 5

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
        self.r_sku_label = toga.Label("SKU: ",
                                      style=Pack(padding=self.DEF_PADDING))

        self.r_sku_entry = toga.TextInput()

        self.no_sku_found_label = toga.Label("No such SKU found.",
                                             style=Pack(color=RED,
                                                        padding=self.DEF_PADDING,
                                                        ))

        self.sku_label_box = toga.Box(style=Pack(padding=self.DEF_PADDING),
                                      children=[self.r_sku_label,])

        self.sku_entry_box = toga.Box(style=Pack(padding=self.DEF_PADDING,
                                                 direction=COLUMN,
                                                 flex=1),
                                      children=[self.r_sku_entry,])

        self.r_inner_sku_box = toga.Box(style=Pack(padding=self.DEF_PADDING,
                                                   direction=ROW,
                                                   flex=1),
                                        children=[self.sku_label_box,
                                                  self.sku_entry_box,
                                                  ])

        self.no_sku_label_box = toga.Box(style=Pack(padding=self.DEF_PADDING,
                                                    flex=1,
                                                    alignment=CENTER
                                                    ),
                                         children=[self.no_sku_found_label,
                                                   ])

        self.r_outer_sku_box = toga.Box(style=Pack(padding=self.DEF_PADDING,
                                                   direction=COLUMN,
                                                   alignment=CENTER,
                                                   ),
                                        children=[self.r_inner_sku_box,
                                                  ])

        self.receiving_box = toga.Box(style=Pack(padding=self.DEF_PADDING,
                                                 direction=COLUMN),
                                      children=[self.r_outer_sku_box,
                                                ])

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
            style=Pack(padding=self.DEF_PADDING,
                       font_size=self.MENU_FONT_SIZE,
                       alignment=BOTTOM)
        )

        self.spacer = toga.Box(
            id="spacer",
            style=Pack(flex=1),
        )

        self.enter_button = toga.Button(
            "Enter",
            on_press=self.r_enter,
            style=Pack(padding=self.DEF_PADDING,
                       font_size=self.MENU_FONT_SIZE,
                       alignment=BOTTOM)
        )

    def add_main_menu(self):
        self.receiving_button = toga.Button(
            "Receiving",
            on_press=self.receiving,
            style=Pack(padding=self.DEF_PADDING,
                       font_size=self.MENU_FONT_SIZE),
        )

        self.putaway_button = toga.Button(
            "Put away",
            on_press=self.putaway,
            style=Pack(padding=self.DEF_PADDING,
                       font_size=self.MENU_FONT_SIZE)
        )

        self.picking_button = toga.Button(
            "Picking",
            on_press=self.picking,
            style=Pack(padding=self.DEF_PADDING,
                       font_size=self.MENU_FONT_SIZE),
        )

        self.main_box.add(self.receiving_button)
        self.main_box.add(self.putaway_button)
        self.main_box.add(self.picking_button)

    def receiving(self, widget):
        self.r_sku_entry.value = ""
        self.__remove_no_sku_label()
        self.receiving_box.add(self.spacer)
        self.receiving_box.add(toga.Box(style=Pack(padding=self.DEF_PADDING,
                                                   direction=ROW),
                                        children=[toga.Box(style=Pack(direction=COLUMN,
                                                                      flex=1),
                                                           children=[self.enter_button,]),
                                                  toga.Box(style=Pack(direction=COLUMN,
                                                                      flex=1),
                                                           children=[self.back_button,]),
                                                  ]
                                        )
                               )

        self.main_window.content = self.receiving_box

    def putaway(self, widget):
        self.putaway_box.add(self.spacer)
        self.putaway_box.add(self.back_button)
        self.main_window.content = self.putaway_box

    def picking(self, widget):
        self.picking_box.add(self.spacer)
        self.picking_box.add(self.back_button)
        self.main_window.content = self.picking_box

    def r_enter(self, widget):
        sku = self.r_sku_entry.value
        if sku == "111":
            self.__remove_no_sku_label()
            #self.receive_product(sku)
        else:
            self.r_outer_sku_box.insert(1, self.no_sku_label_box)

    def receive_product(self, sku):
        pass

    def back(self, widget):
        self.main_window.content = self.main_box

    def __remove_no_sku_label(self):
        self.r_outer_sku_box.remove(self.no_sku_label_box)


def main():
    return WMSApp()
