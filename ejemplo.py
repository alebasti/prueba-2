

menu = 1

while menu == 1:
    print("1) Opcion 1")
    print("2) Opcion 2")
    print("3) Opcion 3")
    print("4) Opcion 4")
    print("5) Opcion 5")
    while True:
        try:
            op1=int(input("Ingrese una opcion: "))
            if 0 < op1 < 6:
                break
            else:
                print("Opcion Invalida")
        except:
            print("Error. Debe ingresar solo numeros. Intente nuevamente") 
    if op1 == 1:
        print("estoy en la opcion 1")
    elif op1 == 2:
        print("estoy en la opcion 2")
    elif op1 == 3:
        print("estoy en la opcion 3")
    elif op1 == 4:
        print("estoy en la opcion 4")
    else:
        print("Adios")
        menu = 2