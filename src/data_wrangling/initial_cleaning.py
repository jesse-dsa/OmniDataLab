import pandas as pd
from loaders.data_loader import DataLoader


def sanitize_column_names(df):
    """
    Corrige os nomes das colunas: letras minúsculas e underline para espaços.
    """
    df.columns = (
        df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace("-", "_")
    )
    return df


def convert_datetime_columns(df):
    """
    Converte automaticamente colunas que são prováveis de datas para datetime64[ns, UTC].
    """
    datetime_candidates = [
        "created_at",
        "updated_at",
        "release_date",
        "authorized_date",
        "last_change_date",
        "last_updated_date",
        "_datalancamentoproduto",
    ]

    for col in datetime_candidates:
        if col in df.columns:
            try:
                df[col] = pd.to_datetime(df[col], utc=True, errors="coerce")
                print(f"🕒 Coluna '{col}' convertida para datetime com timezone UTC.")
            except Exception as e:
                print(f"⚠️ Erro ao converter '{col}': {e}")

    return df


def basic_cleaning(df):
    """
    Aplica limpezas básicas no DataFrame:
    - Ajusta nomes das colunas
    - Remove colunas totalmente nulas
    - Corrige colunas de data
    """
    df = sanitize_column_names(df)
    df = df.dropna(axis=1, how="all")
    df = convert_datetime_columns(df)
    return df


def main():
    print("Iniciando primeira etapa de Data Wrangling...")

    loader = DataLoader()
    all_tables = loader.load_all_tables()

    cleaned_tables = {}

    for table_name, df in all_tables.items():
        print(f"\nLimpando tabela: {table_name}")
        cleaned_df = basic_cleaning(df)

        print(
            f"- {len(cleaned_df)} linhas, {len(cleaned_df.columns)} colunas após limpeza."
        )
        cleaned_tables[table_name] = cleaned_df

    print("\n✅ Wrangling inicial concluído!")
    return cleaned_tables


if __name__ == "__main__":
    cleaned_data = main()
