import csv
import time

from db import db_session
from model import Salary


def read_csv(filename):
    with open(filename, 'r', encoding='utf8') as f:

        fields = ['name', 'city', 'address',
                  'company', 'job', 'phone_number',
                  'email', 'date_of_birth', 'salary']

        reader = csv.DictReader(f, fields, delimiter=';')
        salary_data = []

        for row in reader:
            salary_data.append(row)

        save_salary_data(salary_data)


def save_salary_data(data):
    db_session.bulk_insert_mappings(Salary, data)
    db_session.commit()


if __name__ == '__main__':
    start = time.monotonic()
    read_csv('salary.csv')
    print(f'Загрузка заняла - {time.monotonic() - start:.5f}')