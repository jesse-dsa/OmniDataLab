from loaders.data_loader import DataLoader


def main():
    loader = DataLoader()

    # Carregar uma tabela específica (exemplo: 'skus')
    skus = loader.load_table("skus")
    print(skus.head())  # Mostrar as primeiras linhas

    # Carregar todas as tabelas
    all_tables = loader.load_all_tables()
    print(all_tables.keys())  # Mostrar quais tabelas foram carregadas


if __name__ == "__main__":
    main()
