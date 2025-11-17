#Definimos la variable y la lista
Inventario=[]
check=True
def agregar_productos():        #Abrimos la funcion 
    check=True
    Ingre=input("Quieres ingresar un producto (s/n)")
    while Ingre == "s":
        nombre=input("Ingresa el nombre producto ->")
        break
    
    while check:
            try:
                precio=float(input("Ingresa el precio ->"))
                if precio >0:
                    break                                       #Dentro de la funcion hacemos varios bucles con while para                                                                #
                else:                                           #que se repitan las variables que le preguntan al
                    print("Ingresa un valor valido")            #usuario x dato y cerramos los bucles con break
            except:
                print("Ingrese un valor valido")

    while check:
        try:
            cantidad=int(input("Ingresa una cantidad ->"))      #Utilizamos el try y except para que no nos lleve
            if cantidad >0:                                     #a un error de la terminal
                break
            else:
                print("Cantidad valida")
        except:
            print("Ingresa un valor valido")
    #Abrimos la biblioteca y le definimos su clave
    Producto={"Nombre": nombre,"Precio": precio,"Cantidad": cantidad}   #le permitimos al usuario ingresar su valor
    Inventario.append(Producto)                                         #Abrimos la lista para ingresar los datos


def mostrar_inventario():           #Abrimos otra funcion
    for producto in Inventario:     #En ella hacemos que se recorra la lista("Inventario")
        print(producto)
    if len(Inventario) ==0:         #Y con el len hacemos que revise la cantidad de "objetos" que hay
        print("Lista vacia")        #en la biblioteca y si es igual a cero mostrar "lista vacia"

def calcular_estadisticas():
    while check:
        try:     
            total = sum(float(Producto['Precio'] * Producto['Cantidad']) for Producto in Inventario) 
            to_inven=len(Inventario)
            print(f"El total de objetos del inventario es--> {to_inven} \nEl valor del inventario es--> {total}")  #En esta funcion se calcula el valor total del inventario
            break                                                                                                  #y el valor total de "Objetos" del inventario
        except:
            print("Ingresa un valor valido")
            


while check:
    try: 
        Entrar=int(input("'''(1) Agregar producto'''\n   (2) Ver inventario  \n   (3) Calcular estadisticas  \n   (4) Salir\n       -->"))
        if Entrar == 1:
            agregar_productos()
        if Entrar == 2: 
            mostrar_inventario()                        #En este while hacemos que funcione como una lista para entrar
        if Entrar == 3:                                 #a las diferentes funciones utilizando el if  y el ==                
            calcular_estadisticas() 
        if Entrar ==4:
            break   
    except:
        print("Ingresa un valor valido")
