#Definimos las variables

cantidad=0
Precio=0
check = True
Nombre = (input("Ingresa el nombre del producto "))

while check:   #Utilizamos while para tener un bucle con condicion
      try:
        cantidad = int(input(f"que cantidad de {Nombre} quieres llevar: " )) 
        while cantidad <=0:        #utilizamos otro while ponemos la condicion
         cantidad=int(input("Ingresa numero valido "))
        check =False
      except:  #Try y except nos sirve para atrapar un error dentro del bucle y que no llegue al syntaxis
       print("Ingresa un valor valido")
     
        


        
while check == False: #Utilizamos el mismo bucle metiendo la variable precio adentro
      try:
       Precio = float(input("Ingresa el precio"))    #Le preguntamos al usuario
       while Precio <=0:                             #Usamos el mismo bucle para sea igual o menor a cer se repita
         Precio=float(input("Ingresa un valor valido")) 
       check = True                                  #Cambiamos el valor de check para que el bucle termine
      except:
       print("Ingresa un valor valido")

print(f"{Nombre}|Precio:{Precio}|Cantidad:{cantidad}|Total:{Precio*cantidad}")   #Se muestra el resultado 

  
#Este programa es para calcular el precio de un producto ingresado por el usuario mostrando su nombre,precio,cantidad y el total
   
