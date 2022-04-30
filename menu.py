from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from Controller.controller import MyScreenController
from Model.model import MyScreenModel
from kivy.core.window import Window
from kivy.metrics import dp


class PassMVC(MDApp):
    def __init__(self):
        super().__init__()
        self.table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.6},
            size_hint=(1, 0.85),
            use_pagination=True,
            elevation=2,
            rows_num=4,
            pagination_menu_height=120,
            background_color=(0, 1, 0, .10),
            column_data=[
                ("[size=30]Number[/size]", dp(30)),
                ("[size=30]Departure station[/size]", dp(60), self.sort_by_departure_station),
                ("[size=30]Arrival station[/size]", dp(60), self.sort_by_arrival_station),
                ("[size=30]Departure time[/size]", dp(50)),
                ("[size=30]Arrival time[/size]", dp(40)),
                ("[size=30]Travel time[/size]", dp(45), self.sort_by_travel_time)
            ],
        )
        self.model = MyScreenModel(table=self.table)
        self.controller = MyScreenController(self.model)

    @staticmethod
    def sort_by_departure_station(data):
        return zip(*sorted(enumerate(data), key=lambda l: l[1][1]))

    @staticmethod
    def sort_by_arrival_station(data):
        return zip(*sorted(enumerate(data), key=lambda l: l[1][2]))

    @staticmethod
    def sort_by_travel_time(data):
        return zip(*sorted(enumerate(data), key=lambda l: l[1][-1]))

    def build(self):
        Window.size = (1470, 800)
        Window.title = "Train schedule"
        return self.controller.get_screen()


PassMVC().run()


# from Model.train_schedule_parser import schedule
#
# from kivymd.app import MDApp
# from kivy.core.window import Window
#
# from kivymd.uix.boxlayout import MDBoxLayout
# from kivymd.uix.bottomnavigation import MDBottomNavigation
# from kivy.metrics import dp
# from kivymd.uix.datatables import MDDataTable
#
#
# Window.size = (1470, 800)
# Window.title = "Train schedule"
#
#
# class TrainScheduleApp(MDApp):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.layout = MDBoxLayout(orientation="vertical")
#
#     def build(self):
#         data_tables = MDDataTable(
#             size_hint=(1, .9),
#             use_pagination=True,
#             rows_num=10,
#             column_data=[
#                 ("[size=30]Number[/size]", dp(30), self.sort_by_number),
#                 ("[size=30]Departure station[/size]", dp(60), self.sort_by_departure_station),
#                 ("[size=30]Arrival station[/size]", dp(60), self.sort_by_arrival_station),
#                 ("[size=30]Departure time[/size]", dp(50)),
#                 ("[size=30]Arrival time[/size]", dp(40)),
#                 ("[size=30]Travel time[/size]", dp(45), self.sort_by_travel_time)
#             ],
#             row_data=[
#                 (value["number"],
#                  value["departure station"],
#                  value["arrival station"],
#                  value["departure time"],
#                  value["arrival time"],
#                  value["arrival time"] - value["departure time"])
#                 for value in schedule.values()
#             ],
#         )
#         navigation_bar = MDBottomNavigation(
#             size_hint=(1, .1)
#         )
#         self.layout.add_widget(navigation_bar)
#         self.layout.add_widget(data_tables)
#         # self.layout.add_widget(navigation_bar)
#         return self.layout
#
#     @staticmethod
#     def sort_by_number(data):
#         return zip(*sorted(enumerate(data), key=lambda l: l[1][0]))
#
#     @staticmethod
#     def sort_by_departure_station(data):
#         return zip(*sorted(enumerate(data), key=lambda l: l[1][1]))
#
#     @staticmethod
#     def sort_by_arrival_station(data):
#         return zip(*sorted(enumerate(data), key=lambda l: l[1][2]))
#
#     @staticmethod
#     def sort_by_travel_time(data):
#         return zip(*sorted(enumerate(data), key=lambda l: l[1][-1]))
#
#
# if __name__ == "__main__":
#     TrainScheduleApp().run()
