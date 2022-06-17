from db import db_session
from models import User

user = User(name='Semund', salary=120000, email='semund@vk.com')
db_session.add(user)
db_session.commit()
