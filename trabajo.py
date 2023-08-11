from random import randint
import os
import datetime
class Quiniela:
    operacion = int
    nombre = str
    dni = str
    nroSorteados = [] 
    nroSorteadosQUini =[]
    apuestas = []
    montoTotal = 0
    comprobantes = 0
   #metodo que se ejecuta solo una vez en la vida del programa
    def inicio(self):
        #Limpia la consola
        os.system('cls')
        print("\n\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")
        print("   Bienvenido a QUINIBAU agencia de quiniela")
        print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")  
        print(" Por favor, siga las instrucciones.\n")

        Quiniela.nombre= input("Ingrese su nombre: ")
        Quiniela.dni= input("Ingrese su DNI: ")
    def menu(self):
        os.system('cls')
        print("\n================QUINIBAU================")
        print("  1. Quiniela")
        print("  2. Quini 6")
        print("  3. Comprobar si la apuesta es ganadora (Sortear)")
        print("  4. Arqueo de caja")
        print("  5. Salir")
        print("========================================\n")  
    def operar(self):
        # diccionario para llamar a los metodos que se eligen en el menu
        opciones = {
        1: Quiniela.quiniela,
        2: Quiniela.quini6,
        3: Quiniela.comprobar,
        4: Quiniela.arquear,
        5: Quiniela.salir
        }
        
        self.operacion = int(input("Opción: "))
        # LLama al metodo correspondiente sino llama al metodo error
        opciones.get(self.operacion, Quiniela.error)()

   #Los metodos eleccionables son estaticos para poder llamarlos con el diccinario dentro del metodo operar
    @staticmethod     
    def quiniela():
        os.system('cls')
        print("\n\n********************************")
        print("            QUINIELA")
        print(f" {Quiniela.nombre}\n {Quiniela.dni}")
        print("********************************\n")  
        apuesta = input("Ingrese un numero entre 2 o 4 cifras: ")
        monto = float(input("Ingrese el monto de la apuesta($): "))
        Quiniela.montoTotal += monto
        ## while para que el usuario si o si ponga un numero de 1 a 4 digitos 
        while len(apuesta) < 2 or len(apuesta) > 4:
            print("La apuesta debe tener entre 2 y 4 cifras")
            apuesta = int(input("Ingrese un numero entre 2 o 4 cifras: "))
            monto = float(input("Ingrese el monto de la apuesta: "))
        hora = datetime.datetime.now()
        Quiniela.generarTicket("Quiniela",apuesta,monto,hora)

            
     

    @staticmethod    
    def quini6():
        nrosQuini = []
        primerNro= 0
        sengundoNro = 0
        os.system('cls')
        print("\n\n********************************")
        print("            Quini6")
        print(f" {Quiniela.nombre}\n {Quiniela.dni}")
        print("********************************\n")  
        print("Desea generar apuesta aleatoria?")
        print("1. Si")
        print("2. No")
        opcion = int(input("Opción: "))
        while opcion < 1 or opcion > 2:
            print("Opcion incorrecta")
            opcion = int(input("Opción: "))
        if opcion == 1:
         
            nrosQuini = Quiniela.sorteadorQuini6()
        if opcion == 2:
            for i in range(6):
                print("Ingresar numero entre 01 y 45")
                resultado = input(f"Ingrese el {i+1}. numero: ") 
                if resultado in nrosQuini:
                    i -= 1
                    print("El numero ya fue ingresado")
                else:
                    nrosQuini.append(resultado)


        print("Apuesta generada: ",nrosQuini)
        monto = float(input("Ingrese el monto de la apuesta($): "))
        Quiniela.montoTotal += monto
        hora = datetime.datetime.now()
        Quiniela.generarTicket("Quini6",nrosQuini,monto,hora)

    @staticmethod    
    def comprobar():
        os.system('cls')
        print("\n\n********************************")
        print("            SORTEO")
        print("********************************\n")
        Quiniela.sortearNumeros()
        Quiniela.ganadores("Quiniela")
        Quiniela.ganadores("Quini6")
        if not Quiniela.ganadores() :  # si no se gana nada devuelve un false
            print("No haz ganado nada")
        Quiniela.nroSorteados = []
        Quiniela.apuestas = []
        input("Presione enter para continuar")

    @staticmethod    
    def arquear(): 
        neto = round(Quiniela.montoTotal-Quiniela.montoTotal* 0.47)
        print("-------------------------------------------\n")
        print(f"Monto en apuestas: ${Quiniela.montoTotal}")
        print(f"-${round(Quiniela.montoTotal* 0.47,2)} retención del Estado")

        print(f"Ganacia neta: ${neto}")
        print("\n-------------------------------------------")

        Quiniela.montoTotal = 0
        input("Presione enter para continuar")

    @staticmethod
    def ganadores(juego):
        gano =False
        for i in range(len(Quiniela.apuestas)):
            for j in range(len(Quiniela.nroSorteados)):
                if Quiniela.apuestas[i]["apuesta"] in Quiniela.nroSorteados[j]:
                    print("__________________________________________________________")
                    print(f"Tcket Nro. {Quiniela.apuestas[i]['comprobante']} ganador")
                    print(f"Apuesta al: {Quiniela.apuestas[i]['apuesta']}")
                    print(f"Número ganador: {Quiniela.nroSorteados[j]}")
                    print(f"Monto ganado: ${ Quiniela.apuestas[i]['monto']*500}")
                    print("__________________________________________________________")
                    gano = True
        return gano
                
    @staticmethod
    def generarTicket(juego,apuesta,monto,hora):
        os.system('cls')
        Quiniela.comprobantes += 1
        Quiniela.apuestas.append({"apuesta":apuesta,"monto":monto,"hora":hora,"comprobante":Quiniela.comprobantes})
        print("\n_________QUINIBAU_________")
        print(f"\n{juego}\n{hora}\nNro. comprobante:{Quiniela.comprobantes}\n{Quiniela.nombre}\n{Quiniela.dni}\nNro. de apuesta: {apuesta}\nTOTAL: ${monto}")
        print("___________________________\n")  

        input("Presione enter para continuar")
    @staticmethod        
    def salir():
        return 
    
    @staticmethod
    def sortearNumeros():
        os.system('cls')
        # Sorteo del quini
        Quiniela.nroSorteadosQuini6 = Quiniela.sorteadorQuini6()
        
        print("\n---------Sorteo quini6------------\n")
        for i in range(len(Quiniela.nroSorteadosQuini6)):
         print(f"{Quiniela.nroSorteadosQuini6[i]}",end=" ")
        
        print("\n\n---------Sorteo quiniela------------\n")
        # Sorteo de la quiniela
        for i in range(20):
         nro = ""
         for j in range(4):
               nro+= str(randint(0,9))
         Quiniela.nroSorteados.append(nro)
        
        for i in range(len(Quiniela.nroSorteados)):

            if i <  10:
                if i % 2== 0:
                    print(f"0{i+1}. {Quiniela.nroSorteados[i]}",end=" ")
                else:
                    print(f"0{i+1}. {Quiniela.nroSorteados[i]}")
            else:
                if i % 2== 0:
                    print(f"{i+1}. {Quiniela.nroSorteados[i]}",end=" ")
                else:
                    print(f"{i+1}. {Quiniela.nroSorteados[i]}")
        print("----------------------------------\n")       
          
           
         
        
        
    @staticmethod
    def error():
        print("Opcion incorrecta")
        input("Presione enter para continuar")
    @staticmethod
    def sorteadorQuini6():
        nrosQuini = []

            #no juzguen mis metodos sino mis resultados xD
        for i in range(6):
            resultado = Quiniela.nroAleatoriosNoRepetidos()
            while resultado in nrosQuini:
                 resultado= Quiniela.nroAleatoriosNoRepetidos()
            nrosQuini.append(resultado)
        return nrosQuini
    @staticmethod
    def nroAleatoriosNoRepetidos():
            for i in range(6):
             primerNro = randint(0,4)
             if primerNro == 4:
                 sengundoNro = randint(0,5)
             if primerNro == 0:
                 sengundoNro = randint(1,9)
             else: 
                 sengundoNro = randint(0,9)

             return str(primerNro)+str(sengundoNro)
if __name__ == "__main__":
    quiniela = Quiniela()
    quiniela.inicio()
    quiniela.menu()
    quiniela.operar()
    # while para que el programa se ejecute hasta que el usuario elija la opcion salir
    while(quiniela.operacion!=5):
        quiniela.menu()
        quiniela.operar()
