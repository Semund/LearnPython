from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import Query
from sqlalchemy.orm import relationship

from db import Base, engine


class Company(Base):
    # query: Query
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    city = Column(String)
    address = Column(String)
    phone = Column(String)
    employees = relationship('Employee', lazy='joined', back_populates='companies')

    def __repr__(self):
        return f"Company {self.id=}, {self.name=}"


class Employee(Base):
    # query: Query
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, ForeignKey(Company.id), index=True, nullable=False)
    name = Column(String)
    job = Column(String)
    phone_number = Column(String)
    email = Column(String)
    date_of_birth = Column(Date)
    companies = relationship('Company', lazy='joined', back_populates='employees')
    payments = relationship('Payment', back_populates='employees')

    def __repr__(self):
        return f"Employee {self.id=}, {self.name=}"


class Payment(Base):
    # query: Query
    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey(Employee.id), index=True, nullable=False)
    payment_date = Column(Date)
    amount = Column(Integer)
    employees = relationship('Employee', lazy='joined', back_populates='payments')

    def __repr__(self):
        return f"Payment {self.id=}, {self.payment_date=}"


class Project(Base):
    # query: Query
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, ForeignKey(Company.id), index=True, nullable=False)
    name = Column(String)
    company = relationship('Company', lazy='joined')
    employees = relationship('ProjectEmployee', back_populates='project')

    def __repr__(self):
        return f"Project {self.id=}, {self.name=}"


class ProjectEmployee(Base):
    # query: Query
    __tablename__ = 'projects_employees'

    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey(Employee.id), index=True, nullable=False)
    project_id = Column(Integer, ForeignKey(Project.id), index=True, nullable=False)
    date_start = Column(Date)
    date_end = Column(Date)
    employee = relationship('Employee', lazy='joined')
    project = relationship('Project', lazy='joined', back_populates='employees')

    def __repr__(self):
        return f"ProjectEmployee project {self.project_id=}, employee {self.employee_id=}"


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
