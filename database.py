import sqlite3
import pandas

class Database:

    types = {
        'int64': 'INTEGER',
        'int32': 'INTEGER',
        'float64': 'REAL',
        'float32': 'REAL',
        'bool': 'BOOLEAN',
        'datetime64[ns]': 'TEXT',
        'object': 'TEXT',
        'string': 'TEXT'
    }

    def __init__(self, name: str) -> None:

        self.connection = sqlite3.connect(f'{name}.sqlite')
        self.cursor = self.connection.cursor()


    def create(self, dataframe: pandas.DataFrame, table: str) -> None:

        columns = ', '.join(
            f'"{column}" {self.types[str(dtype)]}'
            for column, dtype in dataframe.dtypes.items()
        )

        self.cursor.execute(
            sql = f'CREATE TABLE IF NOT EXISTS "{table}" ({columns})'
        )
        self.connection.commit()


    def write(self, dataframe: pandas.DataFrame, table: str) -> None:

        columns = ', '.join(f'"{column}"' for column in dataframe.columns)
        placeholders = ', '.join(['?'] * dataframe.shape[1])

        self.cursor.executemany(
            sql = f'INSERT INTO "{table}" ({columns}) VALUES ({placeholders})',
            parameters = [tuple(row) for row in dataframe.values]
        )
        self.connection.commit()


    def read(self, table: str) -> pandas.DataFrame:

        sql = f'SELECT * FROM "{table}"'
        self.cursor.execute(sql)

        return pandas.DataFrame(
            data = self.cursor.fetchall(),
            columns = [desc[0] for desc in self.cursor.description]
        )


    def close(self):

        self.connection.close()
