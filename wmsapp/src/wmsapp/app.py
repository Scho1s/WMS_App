"""
WMS application for android scanners to work together with Dynamics GP
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER, RIGHT, LEFT
from toga.constants import RED, WHITE


class Receive:
    def __init__(self, root):
        self.root = root
        self.__create_receiving_main_window()
        self.__create_receiving_detail_window()

    def __create_receiving_main_window(self):
        self.sku_label = toga.Label("SKU:", style=self.root.DEF_LABEL_STYLE)

        self.sku_entry = toga.TextInput(style=self.root.DEF_ENTRY_STYLE)

        self.no_sku_found_label = toga.Label("", style=self.root.DEF_ERROR_STYLE)

        self.spacer = toga.Box(style=self.root.DEF_SPACER_STYLE)

        self.enter_button = toga.Button(
            "Enter",
            on_press=self.enter_receiving_detail,
            style=self.root.DEF_LOW_MENU_STYLE,
        )

        self.back_button = toga.Button(
            "Back",
            on_press=self.root.back_to_main,
            style=self.root.DEF_LOW_MENU_STYLE,
        )

        self.sku_box = toga.Box(style=Pack(padding=self.root.DEF_PADDING,
                                           alignment=RIGHT,
                                           background_color=WHITE,
                                           flex=1),
                                children=[self.sku_label,
                                          self.sku_entry,
                                          ])

        self.no_sku_label_box = toga.Box(style=Pack(padding=self.root.DEF_PADDING,
                                                    alignment=RIGHT,
                                                    background_color=WHITE,
                                                    ),
                                         children=[self.no_sku_found_label,
                                                   ])

        self.outer_sku_box = toga.Box(style=Pack(direction=COLUMN,
                                                 alignment=CENTER,
                                                 background_color=WHITE,
                                                 ),
                                      children=[self.sku_box,
                                                self.no_sku_label_box,
                                                ])

        self.spacer_box = toga.Box(style=Pack(direction=COLUMN,
                                              background_color=WHITE,
                                              flex=1),
                                   children=[self.spacer,
                                             ])

        self.lower_menu_box = toga.Box(style=Pack(padding=self.root.DEF_PADDING,
                                                  background_color=WHITE,
                                                  ),
                                       children=[self.enter_button,
                                                 self.back_button,
                                                 ])

        self.main_box = toga.Box(style=Pack(padding=self.root.DEF_PADDING,
                                            background_color=WHITE,
                                            direction=COLUMN),
                                 children=[self.outer_sku_box,
                                           self.spacer_box,
                                           self.lower_menu_box,
                                           ])

    def __clear_receiving_main_window(self):
        self.sku_entry.value = ""
        self.outer_sku_box.remove(self.no_sku_label_box)

    def enter_receiving_main(self, widget):
        self.__clear_receiving_main_window()
        self.root.change_window("Receiving", self.main_box)

    def __create_receiving_detail_window(self):
        self.item_code_label = toga.Label("", style=Pack(padding=self.root.LABEL_PADDING))

        self.item_desc_label = toga.Label("", style=Pack(padding=self.root.LABEL_PADDING))

        self.quantity_label = toga.Label("Quantity: ", style=self.root.DEF_LABEL_STYLE)

        self.quantity_entry = toga.NumberInput(style=self.root.DEF_ENTRY_STYLE)

        self.weight_label = toga.Label("Weight: ", style=self.root.DEF_LABEL_STYLE)

        self.weight_entry = toga.NumberInput(style=self.root.DEF_ENTRY_STYLE, step=0.001)

        self.best_before_label = toga.Label("Best Before: ", style=self.root.DEF_LABEL_STYLE)

        self.best_before_entry = toga.DateInput(style=self.root.DEF_ENTRY_STYLE)

        self.batch_code_label = toga.Label("Batch Code: ", style=self.root.DEF_LABEL_STYLE)

        self.batch_code_entry = toga.TextInput(style=self.root.DEF_ENTRY_STYLE)

        self.tag_label = toga.Label("Tag: ", style=self.root.DEF_LABEL_STYLE)

        self.tag_entry = toga.TextInput(style=self.root.DEF_ENTRY_STYLE)

        self.spacer = toga.Box(style=Pack(flex=1, direction=COLUMN, background_color=WHITE))

        self.save_button = toga.Button(
            "Save",
            on_press=self.save_details,
            style=self.root.DEF_LOW_MENU_STYLE,
        )

        self.back_button = toga.Button(
            "Back",
            on_press=self.back_to_receiving_main,
            style=self.root.DEF_LOW_MENU_STYLE,
        )

        self.item_details_box = toga.Box(style=self.root.DEF_DETAILS_BOX_STYLE,
                                         children=[self.item_code_label, self.item_desc_label])

        self.quantity_box = toga.Box(style=self.root.DEF_DETAILS_BOX_STYLE,
                                     children=[self.quantity_label, self.quantity_entry])

        self.weight_box = toga.Box(style=self.root.DEF_DETAILS_BOX_STYLE,
                                   children=[self.weight_label, self.weight_entry])

        self.best_before_box = toga.Box(style=self.root.DEF_DETAILS_BOX_STYLE,
                                        children=[self.best_before_label, self.best_before_entry])

        self.batch_code_box = toga.Box(style=self.root.DEF_DETAILS_BOX_STYLE,
                                       children=[self.batch_code_label, self.batch_code_entry])

        self.tag_box = toga.Box(style=self.root.DEF_DETAILS_BOX_STYLE,
                                children=[self.tag_label, self.tag_entry])

        self.spacer_box = toga.Box(style=Pack(direction=COLUMN, flex=1, background_color=WHITE),
                                   children=[self.spacer])

        self.lower_menu_box = toga.Box(style=self.root.DEF_DETAILS_BOX_STYLE,
                                       children=[self.save_button, self.back_button])

        self.details_box = toga.Box(style=Pack(padding=self.root.DEF_PADDING, direction=COLUMN, background_color=WHITE),
                                    children=[self.item_details_box,
                                              self.quantity_box,
                                              self.weight_box,
                                              self.best_before_box,
                                              self.batch_code_box,
                                              self.tag_box,
                                              self.spacer_box,
                                              self.lower_menu_box,
                                              ])

    def __clear_receiving_details_window(self):
        self.quantity_entry.value = None
        self.weight_entry.value = None
        self.best_before_entry.value = None
        self.batch_code_entry.value = None
        self.tag_entry.value = None

    def enter_receiving_detail(self, widget):
        sku = self.sku_entry.value
        self.__clear_receiving_main_window()
        self.__clear_receiving_details_window()
        if sku == "111":
            self.root.main_window.content = self.details_box
        else:
            self.no_sku_found_label.text = f"SKU {sku} not found."
            self.outer_sku_box.insert(1, self.no_sku_label_box)

    def save_details(self, widget):
        print(self.best_before_entry.value)           # TODO: Add a SQL query to save details into the database.
        self.enter_receiving_main(widget)

    def back_to_receiving_main(self, widget):
        self.enter_receiving_main(widget)


class Putaway:
    def __init__(self, root):
        self.root = root
        self.__create_putaway_main_window()
        self.__create_putaway_detail_window()

    def __create_putaway_main_window(self):
        self.tag_label = toga.Label("Tag:", style=self.root.DEF_LABEL_STYLE)

        self.tag_entry = toga.TextInput(style=self.root.DEF_ENTRY_STYLE)

        self.no_tag_found_label = toga.Label("", style=self.root.DEF_ERROR_STYLE)

        self.spacer = toga.Box(style=self.root.DEF_SPACER_STYLE)

        self.enter_button = toga.Button(
            "Enter",
            on_press=self.enter_putaway_detail,
            style=self.root.DEF_LOW_MENU_STYLE,
        )

        self.back_button = toga.Button(
            "Back",
            on_press=self.root.back_to_main,
            style=self.root.DEF_LOW_MENU_STYLE,
        )

        self.tag_box = toga.Box(style=Pack(padding=self.root.DEF_PADDING,
                                           alignment=RIGHT,
                                           background_color=WHITE,
                                           flex=1),
                                children=[self.tag_label,
                                          self.tag_entry,
                                          ])

        self.no_tag_label_box = toga.Box(style=Pack(padding=self.root.DEF_PADDING,
                                                    alignment=RIGHT,
                                                    background_color=WHITE,
                                                    ),
                                         children=[self.no_tag_found_label,
                                                   ])

        self.outer_tag_box = toga.Box(style=Pack(direction=COLUMN,
                                                 alignment=CENTER,
                                                 background_color=WHITE,
                                                 ),
                                      children=[self.tag_box,
                                                self.no_tag_label_box,
                                                ])

        self.spacer_box = toga.Box(style=Pack(direction=COLUMN,
                                              background_color=WHITE,
                                              flex=1),
                                   children=[self.spacer,
                                             ])

        self.lower_menu_box = toga.Box(style=Pack(padding=self.root.DEF_PADDING,
                                                  background_color=WHITE,
                                                  ),
                                       children=[self.enter_button,
                                                 self.back_button,
                                                 ])

        self.main_box = toga.Box(style=Pack(padding=self.root.DEF_PADDING,
                                            background_color=WHITE,
                                            direction=COLUMN),
                                 children=[self.outer_tag_box,
                                           self.spacer_box,
                                           self.lower_menu_box,
                                           ])

    def __clear_putaway_main_window(self):
        self.tag_entry.value = None
        self.outer_tag_box.remove(self.no_tag_label_box)

    def enter_putaway_main(self, widget):
        self.__clear_putaway_main_window()
        self.root.change_window("Putaway", self.main_box)

    def __create_putaway_detail_window(self):
        self.tag_label = toga.Label("", style=self.root.DEF_LABEL_STYLE)
        
        self.item_code_label = toga.Label("", style=self.root.DEF_LABEL_STYLE)
        self.item_desc_label = toga.Label("", style=self.root.DEF_LABEL_STYLE)

        self.quantity_label = toga.Label("Quantity: ", style=self.root.DEF_LABEL_STYLE)
        self.quantity_value_label = toga.Label("", style=self.root.DEF_LABEL_STYLE)

        self.weight_label = toga.Label("Weight: ", style=self.root.DEF_LABEL_STYLE)
        self.weight_value_label = toga.Label("", style=self.root.DEF_LABEL_STYLE)

        self.best_before_label = toga.Label("Best Before: ", style=self.root.DEF_LABEL_STYLE)
        self.best_before_value_label = toga.Label("", style=self.root.DEF_LABEL_STYLE)

        self.batch_code_label = toga.Label("Batch Code: ", style=self.root.DEF_LABEL_STYLE)
        self.batch_code_value_label = toga.Label("", style=self.root.DEF_LABEL_STYLE)

        self.location_from_label = toga.Label("From:", style=self.root.DEF_LABEL_STYLE)
        self.location_from_value_label = toga.Label("", style=self.root.DEF_LABEL_STYLE)

        self.location_to_label = toga.Label("To:", style=self.root.DEF_LABEL_STYLE)
        self.location_to_entry = toga.TextInput(style=self.root.DEF_ENTRY_STYLE)

        self.spacer = toga.Box(style=Pack(flex=1, direction=COLUMN, background_color=WHITE))

        self.save_button = toga.Button("Save",
                                       on_press=self.save_tag,
                                       style=self.root.DEF_LOW_MENU_STYLE)

        self.back_button = toga.Button("Back",
                                       on_press=self.back_to_putaway_main,
                                       style=self.root.DEF_LOW_MENU_STYLE,
                                       )

        self.tag_box = toga.Box(style=self.root.DEF_DETAILS_BOX_STYLE,
                                children=[self.tag_label, ])

        self.item_details_box = toga.Box(style=self.root.DEF_DETAILS_BOX_STYLE,
                                         children=[self.item_code_label, self.item_desc_label])

        self.quantity_box = toga.Box(style=self.root.DEF_DETAILS_BOX_STYLE,
                                     children=[self.quantity_label, self.quantity_value_label])

        self.weight_box = toga.Box(style=self.root.DEF_DETAILS_BOX_STYLE,
                                   children=[self.weight_label, self.weight_value_label])

        self.best_before_box = toga.Box(style=self.root.DEF_DETAILS_BOX_STYLE,
                                        children=[self.best_before_label, self.best_before_value_label])

        self.batch_code_box = toga.Box(style=self.root.DEF_DETAILS_BOX_STYLE,
                                       children=[self.batch_code_label, self.batch_code_value_label])

        self.location_from_box = toga.Box(style=self.root.DEF_DETAILS_BOX_STYLE,
                                          children=[self.location_from_label, self.location_from_value_label])

        self.location_to_box = toga.Box(style=self.root.DEF_DETAILS_BOX_STYLE,
                                        children=[self.location_to_label, self.location_to_entry])

        self.spacer_box = toga.Box(style=Pack(direction=COLUMN, flex=1, background_color=WHITE),
                                   children=[self.spacer])

        self.lower_menu_box = toga.Box(style=self.root.DEF_DETAILS_BOX_STYLE,
                                       children=[self.save_button, self.back_button])

        self.details_box = toga.Box(style=Pack(padding=self.root.DEF_PADDING, direction=COLUMN, background_color=WHITE),
                                    children=[self.tag_box,
                                              self.item_details_box,
                                              self.quantity_box,
                                              self.weight_box,
                                              self.best_before_box,
                                              self.batch_code_box,
                                              self.location_from_box,
                                              self.location_to_box,
                                              self.spacer_box,
                                              self.lower_menu_box,
                                              ])

    def __clear_putaway_detail_window(self):
        pass

    def enter_putaway_detail(self, widget):
        self.__clear_putaway_detail_window()
        if self.tag_entry.value == "222":                           # TODO: Change to query a database.
            self.location_to_entry.value = "A01"                    # TODO: Change to get a default location from SQL.
            self.root.main_window.content = self.details_box
        else:
            pass

    def back_to_putaway_main(self, widget):
        self.enter_putaway_main(widget)

    def save_tag(self, widget):
        pass


class WMSApp(toga.App):
    MENU_FONT_SIZE = 20
    ERROR_FONT_SIZE = 15
    DEF_PADDING = 5
    DEF_BUTTON_FONT = "Roboto_Thin"
    DEF_LABEL_FONT = "Roboto_Black"
    DEF_LABEL_VALUE_FONT = "Roboto_Italic"
    DEF_ERROR_FONT = "Roboto_Medium"
    LABEL_PADDING = (DEF_PADDING, 1, DEF_PADDING, DEF_PADDING)
    ENTRY_PADDING = (DEF_PADDING, DEF_PADDING, DEF_PADDING, 1)
    DEF_ENTRY_STYLE = Pack(direction=COLUMN, flex=1)
    DEF_LABEL_STYLE = Pack(padding=LABEL_PADDING, font_family=DEF_LABEL_FONT, alignment=RIGHT,
                           width=75, background_color=WHITE)
    DEF_LABEL_VALUE_STYLE = Pack(padding=LABEL_PADDING, font_family=DEF_LABEL_VALUE_FONT, alignment=LEFT,
                                 flex=1, background_color=WHITE)
    DEF_MAIN_MENU_STYLE = Pack(padding=DEF_PADDING, font_size=MENU_FONT_SIZE, font_family=DEF_BUTTON_FONT)
    DEF_LOW_MENU_STYLE = Pack(padding=DEF_PADDING, font_size=MENU_FONT_SIZE, font_family=DEF_BUTTON_FONT, flex=1)
    DEF_DETAILS_BOX_STYLE = Pack(padding=DEF_PADDING, background_color=WHITE)
    DEF_ERROR_STYLE = Pack(padding=DEF_PADDING, font_size=ERROR_FONT_SIZE, font_family=DEF_ERROR_FONT,
                           alignment=RIGHT, color=RED, background_color=WHITE)
    DEF_BG_STYLE = Pack(direction=COLUMN, padding=(10, DEF_PADDING, DEF_PADDING, DEF_PADDING), background_color=WHITE)
    DEF_SPACER_STYLE = Pack(direction=COLUMN, flex=1, background_color=WHITE)

    def startup(self):
        self.__create_helpers()
        self.__create_windows()
        self.__add_main_menu()

        # TODO: Create login page
        # TODO: Create full logging from receiving to shipping
        # TODO: Create client-server sockets

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
        toga.Font.register("Roboto_Italic", "resources/Roboto-Italic.ttf")

    def __create_windows(self):
        self.receive = Receive(self)
        self.putaway = Putaway(self)

    def __add_main_menu(self):
        self.receiving_button = toga.Button(
            "Receiving",
            on_press=self.receive.enter_receiving_main,
            style=self.DEF_MAIN_MENU_STYLE,
        )

        self.putaway_button = toga.Button(
            "Put away",
            on_press=self.putaway.enter_putaway_main,
            style=self.DEF_MAIN_MENU_STYLE,
        )

        self.picking_button = toga.Button(
            "Picking",
            style=self.DEF_MAIN_MENU_STYLE,
        )

        self.cuts_button = toga.Button(
            "Cuts",
            style=self.DEF_MAIN_MENU_STYLE,
        )

        self.inventory_check_button = toga.Button(
            "Inventory Check",
            style=self.DEF_MAIN_MENU_STYLE,
        )

        self.exit_button = toga.Button(
            "Exit",
            on_press=self.__exit,
            style=self.DEF_MAIN_MENU_STYLE,
        )

    def back_to_main(self, widget):
        self.change_window("Home", self.main_box)

    def change_window(self, new_title, new_window):
        self.main_window.title = new_title
        self.main_window.content = new_window

    def __exit(self, widget):
        self.request_exit()


def main():
    return WMSApp()
