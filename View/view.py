import os

import Utils.dialog_windows as dialog

from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen


class MyScreenView(MDScreen):

    controller = ObjectProperty()
    model = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.model.add_observer(self)
        self.recently_opend_dialogs = []
        self.dialog = []

    def open_dialog(self, mode: str):
        """ Call input, filter and delete windows, save and upload """
        if mode == "input":
            self.dialog.append(dialog.InputWindow(model=self.model, controller=self.controller))
        elif mode == "filter":
            self.dialog.append(dialog.FilterWindow(model=self.model, controller=self.controller))
        elif mode == "delete":
            self.dialog.append(dialog.DeleteWindow(model=self.model, controller=self.controller))
        elif mode == "upload":
            self.dialog.append(dialog.UploadWindow(model=self.model, controller=self.controller))
        elif mode == "save":
            self.dialog.append(dialog.SaveWindow(model=self.model, controller=self.controller))
        elif mode == "ND":
            self.dialog.append(dialog.ND_Dialog(model=self.model, controller=self.controller, mode=mode))
        elif mode == "DA":
            self.dialog.append(dialog.DA_Dialog(model=self.model, controller=self.controller, mode=mode))
        elif mode == "DAS":
            self.dialog.append(dialog.DAS_Dialog(model=self.model, controller=self.controller, mode=mode))
        elif mode == "TT":
            self.dialog.append(dialog.TT_Dialog(model=self.model, controller=self.controller, mode=mode))
        self.dialog[-1].open()
        self.recently_opend_dialogs.append(self.dialog[-1])
        self.controller.dialog(mode, self.dialog)

    def close_dialog(self, dialog_data: list | tuple):
        if self.dialog[-1].mode == "input":
            self.controller.input_stock(dialog_data)
        elif self.dialog[-1].mode == "filter":
            match dialog_data:
                case "number":
                    self.open_dialog(mode="ND")
                case "time":
                    self.open_dialog(mode="DA")
                case "station":
                    self.open_dialog(mode="DAS")
                case "travel time":
                    self.open_dialog(mode="TT")
        elif self.dialog[-1].mode == "delete":
            match dialog_data:
                case "number":
                    self.open_dialog(mode="ND")
                case "time":
                    self.open_dialog(mode="DA")
                case "station":
                    self.open_dialog(mode="DAS")
                case "travel time":
                    self.open_dialog(mode="TT")
        elif self.dialog[-1].mode == "upload":
            self.controller.upload_from_file(dialog_data)
        elif self.dialog[-1].mode == "save":
            self.controller.save_in_file(dialog_data)
        elif self.dialog[-1].mode == "ND":
            for element in self.recently_opend_dialogs[::-1]:
                if "DeleteWindow" in str(element):
                    self.controller.delete_stock(dialog_data, "ND")
                elif "FilterWindow" in str(element):
                    print("FilterWindow")
                    self.controller.filter_stock(dialog_data, "ND")
        elif self.dialog[-1].mode == "DA":
            for element in self.recently_opend_dialogs[::-1]:
                if "DeleteWindow" in str(element):
                    self.controller.delete_stock(dialog_data, "DA")
                elif "FilterWindow" in str(element):
                    print("FilterWindow")
                    self.controller.filter_stock(dialog_data, "DA")
        elif self.dialog[-1].mode == "DAS":
            for element in self.recently_opend_dialogs[::-1]:
                if "DeleteWindow" in str(element):
                    self.controller.delete_stock(dialog_data, "DAS")
                elif "FilterWindow" in str(element):
                    print("FilterWindow")
                    self.controller.filter_stock(dialog_data, "DAS")
        elif self.dialog[-1].mode == "TT":
            for element in self.recently_opend_dialogs[::-1]:
                if "DeleteWindow" in str(element):
                    self.controller.delete_stock(dialog_data, "TT")
                elif "FilterWindow" in str(element):
                    print("FilterWindow")
                    self.controller.filter_stock(dialog_data, "TT")
        pop_element = self.dialog.pop(0)
        print("Pop element", pop_element, "\n", self.dialog)

    def model_is_changed(self, data):
        """ The method is called when the Model changes. """
        self.close_dialog(data)

    def refresh(self):
        self.controller.update()

    def build(self):
        self.add_widget(self.model.table)
        return self


Builder.load_file(os.path.join(os.path.dirname(__file__), "view.kv"))
