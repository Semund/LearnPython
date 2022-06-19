from sqlalchemy import func

from db import db_session
from models import Project, Company, ProjectEmployee, Employee


def company_projects_employees(company_name):
    query = Project.query.join(Project.company, Project.employees).filter(Company.name == company_name)
    for project in query:
        print('-' * 20)
        print(project.name)
        for project_employee in project.employees:
            delta = (project_employee.date_end - project_employee.date_start).days
            print(f'{project_employee.employee.name} -- {delta}')


def project_time_total(company_name):
    query = db_session.query(
        Project.name,
        func.sum(ProjectEmployee.date_end - ProjectEmployee.date_start)
    ).join(
        Project.company, Project.employees
    ).filter(Company.name == company_name).group_by(Project.name)

    for project_name, sum_days in query:
        print(f'{project_name} -- {sum_days}')


def project_employee_time_total(company_name):
    query = db_session.query(
        Project.name,
        Employee.name,
        func.sum(ProjectEmployee.date_end - ProjectEmployee.date_start)
    ).join(
        Project.company, Project.employees, ProjectEmployee.employee
    ).filter(Company.name == company_name).group_by(Project.name, Employee.name)

    for project_name, employee_name, sum_days in query:
        print(f'{project_name} -- {employee_name} -- {sum_days}')


if __name__ == '__main__':
    # company_projects_employees('Лента')
    # project_time_total('Лента')
    project_employee_time_total('Лента')
