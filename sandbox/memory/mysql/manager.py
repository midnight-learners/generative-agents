import os
from mysql.connector import (
    connect, 
    MySQLConnection
)
import pandas as pd

from .column_spec import MySQLColumnSpec
from ...utils import (
    KEY_OF_MYSQL_USER,
    KEY_OF_MYSQL_PASSWORD
)

LOCAL_HOST = 'localhost'
PRIMARY_KEY = 'PRIMARY KEY'
AUTO_INCREMENT = 'auto_increment'

class MySQLManager:
    
    def __init__(
            self,
            db_name: str,
            host: str = LOCAL_HOST,
            user: str = os.getenv(KEY_OF_MYSQL_USER),
            password: str = os.getenv(KEY_OF_MYSQL_PASSWORD)
        ) -> None:
        """A simple MySQL database manager.

        Parameters
        ----------
            db_name (str): Name of the MySQL database. 
            user (str) = User name. Defaults to USER,
            password (str) = Password. Defaults to PASSWORD,
            host (str, optional): Host. Defaults to LOCAL_HOST.
        """
       
        self._db_name = db_name
  
        # database connection
        self._connection: MySQLConnection = connect(
            host=host,
            user=user,
            password=password,
            database=self._db_name
        )
        
        # cursor, used to execute queries
        self._cursor = self._connection.cursor()
    
    def __enter__(self) -> MySQLConnection:
        
        # connect to database
        return self
        
    def __exit__(self, exception_type, exception_value, exception_traceback):
        
        # close the database connection
        self.close()
        
    def create_table(
            self, 
            table: str, 
            column_specs: list[MySQLColumnSpec]
        ) -> None:
        """Create a table from column specifications.
        If the table already exists, 
        then this database operation will be ignored.

        Parameters
        ----------
            table (str): Table name.
            column_specs (list[MySQLColumnSpec]): A list of column specifications.
        """
        
        # prepare SQL
        sql = f'''CREATE TABLE IF NOT EXISTS {table}
        '''
        
        # make SQL of column definitions
        
        column_definitions = []
        for spec in column_specs:
            column_definition = f'''\
            {spec.field} {spec.type} \
            {'' if spec.null else 'NOT NULL'} \
            {AUTO_INCREMENT if spec.extra == AUTO_INCREMENT else ''} \
            {PRIMARY_KEY if spec.is_primary_key() else ''} \
            '''
            column_definitions.append(column_definition)
            
        sql_of_column_definitions = ','.join(column_definitions)
        
        # finalize the SQL
        sql = f'{sql} ({sql_of_column_definitions})'
        
        # execute SQL
        self._cursor.execute(sql)
        self._connection.commit()
    
    def close(self) -> None:
        """Close the database connection.
        """
        
        self._connection.close()
        
    def show_tables(self) -> list[str]:
        """Show all existing tables in the database.
        
        Returns
        -------
            list[str]: A list of table names.
        """
        
        # prepare SQL
        sql = '''SHOW TABLES
        '''
        
        # execute SQL
        self._cursor.execute(sql)
        
        # unpack result to get all table names
        result = self._cursor.fetchall()
        tables = []
        for row in result:
            table = row[0]
            tables.append(table)
        
        return tables
    
    def get_column_specs(self, table: str) -> list[MySQLColumnSpec]:
        """Get all column specifications of the given table.
        
        Parameters
        ----------
            table (str): Table name.
            
        Returns
        -------
            list[MySQLColumnSpec]: A list of column specifications.
        """
        
        # prepare SQL
        sql = f'''SHOW COLUMNS FROM {table};
        '''
        
        # execute SQL
        self._cursor.execute(sql)
        
        # unpack result to get all table column specifications
        result = self._cursor.fetchall()
        column_specs = []
        for row in result:
            column_spec = MySQLColumnSpec(*row)
            column_specs.append(column_spec)
        
        return column_specs
    
    def get_table_fields(self, table: str) -> list[str]:
        """Get all fields in the given table.
        
        Parameters
        ----------
            table (str): Table name.
            
        Returns
        -------
            list[str]: A list of fields.
        """
        
        # get all column specifications
        column_specs = self.get_column_specs(table)
  
        # only need the fields
        fields = list(map(
            lambda spec: spec.field,
            column_specs
        ))
        
        return fields
    
    def convert_table_to_dataframe(self, table: str) -> pd.DataFrame:
        """Convert the table in the database to Panda's DataFrame.

        Parameters
        ----------
            table (str): Table name.
            
        Returns
        -------
            pd.DataFrame: Table as the data frame.
        """
      
        # prepare SQL
        sql = f'''SELECT * FROM {table};
        '''
        
        # execute SQL
        self._cursor.execute(sql)
        
        # unpack result to get all records
        result = self._cursor.fetchall()
        records = []
        for row in result:
            record = row
            records.append(record)
            
        # get table fields
        fields = self.get_table_fields(table)
        
        # construct the data frame
        df = pd.DataFrame(records, columns=fields)
        
        return df
        
def open_database(
        db_name: str,
        user: str = os.getenv(KEY_OF_MYSQL_USER),
        password: str = os.getenv(KEY_OF_MYSQL_PASSWORD),
        host: str = LOCAL_HOST
    ) -> MySQLManager:
    """Open a MySQL database. A `MySQLManager` object will be returned.

        Parameters
        ----------
            db_name (str): Name of the MySQL database. 
            user (str): User name. Defaults to USER.
            password (str): Password. Defaults to PASSWORD.
            host (str, optional): Host. Defaults to LOCAL_HOST.
            
        Returns
        -------
            MySQLManager: A simple MySQL manager that is responsible for
            handling SQL quires.
        """
    
    return MySQLManager(
        db_name=db_name,
        user=user,
        password=password,
        host=host
    )
 