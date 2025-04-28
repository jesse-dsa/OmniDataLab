import os
import pandas as pd


class DataLoader:
    def __init__(self, data_dir="outputs"):
        """
        Classe para carregar tabelas extraídas do PostgreSQL em DataFrames.

        :param data_dir: Diretório onde estão os CSVs extraídos.
        """
        self.data_dir = data_dir

    def load_table(self, table_name):
        """
        Carrega uma tabela específica.

        :param table_name: Nome da tabela (sem '.csv')
        :return: DataFrame da tabela
        """
        file_path = os.path.join(self.data_dir, f"{table_name}.csv")
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Arquivo {file_path} não encontrado.")

        print(f"Carregando tabela: {table_name}...")
        df = pd.read_csv(file_path)
        print(f"Tabela {table_name} carregada com {len(df)} registros.")
        return df

    def load_all_tables(self):
        """
        Carrega todas as tabelas no diretório de outputs.

        :return: Dicionário {nome_tabela: DataFrame}
        """
        tables = {}
        print(f"Carregando todas as tabelas do diretório: {self.data_dir}...")
        for file in os.listdir(self.data_dir):
            if file.endswith(".csv"):
                table_name = file.replace(".csv", "")
                file_path = os.path.join(self.data_dir, file)
                df = pd.read_csv(file_path)
                tables[table_name] = df
                print(f"Tabela {table_name} carregada ({len(df)} registros).")

        if not tables:
            print("Nenhuma tabela CSV encontrada!")

        return tables
