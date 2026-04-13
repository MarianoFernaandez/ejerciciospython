lista = ["pepe", "carlos", "juan","alejandro"]
print("-------------------------------------------------")
print("Aprete 1 si quiere agregar algo a la lista")
print("Aprete 2 si quiere borrar algo de la lista")
print("Aprete 3 si quiere modificar algo de la lista")
print("Aprete 4 si quiere ver algo de la lista")
print("-------------------------------------------------")

salida = input("ingrese su eleccion:")
print (salida)

while(salida != "0"):

    if salida == "1":
        variable = input()
        lista.append(variable)
        print("Se agrego correctamente")

    if salida == "2":
        variable = input()
        variable = int()
        lista.pop(variable)
        print(lista)

    if salida == "3":
        print(lista)
        print("Que elemento desea modificar?")
        variable = input()
        indiceborrado = lista.index(variable)
        variable = int()
        lista.pop(variable)
        print("Que elemento desea guardar?")
        variable = input()
        lista.insert(indiceborrado, variable)

    if salida == "4":
        variable = input()
        lista.index(variable)
        print(lista.index(variable))

    print("Aprete 1 si quiere agregar algo a la lista")
    print("Aprete 2 si quiere borrar algo de la lista")
    print("Aprete 3 si quiere modificar algo de la lista")
    print("Aprete 4 si quiere ver algo de la lista")
    salida = input("")

print(lista)
        
