import xml.dom.minidom
import xml.sax
import time


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
                "arrival time": ""
            }

    def characters(self, content):
        if self.__current == "number":
            self.__number = content
        if self.__current == "departure_station":
            self.__departure_station = content
        if self.__current == "arrival_station":
            self.__arrival_station = content
        if self.__current == "departure time":
            self.__departure_time = content
        if self.__current == "arrival time":
            self.__arrival_time = content

    def endElement(self, name):
        if self.__current == "number":
            self.__trains[self.__current_id]["number"] = self.__number
        if self.__current == "departure_station":
            self.__trains[self.__current_id]["departure station"] = self.__departure_station
        if self.__current == "arrival_station":
            self.__trains[self.__current_id]["arrival station"] = self.__arrival_station
        if self.__current == "departure time":
            self.__trains[self.__current_id]["departure time"] = self.__departure_time
        if self.__current == "arrival time":
            self.__trains[self.__current_id]["arrival time"] = self.__arrival_time


def save_xml(train_number: str, train_departure_station: str, train_arrival_station: str,
             train_departure_time: str, train_arrival_time: str, xml_file_name: str = "trains.xml"):

    xml_save = xml.dom.minidom.Document()
    trains_group = xml_save.createElement("trains")

    new_train = xml_save.createElement("train")
    new_train.setAttribute("id", "47")

    number = xml_save.createElement("number")
    number.appendChild(xml_save.createTextNode(train_number))

    departure_station = xml_save.createElement("departure_station")
    departure_station.appendChild(xml_save.createTextNode(train_departure_station))

    arrival_station = xml_save.createElement("arrival_station")
    arrival_station.appendChild(xml_save.createTextNode(train_arrival_station))

    departure_time = xml_save.createElement("departure_time")
    departure_time.appendChild(xml_save.createTextNode(train_departure_time))

    arrival_time = xml_save.createElement("arrival_time")
    arrival_time.appendChild(xml_save.createTextNode(train_arrival_time))

    new_train.appendChild(number)
    new_train.appendChild(departure_station)
    new_train.appendChild(arrival_station)
    new_train.appendChild(departure_time)
    new_train.appendChild(arrival_time)

    trains_group.appendChild(new_train)
    xml_save.appendChild(trains_group)

    with open(xml_file_name, "w") as f:
        f.write(xml_save.toprettyxml())


save_xml("666", "Jordan", "Oman", "14:14:01:03:2011", "01:01:09:11:2003")
