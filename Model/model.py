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
        for element in elements.values():
            self.__add_to_table(
                (
                    element["number"], element["departure station"], element["arrival station"],
                    element["departure time"], element["arrival time"], element["travel time"]
                )
            )

    def load_from_file(self, file_name: str):
        """Load saved trains schedule and add it in table."""
        try:
            self.__train_schedule.load_schedule_xml(file_name)
        except Exception as err:
            print(err)
            Snackbar(text="This file doesn't exist.").open()
            return
        self.load_elements_to_table(self.__train_schedule.train_schedule)

    def save_file(self, file_name: str):
        """Save train schedule in xml."""
        try:
            self.__train_schedule.save_schedule_xml(file_name)
        except Exception as err:
            print(err)
            Snackbar(text="This file doesnt exist.").open()
            return

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

    def delete_from_table(self, delete_elements: dict):
        """Delete elements from data table and dict by key."""
        if not delete_elements:
            return
        self.__train_schedule.delete_elements(delete_elements)
        self.__clear_table()
        self.load_elements_to_table(self.__train_schedule.train_schedule)

    def __clear_table(self):
        """Delete all elements from table."""
        if not self.table.row_data:
            print("Table has already been cleared.")
            Snackbar(text="Table has already been cleared.").open()
            return
        self.__table = []

    def find_elements_in_table(self, find_elements: tuple | list):
        """Find elements and load it to table."""
        self.__clear_table()
        self.load_elements_to_table(self.__train_schedule.find_elements(find_elements))

    # def refresh_stock_in_table(self):
    #     try:
    #         self.table.row_data += self._not_filtered
    #         self._not_filtered = []
    #     except Exception as e:
    #         pass
    #
    # def select_stock_by_filters(self, filters: list):
    #     not_filtered_stock = []
    #     for row in self.table.row_data:
    #         # first case
    #         if filters[0] or filters[3]:  # product
    #             if not (row[0] == filters[0] or row[3] == filters[3]):
    #                 not_filtered_stock.append(tuple(row))
    #                 print(len(not_filtered_stock))
    #                 continue
    #         # second case
    #         elif filters[1] or filters[2]:  # product
    #             if not (row[1] == filters[1] or row[2] == filters[2]):
    #                 not_filtered_stock.append(tuple(row))
    #                 print(len(not_filtered_stock))
    #                 continue
    #         # third case
    #         elif filters[4]:
    #             if re.match(r'\d{1,5}\s\w.\s(\b\w*\b\s){1,2}\w*\.', filters[3]):
    #                 start, end = filters[4].split('-')
    #                 if int(row[4]) not in range(int(start), int(end) + 1):
    #                     not_filtered_stock.append(tuple(row))
    #                     continue
    #     return not_filtered_stock
    #
    # def filter_stock_in_table(self, filters: list):
    #     self._not_filtered = self.select_stock_by_filters(filters=filters)
    #     for row in self._not_filtered:
    #         self.table.row_data.remove(row)
    #
    # @staticmethod
    # def empty_filters(filters):
    #     for filter in filters:
    #         if filter != '':
    #             return False
    #     return True
