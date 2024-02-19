import pickle

# Crear la clase  
class Vehiculos():

    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

    def arrancar(self):
        self.enmarcha=True
    
    def acelerar(self):
        self.acelera=True
    
    def frenar(self):
        self.frena=True
    
    def estado(self):
        print("\nMarca: ",self.marca, "\nModelo: ", self.modelo,"\nEn marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera
            , "\nFrenado:  ", self.frena)

#Crear objetos 

coche1=Vehiculos("Ford", "Mustang")
coche2=Vehiculos("Subaru", "BRZ")
coche3=Vehiculos("Nissan", "GTR")

# Serializar objetos

coches=[coche1, coche2, coche3]

#Creamos el archivo binario

fichero = open("losCoches", "wb")

# Volcamos los objetos

pickle.dump(coches, fichero)
fichero.close()
del (fichero)

# Aperturamos el volcado

ficheroApertura = open("losCoches", "rb")
misCoches=pickle.load(ficheroApertura)
ficheroApertura.close()

for c in misCoches:
    print("***********************")
    print(c.estado())
