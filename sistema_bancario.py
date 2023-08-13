import datetime as dt

QUANTIDADE_SAQUE = 3
contador_saque = 0

LIMITE_SAQUE = 1500
somador_saque = 0

saldo = 1500.00
extrato = ""

def menu():
    print( """
[D] -> Depositar
[S] -> Sacar
[E] -> Extrato
[Q] -> Sair
    """)

def sacar(valor: float):
    if valor < 0:
        return -1
    elif valor > 500:
        return -2
    else:
        return valor
    
def depositar(valor: float):
    if valor < 0:
        return -3
    else:
        return valor
    
def mensagem_erro(valor: int):
    match valor:
        case -1:
            msg = "Não é permitido valor negativo para saque"
        case -2:
            msg = "Valor superior ao limite permitido: R$ 500.00"
        case -3:
            msg = "Não é permitido valor negativo para depósito"
    return msg
      
def movimentacao_fincanceira(valor, operacao):
    tipo_operacao = ("<class 'str'>")
    tipo_valor = ("<class 'int'>", "<class 'float'>")
    global saldo
    global extrato
    global contador_saque
    global somador_saque
    global LIMITE_SAQUE
    if str(type(operacao)) not in tipo_operacao:
        print("Por favor, digite uma opção valida. ")
    elif str(type(valor)) not in tipo_valor:
        print("Por favor, o valor precisa ser numérico.")
    else:
        match operacao:
            case 'D':
               deposito = depositar(valor)
               if deposito < 0:
                   print(mensagem_erro(deposito))
               else:
                  saldo = saldo + deposito
                  extrato = extrato + f"Depósito de RS{str(deposito)} efetuado em {dt.datetime.now()} \n"
            case 'S':
               saque = sacar(valor)
               if saque < 0:
                   print(mensagem_erro(saque))
               else:
                    if (LIMITE_SAQUE - (somador_saque + saque) < 0) or (contador_saque >= 3):
                        print("Limite diário financeiro alcançado. Não é possível efetivar a operação")
                    else:
                        saldo = saldo - saque
                        extrato = extrato + f"Saque de RS{str(saque)} efetuado em {dt.datetime.now()} \n"
                        contador_saque = contador_saque + 1
                        somador_saque = somador_saque + saque
            case 'E':
                print(extrato)
                print(f"Saldo total {saldo:.2f} em {dt.datetime.now()}")
            case _:
                print("Opção invalida")
              




while True:
    quantidade_saque = 0
    total_saque = 0
    menu()
    operacao = input("Digite a operação desejada: ").upper()
    if operacao == "E":
         movimentacao_fincanceira(0, operacao)
    elif operacao == "Q":
        break
    else:
        valor = float(input("Digite o valor: "))
        movimentacao_fincanceira(valor, operacao)
  
