import os
import datetime as dt

from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.picker import MDDatePicker, MDTimePicker


# Dialog windows content
class DialogContent(BoxLayout):
    pass


class InputDialogContent(DialogContent):
    # Input date and time pickers
    def __init__(self):
        super(InputDialogContent, self).__init__()
        self._input_departure_date = None
        self._input_departure_time = None
        self._input_arrival_date = None
        self._input_arrival_time = None

    @property
    def input_departure_date(self):
        return self._input_departure_date

    @property
    def input_departure_time(self):
        return self._input_departure_time

    @property
    def input_arrival_date(self):
        return self._input_arrival_date

    @property
    def input_arrival_time(self):
        return self._input_arrival_time

    # Departure date widget
    def input_departure_date_picker(self):
        date_dialog = MDDatePicker(
            radius=[26, 26, 26, 26]
        )
        date_dialog.bind(
            on_save=self.input_departure_date_picker_on_save,
            on_cancel=self.date_picker_on_cancel
        )
        date_dialog.open()

    # Arrival date widget
    def input_arrival_date_picker(self):
        date_dialog = MDDatePicker(
            radius=[26, 26, 26, 26]
        )
        date_dialog.bind(
            on_save=self.input_arrival_date_picker_on_save,
            on_cancel=self.date_picker_on_cancel
        )
        date_dialog.open()

    # OK option for departure date widget
    def input_departure_date_picker_on_save(self, instance, value, date_range):
        print(instance, value, date_range)
        self._input_departure_date = value

    # OK option for arrival date widget
    def input_arrival_date_picker_on_save(self, instance, value, date_range):
        print(instance, value, date_range)
        self._input_arrival_date = value

    # Cancel option for date widget
    @staticmethod
    def date_picker_on_cancel(instance, value):
        pass

    # Departure time widget
    def input_departure_time_picker(self):
        time_dialog = MDTimePicker(
            minute_radius=[26, 26, 26, 26],
            hour_radius=[26, 26, 26, 26],
            am_pm_radius=26
        )
        time_dialog.bind(time=self.get_input_departure_time)
        time_dialog.open()

    # Arrival time widget
    def input_arrival_time_picker(self):
        time_dialog = MDTimePicker(
            minute_radius=[26, 26, 26, 26],
            hour_radius=[26, 26, 26, 26],
            am_pm_radius=26
        )
        time_dialog.bind(time=self.get_input_arrival_time)
        time_dialog.open()

    # Departure time getter
    def get_input_departure_time(self, instance, time):
        print(time)
        self._input_departure_time = time

    # Arrival time getter
    def get_input_arrival_time(self, instance, time):
        print(time)
        self._input_arrival_time = time


class FilterDialogContent(DialogContent):
    pass


class DeleteDialogContent(DialogContent):
    pass


class UploadDialogContent(DialogContent):
    pass


class SaveDialogContent(DialogContent):
    pass


# Dialog windows
class DialogWindow(MDDialog):
    def __init__(self, **kwargs):
        super().__init__(
            title=kwargs["title"],
            type="custom",
            content_cls=kwargs["content_cls"],
            buttons=[
                MDFlatButton(
                    text="OK",
                    theme_text_color="Custom",
                    on_release=self.close
                ),
            ],
        )
        self.mode = kwargs["mode"]
        self.controller = kwargs["controller"]
        self.model = kwargs["model"]

    def close(self, obj):
        self.dismiss()


class InputWindow(DialogWindow):
    def __init__(self, **kwargs):
        super().__init__(
            title="New Train",
            content_cls=InputDialogContent(),
            mode="input",
            controller=kwargs["controller"],
            model=kwargs["model"]
        )

    def close(self, obj):
        self.dismiss()
        self.controller.close_dialog(
            [
                self.content_cls.ids.input_train_number.text,
                self.content_cls.ids.input_departure_station.text,
                self.content_cls.ids.input_arrival_station.text,
                dt.datetime.strptime(
                    f"{self.content_cls.input_departure_date} {self.content_cls.input_departure_time}",
                    "%Y-%m-%d %H:%M:%S"
                ),
                dt.datetime.strptime(
                    f"{self.content_cls.input_arrival_date} {self.content_cls.input_arrival_time}",
                    "%Y-%m-%d %H:%M:%S"
                )
            ]
        )


class FilterWindow(DialogWindow):
    def __init__(self, **kwargs):
        super().__init__(
            title="Filter stock: ",
            content_cls=FilterDialogContent(),
            mode="filter",
            controller=kwargs["controller"],
            model=kwargs["model"]
        )


class DeleteWindow(DialogWindow):
    def __init__(self, **kwargs):
        super().__init__(
            title="Delete stock: ",
            content_cls=DeleteDialogContent(),
            mode="delete",
            controller=kwargs["controller"],
            model=kwargs["model"]
        )

    def close(self, obj):
        self.dismiss()
        self.controller.close_dialog(
            [
                self.content_cls.ids.delete_product.text,
                self.content_cls.ids.delete_line_up.text,
                self.content_cls.ids.delete_position.text,
                self.content_cls.ids.delete_titles.text,
                self.content_cls.ids.delete_street.text
            ]
        )


class SaveWindow(DialogWindow):
    def __init__(self, **kwargs):
        super().__init__(
            title="Saving: ",
            content_cls=SaveDialogContent(),
            mode="save",
            controller=kwargs["controller"],
            model=kwargs["model"]
        )

    def close(self, obj):
        self.dismiss()
        self.controller.close_dialog(self.content_cls.ids.save_path.text)


class UploadWindow(DialogWindow):
    def __init__(self, **kwargs):
        super().__init__(
            title="Upload: ",
            content_cls=UploadDialogContent(),
            mode="upload",
            controller=kwargs["controller"],
            model=kwargs["model"]
        )

    def close(self, obj):
        self.dismiss()
        self.controller.close_dialog(self.content_cls.ids.upload_path.text)


Builder.load_file(os.path.join(os.path.dirname(__file__), "dialog_windows.kv"))
