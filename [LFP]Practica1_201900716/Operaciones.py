import webbrowser
from GuardarDatos import GuardarDatos


class Operaciones:
    #Mostrar las notas de forma ascendente
    def ordenamiento_ascendete(self):
        aux = []
        aux2 = []
        numeros=[]
        numeros=self.bubbleSort_ascendete()
        GuardarDatos.parametro.append("ASC")
        longitud=len(numeros)
        # Comaparar las notas para obtener los nombres de los estudiantes
        for n in numeros:
            for dato in GuardarDatos.datos:
                if n == int(dato.nota):
                    #print(dato.nombre+" Nota: "+dato.nota)
                    aux.append(dato.nombre)

        # Eliminar datos repetidos
        for j in aux:
            if j not in aux2:
                aux2.append(j)
        #self.parametro+="<table><tr><td id=\"nombre\">Nombre</td><td id=\"nombre\">Nota</td></tr>"
        for i in range(longitud):
            print(aux2[i]+" Nota: "+str(numeros[i]))
           # self.parametro+="<tr><td id=\"nombre\">"+aux2[i]+"</td><td id=\"nota\"style=\"color: aqua;\">"+str(numeros[i])+"</td></tr>"
       # self.parametro+="</table>"

    # Metodo de ordenamiento de burbuja de forma ascendente
    def bubbleSort_ascendete(self):
        numeros = []
        
        
        for dato in GuardarDatos.datos:
            numeros.append(int(dato.nota))

        longitud = len(numeros)
        # Algoritmo  de ordenamiento Bubble Sort
        for i in range(1, longitud):
            for j in range(0, longitud-i):
                if numeros[j+1] < numeros[j]:
                    temp = numeros[j]
                    numeros[j] = numeros[j+1]
                    numeros[j+1] = temp
        return numeros
        
     #Mostrar las notas de forma ascendente
    def ordenamiento_descendente(self):
        GuardarDatos.parametro.append("DESC")
        aux = []
        aux2 = []
        numeros = []
        numeros=self.bubbleSort_descendente()
        longitud=len(numeros)
         # Comaparar las notas para obtener los nombres de los estudiantes
        for n in numeros:
            for dato in GuardarDatos.datos:
                if n == int(dato.nota):
                    #print(dato.nombre+" Nota: "+dato.nota)
                    aux.append(dato.nombre)
        # Eliminar datos repetidos
        for j in aux:
            if j not in aux2:
                aux2.append(j)

        for i in range(longitud):
            print(aux2[i]+" Nota: "+str(numeros[i]))
    # Metodo de ordenamiento de burbuja de forma descendente

    def bubbleSort_descendente(self):
        numeros = []
        
        # Obtener las notas
        for dato in GuardarDatos.datos:
            numeros.append(int(dato.nota))

        longitud = len(numeros)
        # Algoritmo de ordenamiento Bubble Sort de forma descendente
        for i in range(1, longitud):
            for j in range(0, longitud-i):
                if numeros[j+1] > numeros[j]:
                    temp = numeros[j+1]
                    numeros[j+1] = numeros[j]
                    numeros[j] = temp
        return numeros
       
    #Mostrar Promedio   
    def mostrar_promedio(self):
        GuardarDatos.parametro.append("AVG")
        print(self.obtener_promedio())
    # Promedio de los estudiantes del curso

    def obtener_promedio(self):
        numeros = []
        suma = 0
        promedio = 0
        # Obtener las notas
        for dato in GuardarDatos.datos:
            numeros.append(int(dato.nota))
        longitud = len(numeros)
        # Realizar el promedio
        for i in numeros:
            suma += i

        promedio = round(suma/longitud, 2)
        return promedio
    #Mostrar la nota maxima del curso
    def mostrar_notaMax(self):
        GuardarDatos.parametro.append("MAX")
        numeroMax=self.nota_maxima()
        for dato in GuardarDatos.datos:
            if numeroMax == int(dato.nota):
                print(dato.nombre+" Nota:"+dato.nota)
    # Obtener la nota máxima de los estudiantes del curso

    def nota_maxima(self):
        numeros = []
        for dato in GuardarDatos.datos:
            numeros.append(int(dato.nota))

        longitud = len(numeros)
        # Algoritmo de ordenamiento Bubble Sort de forma descendente
        for i in range(1, longitud):
            for j in range(0, longitud-i):
                if numeros[j+1] > numeros[j]:
                    temp = numeros[j+1]
                    numeros[j+1] = numeros[j]
                    numeros[j] = temp

        numeroMax = numeros[0]
        return numeroMax
    #Mostrar nota minima
    def mostrar_notaMin(self):
        GuardarDatos.parametro.append("MIN")
        numeroMin=self.nota_minima()
        for dato in GuardarDatos.datos:
            if numeroMin == int(dato.nota):
                print(dato.nombre+" Nota:"+dato.nota)
    # Obtener la nota minima de los estudiantes del curso

    def nota_minima(self):
        numeros = []
        for dato in GuardarDatos.datos:
            numeros.append(int(dato.nota))

        longitud = len(numeros)

        for i in range(1, longitud):
            for j in range(0, longitud-i):
                if numeros[j+1] < numeros[j]:
                    temp = numeros[j]
                    numeros[j] = numeros[j+1]
                    numeros[j+1] = temp

        numeroMin = numeros[0]
        return numeroMin
    #Mostrar estudiante aprobados
    def mostrar_aprobados(self):
        GuardarDatos.parametro.append("APR")
        suma = 0
        for dato in GuardarDatos.datos:
            if int(dato.nota) >= 61:
                print(dato.nombre+" Nota:"+dato.nota)
                suma += 1
        print("\nCantidad de estudiantes aprobados:"+str(suma))
    # Obtener el numero de estudiantes aprobados en el curso
    def numero_de_aprobados(self):
        
        suma = 0
        for dato in GuardarDatos.datos:
            if int(dato.nota) >= 61:
                
                suma += 1
        return str(suma)

    #Mostrar estudiantes reprobados
    def mostrar_reprobados(self):
        GuardarDatos.parametro.append("REP")
        suma = 0
        for dato in GuardarDatos.datos:
            if int(dato.nota) < 61:
                print(dato.nombre+" Nota:"+dato.nota)
                suma += 1
        print("\nCantidad de estudiantes reprobados:"+str(suma)) 
    # Obtener el numero de estudiantes reprobados en el curso

    def numero_de_reprobados(self):
        suma = 0
        for dato in GuardarDatos.datos:
            if int(dato.nota) < 61:
                #print(dato.nombre+" Nota:"+dato.nota)
                suma += 1
        return str(suma)


    def generar_reporte(self):
        print("hola",GuardarDatos.parametro)
        fi = open('Reporte.html', 'w')
        nombre=""
        nota=""
        ascendente=""
        descendente=""
        promedio=""
        notaMax=""
        general=""
        #Generar la tabla con los estudiantes y su nota
        for dato in GuardarDatos.datos:
            if int(dato.nota) >= 61:
                print(dato.nota)
                nombre+="<tr><td id=\"nombre\">"+dato.nombre+"</td><td id=\"nota\"style=\"color: aqua;\">"+dato.nota+"</td></tr>"
            if int(dato.nota)<61:
                nombre+="<tr><td id=\"nombre\">"+dato.nombre+"</td><td id=\"nota\"style=\"color: red;\">"+dato.nota+"</td></tr>"
        
        #Mostara segun el parametro
        for i in GuardarDatos.parametro:
            if i=="ASC":
                aux = []
                aux2 = []
                numeros=[]
                numeros=self.bubbleSort_ascendete() 
                longitud=len(numeros)
                # Comaparar las notas para obtener los nombres de los estudiantes
                for n in numeros:
                    for dato in GuardarDatos.datos:
                        if n == int(dato.nota):
                        #print(dato.nombre+" Nota: "+dato.nota)
                            aux.append(dato.nombre)

                        # Eliminar datos repetidos
                for j in aux:
                    if j not in aux2:
                        aux2.append(j)
                general+="<div><h2>Notas ordenadas de forma ascendente:</h2><table><tr><td id=\"nombre\">Nombre</td><td id=\"nombre\">Nota</td></tr>"
                for i in range(longitud):
                    if numeros[i] >= 61:
                        general+="<tr><td id=\"nombre\">"+aux2[i]+"</td><td id=\"nota\"style=\"color: aqua;\">"+str(numeros[i])+"</td></tr>"
                    if numeros[i] < 61:
                        general+="<tr><td id=\"nombre\">"+aux2[i]+"</td><td id=\"nota\"style=\"color: red;\">"+str(numeros[i])+"</td></tr>"
                general+="</table></div>"
            #Orden descendete
            if i=="DESC":
                aux = []
                aux2 = []
                numeros=[]
                numeros=self.bubbleSort_descendente() 
                longitud=len(numeros)
                # Comaparar las notas para obtener los nombres de los estudiantes
                for n in numeros:
                    for dato in GuardarDatos.datos:
                        if n == int(dato.nota):
                        #print(dato.nombre+" Nota: "+dato.nota)
                            aux.append(dato.nombre)

                        # Eliminar datos repetidos
                for j in aux:
                    if j not in aux2:
                        aux2.append(j)
                general+="<div><h2>Notas ordenadas de forma descendente:</h2><table><tr><td id=\"nombre\">Nombre</td><td id=\"nombre\">Nota</td></tr>"
                for i in range(longitud):
                    if numeros[i] >= 61:
                        general+="<tr><td id=\"nombre\">"+aux2[i]+"</td><td id=\"nota\"style=\"color: aqua;\">"+str(numeros[i])+"</td></tr>"
                    if numeros[i] < 61:
                       general+="<tr><td id=\"nombre\">"+aux2[i]+"</td><td id=\"nota\"style=\"color: red;\">"+str(numeros[i])+"</td></tr>"
                general+="</table></div>"
            #Promedio
            if i=="AVG":
                general+="<div><h2>Promedio de las notas:</h2><table><tr><td id=\"nombre\">Promedio</td><td id=\"nombre\"style=\"color: blum;\">"+str(self.obtener_promedio())+"</td></tr>"
                general+="</table></div>"
                
            #Nota maxima
            if i=="MAX":
                numeroMax=self.nota_maxima()
                general+="<div><h2>NOTA MAXIMA DEL CURSO:</h2><table><tr><td id=\"nombre\">Nombre</td><td id=\"nombre\">Nota</td></tr>"
                for dato in GuardarDatos.datos:
                    if numeroMax == int(dato.nota):
                        if numeroMax >= 61:
                            general+="<tr><td id=\"nombre\">"+dato.nombre+"</td><td id=\"nota\"style=\"color: aqua;\">"+dato.nota+"</td></tr>"
                        if numeroMax < 61:
                            general+="<tr><td id=\"nombre\">"+dato.nombre+"</td><td id=\"nota\"style=\"color: red;\">"+dato.nota+"</td></tr>"
                general+="</table></div>"
            #Nota minima
            if i=="MIN":
                numeroMin=self.nota_minima()
                general+="<div><h2>NOTA MINIMA DEL CURSO:</h2><table><tr><td id=\"nombre\">Nombre</td><td id=\"nombre\">Nota</td></tr>"
                for dato in GuardarDatos.datos:
                    if numeroMin == int(dato.nota):
                        if numeroMin >= 61:
                            general+="<tr><td id=\"nombre\">"+dato.nombre+"</td><td id=\"nota\"style=\"color: aqua;\">"+dato.nota+"</td></tr>"
                        if numeroMin < 61:
                            general+="<tr><td id=\"nombre\">"+dato.nombre+"</td><td id=\"nota\"style=\"color: red;\">"+dato.nota+"</td></tr>"
                general+="</table></div>" 
            #Estudiantes aprobados
            if i=="APR":
                general+="<div><h2>Estudiantes aprobados: "+self.numero_de_aprobados()+"</h2><table><tr><td id=\"nombre\">Nombre</td><td id=\"nombre\">Nota</td></tr>"
                for dato in GuardarDatos.datos:
                    if int(dato.nota) >= 61:
                        general+="<tr><td id=\"nombre\">"+dato.nombre+"</td><td id=\"nota\"style=\"color: aqua;\">"+dato.nota+"</td></tr>"
                general+="</table></div>"  
            #Estudiantes reprobados
            if i=="REP":
                general+="<div><h2>Estudiantes reprobados: "+self.numero_de_reprobados()+"</h2><table><tr><td id=\"nombre\">Nombre</td><td id=\"nombre\">Nota</td></tr>"
                for dato in GuardarDatos.datos:
                    if int(dato.nota) < 61:
                        general+="<tr><td id=\"nombre\">"+dato.nombre+"</td><td id=\"nota\"style=\"color: red;\">"+dato.nota+"</td></tr>"
                general+="</table></div>"                  
        #Contenido
        contenido = """<!DOCTYPE html>
                    <html lang="en">
                    <head>
                    <meta charset="UTF-8">
                    <meta http-equiv="X-UA-Compatible" content="IE=edge">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Reporte</title>
                    <style>
                        body {
                            margin: 0;
                            padding: 0;
                            background: linear-gradient(75deg, black, #030c42, #031547, rgb(8, 5, 31), rgb(12, 12, 12));
                            background-size: cover;
                            font-family: sans-serif;
                            height: 100vh;
        
                            }
                     h1{
                        color: aliceblue;
                        font-size: 50px;
                        font-family: 'Courier New', Courier, monospace;
                        }
                    </style>
                    <style>
                    table{
               
                        border: 1px solid white
                    }
                    tr,td{
                        font-size: 40px;
                        border: 1px solid white;
                    }
                    #nombre{
                        color: white;
                    }
                    #principal{
                        font-size: 90px;
                        color: plum;
                    }
                    h2{
                        font-size: 30px;
                        font-family: 'Courier New', Courier, monospace;
                        color: plum;
                    }
                    </style>
                </head>
             <body>

                <center>
                 <h1 id="principal">Reporte de notas</h1>
                <h1>"""+GuardarDatos.nombreCurso[0]+"""</h1>
                <table>
                    <tr>
                        <td id="nombre">Nombre</td>
                        <td id="nombre">Nota</td>
                    </tr>"""+nombre+"""</table>"""+general+""""</center>
                </body>
                </html>"""
        fi.write(contenido)
        fi.close()
        webbrowser.open_new_tab('Reporte.html')
