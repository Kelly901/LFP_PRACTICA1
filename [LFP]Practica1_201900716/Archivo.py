from tkinter import filedialog as FileDialog
from GuardarDatos import GuardarDatos
from Operaciones import Operaciones
guardar=GuardarDatos()
operacion=Operaciones()
parametro=""
class Archivo:
    contenido=""
    def archivo(self):
        fichero=FileDialog.askopenfilename(title="Abrir un fichero")
        abrir=open(fichero,'r')
        self.contenido=abrir.read()
          
    def mostrar(self):
        c=self.contenido.split("\n")
        
        print("\nContenido:\n",self.contenido)

        #print(c)
        cadena=""
        for i in c:
            
            lista=i.split("\n")
            
            if lista[0]!="":
                for li in lista:
                    cadena+=li

        print(cadena)
        #Nombre

        listaNombre=cadena.split("{")
        nombre1=listaNombre[0]
        print("Nombre",nombre1)
        n=nombre1.split("=")
        print("n",n)
        nombre=n[0]
        

        #Cursos
        listaCurso=listaNombre[1].split("}")
        #print("\nlista de cursos\n",listaCurso) 
        cursos=listaCurso[0]
        prueba=cursos.replace("<","")
        prueba2=prueba.replace(">","")
        #print(prueba2)
        prueba3=prueba2.split(",")
        print(prueba3)
        print("___________________________________")

        for i in prueba3:

           cursito=i.split(";")
           student=cursito[0].split("\"")
           nota=cursito[1].replace(" ","")
           #print("->"+student[1]+"<-"+"Nota:"+nota)
           guardar.guardarDatos(student[1],nota)
        guardar.imprimir()   


        #PARAMETRO
        parametros=listaCurso[1]
        self.parametro=parametros.replace(" ","")
        print("___________________________\n")
        print("Nombre del Curso:->"+nombre+"")
        GuardarDatos.nombreCurso.append(nombre)
        print("\n->"+self.parametro+"<-.")
        
        if "ASC"in self.parametro:
            print("\nOrden Ascendente")     
            operacion.ordenamiento_ascendete()
            print("__________________________")
        #Descendente
        if "DESC"in self.parametro:
            print("Orden Descendete")     
            operacion.ordenamiento_descendente()
            print("__________________________")
        
        #Promedio de los estudiantes
        if "AVG"in self.parametro:
            print("Promedio de los estudiantes del curso")     
            operacion.mostrar_promedio()
            print("__________________________")

        #Minino
        if "MIN"in self.parametro:
            print("Nota MINIMA")
            operacion.mostrar_notaMin()
            print("__________________________")
        #Minino
        if "MAX"in self.parametro:
            print("Nota MAXIMA")
            operacion.mostrar_notaMax() 
            print("__________________________")   
        #Cantidad de estudiantes aprobados
        if "APR"in self.parametro:
            print("LISTADO DE ESTUDIANTES APROBADOS\n")
            operacion.mostrar_aprobados()
            print("__________________________")
        
        #Cantidad de estudiantes reprobados
        if "REP"in self.parametro:
            print("LISTADO DE ESTUDIANTES Reprobados\n")
            operacion.mostrar_reprobados()
            print("__________________________")
        

