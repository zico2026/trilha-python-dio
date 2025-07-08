# Menu de opções apresentado ao usuário
menu = """
[1] Depositar
[2] Sacar 
[3] Extrato 
[0] Sair 
=> """  # Seta que indica onde o usuário deve digitar

# Estado inicial da conta
saldo = 0
limite = 1000  # Limite máximo por saque
extrato = ""   # Histórico de movimentações
numero_saques = 0
LIMITE_SAQUES = 5  # Quantidade máxima de saques permitidos por dia

# Loop principal do programa
while True:
    opcao = input(menu)

    # Depósito
    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")

    # Saque
    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        # Validações
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        # Verificações em ordem de prioridade
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! Valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")

    # Exibe extrato
    elif opcao == "3":
        print("\n================ EXTRATO ================")
        # Mostra extrato se houver, senão exibe mensagem de vazio
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    # Encerra o programa
    elif opcao == "0":
        break

    # Opção inválida
    else:
        print("Operação inválida. Tente novamente.")