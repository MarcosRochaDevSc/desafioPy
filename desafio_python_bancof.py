def depositar(saldo, valor, movimentacoes):
    """Função para realizar um depósito."""
    if valor > 0:
        saldo += valor
        movimentacoes.append(f"Depósito: R$ {valor:.2f}")
    else:
        print("Valor de depósito deve ser positivo.")
    return saldo, movimentacoes

def sacar(*, saldo, valor, movimentacoes, limite_saque=500, numero_saques, limite_saques=3):
    """Função para realizar um saque."""
    if numero_saques >= limite_saques:
        print("Limite de saques diários atingido.")
    elif valor > limite_saque:
        print(f"Limite de saque por operação é de R$ {limite_saque:.2f}.")
    elif valor <= saldo:
        saldo -= valor
        movimentacoes.append(f"Saque: R$ {valor:.2f}")
        numero_saques += 1
    else:
        print("Saldo insuficiente para saque.")
    return saldo, movimentacoes, numero_saques

def exibir_extrato(saldo, *, movimentacoes):
    """Função para exibir o extrato de movimentações."""
    if not movimentacoes:
        print("Não foram realizadas movimentações.")
    else:
        print("Extrato de Movimentações:")
        for mov in movimentacoes:
            print(mov)
        print(f"Saldo atual: R$ {saldo:.2f}")

# Estruturas para usuários e contas
usuarios = []
contas = []

def cadastrar_usuario(nome, data_nascimento, cpf, endereco):
    """Função para cadastrar um novo usuário."""
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("Usuário com este CPF já cadastrado.")
            return
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

def criar_conta_corrente(cpf_usuario):
    """Função para criar uma conta corrente vinculada a um usuário."""
    global contas
    usuario_encontrado = False
    for usuario in usuarios:
        if usuario['cpf'] == cpf_usuario:
            usuario_encontrado = True
            break
    if not usuario_encontrado:
        print("Usuário não encontrado.")
        return
    numero_conta = len(contas) + 1
    contas.append({"agencia": "0001", "numero_conta": numero_conta, "usuario": cpf_usuario})

# Exemplo de uso das funções
saldo = 0
movimentacoes = []
saques_diarios = 0

# Cadastramento de usuário
cadastrar_usuario("João Silva", "01/01/1980", "12345678900", "Rua Exemplo, 123 - Centro - São Paulo/SP")
# Criando uma conta corrente para o usuário cadastrado
criar_conta_corrente("12345678900")

# Usando as funções de depósito e saque
saldo, movimentacoes = depositar(saldo, 1000, movimentacoes)
saldo, movimentacoes, saques_diarios = sacar(saldo=saldo, valor=200, movimentacoes=movimentacoes, numero_saques=saques_diarios)

# Imprimindo o extrato
exibir_extrato(saldo, movimentacoes=movimentacoes)

# Informações dos usuários e contas cadastradas
print(usuarios, contas)
