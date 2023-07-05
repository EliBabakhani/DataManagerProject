import unittest

from data_manager.db_manager import DBManager


class TestModel(BaseModel):
    TABLE_NAME='testtable'
    COLUMNS={"data":("data", "VARCHAR(50)")}

    def __init__(self, data="Test") -> None:
        super().__init__()
        self.data = data

    def __str__(self) -> str:
        return f'TestModel #{self._id}: {self.data}'

    pass

class TestDb(unittest.TestCase):
    config={'db_config':{'dbname':'test', 'host':'localhost', 'password':'123Elnaz321', 'user':'postgres'}}
    db=DBManager(config)  
    def test_create(self): 
        a=TestModel('test')
        i_id=DBManager.create(a)
        qu=f"SELECT * FROM  "




