from random import randint
import xml.sax
import xml.dom.minidom
import datetime as dt


class TrainSchedule:

    def __init__(self) -> None:
        self._train_schedule: dict = {}
        self._ids: set = set()

    @property
    def train_schedule(self) -> dict:
        return self._train_schedule

    def add_element(self, train_number: str, departure_station: str, arrival_station: str,
                    departure_time: dt.datetime, arrival_time: dt.datetime):
        """Add input element to dict."""
        new_id: str = str(randint(0, 1000))
        while new_id in self._ids:
            new_id = str(randint(0, 1000))
        self._ids.add(new_id)
        self._train_schedule[new_id] = {
            "number": train_number,
            "departure station": departure_station,
            "arrival station": arrival_station,
            "departure time": departure_time,
            "arrival time": arrival_time
        }

    def load_schedule_xml(self, file_name="trains.xml") -> dict:
        """Load xml save and return loaded data in dict type."""

        class TrainHandler(xml.sax.handler.ContentHandler):

            def __init__(self):
                super().__init__()
                self.__current = None
                self.__trains: dict = {}
                self.__current_id = 0
                self.__number = ""
                self.__departure_station = ""
                self.__arrival_station = ""
                self.__departure_time = ""
                self.__arrival_time = ""

            @property
            def trains(self):
                return self.__trains

            def startElement(self, name, attrs):
                self.__current = name
                if name == "train":
                    self.__current_id = attrs["id"]
                    self.__trains[self.__current_id] = {
                        "number": "",
                        "departure station": "",
                        "arrival station": "",
                        "departure time": "",
                        "arrival time": "",
                    }

            def characters(self, content):
                if self.__current == "number":
                    self.__number = content
                if self.__current == "departure_station":
                    self.__departure_station = content
                if self.__current == "arrival_station":
                    self.__arrival_station = content
                if self.__current == "departure_time":
                    self.__departure_time = content
                if self.__current == "arrival_time":
                    if content not in [" ", "\n", "    ", "\t"]:
                        self.__arrival_time = content

            def endElement(self, name):
                format_string = "%Y-%m-%d %H:%M:%S"
                if self.__current == "number":
                    self.__trains[self.__current_id]["number"] = self.__number
                if self.__current == "departure_station":
                    self.__trains[self.__current_id]["departure station"] = self.__departure_station
                if self.__current == "arrival_station":
                    self.__trains[self.__current_id]["arrival station"] = self.__arrival_station
                if self.__current == "departure_time":
                    self.__trains[self.__current_id]["departure time"] = dt.datetime.strptime(self.__departure_time,
                                                                                              format_string)
                if self.__current == "arrival_time":
                    self.__trains[self.__current_id]["arrival time"] = dt.datetime.strptime(self.__arrival_time,
                                                                                            format_string)

        schedule_parse = TrainHandler()
        xml.sax.parse(file_name, schedule_parse)
        self._train_schedule = schedule_parse.trains
        self._ids = set(id for id in schedule_parse.trains.keys())
        return schedule_parse.trains

    def save_schedule_xml(self, xml_file_name: str = "trains.xml"):
        """Save schedule in xml."""

        xml_save = xml.dom.minidom.Document()
        trains_group = xml_save.createElement("trains")

        for id, schedule in self._train_schedule.items():
            new_train = xml_save.createElement("train")
            new_train.setAttribute("id", id)

            number = xml_save.createElement("number")
            number.appendChild(xml_save.createTextNode(schedule["number"]))

            departure_station = xml_save.createElement("departure_station")
            departure_station.appendChild(xml_save.createTextNode(schedule["departure station"]))

            arrival_station = xml_save.createElement("arrival_station")
            arrival_station.appendChild(xml_save.createTextNode(schedule["arrival station"]))

            departure_time = xml_save.createElement("departure_time")
            departure_time.appendChild(xml_save.createTextNode(str(schedule["departure time"])))

            arrival_time = xml_save.createElement("arrival_time")
            arrival_time.appendChild(xml_save.createTextNode(str(schedule["arrival time"])))

            new_train.appendChild(number)
            new_train.appendChild(departure_station)
            new_train.appendChild(arrival_station)
            new_train.appendChild(departure_time)
            new_train.appendChild(arrival_time)

            trains_group.appendChild(new_train)

        xml_save.appendChild(trains_group)

        with open(xml_file_name, "w") as f:
            f.write(xml_save.toprettyxml())
