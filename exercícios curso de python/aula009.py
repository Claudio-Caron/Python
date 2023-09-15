#listas/array, incrementações, tamanho, alterações e impressões
suplementos=["creatina", "whey", "omg3", "beta-alanina", "vitamina"]
print ("\nsuplementos da lista:", suplementos, "\nquantidade:", len(suplementos))
print ("\nlista, item 3:", suplementos[2], "\n")
suplementos[2].upper()
print ("alterando posição e usando função upper:", suplementos[2])
suplementos.append("maltodextrina")
suplementos.append("Diana")
suplementos.append("Deca")
suplementos.append("Dura")
print ("\nalterado pela função append:", suplementos[6], "\n")
print ("\nsuplementos da lista:", suplementos, "\nquantidade:", len(suplementos))
suplementos.pop()
print ("\nSem o último termo(removido pela função pop):\n", suplementos)
del suplementos[2]
print ("\nSem o termo 3-'OMG3'(removido pela função del):\n", suplementos)
suple=suplementos
print ("\nvariavel copiada ==", suple, "\n")
suplementos.clear()
print ("\nelementos removidos?(em boleano feito pelo clear): ", bool(suplementos), "\n")