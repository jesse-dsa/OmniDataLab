import psycopg2
import pytest
from psycopg2 import OperationalError
from unittest.mock import patch
from _pytest.outcomes import Failed


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
<<<<<<< HEAD
        msg = "Falha na conexão com o banco de dados"
        pytest.fail(f"{msg}: {str(e)}")
=======
        msg = "Falha ao estabelecer conexão com o banco de dados: "
        pytest.fail(f"{msg}{str(e)}")
>>>>>>> 545aaaca43fd2592770de419e0169a905ffa9487


def test_postgresql_connection_success(db_connection):
    """Testa conexão bem-sucedida com PostgreSQL"""
    assert not db_connection.closed
    assert db_connection.info.protocol_version in (2, 3)
    assert db_connection.status == psycopg2.extensions.STATUS_READY


def test_postgresql_connection_failure():
    """Testa cenários de falha na conexão"""
    with pytest.raises(OperationalError):
        psycopg2.connect(
            dbname="vtex_catalog",
            user="postgres",
            password="senha_incorreta",
            host="127.0.0.1",
            port="5432",
        )


@patch("psycopg2.connect", side_effect=OperationalError("Erro simulado"))
def test_db_connection_fixture_failure(mock_connect):
    """Testa falha na fixture db_connection"""
    with pytest.raises(Failed):
        next(db_connection())