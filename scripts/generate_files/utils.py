import pandas as pd
from sqlalchemy import create_engine
import glob
import os

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

def wipe_dir(dir_):
    """Delete all files of directory

    Args:
        dir_ (string): Directory to clean
    """

    n_files_deleted=0
    for f in glob.glob(dir_+"*"):
        os.remove(f)
        n_files_deleted+=1
    
    return n_files_deleted

def get_data(connection_alias, db_url):
    QUERY = "SELECT * FROM barometre.tous_indicateurs"

    db = DatabaseHelper(connection_alias, db_url)
    db.connect()
    res = db.query(QUERY)
    db.disconnect()

    return res

def get_metadata(connection_alias, db_url):
    QUERY = "SELECT * FROM barometre.baro_meta_indicateurs"

    db = DatabaseHelper(connection_alias, db_url)
    db.connect()
    res = db.query(QUERY)
    db.disconnect()

    return res

def get_metadata_ch(connection_alias, db_url):
    QUERY = "SELECT * FROM barometre.baro_meta_chantiers"

    db = DatabaseHelper(connection_alias, db_url)
    db.connect()
    res = db.query(QUERY)
    db.disconnect()

    return res

def get_metadata_engagement(connection_alias, db_url):
    QUERY = "SELECT * FROM barometre.baro_meta_engagement"

    db = DatabaseHelper(connection_alias, db_url)
    db.connect()
    res = db.query(QUERY)
    db.disconnect()

    return res

def export_by_indic(data_, out_dir):

    n_files_exported=0
    for i, group in data_.groupby(['indic_id']):
        indic_id = i[0]
        file_path = f'{out_dir}{indic_id.lower()}.csv'
        group.to_csv(file_path, index=False)
        n_files_exported+=1
        print('Exported:', indic_id, 'at', f'{out_dir}{indic_id.lower()}.csv', '- file', n_files_exported)
    
    return n_files_exported
