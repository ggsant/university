# Constantes para os preços dos modelos de camisetas
PRECO_MCS = 1.80  # Manga Curta Simples
PRECO_MLS = 2.10  # Manga Longa Simples
PRECO_MCE = 2.90  # Manga Curta Com Estampa
PRECO_MLE = 3.20  # Manga Longa Com Estampa

# Constantes para os valores de frete
FRETE_TRANSPORTADORA = 100.00
FRETE_SEDEX = 200.00
FRETE_RETIRADA = 0.00

def exibir_menu_inicial():
    print("\nBem-vindo à Fábrica de Camisetas da Gabriela Pereira dos Santos\n")


def selecionar_modelo():
    print("Modelos disponíveis:")
    print("MCS - Manga Curta Simples")
    print("MLS - Manga Longa Simples")
    print("MCE - Manga Curta Com Estampa")
    print("MLE - Manga Longa Com Estampa")

    while True:
        modelo = input('Entre com o modelo desejado: ').upper()
        if modelo in ['MCS', 'MLS', 'MCE', 'MLE']:
            return modelo
        else:
            print('Escolha inválida, entre com o modelo novamente.\n')


def obter_quantidade_camisetas():
    while True:
        try:
            quantidade = int(input('Entre com o número de camisetas: '))
            if quantidade > 20000:
                print("Quantidade de camisetas não aceita! Tente novamente.\n")
            elif quantidade >= 2000:
                return quantidade * 0.88  # Desconto de 12%
            elif quantidade >= 200:
                return quantidade * 0.93  # Desconto de 7%
            elif quantidade >= 20:
                return quantidade * 0.95  # Desconto de 5%
            elif quantidade > 0:
                return quantidade  # Sem desconto
            else:
                print("Quantidade inválida! Tente novamente.\n")
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.\n")


def selecionar_frete():
    print("Escolha o tipo de frete:")
    print(f"1 - Frete por transportadora - R$ {FRETE_TRANSPORTADORA:.2f}")
    print(f"2 - Frete por Sedex - R$ {FRETE_SEDEX:.2f}")
    print(f"0 - Retirar pedido na fábrica - R$ {FRETE_RETIRADA:.2f}")
    
    while True:
        try:
            opcao_frete = int(input('Digite a opção desejada: '))
            if opcao_frete in [0, 1, 2]:
                return opcao_frete
            else:
                print('Escolha inválida, entre com a opção de frete novamente.\n')
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.\n")


def calcular_valor_unitario(modelo):
    # Retorna o valor unitário com base no modelo escolhido
    if modelo == 'MCS':
        return PRECO_MCS
    elif modelo == 'MLS':
        return PRECO_MLS
    elif modelo == 'MCE':
        return PRECO_MCE
    elif modelo == 'MLE':
        return PRECO_MLE


def calcular_valor_frete(opcao_frete):
    # Retorna o valor do frete baseado na opção escolhida
    if opcao_frete == 1:
        return FRETE_TRANSPORTADORA
    elif opcao_frete == 2:
        return FRETE_SEDEX
    else:
        return FRETE_RETIRADA


def calcular_total(valor_unitario, quantidade, valor_frete):
    # Calcula o valor total do pedido
    return (valor_unitario * quantidade) + valor_frete


# Execução principal do programa
exibir_menu_inicial()
modelo = selecionar_modelo()
quantidade = obter_quantidade_camisetas()
opcao_frete = selecionar_frete()

valor_unitario = calcular_valor_unitario(modelo)
valor_frete = calcular_valor_frete(opcao_frete)
total = calcular_total(valor_unitario, quantidade, valor_frete)

# Exibição do resultado final
print(f'\nTotal: R$ {total:.2f} (Modelo: R$ {valor_unitario:.2f} * Quantidade (com desconto): {quantidade:.2f} + Frete: R$ {valor_frete:.2f})')
