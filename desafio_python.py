saldo = 0
movimentacoes = []
saques_diarios = 0

while True:
    print("\nMenu do Banco")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Exibir Extrato")
    print("4. Sair")
    opcao = input("Escolha uma opção (1-4): ")

    if opcao == '1':
        valor = float(input("Valor para depósito: R$ "))
        if valor > 0:
            saldo += valor
            movimentacoes.append(f"Depósito: R$ {valor:.2f}")
        else:
            print("Valor de depósito deve ser positivo.")

    elif opcao == '2':
        valor = float(input("Valor para saque: R$ "))
        if saques_diarios >= 3:
            print("Limite de saques diários atingido.")
        elif valor > 500:
            print("Limite de saque por operação é de R$ 500,00.")
        elif valor <= saldo:
            saldo -= valor
            movimentacoes.append(f"Saque: R$ {valor:.2f}")
            saques_diarios += 1
        else:
            print("Saldo insuficiente para saque.")

    elif opcao == '3':
        if not movimentacoes:
            print("Não foram realizadas movimentações.")
        else:
            print("Extrato de Movimentações:")
            for mov in movimentacoes:
                print(mov)
            print(f"Saldo atual: R$ {saldo:.2f}")

    elif opcao == '4':
        print("Saindo do sistema bancário.")
        break
    else:
        print("Opção inválida. Por favor, escolha entre 1-4.")
