import random
import os
os.system ("cls")
x=random.randrange(1,10)
c=0
print ("Você tem 3 tentativas totais")
for n in range(0,10):
    y=int (input("advinhe o número de 1 a 10:"))
    if x==y :
        os.system ("cls")
        print ("Parabéns!!! voçê acertou o número\n")
        c+=1
        break
    else:
        os.system ("cls")
        print ("número incorreto")
        if x>y:
            print ("O número digitado é menor que o valor procurado")
        else:
            print ("O número digitado é maior que o valor procurado")
if c==0:
    print ("\nVOCÊ ESGOTOU TODAS AS TENTATIVAS")
print ("\nFim_alg")