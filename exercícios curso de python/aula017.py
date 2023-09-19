#dictionary -> key(field, become the value of index)/ variable value
import os
os.system("cls")
dictionary={"name": "Cláudio",
            "years_old":18,
            "hobbie":"I love workout",
            "where_you_live":"Shiny_River",
            "favorite_food": "burguer and fries potatoes"
            }
for x in dictionary:
    print (x, "-> ", dictionary[x])#x print from field because get value of index
print ("\nFIM_ALG")