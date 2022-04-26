from train_schedule import schedule

from kivymd.app import MDApp
from kivy.core.window import Window

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton, MDRaisedButton
from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable


Window.size = (1450, 800)
Window.title = "Train schedule"


class TrainScheduleApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = MDBoxLayout()

    def build(self):
        data_tables = MDDataTable(
            size_hint=(1, .85),
            use_pagination=True,
            rows_num=10,
            column_data=[
                ("[size=30]Number[/size]", dp(30), self.sort_by_number),
                ("[size=30]Departure station[/size]", dp(60), self.sort_by_departure_station),
                ("[size=30]Arrival station[/size]", dp(60), self.sort_by_arrival_station),
                ("[size=30]Departure time[/size]", dp(50)),
                ("[size=30]Arrival time[/size]", dp(40)),
                ("[size=30]Travel time[/size]", dp(45), self.sort_by_travel_time)
            ],
            row_data=[
                (value["number"],
                 value["departure station"],
                 value["arrival station"],
                 value["departure time"],
                 value["arrival time"],
                 value["arrival time"] - value["departure time"])
                for value in schedule.values()
            ],
        )
        self.layout.add_widget(data_tables)
        return self.layout

    @staticmethod
    def sort_by_number(data):
        return zip(*sorted(enumerate(data), key=lambda l: l[1][0]))

    @staticmethod
    def sort_by_departure_station(data):
        return zip(*sorted(enumerate(data), key=lambda l: l[1][1]))

    @staticmethod
    def sort_by_arrival_station(data):
        return zip(*sorted(enumerate(data), key=lambda l: l[1][2]))

    @staticmethod
    def sort_by_travel_time(data):
        return zip(*sorted(enumerate(data), key=lambda l: l[1][-1]))


if __name__ == "__main__":
    TrainScheduleApp().run()
