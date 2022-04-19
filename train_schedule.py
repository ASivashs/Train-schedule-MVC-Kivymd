# import xml.dom.minidom as md
import xml.sax
import json
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


handler = TrainHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse("trains.xml")
print(handler.trains)
