from kivymd.app import MDApp
from kivy.core.window import Window

from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.anchorlayout import AnchorLayout

from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable


Window.size = (1750, 800)


class TrainScheduleApp(MDApp):
    title = "Train schedule"
    def build(self):

        layout = AnchorLayout()
        data_tables = MDDataTable(
            size_hint=(1, .9),
            use_pagination=True,
            rows_num=10,
            column_data=[
                ("[size=40]Number[/size]", dp(40)),
                ("[size=40]Departure station[/size]", dp(75)),
                ("[size=40]Arrival station[/size]", dp(60)),
                ("[size=40]Departure time[/size]", dp(65)),
                ("[size=40]Arrival time[/size]", dp(50)),
                ("[size=40]Travel time[/size]", dp(50))
            ],
            row_data=[
                (_, _, _, _, _, _) for _ in range(1, 100 + 1)
            ],
        )
        layout.add_widget(data_tables)
        return layout


if __name__ == "__main__":
    TrainScheduleApp().run()
