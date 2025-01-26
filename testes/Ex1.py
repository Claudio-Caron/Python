r=1
valoresR = []
while r!=0:
    print ("Insira o valor : ")
    r=float (input())
    if (r!=0):
        valoresR.append(r)
print("Valor 0 inserido")
for i in valoresR:
    r+=i
print ("Media : ", r/valoresR.count)
