# Operações de depósito, saque e extrato

menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> '''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == 'd':        
        deposito = float(input('Digite o valor a ser depositado: '))
        
        if deposito <= 0:
            print('Valor digitado não é válido. Por favor digite um valor positivo para depósito.')
        else:
            saldo += deposito
            extrato += f'Depósito: R$ {deposito:.2f}\n'
            print(f'Depósito de {deposito:.2f} realizado com sucesso.')    
    
    elif opcao == 's':
        
        sacar = float(input('Digite o valor a ser sacado: '))

        if sacar <= 0:
            print('Valor digitado não é válido. Por favor digite um valor positivo para sacar.')
        elif sacar > saldo:
            print('Saldo insuficiente.')
        elif sacar > limite:
            print('O valor excede o limite de saque.')
        elif numero_saques > LIMITE_SAQUES:
            print('Número máximo de saques exedido.')
        else:
            saldo -= sacar
            numero_saques += 1
            extrato += f'Saque: R$ {sacar:.2f}\n'
            print(f'Saque de R$ {sacar:.2f} realizado com sucesso.')           
        
    elif opcao == 'e':
        print("\n================ EXTRATO ================\n")
        print(extrato if extrato else "Não foram realizadas movimentações.")
        print(f"\nSaldo: R$ {saldo:.2f}")
        print(f"Saques realizados: {numero_saques}/{LIMITE_SAQUES}")
        print("\n=========================================")

    
    elif opcao == 'q':
        print('Obrigado por usar nosso sistema bancário!')
        break

    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')

