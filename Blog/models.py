from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

    creator = relationship("User", back_populates="blogs")

class User(Base):
    __tablename__ = 'users'

    name = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    password = Column(String)

    blog = relationship("Blog", back_populates="creator")