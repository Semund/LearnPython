import json
from pprint import pprint

FILE_PATH = "metro.json"


def get_metro_repair_stations(data_json):
    with open(data_json, 'r', encoding='cp1251') as json_file:
        metro_statistic = json.load(json_file)
    output_stations = set()
    index = 1
    for station in metro_statistic:
        if station['RepairOfEscalators'] and station['NameOfStation'] not in output_stations:
            print(f"{index}. Станция {station['NameOfStation']}: "
                  f"Даты выполнения работ - {station['RepairOfEscalators'][0]['RepairOfEscalators']}")
            index += 1
            output_stations.add(station['NameOfStation'])


if __name__ == '__main__':
    get_metro_repair_stations(FILE_PATH)