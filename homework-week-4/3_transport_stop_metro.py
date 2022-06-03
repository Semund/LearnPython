import csv
import json
import re

from collections import defaultdict
from pprint import pprint
from math import acos, sin, cos

FILE_STOP_PATH = "./ground_transport_stops.csv"
FILE_METRO_PATH = "./metro.json"


def get_transport_stop_geodata(data_file):
    transport_stop_geodata = defaultdict(list)
    with open(data_file, 'r', encoding='cp1251') as csv_file:
        transport_stop_data = csv.DictReader(csv_file, delimiter=';')

        for row in transport_stop_data:
            if 'Метро ' in row["StationName"]:
                metro_stop_name = re.sub(r'\(.+\)', '', row["StationName"]).split(' - ')[0].removeprefix('Метро ')
                transport_stop_geodata[metro_stop_name.strip().lower()].append((row["Longitude_WGS84"],
                                                                                row["Latitude_WGS84"]))

    return transport_stop_geodata


def get_metro_station_geodata(data_file):
    metro_stations_geodata = defaultdict(list)
    with open(data_file, 'r', encoding='cp1251') as json_file:
        metro_stations_data = json.load(json_file)
        for station in metro_stations_data:
            metro_name = station['NameOfStation'].lower()
            metro_stations_geodata[metro_name].append((station['Longitude_WGS84'], station['Latitude_WGS84']))
    return metro_stations_geodata


def is_calc_distance_less_set_value(coordinate1: tuple, coordinate2: tuple, set_value=0.5) -> bool:
    long = 6371
    lmbd1, phi1 = map(float, coordinate1)
    lmbd2, phi2 = map(float, coordinate2)
    angle_long = acos(sin(phi1) * sin(phi2) + cos(phi1) * cos(phi2) * cos(lmbd2 - lmbd1))
    return long * angle_long <= set_value



if __name__ == '__main__':
    transport_stop_geodata = get_transport_stop_geodata(FILE_STOP_PATH)
    metro_stations_geodata = get_metro_station_geodata(FILE_METRO_PATH)
    for station in transport_stop_geodata:
        for transport_coordinate in transport_stop_geodata[station]:
            for metro_coordinate in metro_stations_geodata[station]:
                if is_calc_distance_less_set_value(metro_coordinate, transport_coordinate):
                    print(station)
