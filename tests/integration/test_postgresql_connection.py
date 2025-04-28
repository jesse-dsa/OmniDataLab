import psycopg2
import pytest


def test_postgresql_connection():
    try:
        # Configurações de conexão com o banco de dados
        connection = psycopg2.connect(
            dbname="vtex_catalog",  # Nome do banco de dados
            user="postgres",  # Substitua com seu nome de usuário
            password="Jotta@1440",  # Substitua com sua senha
            host="127.0.0.1",  # Ou o IP do servidor
            port="5432",  # O padrão do PostgreSQL
        )
        # Se a conexão for bem-sucedida, fecha a conexão
        connection.close()
        print("Conexão bem-sucedida ao banco de dados.")
    except Exception as e:
        pytest.fail(f"Falha na conexão com o banco de dados: {str(e)}")
