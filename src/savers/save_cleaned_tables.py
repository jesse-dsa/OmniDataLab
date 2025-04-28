import os
from datetime import datetime
from data_wrangling.initial_cleaning import main as wrangling_main


def save_cleaned_dataframes(cleaned_tables, output_dir="outputs/cleaned"):
    """
    Salva todos os DataFrames limpos em CSV na pasta especificada, adicionando timestamp.

    :param cleaned_tables: Dicionário {nome_tabela: DataFrame}
    :param output_dir: Pasta onde os CSVs serão salvos
    """
    # Garante que a pasta de destino existe
    os.makedirs(output_dir, exist_ok=True)

    # Timestamp para versionar os arquivos
    timestamp = datetime.now().strftime("%Y%m%d")

    for table_name, df in cleaned_tables.items():
        # Se DataFrame estiver vazio, não salva
        if df.empty:
            print(f"⚠️ Tabela {table_name} vazia — não será salva.")
            continue

        filename = f"{table_name}_{timestamp}.csv"
        file_path = os.path.join(output_dir, filename)

        df.to_csv(file_path, index=False)
        print(f"✅ Tabela '{table_name}' salva em '{file_path}'.")


def main():
    print("Iniciando processo de salvar tabelas limpas...")

    # Roda a limpeza e obtém os DataFrames
    cleaned_tables = wrangling_main()

    # Salva os DataFrames
    save_cleaned_dataframes(cleaned_tables)

    print("\n🏁 Processo de salvamento concluído.")


if __name__ == "__main__":
    main()
