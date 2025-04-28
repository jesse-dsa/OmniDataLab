import os

# Define a estrutura do projeto OmniDataLab
structure = {
    ".github": ["workflows/", "ISSUE_TEMPLATE/"],
    ".vscode": ["settings.json"],
    "audit": [
        "data_lineage/",
        "access_logs/",
        "data_quality/",
        "compliance/",
        "reports/",
    ],
    "config": [
        "env/dev/",
        "env/staging/",
        "env/prod/",
        "connections/",
        "constraints/",
        "setup/",  # Onde estará este script!
    ],
    "data": [
        "raw/oms/",
        "raw/ga4/",
        "raw/catalog/",
        "raw/webscraping/",
        "raw/product/",
        "staged/",
        "processed/",
        "feature_store/",
    ],
    "docs": ["data_dictionary/", "api_specs/", "po_cases/", "architecture/"],
    "infrastructure": ["terraform/", "kubernetes/"],
    "notebooks": ["exploration/", "prototyping/", "po_experiments/"],
    "pipelines": ["etl/oms_pipeline/", "etl/ga4_pipeline/", "ml/", "po/"],
    "src": [
        "connectors/",
        "core/",
        "analytics/",
        "ml/",
        "optimization/",
        "audit/",
        "utils/",
        "api/",
    ],
    "tests": ["unit/", "integration/", "e2e/", "data/"],
    "": [  # Arquivos no diretório raiz
        ".env.template",
        "Makefile",
        "pyproject.toml",
        "Dockerfile",
        "docker-compose.yml",
        "README.md",
    ],
}


def create_project_structure(base_path="."):
    print(f"🔧 Criando estrutura do projeto em: {base_path}\n")

    for parent, children in structure.items():
        parent_path = os.path.join(base_path, parent)

        if parent and not os.path.exists(parent_path):
            os.makedirs(parent_path, exist_ok=True)
            print(f"📁 Diretório criado: {parent_path}")

        for child in children:
            child_path = os.path.join(parent_path, child)

            if child.endswith("/"):
                os.makedirs(child_path, exist_ok=True)
                print(f"📂 Subdiretório criado: {child_path}")
            else:
                os.makedirs(os.path.dirname(child_path), exist_ok=True)
                if not os.path.exists(child_path):
                    with open(child_path, "w", encoding="utf-8") as f:
                        pass
                    print(f"📄 Arquivo criado: {child_path}")

    print("\n✅ Estrutura do OmniDataLab criada com sucesso!")


if __name__ == "__main__":
    # Cria a estrutura a partir da raiz do repositório
    base_project_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../")
    )
    create_project_structure(base_path=base_project_path)
