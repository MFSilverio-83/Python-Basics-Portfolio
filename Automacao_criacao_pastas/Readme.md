# Criador de Pastas para Orçamentos

Este é um script Python simples para automatizar a criação de uma estrutura de pastas padrão, ideal para organizar orçamentos ou projetos de forma mensal.

Ele foi projetado para ser facilmente configurável e robusto, evitando erros caso as pastas já existam e criando subdiretórios de forma condicional.

## ✨ Recursos

-   Cria uma estrutura de pastas complexa com um único comando.
-   **É seguro executar várias vezes**: o script não gera erros se as pastas já existirem.
-   **Fácil de configurar**: basta alterar as variáveis no início do script para adaptar a qualquer necessidade.
-   Lógica específica para criar subpastas (`SERVIÇOS`, `VENDAS`) apenas dentro do diretório `PRONTEC`.

## 📋 Pré-requisitos

-   Python 3.6 ou superior.
-   Nenhuma biblioteca externa é necessária (utiliza apenas a biblioteca padrão `pathlib`).

## 🚀 Como Usar

1.  **Baixe o script** (`cria_pastas.py`) para o seu computador.
2.  **Abra o arquivo** em um editor de código (como VS Code, Sublime Text, etc.).
3.  **Configure as variáveis** na seção `--- Configuração ---` de acordo com suas necessidades:

    ```python
    # --- Configuração ---

    # 1. Defina o caminho principal onde a estrutura será criada.
    #    Altere 'W:' para o seu drive e 'FEVEREIRO' para o mês desejado.
    caminho_base = Path('W:/ORÇAMENTOS 2023/FEVEREIRO')

    # 2. Lista de pastas principais a serem criadas no caminho base.
    pastas_principais = ['PRONTEC', 'DIMEP', 'TERCEIROS']

    # 3. Lista de subpastas que serão criadas APENAS dentro da pasta 'PRONTEC'.
    sub_pastas_prontec = ['SERVIÇOS', 'VENDAS']
    ```

4.  **Execute o script** através do seu terminal:

    ```bash
    python cria_pastas.py
    ```

## 📁 Estrutura de Pastas Gerada

Ao executar o script com a configuração padrão acima, a seguinte estrutura de diretórios será criada:

```
W:/ORÇAMENTOS 2023/FEVEREIRO/
├── DIMEP/
├── PRONTEC/
│   ├── SERVIÇOS/
│   └── VENDAS/
└── TERCEIROS/
```

## 📜 Código de Referência

Para referência, este é o código-fonte principal do script.

```python
from pathlib import Path

# --- Configuração ---
# Defina o caminho base em uma única variável.
caminho_base = Path('W:/ORÇAMENTOS 2023/FEVEREIRO')

# Listas de pastas a serem criadas.
pastas_principais = ['PRONTEC', 'DIMEP', 'TERCEIROS']
sub_pastas_prontec = ['SERVIÇOS', 'VENDAS']


# --- Lógica de Criação ---
print("Iniciando criação da estrutura de pastas...")

# 1. Loop para criar todas as pastas principais.
for pasta in pastas_principais:
    caminho_da_pasta = caminho_base / pasta
    caminho_da_pasta.mkdir(parents=True, exist_ok=True)
    print(f"Pasta criada ou já existente: {caminho_da_pasta}")

    # 2. Condição: se a pasta atual for 'PRONTEC', cria as subpastas dentro dela.
    if pasta == 'PRONTEC':
        for sub_pasta in sub_pastas_prontec:
            caminho_da_sub_pasta = caminho_da_pasta / sub_pasta
            caminho_da_sub_pasta.mkdir(exist_ok=True)
            print(f"  -> Subpasta criada ou já existente: {caminho_da_sub_pasta}")


print("\nEstrutura de pastas criada com sucesso!")
```

## 📄 Licença

Este projeto é de código aberto e distribuído sob a Licença MIT.