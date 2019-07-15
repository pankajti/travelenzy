from database.connection.mysql_connection import get_session

class GenericDao():
    def insert_record(self,record):
        session = get_session()
        session.add(record)
        session.commit()
        session.flush()
        print('inserted record :: {}'.format(record))

    def get_all_records(self, Type):
        return get_session().query(Type).all()

