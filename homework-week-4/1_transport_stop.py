import csv
import time
from collections import Counter

FILE_PATH = "./ground_transport_stops.csv"


def timer_execution(func):
    def wrapper(*args, **kwargs):
        start_time = time.monotonic()
        result_func = func(*args, **kwargs)
        end_time = time.monotonic()
        print(f"Результат {func.__name__}: {end_time - start_time:.5f}")
        return result_func
    return wrapper


@timer_execution
def get_most_common_transport_stop(data_file):
    transport_stop_statistic = {}
    with open(data_file, 'r', encoding='cp1251') as csv_file:
        transport_stop_data = csv.DictReader(csv_file, delimiter=';')
        for row in transport_stop_data:
            street_frequency = transport_stop_statistic.get(row["Street"], 0)
            transport_stop_statistic[row["Street"]] = street_frequency + 1

    max_transport_stop_frequency = max(transport_stop_statistic.values())
    max_transport_stop_dict = {key: value for key, value in transport_stop_statistic.items() if
                               value == max_transport_stop_frequency}

    return max_transport_stop_dict


@timer_execution
def get_most_common_transport_stop_withCounter(data_file):
    with open(data_file, 'r', encoding='cp1251') as csv_file:
        transport_stop_data = csv.DictReader(csv_file, delimiter=';')
        return Counter(row['Street'] for row in transport_stop_data).most_common(1)


if __name__ == '__main__':
    print(get_most_common_transport_stop(FILE_PATH))
    print(get_most_common_transport_stop_withCounter(FILE_PATH))


