from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine('postgresql://semund:4228@localhost:5432/semund')

db_session = scoped_session(sessionmaker(bind=engine))
""":type: sqlalchemy.orm.scoped_session"""

Base = declarative_base()

Base.query = db_session.query_property()