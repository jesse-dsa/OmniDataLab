import psycopg2
import pytest
from psycopg2 import OperationalError
from unittest.mock import patch
from _pytest.outcomes import (
    Failed,  # ✅ Correto para capturar falha de pytest.fail
)


# Fixture para conexão segura com tratamento de erro
@pytest.fixture
def db_connection():
    try:
        connection = psycopg2.connect(
            dbname="vtex_catalog",
            user="postgres",
            password="Jotta@1440",
            host="127.0.0.1",
            port="5432",
        )
        yield connection
        connection.close()
    except OperationalError as e:
        pytest.fail(f"Falha ao estabelecer conexão com o banco de dados: {str(e)}")


# Teste de conexão bem-sucedida
def test_postgresql_connection_success(db_connection):
    """Testa uma conexão bem-sucedida com o PostgreSQL"""
    assert not db_connection.closed
    assert db_connection.info.protocol_version in (2, 3)
    assert db_connection.status == psycopg2.extensions.STATUS_READY


# Teste de falha direta (senha errada / banco inexistente)
def test_postgresql_connection_failure():
    """Testa cenários de falha ao conectar diretamente"""
    with pytest.raises(OperationalError):
        psycopg2.connect(
            dbname="vtex_catalog",
            user="postgres",
            password="senha_incorreta",
            host="127.0.0.1",
            port="5432",
        )
    with pytest.raises(OperationalError):
        psycopg2.connect(
            dbname="database_inexistente",
            user="postgres",
            password="Jotta@1440",
            host="127.0.0.1",
            port="5432",
        )


# Teste forçando a fixture a falhar (mockando psycopg2.connect)
@patch(
    "psycopg2.connect",
    side_effect=OperationalError("Erro simulado na conexão"),
)
def test_db_connection_fixture_failure(mock_connect):
    """Testa falha no momento de usar a fixture db_connection"""
    with pytest.raises(Failed):  # ✅ Correto para capturar o pytest.fail
        next(db_connection())  # Chamamos manualmente para capturar o erro do yield
