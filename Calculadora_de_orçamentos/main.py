def calcular_orcamento():
    try:
        print(' CALCULADORA DE ORÇAMENTO '.center(60, '='))
        cliente = input('Cliente: ')
        servico = input('Descrição do serviço: ')
        qt_horas = int(input('Quantidade horas: '))
        preco_hora = float(input('Valor da hora: R$ '))
        desconto = float(input('Percentual de desconto (%): '))
    
        sub_total = qt_horas * preco_hora
        valor_desconto = sub_total * (desconto / 100)
        total = sub_total - valor_desconto

        print(' RESULTADO '.center(60, '='))
        print(f'''
        Cliente: {cliente}
        Serviço: {servico}
        Horas para execução: {qt_horas} horas
        Subtotal: R$ {sub_total:.2f}
        Desconto: {desconto:.2f} % Valor do desconto: R$ {valor_desconto:.2f}
        Valor final do orçamento: R$ {total:.2f}
        ''')
        print('=' * 60)

    except ValueError:
        print("\n[ERRO] Por favor, digite apenas números válidos para horas, valor e desconto.\n")

def main():
    while True:
        calcular_orcamento()
        continuar = input('Deseja criar um novo orçamento? [S/N]: ').strip().upper()
        if continuar == 'N':
            print("\nEncerrando a Calculadora de Orçamento. Obrigado!\n")
            break

if __name__ == "__main__":
    main()