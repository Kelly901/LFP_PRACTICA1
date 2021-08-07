from Archivo import Archivo
from Operaciones import Operaciones
class Menu:
    archivo=Archivo()
    def menu(self):
        print(">>>>>>>>>>>>MENU PRINCIPAL<<<<<<<<<<<<<")
        print("\n1.Cargar Achivo")
        print("2.Mostrar Reporte")
        print("3.Exportar Reporte")
        print("4.Salir")
        opcion=input("Ingrese una opcion por favor->")
        self.escoger_opcion(opcion)
    def escoger_opcion(self,opcion):

        if opcion=="1":
            print("Opcion 1")
            self.archivo.archivo()
            self.menu()
        elif opcion=="2":
            print("_________________________________________")
            print("Opcion 2")
            self.archivo.mostrar()

            print("\n___________________________________\n")
            self.menu()
        elif opcion=="3":
            print("Opcion 3")
            operacion=Operaciones()
            operacion.generar_reporte()
            
            print("\n___________________________________\n")
            self.menu()
        elif opcion=="4":
            print("Opcion 4") 
        else:
            print("La opción ingresada es incorrecta.\n Vuelva a intertarlo....")
            self.menu()
        
m=Menu()
m.menu()    
            
