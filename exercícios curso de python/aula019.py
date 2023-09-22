#funções(procedimentos)
import os
os.system ("cls")
x=-1
y=-1
def situação (a,b):
    a=(a+b)/2
    print ("A nota final do aluno é:", a)
    print ("situação atual do aluno: ")
    if a<6:
        print ("REPROVADO")
    else :
        print ("APROVADO")
while x<0 or x>10 or y<0 or y>10:
    x=float(input("\ninsira a primeira nota\n"))
    y=float(input("\ninsira a segunda:\n"))
    if x<0 or x>10 or y<0 or y>10:
        os.system ("cls")
        print ("voce inseriu uma nota inválida, insira novamente")
os.system ("cls")
situação(x,y)
print ("\nfim_alg")