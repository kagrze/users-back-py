from model import Base
from model import User
from model import Group
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class PersistenceService(object):
    def __init__(self):
        engine = create_engine('sqlite:///:memory:', echo=True)
        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        self._session = Session()

        self._insert_test_data()

    def _insert_test_data(self):
        test_user = User(name='John Smith', email='john@smith.mx')
        self._session.add(test_user)
        test_group = Group(name='All users group')
        self._session.add(test_group)
        test_user.groups.append(test_group)
        self._session.commit()

    def load_users(self):
        return self._session.query(User)

    def load_user(self, user_id):
        return self._session.query(User).filter_by(id=user_id).one()

    def save_user(self, user):
        self._session.add(user)
        self._session.commit()
        return user

    def del_user(self, user_id):
        user = self._session.query(User).filter_by(id=user_id).one()
        self._session.delete(user)
        self._session.commit()

    def load_groups(self):
        return self._session.query(Group)

    def load_group(self, group_id):
        return self._session.query(Group).filter_by(id=group_id).one()

    def save_group(self, group):
        self._session.add(group)
        self._session.commit()
        return group

    def del_group(self, group_id):
        group = self._session.query(Group).filter_by(id=group_id).one()
        self._session.delete(group)
        self._session.commit()

    def save_users_group(self, user_id, group_id):
        user = self._session.query(User).filter_by(id=user_id).one()
        group = self._session.query(Group).filter_by(id=group_id).one()
        user.groups.append(group)
        self._session.commit()

    def del_users_group(self, user_id, group_id):
        user = self._session.query(User).filter_by(id=user_id).one()
        group = self._session.query(Group).filter_by(id=group_id).one()
        user.groups.remove(group)
        self._session.commit()
