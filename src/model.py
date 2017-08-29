from sqlalchemy import Table, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def get_fields(self):
    d = dict(self.__dict__)
    del d['_sa_instance_state']
    return d

Base.get_fields = get_fields


user_groups = Table('user_groups', Base.metadata,
    Column('user_id', ForeignKey('users.id'), primary_key=True),
    Column('group_id', ForeignKey('groups.id'), primary_key=True)
)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

    groups = relationship('Group',
                          secondary=user_groups,
                          back_populates='users')


class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    users = relationship('User',
                         secondary=user_groups,
                         back_populates='groups')
