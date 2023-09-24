import os
import time
x='1'
os.system ("cls")
while x!='*' or '/' or '+' or '-':
    x=str(input("insira o operador:\n\t'*'  '/'  '+'  '-'\n"))
    if x!='*' or '/' or '+' or '-':
        os.system ("cls")
        print ("\t\tinsira um operador válido!\n")
a=float(input("digite o primeiro operando\n"))
b=float(input ("digite o segundo\n"))
if x=='*':
    print ("\nresuldo =", (lambda q,w:w*q)(a,b))
elif x=='/':
    while b==0:
        os.system ("cls")
        print("digite um denominador(2° solicitado) difente de zero\n")
        a=float(input("digite um operador\n"))
        b=float(input ("digite outro\n"))
    print ("\nresuldo =", (lambda q,w:w/q)(a,b))

elif x=='+':
    print ("\nresuldo =", (lambda q,w:w+q)(a,b))
elif x=='-':
    print ("\nresuldo =", (lambda q,w:w-q)(a,b))
print ("\n\nfim_alg\n")
