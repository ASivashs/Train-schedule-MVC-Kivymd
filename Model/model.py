from train_schedule_parser import TrainSchedule
from kivymd.uix.snackbar import Snackbar


class MyScreenModel:
    def __init__(self, table):
        self.__train_schedule = TrainSchedule()
        self.__table = table
        self._not_filtered = []
        self._observers = []

    @property
    def schedule(self) -> dict:
        return self.__train_schedule.train_schedule

    @property
    def table(self):
        return self.__table

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, data):
        for x in self._observers:
            x.model_is_changed(data)

    def input_new_elements(self, elements: list | tuple):
        """Add input element to dict and re-draw the table."""
        self.__train_schedule.add_element(
            elements[0], elements[1], elements[2],
            elements[3], elements[4]
        )
        self.__clear_table()
        self.load_elements_to_table(self.__train_schedule.train_schedule)

    def load_elements_to_table(self, elements: dict):
        """Add elements to datatable."""
        if not elements:
            return
        for element in elements.values():
            self.__add_to_table(
                (
                    element["number"], element["departure station"], element["arrival station"],
                    element["departure time"], element["arrival time"], element["travel time"]
                )
            )

    def refresh_table(self):
        self.__clear_table()
        self.load_elements_to_table(self.__train_schedule.train_schedule)

    def load_from_file(self, file_name: str):
        """Load saved trains schedule and add it in table."""
        res = self.__train_schedule.load_schedule_xml(file_name)
        if not res:
            Snackbar(text="This file is unavailable.").open()
            return
        self.load_elements_to_table(self.__train_schedule.train_schedule)

    def save_file(self, file_name: str):
        """Save train schedule in xml."""
        self.__train_schedule.save_schedule_xml(file_name)

    def __add_to_table(self, data: tuple | list):
        """Add one element to table."""
        try:
            self.table.row_data.insert(
                len(self.table.row_data),
                (
                    data[0], data[1], data[2],
                    data[3], data[4], data[5]
                )
            )
        except Exception as err:
            print(err)
            Snackbar(text=f"{err}").open()

    def __clear_table(self):
        """Delete all elements from table."""
        for row in self.table.row_data[:]:
            self.__table.row_data.remove(row)

    def find_elements_in_table(self, find_elements: tuple | list, find_mode: str):
        """Find elements and load it to table."""
        self.__clear_table()
        print("find_elements_in_table(model):", find_elements)
        self.load_elements_to_table(self.__train_schedule.find_elements(find_elements, find_mode))

    def delete_from_table(self, delete_elements: tuple | list, delete_mode: str):
        """Delete elements from data table and dict by key."""
        del_elements = self.__train_schedule.delete_elements(delete_elements, delete_mode)
        if del_elements:
            Snackbar(text=f"Deleted {len(list(del_elements.keys()))} from table.").open()
        else:
            Snackbar(text="Deleted 0 elements from table.").open()
        self.refresh_table()
