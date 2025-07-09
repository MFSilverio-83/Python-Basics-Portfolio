import locale
from datetime import datetime
from pathlib import Path

# Define o local para o português do Brasil para obter o nome do mês corretamente
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

# --- Configuração Dinâmica ---
ano_atual = datetime.now().strftime('%Y')
mes_atual = datetime.now().strftime('%B').upper()

# --- Configuração Manual ---
drive = 'D:'
projeto_raiz = 'ORÇAMENTOS'
pastas_principais = ['PRONTEC', 'DIMEP', 'TERCEIROS']
sub_pastas_prontec = ['SERVIÇOS', 'VENDAS']

# --- Lógica de Criação ---
# Monta o caminho base dinamicamente
caminho_base = Path(drive) / f'{projeto_raiz} {ano_atual}' / mes_atual

print(f"Iniciando criação para {mes_atual.capitalize()}/{ano_atual}...")

# Lógica com a condição para criar subpastas apenas em 'PRONTEC'
for pasta in pastas_principais:
    caminho_da_pasta = caminho_base / pasta
    caminho_da_pasta.mkdir(parents=True, exist_ok=True)
    print(f"Pasta criada ou já existente: {caminho_da_pasta}")

    if pasta == 'PRONTEC':
        for sub_pasta in sub_pastas_prontec:
            caminho_da_sub_pasta = caminho_da_pasta / sub_pasta
            caminho_da_sub_pasta.mkdir(exist_ok=True)
            print(f"  -> Subpasta criada ou já existente: {caminho_da_sub_pasta}")

print(f"\nEstrutura de pastas para {mes_atual.capitalize()}/{ano_atual} criada com sucesso!")