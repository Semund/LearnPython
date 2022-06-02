import csv
import re

FILE_STOP_PATH = "./ground_transport_stops.csv"
FILE_METRO_PATH = "./2_metro.json"


def get_max_transport_stop_around_metro(data_file):
    transport_stop_statistic = {}
    with open(data_file, 'r', encoding='cp1251') as csv_file:
        transport_stop_data = csv.DictReader(csv_file, delimiter=';')

        for row in transport_stop_data:
            if 'Метро ' in row["StationName"]:
                metro_name = re.sub(r'\(.+\)', '', row["StationName"]).strip()
                metro_stop_frequency = transport_stop_statistic.get(metro_name, 0)
                transport_stop_statistic[metro_name] = metro_stop_frequency + 1

    max_transport_stop_frequency = max(transport_stop_statistic.values())
    max_transport_stop_dict = [(key, value) for key, value in transport_stop_statistic.items() if
                               value == max_transport_stop_frequency]

    return max_transport_stop_dict


if __name__ == '__main__':
    metro_stop_stat = get_max_transport_stop_around_metro(FILE_STOP_PATH)
    print(f'Больше всего остановок у станции {metro_stop_stat[0][0]} - {metro_stop_stat[0][1]}')
