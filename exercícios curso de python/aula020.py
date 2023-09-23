import os
os.system("cls")
cash=1500
op=1
def simulator():  #mensagem de banco/SEM RETORNO  
    print ("\tSIMULADOR DE CAIXA ELETRÔNICO\n\n")
def balance():#saldo-COM RETORNO
    print ("saldo atual:", cash)
def sucessfull(y):#mensagem para operação realizada ou não
    os.system ("cls")
    simulator()
    if y==0:
        print ("\nOPERAÇÃO CANCELADA\n")
    else :
        print ("\nOPERAÇÃO REALIZADA COM SUCESSO!!!")
    balance()
def withdrawal ():#saque
    os.system ("cls")
    simulator()
    balance()
    while x<0 or x>=cash:
        print ("INSIRA O VALOR PARA SAQUE:")
        x=float(("(para cancelar a operação, digite 0)\n"))
    sucessfull(x)
    return cash-x
def payment ():
    simulator()
    x=balance()
    print ("INSIRA O VALOR PARA DEPÓSITO:")
    x=float (input ("(para cancelar, digite 0)\n"))
    sucessfull(x)
    return cash+x
while op!=0:
    simulator()
    op=int(input("ESCOLHA UMA OPERAÇÃO:\n1-SALDO\n2-SAQUE\n3-PAGAMENTO\n0-SAIR\n"))
    if op<0 or op>3:
        print ("insira somente uma das opções de entrada:\n")
    elif op==1:#saldo
        os.system("cls")
        simulator()
        balance()
    elif op==2:#saque
        os.system("cls")
        cash=withdrawal()
    elif op==3:#pagamento
        os.system ("cls")
        cash=payment()
    else:
        break
print ("fim_alg")
