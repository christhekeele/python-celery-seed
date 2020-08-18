from sqlalchemy.ext.declarative import declarative_base


class Base(object):
    def to_dict(self):
        return {column.name: getattr(self, column.name, None) for column in self.__table__.columns}


Base = declarative_base(cls=Base)
