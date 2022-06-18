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
    employees = relationship('Employee', lazy='joined')

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
    companies = relationship('Company')
    def __repr__(self):
        return f"Employee {self.id=}, {self.name=}"


class Payment(Base):
    query: Query
    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey(Employee.id), index=True, nullable=False)
    payment_date = Column(Date)
    amount = Column(Integer)

    def __repr__(self):
        return f"Payment {self.id=}, {self.payment_date=}"


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)