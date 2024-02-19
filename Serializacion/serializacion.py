import pickle

lista_nombres=["Pedro", "Ana", "Mariana", "Grecia"] # Lista que queda en el disco duro 
fichero_binario=open("lista_nombres", "wb") # Crear el fichero, esto queda en la memoria
pickle.dump(lista_nombres,fichero_binario) #Volcar la lista de nombres
fichero_binario.close() # Cerrando el fichero 
del (fichero_binario) # Liberando la memoria 