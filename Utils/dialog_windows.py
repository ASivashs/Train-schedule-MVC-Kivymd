import os
import datetime as dt

from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty

from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.picker import MDDatePicker, MDTimePicker
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.menu import MDDropdownMenu


# Dialog windows content
class DialogContent(BoxLayout):
    pass


class InputDialogContent(DialogContent):
    """Dialog window for create new schedule elements.
    This window contains:
    1. Dialog textfield for enter train number;
    2. Dialog textfield for enter departure station;
    3. Dialog textfield for enter arrival station;
    4. Date and time picker for enter departure date and time;
    5. Date and time picker for enter arrival date and time."""
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


class NDDialogContent(DialogContent):
    """Dialog window called in Filter and Delete.
    In this window you can enter train number or choose a date.
    This window contains:
    1. Dialog textfield for enter train number;
    2. Date and time picker for enter departure date and time."""
    def __init__(self):
        super(NDDialogContent, self).__init__()
        self._nd_departure_date = None
        self._nd_departure_time = None

    @property
    def nd_departure_date(self):
        return self._nd_departure_date

    @property
    def nd_departure_time(self):
        return self._nd_departure_time

    # Departure date widget
    def nd_departure_date_picker(self):
        date_dialog = MDDatePicker(
            mode="range",
            radius=[26, 26, 26, 26]
        )
        date_dialog.bind(
            on_save=self.nd_departure_date_picker_on_save,
            on_cancel=self.date_picker_on_cancel
        )
        date_dialog.open()

    # OK option for departure date widget
    def nd_departure_date_picker_on_save(self, instance, value, date_range):
        print(instance, value, date_range)
        self._nd_departure_date = value

    # Cancel option for date widget
    @staticmethod
    def date_picker_on_cancel(instance, value):
        pass

    # ND time widget
    def nd_departure_time_picker(self):
        time_dialog = MDTimePicker(
            minute_radius=[26, 26, 26, 26],
            hour_radius=[26, 26, 26, 26],
            am_pm_radius=26
        )
        time_dialog.bind(time=self.get_nd_departure_time)
        time_dialog.open()

    # ND time getter
    def get_nd_departure_time(self, instance, time):
        print(time)
        self._nd_departure_time = time


class DADialogContent(DialogContent):
    """Dialog window called in Filter and Delete.
    In this window you can choose departure date range or arrival date range.
    This window contains:
    1. Date and time picker for choose departure date and time;
    2. Date and time picker for choose arrival date and time."""
    def __init__(self):
        super(DADialogContent, self).__init__()
        self.__departure_date_range = None
        self.__arrival_date_range = None

    @property
    def departure_date_range(self):
        return self.__departure_date_range

    @property
    def arrival_date_range(self):
        return self.__arrival_date_range

    # Departure date widget
    def da_departure_date_picker(self):
        date_dialog = MDDatePicker(
            mode="range",
            radius=[26, 26, 26, 26]
        )
        date_dialog.bind(
            on_save=self.da_departure_date_picker_on_save,
            on_cancel=self.date_picker_on_cancel
        )
        date_dialog.open()

    # Arrival date widget
    def da_arrival_date_picker(self):
        date_dialog = MDDatePicker(
            mode="range",
            radius=[26, 26, 26, 26]
        )
        date_dialog.bind(
            on_save=self.da_arrival_date_picker_on_save,
            on_cancel=self.date_picker_on_cancel
        )

    # OK option for departure date widget
    def da_departure_date_picker_on_save(self, instance, value, date_range):
        print(instance, value, date_range)
        self.__departure_date_range = ((date_range[0], date_range[-1]), None)

    # OK option for arrival date widget
    def da_arrival_date_picker_on_save(self, instance, value, date_range):
        print(instance, value, date_range)
        self.__arrival_date_range = (None, (date_range[0], date_range[-1]))

    # Cancel option for date widget
    @staticmethod
    def date_picker_on_cancel(instance, value):
        pass


class DASDialogContent(DialogContent):
    """Dialog window called in Filter and Delete.
    In this window you can enter departure or arrival station.
    This window contains:
    1. Dialog textfield for enter departure station;
    2. Dialog textfield for enter arrival station."""
    pass


class TTDialogContent(DialogContent):
    """Dialog window called in Filter and Delete.
    In this window you can choose travel duration (days, time).
    This window contains:
    1. Dialog textfield for enter count of days travel;
    2. Date and time picker for choose trip duration in hours time."""
    def __init__(self):
        super(TTDialogContent, self).__init__()
        self.__travel_time_time = None

    @property
    def travel_time_time(self):
        return self.__travel_time_time

    # Travel time widget
    def travel_time_time_picker(self):
        time_dialog = MDTimePicker(
            minute_radius=[26, 26, 26, 26],
            hour_radius=[26, 26, 26, 26],
            am_pm_radius=26
        )
        time_dialog.bind(time=self.get_travel_time)
        time_dialog.open()

    # Travel time getter
    def get_travel_time(self, instance, time):
        print(time)
        self.__travel_time_time = time


