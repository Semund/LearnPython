import csv
from collections import Counter

FILE_PATH = "./ground_transport_stops.csv"


def get_most_common_transport_stop(data_file):
    transport_stop_statistic = {}
    with open(data_file, 'r', encoding='cp1251') as csv_file:
        transport_stop_data = csv.DictReader(csv_file, delimiter=';')
        for row in transport_stop_data:
            if row["Street"] and row["Street"] != 'проезд без названия':
                street_frequency = transport_stop_statistic.get(row["Street"], 0)
                transport_stop_statistic[row["Street"]] = street_frequency + 1

    max_transport_stop_frequency = max(transport_stop_statistic.values())
    max_transport_stop_dict = {key: value for key, value in transport_stop_statistic.items() if
                               value == max_transport_stop_frequency}

    return max_transport_stop_dict


def get_most_common_transport_stop_withCounter(data_file):
    with open(data_file, 'r', encoding='cp1251') as csv_file:
        transport_stop_data = csv.DictReader(csv_file, delimiter=';')
        return Counter(row['Street'] for row in transport_stop_data).most_common(2)


if __name__ == '__main__':
    most_frequency_street = tuple(get_most_common_transport_stop(FILE_PATH).items())[0]
    most_frequency_street_counter = get_most_common_transport_stop_withCounter(FILE_PATH)[1]

    assert most_frequency_street == most_frequency_street_counter

    print(f'Больше всего остановок на улице {most_frequency_street[0]} - {most_frequency_street[1]}')
