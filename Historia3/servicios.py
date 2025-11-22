from archivos import*

inventario=[]
check=True

#Hacemos el agregar con whiles en cada variable con sus condicionales
def agregar():
    nombre=str(input("Ingresa el nombre del producto\n -->"))
    while not nombre:
        print("Nombre invalido")
        nombre=input("Ingresa el nombre del producto\n -->")
    
    while check:
        try:
            precio=float(input("Ingresa el precio\n -->"))
            if precio <=0:
                print("Ingresa un precio valido")          #Utlizamos el try y except para posibles errores
            else:
                break   
        except:
            print("Caracter invalido")
        
    while check:
        cantidad=(input(f"Ingresa la cantidad de {nombre}\n -->"))
        if not cantidad.isdigit():
            print("Solo numeros")
        else:
            cantidad=int(cantidad)
            break
        
    biblioteca={"Nombre": nombre, "Precio": precio,"Cantidad": cantidad }   #Abrimos un diccionario y lo metemos a una lista
    inventario.append(biblioteca)        

def mostrar():
    if not inventario:                                          #Utilizamos un condicional por si no hay nada en la lista imprima el mensaje
        print("Inventario vacio")
                                                                                                            
    for mostrar in inventario:                                                     
        print(f"--/Nombre:{mostrar["Nombre"]}|Precio:{mostrar["Precio"]}|Cantidad:{mostrar["Cantidad"]}/--") #usamos un for para que recorra la lista con un iterador y llamamos variables

def buscar():                                                   #Usamos mas for para que recorra la lista y pase a la siguiente linea solo si encuentra la clave "Nombre" en ella 
    try:    
        busca=str(input("Ingresa el nombre del producto\n -->"))    
        located=False
        for buscar in inventario:
            if busca == buscar["nombre"]:
                located==True 
                print(f"--/Nombre:{buscar["Nombre"]}|Precio:{buscar["Precio"]}|Cantidad:{buscar["Cantidad"]}/--")    
        if located == False:
            ("No se encontro el producto")
    except:
        print("Caracter invalido")

def update():               
    try:
        located=False
        buscar=input("¿Que quieres actualizar?")
        for actualizar in inventario:
            if buscar ==actualizar["nombre"]:
                cambiar=input("Quires actualizar:\n (1)nombre \n (2)Precio \n (3)Cantidad \n --> ")
                located=True
                if cambiar =="1":
                    new_n=input("Ingresa el nuevo nombre \n -->")
                    actualizar["Nombre"]=new_n
                    print(f"Nombre cambio a {new_n} ")
                elif cambiar =="2":
                    new_p=float(input("Ingresa el nuevo precio\n -->"))    
                    actualizar["Precio"]=new_p
                    print(f"Precio cambio a {new_p} ")
                    if new_p <=0:
                        print("Ingresa un precio valido")
                elif cambiar =="3":
                    new_c=int(input("Ingresa la nueva cantidad\n -->"))
                    actualizar["Cantidad"]=new_c
                    print(f"Cantidad cambio a {new_c}")
                    if new_c <=0:
                        print("Ingres una cantidad valida")      
        if located == False:
            print("No se encontro el producto")       
    except:
        print("Caracter invalido")

def detele():
    busca=str(input(" Nombre de lo que quieres eliminar \n -->"))       
    located=False
    for detele in inventario:
        if busca == detele["Nombre"]:
            inventario.remove(detele)
    if located == False: 
        print("No se encontro el producto")
    
def stats():
    
    if not inventario: 
        print("No hay productos en el inventario") 
        return
    
    unidadesTotales = sum(i['Cantidad'] for i in inventario)
    ValorProductos = sum(i['Precio'] * i['Cantidad'] for i in inventario)
    ProductoCaro = max(inventario, key=lambda p: p["Precio"])
    mayorCantidad = max(inventario, key=lambda p: p["Cantidad"])  
    print(f"Unidades : {unidadesTotales} | valor total de los productos: {ValorProductos} \nProducto mas caro:  {ProductoCaro["Nombre"]} precio {ProductoCaro["Precio"]} | mayor cantidad de productos: {mayorCantidad["Nombre"]} cantidad {mayorCantidad["Cantidad"]}")










#Hacemos el menu con while y condicionales

def menu():
    while check:
        ingresar=(input("/////////////////////////////\n (1)Agregar \n (2)Mostrar \n (3)Buscar \n (4)Actualizar \n (5)Eliminar \n (6)Estadísticas \n (7)Cargar CSV \n (8)Guardar CSV \n (9)Salir  \n///////////////////////////// \n -->"))
        if ingresar =="1":
            agregar()
        elif ingresar =="2":
            mostrar()
        elif ingresar =="3":
            buscar()
        elif ingresar =="4":
            update()
        elif ingresar =="5":
            detele()
        elif ingresar =="6":
            stats()
        elif ingresar =="7":
            cargarcsv()
        elif ingresar =="8":
            guardarcsv()
        else:
            break
