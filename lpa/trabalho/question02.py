def cria_linha_com_texto_centralizado(texto, largura=100):
    quantidade_de_separadores = ((largura - len(texto)) // 2) - 1
    linha = f"{'-' * quantidade_de_separadores} {texto} {'-' * quantidade_de_separadores}"
    if len(linha) < largura:
        linha += '-'
    return linha


def centralizar_texto(texto, largura):
    return texto.center(largura)


def cria_menu():
    largura = 70
    col1_largura = 10
    col2_largura = 25
    col3_largura = 25

    print(cria_linha_com_texto_centralizado(
        "Bem-vindos a Loja de Marmitas da Gabriela Pereira dos Santos", largura))
    print(cria_linha_com_texto_centralizado("Cardápio", largura))

    print("-" * largura)
    print(f"| {centralizar_texto('Tamanho', col1_largura)} | "
          f"{centralizar_texto('Bife Acebolado(BA)', col2_largura)} | "
          f"{centralizar_texto('Filé de Frango(FF)', col3_largura)} |")
    print("-" * largura)
    print(f"| {centralizar_texto('P', col1_largura)} | "
          f"{centralizar_texto('R$ 16.00', col2_largura)} | "
          f"{centralizar_texto('R$ 15.00', col3_largura)} |")
    print(f"| {centralizar_texto('M', col1_largura)} | "
          f"{centralizar_texto('R$ 18.00', col2_largura)} | "
          f"{centralizar_texto('R$ 17.00', col3_largura)} |")
    print(f"| {centralizar_texto('G', col1_largura)} | "
          f"{centralizar_texto('R$ 22.00', col2_largura)} | "
          f"{centralizar_texto('R$ 21.00', col3_largura)} |")
    print("-" * largura)
    print()


def selecionar_sabor_e_tamanho():
    while True:
        sabor = input('Entre com o sabor desejado (BA/FF): ').upper()
        if sabor not in ['BA', 'FF']:
            print('Sabor inválido. Tente novamente.')
            print()
            continue  # Volta ao início do loop para selecionar o sabor novamente

        tamanho = input('Entre com o tamanho desejado (P/M/G): ').upper()
        if tamanho not in ['P', 'M', 'G']:
            print('Tamanho inválido. Tente novamente.')
            print()
            continue  # Se o tamanho for inválido, volta para selecionar o sabor

        return sabor, tamanho


def calcular_valor_da_marmita(sabor, tamanho):
    if sabor == 'BA':
        if tamanho == 'P':
            return 16.00
        elif tamanho == 'M':
            return 18.00
        elif tamanho == 'G':
            return 22.00
    elif sabor == 'FF':
        if tamanho == 'P':
            return 15.00
        elif tamanho == 'M':
            return 17.00
        elif tamanho == 'G':
            return 21.00


def seleciona_novo_pedido(valor_total):
    while True:
        deseja_novo_pedido = input('Deseja pedir mais alguma coisa? (S/N): ').upper()
        if deseja_novo_pedido == 'S':
            return True
        elif deseja_novo_pedido == 'N':
            print(f'O valor total a ser pago: R$ {valor_total:.2f}')
            return False
        else:
            print('Opção inválida. Tente novamente.')
            continue  # Mantém o loop até que uma opção válida seja fornecida


def criar_pedido():
    valor_total = 0.0
    while True:
        sabor, tamanho = selecionar_sabor_e_tamanho()
        valor_marmita = calcular_valor_da_marmita(sabor, tamanho)
        
        # Mapeando o código do sabor para o nome completo do prato
        sabor_texto = "Bife Acebolado" if sabor == "BA" else "Filé de Frango"
        
        valor_total += valor_marmita
        print(f'Você pediu um {sabor_texto} no tamanho {tamanho}: R$ {valor_marmita:.2f}')
        print()

        if not seleciona_novo_pedido(valor_total):
            break  # Sai do loop e finaliza o pedido


def iniciar_sistema_de_pedidos():
    cria_menu()
    criar_pedido()


# Código principal
iniciar_sistema_de_pedidos()
