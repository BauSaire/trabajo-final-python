class Quiniela:
    operacion = int
    nombre = str
    dni = str
    apuesta = str   
   #metodo que se ejecuta solo una vez en la vida del programa
    def inicio(self):
        print("\n\n==================================================\n\n")
        print("          Bienvenido a QUINIBAU quinielas")
        print("\n\n==================================================\n\n")  
        print(" Por favor, siga las instrucciones.\n")

        self.nombre= input("Ingrese su nombre: ")
        self.dni= input("Ingrese su DNI: ")
    def menu(self):
        print("\n\n\n================QUINIBAU================")
        print("  1. Quiniela")
        print("  2. Quini 6")
        print("  3. Comprobar si la apuesta es ganadora")
        print("  4. Arqueo de caja")
        print("  5. Salir")
        print("========================================\n\n\n")  
    def operar(self):
        opciones = {
        1: Quiniela.quiniela,
        2: Quiniela.quini6,
        3: Quiniela.comprobar,
        4: Quiniela.arquear,
        5: Quiniela.salir
        }
        self.operacion = int(input("Opción: "))
        opciones.get(self.operacion)(self.nombre,self.dni)

   #Los metodos eleccionables son estaticos para poder llamarlos con el diccinario dentro del metodo operar
    @staticmethod   
    def quiniela(nombre,dni):
        print("\n\n================QUINIELA================")
        print(f"    Apostador: {nombre}  {dni}")
        print("========================================\n\n")  


        apuesta = input("Ingrese un numero entre 1 o 4 cifras: ")
        if len(apuesta) < 1 or len(apuesta) > 4:
            print("La apuesta debe tener entre 1 y 4 cifras")
            return
        input("Monto($): ")

    @staticmethod    
    def quini6():
        print("quini6")
    @staticmethod    
    def comprobar():
        print("Comprobar")
    @staticmethod    
    def arquear(): 
        print("arqueo")
    @staticmethod        
    def salir():
        return ""



if __name__ == "__main__":
    quiniela = Quiniela()
    quiniela.inicio()
    quiniela.menu()
    quiniela.operar()
    while(quiniela.operacion!=5):
        quiniela.menu()
        quiniela.operar()
