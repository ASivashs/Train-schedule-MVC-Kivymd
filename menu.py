from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable

from Controller.controller import MyScreenController
from Model.model import MyScreenModel

from kivy.core.window import Window
from kivy.metrics import dp


class TrainScheduleApp(MDApp):
    def __init__(self):
        super().__init__()
        self.__table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.6},
            size_hint=(1, 0.85),
            use_pagination=True,
            rows_num=10,
            column_data=[
                ("[size=30]Number[/size]", dp(30)),
                ("[size=30]Departure station[/size]", dp(60), self.sort_by_departure_station),
                ("[size=30]Arrival station[/size]", dp(60), self.sort_by_arrival_station),
                ("[size=30]Departure time[/size]", dp(50)),
                ("[size=30]Arrival time[/size]", dp(40)),
                ("[size=30]Travel time[/size]", dp(45), self.sort_by_travel_time)
            ],
        )
        self.__model = MyScreenModel(table=self.__table)
        self.__controller = MyScreenController(self.__model)

    # Table sort option
    @staticmethod
    def sort_by_departure_station(data):
        return zip(*sorted(enumerate(data), key=lambda l: l[1][1]))

    # Table sort option
    @staticmethod
    def sort_by_arrival_station(data):
        return zip(*sorted(enumerate(data), key=lambda l: l[1][2]))

    # Table sort option
    @staticmethod
    def sort_by_travel_time(data):
        return zip(*sorted(enumerate(data), key=lambda l: l[1][-1]))

    def build(self):
        Window.size = (1470, 800)
        Window.title = "Train schedule"
        return self.__controller.get_screen()


if __name__ == "__main__":
    TrainScheduleApp().run()
