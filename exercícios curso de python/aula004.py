#funções tipo set e range , list/array, dictionary, tuplas
y=("testecampo0", "posição2", "posição 3", 3, 3.00)#Tuplas(não ateram o valor)
z=[12, 12.3, "posição 3", True]#array/list
a={
    "campo01" : "dicionariocampo01",
    "campo02" : "dicionariocampo02",
    "campo03" : "dicionariocampo03",
    "campo04" : 14.5
}
x={1, 3, 5, 3, 6, 8, 9, 9, 9, 3, 3, 2, 7}#tipo set
b= range(0,50,1)
print ("array campo 02: ", z[1])
print ("Tupla campo 1: ", z[0])
print ("dictionary campo 4: ", a["campo04"])
print ("retorno do set :(1,3,5,3,6,8,9,9,9,3,3,2,7)", x)
print ("retorno da range/campo 49:", b[48])