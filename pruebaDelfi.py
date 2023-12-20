def promedio(arreglo):
    suma = 0 #arranco la suma en 0
    for i in arreglo:#voy por cada elemento del arreglo
        suma += arreglo[i] #lo voy sumando
    prom = suma/len(arreglo) #divido por la cantidad de elementos para el promedio (len() te da la cantidad de elementos)
    print(prom) #lo muestro
    return prom #lo devuelvo


#Abrir 'r' significa para lectura
archivo = open('nombreArchivo.txt','r')

contenido = archivo.read()
#El contenido por ejemplo puede ser una lista 
#de valores 
#entonces se podría recorrerlos para calcular cosas
#por ejemplo si querriamos obtener el promedio 
#del archivo, llamariamos a la funcion promedio hecha
promedioArchivo = promedio(contenido)


#cerrar archivo
archivo.close()

