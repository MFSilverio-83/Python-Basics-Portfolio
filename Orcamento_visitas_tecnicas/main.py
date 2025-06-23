# --- Constantes ---
CUSTO_KM_UNITARIO = 1.50
PRAZO_PAGAMENTO = 28 # DDF significa "Dias Depois do Faturamento" ou similar

def coletar_dados_visita():
    """Coleta os dados iniciais da visita e dos equipamentos."""
    cidade = input('Cidade: ')
    
    while True:
        try:
            km = float(input('Distância em Km: '))
            if km < 0:
                print("A distância não pode ser negativa. Tente novamente.")
                continue
            break
        except ValueError:
            print("[ERRO] Por favor, digite um número válido para a distância em Km.")

    equipamentos = []
    while True:
        equipamento_nome = input('Equipamento com problema: ')
        while True:
            try:
                servico_valor = float(input(f'Valor do serviço para {equipamento_nome}: R$ '))
                if servico_valor < 0:
                    print("O valor do serviço não pode ser negativo. Tente novamente.")
                    continue
                break
            except ValueError:
                print(f"[ERRO] Por favor, digite um número válido para o valor do serviço de {equipamento_nome}.")
        
        equipamentos.append({'nome': equipamento_nome, 'valor': servico_valor})

        continuar = input('Adicionar outro equipamento? [S/N]: ').strip().upper()
        if continuar == 'N':
            break
    
    return cidade, km, equipamentos

def calcular_valores(km, equipamentos):
    """Calcula o valor do deslocamento e o total dos serviços."""
    valor_km = (km * 2) * CUSTO_KM_UNITARIO # Ida e volta
    total_servicos = sum(item['valor'] for item in equipamentos)
    total_geral = valor_km + total_servicos
    return valor_km, total_servicos, total_geral

def formatar_nomes_equipamentos(equipamentos):
    """Formata a string com os nomes dos equipamentos para exibição."""
    nomes = [e['nome'] for e in equipamentos]
    if not nomes:
        return ""
    if len(nomes) == 1:
        return nomes[0]
    return ", ".join(nomes[:-1]) + " e " + nomes[-1]

def exibir_orcamento(cidade, valor_km, equipamentos, total_servicos, total_geral):
    """Exibe o orçamento formatado."""
    equipamentos_str = formatar_nomes_equipamentos(equipamentos)
    
    print(f'\n{" Orçamento da Visita Técnica ".center(50, "*")}')
    print(f'Visita técnica em {cidade} para manutenção em {equipamentos_str}.\n')
    
    print(f'Valor do deslocamento')
    print(f'R$ {valor_km:.2f}\n')
    
    for item in equipamentos:
        print(f'Valor do serviço {item["nome"]}')
        print(f'R$ {item["valor"]:.2f}') # Removido "(valor unitário)" pois já é o valor do serviço
    print() # Linha em branco para separar os serviços do total

    print(f'Total dos serviços: R$ {total_servicos:.2f}')
    print(f'TOTAL GERAL: R$ {total_geral:.2f}\n')
    print(f'Pagamento: {PRAZO_PAGAMENTO} DDF')
    print(f'{"*" * 50}\n')

def main():
    """Função principal que orquestra o programa."""
    cidade, km, equipamentos = coletar_dados_visita()
    valor_km, total_servicos, total_geral = calcular_valores(km, equipamentos)
    exibir_orcamento(cidade, valor_km, equipamentos, total_servicos, total_geral)

if __name__ == '__main__':
    main()

