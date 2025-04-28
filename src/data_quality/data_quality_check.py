from loaders.data_loader import DataLoader


def check_completude(df, threshold=0.3):
    """
    Checa se há colunas com mais de 'threshold' de valores nulos.
    """
    total_rows = len(df)
    missing_info = df.isnull().sum() / total_rows
    critical_columns = missing_info[missing_info > threshold]
    return critical_columns


def check_negative_values(df):
    """
    Checa colunas numéricas para valores negativos (exceto campos permitidos).
    """
    negative_issues = {}
    for column in df.select_dtypes(include=["int64", "float64"]).columns:
        if (df[column] < 0).any():
            negative_issues[column] = df[df[column] < 0].shape[0]
    return negative_issues


def check_column_types(df):
    """
    Mostra tipos de colunas.
    """
    return df.dtypes


def main():
    print("Iniciando checagem de qualidade dos dados...")

    loader = DataLoader(data_dir="outputs/cleaned")
    all_tables = loader.load_all_tables()

    for table_name, df in all_tables.items():
        print(f"\n🔎 Analisando tabela: {table_name}")

        # 1. Completude
        critical_nulls = check_completude(df)
        if not critical_nulls.empty:
            print("⚠️ Colunas com muitos valores nulos (>30%):")
            print(critical_nulls)
        else:
            print("✅ Nenhuma coluna crítica de nulos.")

        # 2. Valores Negativos
        negatives = check_negative_values(df)
        if negatives:
            print("⚠️ Colunas com valores negativos:")
            for col, count in negatives.items():
                print(f"- {col}: {count} valores negativos")
        else:
            print("✅ Nenhum valor negativo incoerente.")

        # 3. Tipos de Coluna
        print("📊 Tipos de dados por coluna:")
        print(check_column_types(df))

    print("\n🏁 Checagem de qualidade dos dados concluída.")


if __name__ == "__main__":
    main()
