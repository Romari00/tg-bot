from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    id:Mapped [int] = mapped_column(primary_key=True)
    name:Mapped [str]
    username:Mapped [str]

class Eco(Base):
    __tablename__ = 'eco'
    id:Mapped [int] = mapped_column(ForeignKey('users.id'), primary_key=True)
    balance:Mapped [int]
    
class UserTransactions(Base):
    __tablename__ = 'user_transactions'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    transaction_amount:Mapped [int]
    transaction_type:Mapped [str]
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

  
