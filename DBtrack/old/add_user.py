from db import db_session
from models import User

user = User(name='MArina', salary=100000, email='marina@mail.com')
db_session.add(user)
db_session.commit()
