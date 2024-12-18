"""
WMS application for android scanners to work together with Dynamics GP
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER, RIGHT
from toga.constants import RED, WHITE


class WMSApp(toga.App):
    MENU_FONT_SIZE = 20
    ERROR_FONT_SIZE = 15
    DEF_PADDING = 5
    DEF_BUTTON_FONT = "Roboto_Thin"
    DEF_LABEL_FONT = "Roboto_Black"
    DEF_ERROR_FONT = "Roboto_Medium"
    LABEL_PADDING = (DEF_PADDING, 1, DEF_PADDING, DEF_PADDING)
    ENTRY_PADDING = (DEF_PADDING, DEF_PADDING, DEF_PADDING, 1)
    DEF_ENTRY_STYLE = Pack(direction=COLUMN, flex=1)
    DEF_LABEL_STYLE = Pack(padding=LABEL_PADDING, font_family=DEF_LABEL_FONT, alignment=RIGHT,
                           width=75, background_color=WHITE)
    DEF_MAIN_MENU_STYLE = Pack(padding=DEF_PADDING, font_size=MENU_FONT_SIZE, font_family=DEF_BUTTON_FONT)
    DEF_LOW_MENU_STYLE = Pack(padding=DEF_PADDING, font_size=MENU_FONT_SIZE, font_family=DEF_BUTTON_FONT, flex=1)
    DEF_ERROR_STYLE = Pack(padding=DEF_PADDING, font_size=ERROR_FONT_SIZE, font_family=DEF_ERROR_FONT,
                           alignment=RIGHT, color=RED, background_color=WHITE)
    DEF_BG_STYLE = Pack(direction=COLUMN, padding=(10, DEF_PADDING, DEF_PADDING, DEF_PADDING), background_color=WHITE)
    DEF_SPACER_STYLE = Pack(direction=COLUMN, flex=1, background_color=WHITE)

    def startup(self):
        self.__create_helpers()
        self.__create_windows()
        self.__add_main_menu()

        # TODO: Create login page

        self.main_box = toga.Box(style=self.DEF_BG_STYLE,
                                 children=[self.receiving_button,
                                           self.putaway_button,
                                           self.picking_button,
                                           self.cuts_button,
                                           self.inventory_check_button,
                                           self.exit_button,
                                           ])

        self.main_window = toga.MainWindow(title="Home")
        self.main_window.content = self.main_box
        self.main_window.show()

    def __create_helpers(self):
        self.spacer = toga.Box(style=self.DEF_SPACER_STYLE)

        toga.Font.register("Roboto_Thin", "resources/Roboto-Thin.ttf")
        toga.Font.register("Roboto_Black", "resources/Roboto-BlackItalic.ttf")
        toga.Font.register("Roboto_Medium", "resources/Roboto-Medium.ttf")

    def __create_windows(self):
        self.__create_receiving_main_window()
        self.__create_receiving_detail_window()
        self.create_picking_window()
        self.create_putaway_window()

    def __add_main_menu(self):
        self.receiving_button = toga.Button(
            "Receiving",
            on_press=self.enter_receiving_main,
            style=self.DEF_MAIN_MENU_STYLE,
        )

        self.putaway_button = toga.Button(
            "Put away",
            on_press=self.enter_putaway_main,
            style=self.DEF_MAIN_MENU_STYLE,
        )

        self.picking_button = toga.Button(
            "Picking",
            on_press=self.enter_picking_main,
            style=self.DEF_MAIN_MENU_STYLE,
        )

        self.cuts_button = toga.Button(
            "Cuts",
            on_press=self.enter_cuts_main,
            style=self.DEF_MAIN_MENU_STYLE,
        )

        self.inventory_check_button = toga.Button(
            "Inventory Check",
            on_press=self.enter_inventory_check_main,
            style=self.DEF_MAIN_MENU_STYLE,
        )

        self.exit_button = toga.Button(
            "Exit",
            on_press=self.__exit,
            style=self.DEF_MAIN_MENU_STYLE,
        )

    # Receiving

    def __create_receiving_main_window(self):
        self.r_sku_label = toga.Label("SKU:",
                                      style=self.DEF_LABEL_STYLE)

        self.r_sku_entry = toga.TextInput(style=Pack(direction=COLUMN,
                                                     flex=1))

        self.no_sku_found_label = toga.Label("",
                                             style=self.DEF_ERROR_STYLE)

        self.r_spacer = toga.Box(style=self.DEF_SPACER_STYLE)

        self.r_enter_button = toga.Button(
            "Enter",
            on_press=self.enter_receiving_detail,
            style=self.DEF_LOW_MENU_STYLE,
        )

        self.r_back_button = toga.Button(
            "Back",
            on_press=self.back_to_main,
            style=self.DEF_LOW_MENU_STYLE,
        )

        self.sku_box = toga.Box(style=Pack(padding=self.DEF_PADDING,
                                           alignment=RIGHT,
                                           background_color=WHITE,
                                           flex=1),
                                children=[self.r_sku_label,
                                          self.r_sku_entry,
                                          ])

        self.no_sku_label_box = toga.Box(style=Pack(padding=self.DEF_PADDING,
                                                    alignment=RIGHT,
                                                    background_color=WHITE,
                                                    ),
                                         children=[self.no_sku_found_label,
                                                   ])

        self.r_outer_sku_box = toga.Box(style=Pack(direction=COLUMN,
                                                   alignment=CENTER,
                                                   background_color=WHITE,
                                                   ),
                                        children=[self.sku_box,
                                                  self.no_sku_label_box,
                                                  ])

        self.r_spacer_box = toga.Box(style=Pack(direction=COLUMN,
                                                background_color=WHITE,
                                                flex=1),
                                     children=[self.r_spacer,
                                               ])

        self.lower_menu_box = toga.Box(style=Pack(padding=self.DEF_PADDING,
                                                  background_color=WHITE,
                                                  ),
                                       children=[self.r_enter_button,
                                                 self.r_back_button,
                                                 ])

        self.r_main_box = toga.Box(style=Pack(padding=self.DEF_PADDING,
                                              background_color=WHITE,
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
                                           style=self.DEF_LABEL_STYLE)

        self.r_quantity_entry = toga.NumberInput(style=self.DEF_ENTRY_STYLE)

        self.r_weight_label = toga.Label("Weight: ",
                                         style=self.DEF_LABEL_STYLE)

        self.r_weight_entry = toga.NumberInput(style=self.DEF_ENTRY_STYLE, step=0.001)

        self.r_best_before_label = toga.Label("Best Before: ",
                                              style=self.DEF_LABEL_STYLE)

        self.r_best_before_entry = toga.DateInput(style=self.DEF_ENTRY_STYLE)

        self.r_batch_code_label = toga.Label("Batch Code: ",
                                             style=self.DEF_LABEL_STYLE)

        self.r_batch_code_entry = toga.TextInput(style=self.DEF_ENTRY_STYLE)

        self.r_tag_label = toga.Label("Tag: ",
                                      style=self.DEF_LABEL_STYLE)

        self.r_tag_entry = toga.TextInput(style=self.DEF_ENTRY_STYLE)

        self.r_spacer2 = toga.Box(
            id="r_spacer2",
            style=Pack(flex=1,
                       direction=COLUMN,
                       background_color=WHITE),
        )

        self.r_save_button = toga.Button(
            "Save",
            on_press=self.r_save_details,
            style=self.DEF_LOW_MENU_STYLE,
        )

        self.r_back_button2 = toga.Button(
            "Back",
            on_press=self.back_to_receiving,
            style=self.DEF_LOW_MENU_STYLE,
        )

        self.r_item_details_box = toga.Box(style=Pack(padding=self.DEF_PADDING, background_color=WHITE),
                                           children=[self.r_item_code_label, self.r_item_desc_label])

        self.r_quantity_box = toga.Box(style=Pack(padding=self.DEF_PADDING, background_color=WHITE),
                                       children=[self.r_quantity_label, self.r_quantity_entry])

        self.r_weight_box = toga.Box(style=Pack(padding=self.DEF_PADDING, background_color=WHITE),
                                     children=[self.r_weight_label, self.r_weight_entry])

        self.r_best_before_box = toga.Box(style=Pack(padding=self.DEF_PADDING, background_color=WHITE),
                                          children=[self.r_best_before_label, self.r_best_before_entry])

        self.r_batch_code_box = toga.Box(style=Pack(padding=self.DEF_PADDING, background_color=WHITE),
                                         children=[self.r_batch_code_label, self.r_batch_code_entry])

        self.r_tag_box = toga.Box(style=Pack(padding=self.DEF_PADDING, background_color=WHITE),
                                  children=[self.r_tag_label, self.r_tag_entry])

        self.r_spacer2_box = toga.Box(style=Pack(direction=COLUMN, flex=1, background_color=WHITE),
                                      children=[self.r_spacer2])

        self.r_lower_menu2_box = toga.Box(style=Pack(padding=self.DEF_PADDING, background_color=WHITE),
                                          children=[self.r_save_button, self.r_back_button2])

        self.r_details_box = toga.Box(style=Pack(padding=self.DEF_PADDING, direction=COLUMN, background_color=WHITE),
                                      children=[self.r_item_details_box,
                                                self.r_quantity_box,
                                                self.r_weight_box,
                                                self.r_best_before_box,
                                                self.r_batch_code_box,
                                                self.r_tag_box,
                                                self.r_spacer2_box,
                                                self.r_lower_menu2_box,
                                                ])

    def enter_receiving_main(self, widget):
        self.__clear_receiving_main_window()
        self.main_window.title = "Receiving"
        self.main_window.content = self.r_main_box

    def __clear_receiving_main_window(self):
        self.r_sku_entry.value = ""
        self.r_outer_sku_box.remove(self.no_sku_label_box)

    def __clear_receiving_details_window(self):
        self.r_quantity_entry.value = None
        self.r_weight_entry.value = None
        self.r_best_before_entry.value = None
        self.r_batch_code_entry.value = None
        self.r_tag_entry.value = None

    def enter_receiving_detail(self, widget):
        sku = self.r_sku_entry.value
        self.__clear_receiving_main_window()
        self.__clear_receiving_details_window()
        if sku == "111":
            self.main_window.content = self.r_details_box
        else:
            self.no_sku_found_label.text = f"SKU {sku} not found."
            self.r_outer_sku_box.insert(1, self.no_sku_label_box)

    def r_save_details(self, widget):
        print(self.r_best_before_entry.value)           # TODO: Add a SQL query to save details into the database.
        self.enter_receiving_main(widget)

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

    # Cuts

    def enter_cuts_main(self, widget):
        pass

    # Inventory Check

    def enter_inventory_check_main(self, widget):
        pass

    def back_to_main(self, widget):
        self.main_window.title = "Home"
        self.main_window.content = self.main_box

    def __exit(self, widget):
        self.request_exit()


def main():
    return WMSApp()
