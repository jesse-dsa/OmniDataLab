import psycopg2
import pandas as pd


class PostgreSQLConnector:
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
            )
            print("Conexão bem-sucedida com o PostgreSQL.")
        except psycopg2.Error as e:
            print(f"Erro ao conectar no PostgreSQL: {e}")
            raise

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Conexão fechada.")

    def get_tables(self):
        if not self.connection:
            raise Exception("Não conectado ao banco de dados.")

        query = """
        SELECT table_schema, table_name
        FROM information_schema.tables
        WHERE table_type = 'BASE TABLE'
        AND table_schema NOT IN ('pg_catalog', 'information_schema')
        ORDER BY table_schema, table_name;
        """
        df = pd.read_sql_query(query, self.connection)
        return df

    def get_all_tables_data(self):
        """Extrai todos os dados de todas as tabelas."""
        if not self.connection:
            raise Exception("Não conectado ao banco de dados.")

        tables_df = self.get_tables()
        all_tables_data = {}

        for _, row in tables_df.iterrows():
            schema = row["table_schema"]
            table = row["table_name"]
            full_table_name = f"{schema}.{table}"

            print(f"Extraindo dados da tabela: {full_table_name}...")

            query = f"SELECT * FROM {full_table_name};"
            df = pd.read_sql_query(query, self.connection)
            all_tables_data[table] = df

        return all_tables_data
