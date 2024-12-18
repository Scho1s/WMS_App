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
        self.__create_receiving_detail_window()
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

        self.no_sku_found_label = toga.Label("",
                                             style=Pack(color=RED,
                                                        padding=self.DEF_PADDING,
                                                        alignment=RIGHT,
                                                        ))

        self.r_spacer = toga.Box(
            id="r_spacer",
            style=Pack(flex=1,
                       direction=COLUMN),
        )

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

        self.no_sku_label_box = toga.Box(style=Pack(padding=self.DEF_PADDING,
                                                    alignment=RIGHT,
                                                    ),
                                         children=[self.no_sku_found_label,
                                                   ])

        self.r_outer_sku_box = toga.Box(style=Pack(direction=COLUMN,
                                                   alignment=CENTER,
                                                   ),
                                        children=[self.sku_box,
                                                  self.no_sku_label_box,
                                                  ])

        self.r_spacer_box = toga.Box(style=Pack(direction=COLUMN,
                                                flex=1),
                                     children=[self.r_spacer,
                                               ])

        self.lower_menu_box = toga.Box(style=Pack(padding=self.DEF_PADDING,
                                                  direction=ROW),
                                       children=[self.r_enter_button,
                                                 self.r_back_button,
                                                 ])

        self.r_main_box = toga.Box(style=Pack(padding=self.DEF_PADDING,
                                              direction=COLUMN),
                                   children=[self.r_outer_sku_box,
                                             self.r_spacer_box,
                                             self.lower_menu_box,
                                             ])

    def __create_receiving_detail_window(self):
        self.r_item_code_label = toga.Label("",
                                            style=Pack(padding=self.LABEL_PADDING))

        self.r_item_desc_label = toga.Label("",
                                            style=Pack(padding=self.LABEL_PADDING))

        self.r_quantity_label = toga.Label("Quantity: ",
                                           style=Pack(padding=self.LABEL_PADDING, alignment=RIGHT, width=100))

        self.r_quantity_entry = toga.TextInput(style=Pack(direction=COLUMN,
                                                          flex=1))

        self.r_weight_label = toga.Label("Weight: ",
                                         style=Pack(padding=self.LABEL_PADDING, alignment=RIGHT, width=100))

        self.r_weight_entry = toga.TextInput(style=Pack(direction=COLUMN,
                                                        flex=1))

        self.r_best_before_label = toga.Label("Best Before: ",
                                              style=Pack(padding=self.LABEL_PADDING, alignment=RIGHT, width=100))

        self.r_best_before_entry = toga.TextInput(style=Pack(direction=COLUMN,
                                                             flex=1))

        self.r_batch_code_label = toga.Label("Batch Code: ",
                                             style=Pack(padding=self.LABEL_PADDING, alignment=RIGHT, width=100))

        self.r_batch_code_entry = toga.TextInput(style=Pack(direction=COLUMN,
                                                            flex=1))

        self.r_spacer2 = toga.Box(
            id="r_spacer2",
            style=Pack(flex=1,
                       direction=COLUMN),
        )

        self.r_save_button = toga.Button(
            "Save",
            on_press=self.r_save_details,
            style=Pack(padding=self.DEF_PADDING,
                       font_size=self.MENU_FONT_SIZE,
                       flex=1)
        )

        self.r_back_button2 = toga.Button(
            "Back",
            on_press=self.back_to_receiving,
            style=Pack(padding=self.DEF_PADDING,
                       font_size=self.MENU_FONT_SIZE,
                       flex=1)
        )

        self.r_item_details_box = toga.Box(style=Pack(padding=self.DEF_PADDING),
                                           children=[self.r_item_code_label, self.r_item_desc_label])

        self.r_quantity_box = toga.Box(style=Pack(padding=self.DEF_PADDING),
                                       children=[self.r_quantity_label, self.r_quantity_entry])

        self.r_weight_box = toga.Box(style=Pack(padding=self.DEF_PADDING),
                                     children=[self.r_weight_label, self.r_weight_entry])

        self.r_best_before_box = toga.Box(style=Pack(padding=self.DEF_PADDING),
                                          children=[self.r_best_before_label, self.r_best_before_entry])

        self.r_batch_code_box = toga.Box(style=Pack(padding=self.DEF_PADDING),
                                         children=[self.r_batch_code_label, self.r_batch_code_entry])

        self.r_spacer2_box = toga.Box(style=Pack(direction=COLUMN, flex=1),
                                      children=[self.r_spacer2])

        self.r_lower_menu2_box = toga.Box(style=Pack(padding=self.DEF_PADDING, direction=ROW),
                                          children=[self.r_save_button, self.r_back_button2])

        self.r_details_box = toga.Box(style=Pack(padding=self.DEF_PADDING, direction=COLUMN),
                                      children=[self.r_item_details_box,
                                                self.r_quantity_box,
                                                self.r_weight_box,
                                                self.r_best_before_box,
                                                self.r_batch_code_box,
                                                self.r_spacer2_box,
                                                self.r_lower_menu2_box,
                                                ])

    def enter_receiving_main(self, widget):
        self.__clear_receiving_window()
        self.main_window.content = self.r_main_box

    def __clear_receiving_window(self):
        self.r_sku_entry.value = ""
        self.r_outer_sku_box.remove(self.no_sku_label_box)

    def enter_receiving_detail(self, widget):
        sku = self.r_sku_entry.value
        self.__clear_receiving_window()
        if sku == "111":
            self.main_window.content = self.r_details_box
        else:
            self.no_sku_found_label.text = f"SKU {sku} not found."
            self.r_outer_sku_box.insert(1, self.no_sku_label_box)

    def receive_product(self, sku):
        print(f"Received {sku}")

    def r_save_details(self, widget):
        pass

    def back_to_receiving(self, widget):
        self.enter_receiving_main(widget)

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
