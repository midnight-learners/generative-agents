import unittest
from sandbox.memory.mysql import (
    open_database,
    MySQLManager
)

class MySQLManagerTester(unittest.TestCase):
    
    def test_show_tables(self):
        
        db: MySQLManager
        with open_database('test_db') as db:
            tables = db.show_tables()
            print(tables)

if __name__  == '__main__':
    unittest.main()