# Some icons for Dropdown items
class IconListItem(OneLineIconListItem):
    icon = StringProperty()


KV_filter = '''
MDScreen

    MDDropDownItem:
        id: drop_item
        pos_hint: {'top': 4, "right": 6}
        text: 'Delete by'
        on_release: root.menu.open()
'''


class FilterDialogContent(DialogContent):
    """Filter dialog window that contains 4 buttons who also called dialog windows.
    You can choose filter mode and enter filter params.
    This window contains:
    1. Number and departure date and time;
    2. Departure date and arrival date;
    3. Departure station and arrival station;
    4. Travel time."""
    def __init__(self):
        super(FilterDialogContent, self).__init__()
        self.screen = Builder.load_string(KV_filter)
        self.menu_items = [
            {
                "viewclass": "IconListItem",
                "icon": "git",
                "text": "Train number and departure date and time",
                "height": dp(56),
                "on_release": lambda x="number": self.set_item(x),
            },
            {
                "viewclass": "IconListItem",
                "icon": "git",
                "text": "Departure and arrival date",
                "height": dp(56),
                "on_release": lambda x="time": self.set_item(x),
            },
            {
                "viewclass": "IconListItem",
                "icon": "git",
                "text": "Departure and arrival station",
                "height": dp(56),
                "on_release": lambda x="station": self.set_item(x),
            },
            {
                "viewclass": "IconListItem",
                "icon": "git",
                "text": "Travel time",
                "height": dp(56),
                "on_release": lambda x="travel time": self.set_item(x),
            },
        ]
        self.menu = MDDropdownMenu(
            caller=self.screen.ids.drop_item,
            items=self.menu_items,
            width_mult=dp(8),
        )
        self.menu.bind()
        self.__filter_mode = ""

    @property
    def filter_mode(self):
        return self.__filter_mode

    def set_item(self, text_item):
        self.__filter_mode = text_item
        self.screen.ids.drop_item.set_item(text_item)
        self.menu.dismiss()


KV_delete = '''
MDScreen

    MDDropDownItem:
        id: drop_item
        pos_hint: {'top': 4, "right": 6}
        text: 'Delete by'
        on_release: root.menu.open()
'''


class DeleteDialogContent(BoxLayout):
    """Filter dialog window that contains 4 buttons who also called dialog windows.
    You can choose delete mode and enter delete params.
    This window contains:
    1. Number and departure date and time;
    2. Departure date and arrival date;
    3. Departure station and arrival station;
    4. Travel time."""
    def __init__(self):
        super(DeleteDialogContent, self).__init__()
        self.screen = Builder.load_string(KV_delete)
        self.menu_items = [
            {
                "viewclass": "IconListItem",
                "icon": "git",
                "text": "Train number and departure date and time",
                "height": dp(56),
                "on_release": lambda x="number": self.set_item(x),
            },
            {
                "viewclass": "IconListItem",
                "icon": "git",
                "text": "Departure and arrival date",
                "height": dp(56),
                "on_release": lambda x="time": self.set_item(x),
            },
            {
                "viewclass": "IconListItem",
                "icon": "git",
                "text": "Departure and arrival station",
                "height": dp(56),
                "on_release": lambda x="station": self.set_item(x),
            },
            {
                "viewclass": "IconListItem",
                "icon": "git",
                "text": "Travel time",
                "height": dp(56),
                "on_release": lambda x="travel time": self.set_item(x),
            },
        ]
        self.menu = MDDropdownMenu(
            caller=self.screen.ids.drop_item,
            items=self.menu_items,
            width_mult=dp(8),
        )
        self.menu.bind()
        self.__delete_mode = ""

    @property
    def delete_mode(self):
        return self.__delete_mode

    def set_item(self, text_item):
        self.__delete_mode = text_item
        self.screen.ids.drop_item.set_item(text_item)
        self.menu.dismiss()


class UploadDialogContent(DialogContent):
    """Upload save schedule. You can enter upload file.
    This window contains:
    1. Dialog textfield for enter file name."""
    pass


class SaveDialogContent(DialogContent):
    """Save your train schedule. You can enter save file.
    This window contains:
    1. Dialog textfield for enter file name."""
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


# Call Input dialog window
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
            (
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
            )
        )


