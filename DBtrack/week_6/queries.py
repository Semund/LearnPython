import time

from db import db_session
from models import Company, Employee, Payment


def employees_by_company(company_name):
    company = Company.query.filter(Company.name == company_name).first()
    employees_list = []
    if company:
        for employee in Employee.query.filter(Employee.company_id == company.id):
            employees_list.append(f"{company_name} - {employee.name}")
    return employees_list


def employees_by_company_joined(company_name):
    query = db_session.query(Employee, Company).join(
        Company, Employee.company_id == Company.id
    ).filter(Company.name == company_name)
    employees_list = []

    for employee, company in query:
        employees_list.append(f"{company.name} - {employee.name}")
    return employees_list


def employees_by_company_relation(company_name):
    company = Company.query.filter(Company.name == company_name).first()
    employees_list = []
    if company:
        for employee in company.employees:
            employees_list.append(f"{company_name} - {employee.name}")
    return employees_list


if __name__ == '__main__':
    # start1 = time.monotonic()
    # for _ in range(1000):
    #     employees_by_company('Лента')
    # print(f'employees_by_company: {time.monotonic() - start1:.6f}')

    # start2 = time.monotonic()
    # for _ in range(1000):
    #     employees_by_company_joined('Лента')
    # print(f'employees_by_company_joined: {time.monotonic() - start2:.6f}')
    #
    start3 = time.monotonic()
    for _ in range(1000):
        employees_by_company_relation('Лента')
    print(f'employees_by_company_relation: {time.monotonic() - start3:.6f}')
