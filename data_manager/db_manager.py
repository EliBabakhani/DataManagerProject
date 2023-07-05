from .base import BaseManager, BaseModel
import psycopg2 as pg

class DBManager(BaseManager):
    
    def __init__(self, config: dict) -> None:
        super().__init__(config)  # {'db_config':{'dbname':'', 'host':'', 'password':'', 'user':'', ...}}
        self._db_config = config['db_config']
        self.__conn = pg.connect(**self._db_config)

    @staticmethod
    def converter_model_to_query(value):
        if isinstance(value, str):
            return f"'{value}'"
        elif value is None:
            return 'NULL'
        else:
            return str(value)

    
    def create_table(self, model_cls: type):
        assert issubclass(model_cls, BaseModel)

        with self.__conn.cursor() as curs:
            cols_dict = model_cls._get_columns()
            sql_cols = ','.join([" ".join(v) for v in cols_dict.values()])
            curs.execute(f"CREATE TABLE {model_cls.TABLE_NAME} ({sql_cols});", )
        
        self.__conn.commit()
    
    def _check_table_exists(self,  model_cls: type):
        with self.__conn.cursor() as curs:
            curs.execute("SELECT * FROM information_schema.tables WHERE table_name=%s",
                        (model_cls.TABLE_NAME,))
            return bool(curs.fetchone())


    def create(self, m: BaseModel):
        if not self._check_table_exists(m.__class__):
            self.create_table(m.__class__)
        
        model_data = m.to_dict()  # {'_id':1, 'username':'akbar', ...}
        converter = self.converter_model_to_query

        with self.__conn.cursor() as curs:
            keys = ','.join(model_data.keys())
            values = ','.join(map(converter, model_data.values())) # 1, 'akbar', 'akbar1',... -> 1, 'akbar', 'akbar1' -> "1, 'akbar', 'akbar1'"
            curs.execute(f"INSERT INTO {m.TABLE_NAME} ({keys}) VALUES ({values}) RETURNING _id")
            new_model_id = curs.fetchone()
            m._id = new_model_id
        
        self.__conn.commit()
        return new_model_id

       
        

    def read(self, id: int, model_cls: type) -> BaseModel:
        # TODO: Complete
        pass


    def update(self, m: BaseModel) -> None:
        # TODO: Complete
        pass


    def delete(self, id: int, model_cls: type) -> None:
        # TODO: Complete
        pass



    def read_all(self, model_cls: type):
        # TODO: Complete
        pass


    def truncate(self, model_cls: type) -> None:
        #TODO: Complete
        pass

    
    
