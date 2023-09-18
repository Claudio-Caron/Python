#input e comando cls
#bolei um exercício básico para treinar
import os
os.system ('cls')
for x in range (1,10):
    x=1
    op=str (input ("escolha o operador(para encerrar, digite algo diferente)[ + - / * ]\n"))
    if op!='+'and op!='-' and op!='/' and op!='*' :
        print ("comando de saída")
        break
    num1=float (input ("digite o primeiro operando:\n"))
    num2=float (input ("digite o segundo operando\n"))
    if op=='+':
        num1+=num2
    elif op=='-':
        num1-=num2
    elif op=='/':
        if num2==0:
            print ("operando inválido\n")
            continue
        num1=num1/num2
    elif op=='*':
        num1=num1*num2
    print ("resultado=", num1, "\n")
print ("fimalg\n\n")
