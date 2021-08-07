from Estudiante import Estudiante
class GuardarDatos:
    datos=[]
    parametro=[]
    nombreCurso=[]
    def guardarDatos(self,nombre,nota):
        self.datos.append(Estudiante(nombre,nota))

    def imprimir(self):
        for i in self.datos:
            print(i.nombre+",Nota:"+i.nota)
