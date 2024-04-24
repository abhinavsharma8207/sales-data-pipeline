from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.models import Base


class DatabaseManager:
    def __init__(self, connection_string):
        self.engine = create_engine(connection_string)
        self.Session = sessionmaker(bind=self.engine)

    def load_to_database(self, data, table_name):
        data.to_sql(table_name, con=self.engine, if_exists='replace', index=False)

    def create_database(self):
        # This will create the tables defined by your SQLAlchemy models
        Base.metadata.create_all(self.engine)
        print("Database tables created.")