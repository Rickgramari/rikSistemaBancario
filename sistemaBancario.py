print("\n************* Sistema Bancário ************")
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] sair

=>"""

saldo = 0
limite = 1500
extrato =""
num_saques = 0
LIMITES_SAQUES = 3

while True:

    opcao = input(menu)

    if  opcao == "d":
        valor =float(input("Informe o valor de deposito: R$ ")) # pergunto para ususario o valor que ira depositar
 
        if valor > 0: # faço uma verificação para evitar numero negativo
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n" #concatenando a string deposito com o valor formatado na variavel extrato 

        else:
            print("Operação cancelada! valor informado invalido")

    elif opcao == "s":
        valor = float(input("Informe o Valor do saque: R$ "))

        excedeu_saldo = valor >saldo #verifico se excedeu saldo
        excedeu_limite = valor > limite #verifico se excedeu limite
        excedeu_saques = num_saques >= LIMITES_SAQUES #verifico se excedeu numero de saques

        if excedeu_saldo:
            print("Operação não executada! não tem saldo suficiente")

        elif excedeu_limite:
            print("Operação não executada! valor do saque exedeu o limite ")

        elif excedeu_saques:
            print("Operação não executada! numero de saques excedido")

        elif valor > 0: # faço uma verificação se não esta digitando numero negativo
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            num_saques += 1 # incremento para que não fique no 0

        else:
            print("Operação não executada! valor informado invalido. ") # se for informado o valor invalido exibe a messagem 

    elif opcao == "e":
        print("\n*************EXTRATO************") # cabeçalho
        print("Não foram realizadas movimentações." if not extrato else extrato)# faço uma verificação se o extrato esta vazio caso não imprime a variavél Extrato
        print("\n--------------------------------")
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("********************************") # rodapé

    elif opcao == "q":
        break

    else:
        print("Operação não executada, selecione novamente a operação desejada")


    
        
