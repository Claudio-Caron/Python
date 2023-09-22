#função com retorno
import os
os.system ("cls")
cash=1500.00
op=1
def simulator():    
    print ("\tSIMULADOR DE CAIXA ELETRÔNICO\n\n")
def balance():
    print ("saldo atual: {}".format(cash))
    return -1
def sucessfull():
    os.system ("cls")
    simulator()
    print ("\nOPERAÇÃO REALIZADA COM SUCESSO!!!")
    x=balance()
def withdrawal ():
    x=balance()
    while x<0 or x>=cash:
        print ("INSIRA O VALOR PARA SAQUE:")
        x=float(("(para cancelar a operação, digite 0)\n"))
    return cash-x
def payment ():
    x=balance()
    print ("INSIRA O VALOR PARA DEPÓSITO:")
    x=float (input ("(para cancelar, digite 0)\n"))
    return cash+x
simulator()
while op!=0:
    op=int(input("ESCOLHA UMA OPERAÇÃO:\n1-SALDO\n2-SAQUE\n3-PAGAMENTO\n0-SAIR\n"))
    if op<0 or op>3
        print ("insira somente uma das opções de entrada:\n")
    elif op==1:
        os.system("cls")
        simulator()
        e=balance()
        sucessfull()
    elif op==2:
        
