continuar = True
limite = 500
saldo = 0
valor = 0
operacoes_diarias = 3
operacoes_usadas = 0
lista_deposito = ""
lista_saque = ""

while continuar == True:

    print("---- Menu ----")
    print("1 - Depósito")
    print("2 - Saque")
    print("3 - Extrato")
    print("4 - Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        print("---- Depósito ----")
        valor = float(input("Digite a quantidade a ser depositada: R$"))

        if (valor > 0):
            saldo += valor
            print("Operação realizada com sucesso!")
            print(f"Saldo: R$ {saldo:.2f}")
            lista_deposito += f"R${valor:.2f}\n"

        else:
            print("Erro na operação.")

    elif opcao == "2":
        print("---- Saque ----")
        valor = float(input("Digite a quantidade a ser sacada: R$"))

        if (operacoes_usadas < operacoes_diarias):
            if (valor > limite):
                print(f"Não é possível realizar operações com valor acima de R${limite:.2f}")

            elif (valor > 0 and valor < saldo):
                saldo -= valor
                print(f"Operação realizada com sucesso! Foi sacado R${valor:.2f} da sua conta.")
                print(f"Saldo: R$ {saldo:.2f} ")
                lista_saque += f"R${valor:.2f}\n"
                operacoes_usadas += 1

            elif (valor > saldo):
                print("Não há saldo suficiente para saque.")

            else:
                print("Erro na operação.")
        else:
            print("quantidade diária de saques excedida.")
    elif opcao == "3":
        print("---- Extrato ----")
        if (lista_deposito != ""):
            print("---- Depósitos realizados ----")
            print(lista_deposito)
        else:
            print("Não foi realizado nenhum depósito.")

        if (lista_saque != ""):
            print("---- Saques realizados ----")
            print(lista_saque)
        else:
            print("Não foi realizado nenhum saque.")

    elif opcao == "4":
        break

    else:
        print("Opção inválida, tente novamente.")
﻿