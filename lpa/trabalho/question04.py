# Funções utilitárias para input
def centraliza_texto(texto):
    largura = 70
    quantidade_de_separadores = ((largura - len(texto)) // 2) - 1
    linha = f"{'-' * quantidade_de_separadores} {texto} {'-' * quantidade_de_separadores}"
    if len(linha) < largura:
        linha += '-'
    print(linha)

def linha_tracejada():
    print('-' * 70)

def input_string(message, errorMessage):
    while True:
        try:
            return str(input(message))
        except ValueError:
            print(errorMessage)

def input_float(message, errorMessage):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print(errorMessage)

def input_int(message, errorMessage):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print(errorMessage)

# Funções principais do menu
def menu_principal():
    menu = {
        1: 'Cadastrar Funcionários',
        2: 'Consultar Funcionário(s)',
        3: 'Remover Funcionário',
        4: 'Sair',
    }
    linha_tracejada()
    centraliza_texto('MENU PRINCIPAL')
    for item in menu:
        print(f"{item}. {menu[item]}")
    return input_int('Escolha uma opção: ', 'Você digitou uma opção inválida. Tente novamente.')

def cadastrar_funcionarios(id):
    linha_tracejada()
    centraliza_texto('MENU CADASTRAR FUNCIONÁRIO')
    print(f'Id do funcionário: {id}')
    nome = input_string('Por favor entre como o nome do Funcionário: ', 'Você digitou o nome incorretamente. Tente novamente.')
    setor = input_string('Por favor entre como o setor do Funcionário: ', 'Você digitou o setor incorretamente. Tente novamente.')
    salario = input_float('Por favor entre como o salário do Funcionário: ', 'Você digitou o salario incorretamente. Tente novamente.')
    
    dados = {'id': id, 'nome': nome, 'setor': setor, 'salario': salario}
    lista_funcionarios.append(dados.copy())

    print("Funcionário cadastrado com sucesso!")

def menu_consulta():
    menu = {
        1: 'Consultar Todos',
        2: 'Consultar por Id(s)',
        3: 'Consultar por setor',
        4: 'Retornar ao menu',
    }
    linha_tracejada()
    centraliza_texto('MENU CONSULTAR FUNCIONÁRIO')
    for item in menu:
        print(f"{item}. {menu[item]}")
    return input_int('Escolha uma opção: ', 'Você digitou uma opção inválida. Tente novamente.')

def consultar_funcionario():
    while True:
        opcao = menu_consulta()
        if opcao == 1:
            linha_tracejada()
            if lista_funcionarios:
                for funcionario in lista_funcionarios:
                    print(f"id: {funcionario['id']}\nnome: {funcionario['nome']}\nsetor: {funcionario['setor']}\nsalário: {funcionario['salario']}\n")
            else:
                print("Nenhum funcionário cadastrado.")
            linha_tracejada()
        elif opcao == 2:
            linha_tracejada()
            funcionario_id = input_int('Digite o id do funcionário: ', 'O valor do id está incorreto. Tente novamente.')
            funcionario = next((func for func in lista_funcionarios if func['id'] == funcionario_id), None)
            if funcionario:
                print(f"id: {funcionario['id']}\nnome: {funcionario['nome']}\nsetor: {funcionario['setor']}\nsalário: {funcionario['salario']}\n")
            else:
                print("Funcionário não encontrado.")
            linha_tracejada()
        elif opcao == 3:
            linha_tracejada()
            setor = input_string('Digite o setor do funcionário: ', 'O nome do setor está incorreto. Tente novamente.')
            funcionarios = [func for func in lista_funcionarios if func['setor'] == setor]
            if funcionarios:
                for funcionario in funcionarios:
                    print(f"id: {funcionario['id']}\nnome: {funcionario['nome']}\nsetor: {funcionario['setor']}\nsalário: {funcionario['salario']}\n")
            else:
                print("Nenhum funcionário encontrado neste setor.")
            linha_tracejada()
        elif opcao == 4:
            break
        else:
            print("Opção inválida! Tente novamente.")

def remover_funcionario():
    id_para_remover = input_int('Digite o id do funcionário a ser removido: ', 'Você digitou o id incorretamente. Tente novamente.')
    for func in lista_funcionarios:
        if func['id'] == id_para_remover:
            lista_funcionarios.remove(func)
            print("Funcionário removido com sucesso.")
            break 
    else:
        print("Id inválido, tente novamente.")

# Início do programa
def iniciar():
    global lista_funcionarios
    lista_funcionarios = []  # Exigência 2 de 8
    id_global = 5028165  # Exigência 2 de 8

    print("\nBem-vindo à empresa da Gabriela Pereira dos Santos\n")  # Exigência 1 de 8

    while True:
        opcao = menu_principal()
        if opcao == 1:
            cadastrar_funcionarios(id_global)
            id_global += 1
        elif opcao == 2:
            consultar_funcionario()
        elif opcao == 3:
            remover_funcionario()
        elif opcao == 4:
            print("Encerrando programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Execução do programa
iniciar()