# Call ND dialog window
class ND_Dialog(DialogWindow):
    def __init__(self, **kwargs):
        super(ND_Dialog, self).__init__(
            title="Filter by number or departure time",
            type="custom",
            mode="ND",
            content_cls=NDDialogContent(),
            controller=kwargs["controller"],
            model=kwargs["model"],
            buttons=[
                MDFlatButton(
                    text="OK",
                    theme_text_color="Custom",
                    on_release=self.close
                )
            ]
        )

    def close(self, obj):
        self.dismiss()
        nd_time = None
        if self.content_cls.nd_departure_date and self.content_cls.nd_departure_time:
            nd_time = dt.datetime.strptime(f"{self.content_cls.nd_departure_date} {self.content_cls.nd_departure_time}",
                                           "%Y-%m-%d %H:%M:%S")
        elif self.content_cls.nd_departure_date and not self.content_cls.nd_departure_time:
            nd_time = (self.content_cls.nd_departure_date, None)
        elif not self.content_cls.nd_departure_date and self.content_cls.nd_departure_time:
            nd_time = (None, self.content_cls.nd_departure_time)
        self.controller.close_dialog(
            (
                self.content_cls.ids.nd_train_number.text if self.content_cls.ids.nd_train_number.text else None,
                nd_time
            )
        )


# Call DA dialog window
class DA_Dialog(DialogWindow):
    def __init__(self, **kwargs):
        super(DA_Dialog, self).__init__(
            title="Filter by departure or arrival time",
            type="custom",
            mode="DA",
            content_cls=DADialogContent(),
            controller=kwargs["controller"],
            model=kwargs["model"],
            buttons=[
                MDFlatButton(
                    text="OK",
                    theme_text_color="Custom",
                    on_release=self.close
                )
            ]
        )
        self.data = ()

    def close(self, obj):
        self.dismiss()
        self.controller.close_dialog(
            (
                (
                    self.content_cls.departure_date_range[0][0],
                    self.content_cls.departure_date_range[0][1]
                ) if self.content_cls.departure_date_range else None,
                (
                    self.content_cls.arrival_date_range[1][0],
                    self.content_cls.arrival_date_range[1][1]
                ) if self.content_cls.arrival_date_range else None
            )
        )


# Call DAS dialog window
class DAS_Dialog(DialogWindow):
    def __init__(self, **kwargs):
        super(DAS_Dialog, self).__init__(
            title="Filter by departure or arrival station",
            type="custom",
            mode="DAS",
            content_cls=DASDialogContent(),
            controller=kwargs["controller"],
            model=kwargs["model"],
            buttons=[
                MDFlatButton(
                    text="OK",
                    theme_text_color="Custom",
                    on_release=self.close
                )
            ]
        )
        self.data = ()

    def close(self, obj):
        self.dismiss()
        self.controller.close_dialog(
            (
                self.content_cls.ids.das_departure_station.text if self.content_cls.ids.das_departure_station.text else None,
                self.content_cls.ids.das_arrival_station.text if self.content_cls.ids.das_arrival_station.text else None
            )
        )


# Call TT dialog window
class TT_Dialog(DialogWindow):
    def __init__(self, **kwargs):
        super(TT_Dialog, self).__init__(
            title="Filter by travel time",
            type="custom",
            mode="TT",
            content_cls=TTDialogContent(),
            controller=kwargs["controller"],
            model=kwargs["model"],
            buttons=[
                MDFlatButton(
                    text="OK",
                    theme_text_color="Custom",
                    on_release=self.close
                )
            ]
        )

    def close(self, obj):
        self.dismiss()
        self.controller.close_dialog(
            (
                self.content_cls.ids.travel_time_days.text if self.content_cls.ids.travel_time_days.text else None,
                self.content_cls.travel_time_time if self.content_cls.travel_time_time else None
            )
        )


# Call Filter dialog window
class FilterWindow(DialogWindow):
    def __init__(self, **kwargs):
        super().__init__(
            title="Filter by",
            content_cls=FilterDialogContent(),
            mode="filter",
            controller=kwargs["controller"],
            model=kwargs["model"]
        )

    def close(self, obj):
        self.dismiss()
        self.controller.close_dialog(
            self.content_cls.filter_mode
        )


# Call Delete dialog window
class DeleteWindow(DialogWindow):
    def __init__(self, **kwargs):
        super().__init__(
            title="Delete by",
            content_cls=DeleteDialogContent(),
            mode="delete",
            controller=kwargs["controller"],
            model=kwargs["model"]
        )

    def close(self, obj):
        self.dismiss()
        self.controller.close_dialog(
            self.content_cls.delete_mode
        )


# Call Save dialog window
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


# Call Upload dialog window
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
