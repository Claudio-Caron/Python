import os
import time
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

    print ("aguarde para prosseguir!\n")
    time.sleep(3)
def withdrawal ():#saque
    os.system ("cls")
    simulator()
    balance()
    x=-1
    while x<0 or x>=cash:
        print ("INSIRA O VALOR PARA SAQUE:")
        x=float(input("(para cancelar a operação, digite 0)\n"))
        if x<0 or x>=cash:
            os.system ("cls")
            print ("operação não pode ser realizada, insira novamente o valor")
    sucessfull(x)
    return cash-x
def payment ():
    simulator()
    balance()
    print ("INSIRA O VALOR PARA DEPÓSITO:")
    x=float (input("(para cancelar, digite 0)\n"))
    sucessfull(x)
    return cash+x
while op!=0:
    simulator()
    op=int(input("ESCOLHA UMA OPERAÇÃO:\n1-SALDO\n2-SAQUE\n3-DEPÓSITO\n0-SAIR\n"))
    op=int(op)
    if op<0 or op>3:
        print ("insira somente uma das opções de entrada:\n")
    elif op==1:#saldo
        os.system("cls")
        balance()
    elif op==2:#saque
        os.system("cls")
        cash=withdrawal()
        balance()
    elif op==3:#pagamento
        os.system ("cls")
        cash=payment()
        balance()
    else:
        os.system ("cls")
        balance()
        print ("VOCÊ SAIU DO SISTEMA\n")
        break
    
print ("fim_alg")
