from sqlalchemy import create_engine, text, select
from sqlalchemy.orm import  sessionmaker


engine = create_engine('sqlite:///pizduki.db')

Session = sessionmaker(bind=engine)

# with Session.begin() as session:
#     session.execute(text('''DELETE FROM users WHERE id = 800252612'''))
#     session.commit()

#
# with Session.begin() as session:
#     result = session.execute(text("SELECT * FROM users"))
#     for row in result:
#         print(row)

