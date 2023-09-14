#manipulações de string parte 01 e parte 02
curso=" Curso de Python "
print ("variavel inicial :", curso)
curso=curso.strip()
print ("usando strip:\n", curso, "\n")
curso=curso.replace("Python","C#")
curso=curso.upper()
curso="alteração com upper, replace e concatenação dentro da variável:\n"+ curso
print (curso)
curso=curso.split(" ")
print ("\nusando split: ", curso[2])