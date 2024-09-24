
numero_saques = 0
conta = float(0)
extrato = []
LIMITE_SAQUES = 3

while True:
    menu = input("- Sistema Bancario -\n\033[32m[1]\033[m Depositar\n\033[32m[2]\033[m Sacar\n\033[32m[3]\033[m Extrato\n\033[32m[4]\033[m Sair\n \033[32mSua Escolha:\033[m ").lower()
    if menu == "4":
        print("Até mais!")
        break
    if menu != "1" and menu != "2" and menu != "3":
        print("Operação Inválida, por favor selecione novamente a operação desejada.")
    match(menu):
        case "1":
            print("- Depositar -")
            deposito = float(input("Valor a ser depositado: "))
            if deposito <= 0:
                print("\033[31mValor Invalido! Este valor não pode ser depositado.\033[m")
            else:
                conta += deposito
                extrato.append(f"Deposito efetuado: R${deposito:.2f}")
                print("Deposito Efetuado com sucesso!")

        case "2":
            if numero_saques == LIMITE_SAQUES:
                print("O limite de saques foi atingido! Aguarde 24 Horas para um novo saque.")
            else:
                print("- Sacar -")
                sacar = float(input("Digite um valor a ser sacado: "))
                if sacar <= 0 or sacar > conta:
                    print("\033[31mValor Invalido! Impossivel sacar este valor.\033[m")
                else:
                    conta -= sacar
                    numero_saques += 1
                    extrato.append(f"Saque efetuado: R${sacar:.2f}")
                    print("Retire o dinheiro abaixo!")
        case "3":
            if extrato == []:
                print("=" * 20)
                print("Não foram realizadas movimentações até o momento.")
                print(f"\033[33mSaldo Bancario:\033[m \033[32mR${conta:.2f}\033[m")
                print("=" * 20)
            else:
                print("="*20)
                print(extrato)
                print(f"\033[33mSaldo Bancario:\033[m \033[32mR${conta:.2f}\033[m")
                print("=" * 20)

