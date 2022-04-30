import os
import Utils.dialog_windows as window
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.screen import Screen
from kivymd.uix.snackbar import Snackbar


class MyScreenView(MDScreen):

    controller = ObjectProperty()
    model = ObjectProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.model.add_observer(self)
        self.screen = Screen()
        self.dialog = None

    def open_dialog(self, mode: str):
        """ Call input, filter and delete windows, save and upload """
        if mode == "input":
            self.dialog = window.InputWindow(model=self.model, controller=self.controller)
        elif mode == "filter":
            self.dialog = window.FilterWindow(model=self.model, controller=self.controller)
        elif mode == "delete":
            self.dialog = window.DeleteWindow(model=self.model, controller=self.controller)
        elif mode == "upload":
            self.dialog = window.UploadWindow(model=self.model, controller=self.controller)
        elif mode == "save":
            self.dialog = window.SaveWindow(model=self.model, controller=self.controller)
        self.dialog.open()
        print(self.controller.dialog)
        self.controller.dialog(mode, self.dialog)

    def close_dialog(self, dialog_data: list = []):
        if self.dialog.mode == "input":
            self.controller.input_stock(dialog_data)
        elif self.dialog.mode == "filter":
            self.controller.filter_stock(dialog_data)
        elif self.dialog.mode == "delete":
            unlucky = self.controller.delete_stock(dialog_data)
            Snackbar(text=f"{unlucky} stock are deleted!").open()
        elif self.dialog.mode == "upload":
            self.controller.upload_from_file(dialog_data)
        elif self.dialog.mode == "save":
            self.controller.save_in_file(dialog_data)
        self.dialog = None

    def model_is_changed(self, data):
        """ The method is called when the Model changes. """
        self.close_dialog(data)

    def refresh(self):
        self.controller.refresh()

    def build(self):
        self.add_widget(self.model.table)
        return self


Builder.load_file(os.path.join(os.path.dirname(__file__), "view.kv"))
