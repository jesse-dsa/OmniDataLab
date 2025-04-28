import os
from connectors.postgresql_connector import PostgreSQLConnector


def extract_all_tables_to_csv(output_dir="outputs"):
    # Conecta no banco
    connector = PostgreSQLConnector(
        dbname="vtex_catalog",
        user="postgres",
        password="Jotta@1440",
        host="127.0.0.1",
        port="5432",
    )

    connector.connect()

    # Extrai todas as tabelas
    all_tables = connector.get_all_tables_data()

    # Cria diretório de saída se não existir
    os.makedirs(output_dir, exist_ok=True)

    # Salva cada tabela como CSV
    for table_name, df in all_tables.items():
        file_path = os.path.join(output_dir, f"{table_name}.csv")
        df.to_csv(file_path, index=False)
        print(f"Tabela '{table_name}' salva em '{file_path}'.")

    connector.disconnect()


if __name__ == "__main__":
    extract_all_tables_to_csv()
