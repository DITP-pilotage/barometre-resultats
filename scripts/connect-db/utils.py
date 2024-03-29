import pandas as pd
from sqlalchemy import create_engine

class DatabaseHelper:
    def __init__(self, connection_alias, pg_url) -> None:
        self.name=connection_alias
        self.alchemyEngine = create_engine(pg_url, pool_recycle=3600)
        pass
    
    def connect(self):
        print(f'Connecting to {self.name}...')
        self.dbConnection = self.alchemyEngine.connect()
        print('Connected')

    def disconnect(self):
        print(f'Disconnecting from {self.name}...')
        self.dbConnection.close()
        print('Disconnected')
        

    def query(self, q):
        return pd.read_sql(q, self.dbConnection)

def get_data(connection_alias, db_url):
    QUERY = "SELECT * FROM barometre.tous_indicateurs"

    db = DatabaseHelper(connection_alias, db_url)
    db.connect()
    res = db.query(QUERY)
    db.disconnect()

    return res
