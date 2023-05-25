#Valor tratamiento
car=250000
imp=475000
ort=800000
#Contadores
contcar=0
contimp=0
contort=0
#Descuentos
dcto10=0
dcto15=0
dcto5=0
dcto=0
#acumuladores
totalc=0
subtotal=0

menu = 1
while menu == 1: #menu principal  
    print("_"*50)
    print("\t \tEl Diente de Oro")
    print("_"*50) 
    print("1)Cotización")
    print("2)Renunciar")
    print("3)Salir")
    while True:
        try:
            op1=int(input("Ingrese una opcion: "))
            if 0 < op1 < 4:
                break
            else:
                print("Opcion Invalida!")
        except:
            print("Error. Ingrese solo numeros. Intente nuevamente")
    if op1 == 1:   #menu de cotizaciones  
        while True:
            print("_"*50)
            print("\t \tCotizacion")
            print("_"*50)
            print("1)Ofrecer Tratamientos y Calcular subtotal")
            print("2)Desplegar el total de la cotización")
            print("3)Terminar y salir")
            while True:
                try:
                    op2=int(input("Ingrese una opcion: "))
                    if 0 < op2 < 4:
                        break
                    else:
                        print("Opcion Invalida!")
                except:
                    print("Error. Ingrese solo numeros. Intente nuevamente")
            if op2 == 1: #menu para agregar tratamientos
                while True:
                    print("_"*50)
                    print("\tAgregando Tratamiento(s)")
                    print("_"*50)
                    print("1)Carillas Porcelana")
                    print("2)Implantes Dentales")
                    print("3)Ortodoncia Brackets")
                    print("4)Terminar y salir")
                    while True:
                        try:
                            op3=int(input("Ingrese una opcion: "))
                            if 0 < op3 < 5:
                                break
                            else:
                                print("Opcion Invalida!")
                        except:
                            print("Error. Ingrese solo numeros. Intente nuevamente")
                    if op3==1: #aqui acumulo tratamientos y sumo el total
                        totalc+=car
                        contcar+=1
                        print("Agrego 1 tratamiento de Carillas Porcelana")
                    elif op3 ==2:
                        totalc+=imp
                        contimp+=1
                        print("Agrego 1 tratamiento de Implantes Dentales")
                    elif op3==3:
                        totalc+=ort
                        contort+=1
                        print("Agrego 1 tratamiento de Ortodoncia Brackets")
                    else:
                        break
                while True:
                    dcto10=0
                    dcto15=0
                    dcto5=0
                    print("_"*50)
                    print("\tCalculando cotizacion")
                    print("_"*50)
                    print("Tiene algun descuento especial?")
                    print("1)Trabajador Auxiliar")
                    print("2)Trabajador Administrativo")
                    print("3)Trabajador Docente")
                    print("4)Ninguno")
                    while True:
                        try:
                            op4=int(input("Ingrese una opcion: "))
                            if 0 < op4 < 5:
                                break
                            else:
                                print("Opcion Invalida!")
                        except:
                            print("Error. Ingrese solo numeros. Intente nuevamente")
                    if op4==1: #Valido los descuentos
                        dcto15=(totalc*0.15)
                        print(f"El subtotal es de ${totalc} y tiene un descuento del 15%.")
                        break                    
                    elif op4==2:
                        dcto10=(totalc*0.10)
                        print(f"El subtotal es de ${totalc} y tiene un descuento del 10%.")  
                        break
                    elif op4==3:
                        dcto5=(totalc*0.05)
                        print(f"El subtotal es de ${totalc} y tiene un descuento del 5%.")  
                        break
                    else:
                        print(f"El subtotal es de ${totalc} y no tiene descuento.")  
                        break
            elif op2==2: #Imprimo cotizaciones
                print("_"*50)
                print("\t \tCotizacion")       
                print("_"*50)
                if contcar>0:
                    print(f"-->{contcar} tratamiento(s) Carilla Porcelana   ${contcar*car}") 
                if contimp>0:
                    print(f"-->{contimp} tratamiento(s) Implantes Dentales   ${contimp*imp}")    
                if contort>0:
                    print(f"-->{contort} tratamiento(s) Ortodoncia Brackets   ${contort*ort}")  
                print("_"*50)
                print(f"subtotal \t${totalc}")
                if dcto15>0:
                    print(f"Descuento 15% \t${round(dcto15)}")
                    dcto=dcto15
                elif dcto10>0:
                    print(f"Descuento 10% \t${round(dcto10)}")
                    dcto=dcto10
                elif dcto5>0:
                    print(f"Descuento 5% \t${round(dcto5)}")
                    dcto=dcto5
                print("_"*50)
                print(f"Total \t \t${round(totalc-dcto)}")
                print(f"Son 12 cuotas de: ${round((totalc-dcto)/12)}")
                print("Sonria Bonito!!!")
            else: #volver al menu
                print("Volviendo al menu principal")
                break
    elif op1==2: #Reinicio cotizaciones
        print("Eliminando cotizacion anterior...")
        totalc=0
        contcar=0
        contimp=0
        contort=0
        dcto10=0
        dcto15=0
        dcto5=0
        dcto=0
        subtotal=0
    else: #salir del programa
        print("Saliendo...") 
        menu=0     
