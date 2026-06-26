import numpy as np
def llenadomatrix (matrices):
    for i in range (len(matrices)):
        for j in range (len(matrices[i])):
            matrices [i][j] = float (input (f"Elemento [{i+1}] [{j+1}]: "))
def sumamatrix (f, c):
    matrix_1 = np.zeros ((f, c))
    matrix_2 = np.zeros ((f, c))
    suma_matrix = np.zeros ((f, c))
    print ("=====1era matriz=====")
    llenadomatrix (matrix_1)
    print ("=====2da matriz===== ")
    llenadomatrix (matrix_2)
    for i in range (f):
        for j in range (c):
            suma_matrix [i][j]= matrix_1 [i][j] + matrix_2 [i][j]
    return suma_matrix
def restamatrix (f, c):
    matrix_1 = np.zeros ((f, c))
    matrix_2 = np.zeros ((f, c))
    resta_matrix = np.zeros ((f, c))
    print ("=====1era matriz=====")
    llenadomatrix (matrix_1)
    print ("=====2da matriz===== ")
    llenadomatrix (matrix_2)
    for i in range (f):
        for j in range (c):
            resta_matrix [i][j]= matrix_1 [i][j] - matrix_2 [i][j]
    return resta_matrix
def multimatrix (f1, c1, f2, c2):
    matrix_1 = np.zeros ((f1, c1))
    matrix_2 = np.zeros ((f2, c2))
    print ("=====1era matriz=====")
    llenadomatrix (matrix_1)
    print ("=====2da matriz===== ")
    llenadomatrix (matrix_2)
    resultado = matrix_1 @ matrix_2
    return resultado
def factorial (f):
    if f == 0 or f == 1:return 1
    else: return f * factorial (f-1) 
def expo (b,e):
    if e == 0: return 1
    else: return b * expo (b, e-1)
def main ():
    while True: 
        print ("======Calculadora======")
        print ("Elija una opción")
        print ("1.Suma")
        print ("2.Resta")
        print ("3.Multiplicación")
        print ("4.División")
        print ("5.Factorial")
        print ("6.Potencia")
        print ("7.Raiz")
        print ("8.Operaciones con matrices")
        print ("9.Salir")
        opcion = int (input ("Opción: "))

        if opcion==9:
            break
        
        match opcion:
            case 1:
                a = float (input ("Ingrese el primer número\n"))
                b = float (input ("Ingrese el segundo némero\n"))
                resultado = f"El resultado es:  {a+b}"
                print (resultado)
            case 2: 
                a = float (input ("Ingrese el primer número\n"))
                b = float (input ("Ingrese el segundo número\n"))
                resultado = f"El resultado es:  {a-b}"
                print (resultado)
            case 3: 
                a = float (input ("Ingrese el primer número\n"))
                b = float (input ("Ingrese el segundo número\n"))
                resultado = f"El resultado es:  {a*b}"
                print (resultado)
            case 4: 
                a = float (input ("Ingrese el primer número\n"))
                while True:
                    b = float (input ("Ingrese el segundo número\n"))
                    if b!=0:
                        break
                r = f"El resultado es:  {a/b}" 
                print (r)
            case 5:
                f = float (input ("Ingrese el número: \n"))
                r = f"El factorial del número es: {factorial (f)}\n"
                print (r)
            case 6: 
                b = float (input ("Ingrese la base\n"))
                e = float (input ("Ingrese el exponente\n"))
                r = f"El resultado de la potencia es: {expo (b,e)}\n"
                print (r)
            case 7: 
                while True:
                    n = float (input ("Ingrese un número positivo: \n"))
                    i = float (input ("Ingrese el índice: \n"))
                    if n >=0 and i !=0 :
                        break
                r = f"El resultado de la raíz es: {n ** (1/i)}\n"
                print (r)
            case 8:
                while True:
                    print ("Elija una opción")
                    print ("1.Desea sumar matrices?")
                    print ("2.Desea restar matrices?")
                    print ("3.Desea multiplicar matrices?")
                    print ("4.Salir de matrices")
                    choose = int (input ("Opción: \n"))
                    if choose == 4: break
                    match choose:
                        case 1:
                            print ("Tamaño de las matrices")
                            filas = int (input ("Filas de las matrices: "))
                            columnas = int  (input ("Columnas de las matrices: "))     
                            r = sumamatrix (filas, columnas)
                            for fila in r:
                                print(fila)
                        case 2: 
                            print ("Tamaño de las matrices")
                            filas = int (input ("Filas de las matrices: "))
                            columnas = int  (input ("Columnas de las matrices: "))     
                            r = restamatrix (filas, columnas)
                            for fila in r:
                                print(fila)
                        case 3:
                            print ("Tamaño de la primera matriz")
                            filas1 = int (input ("Filas de la 1era matriz: "))
                            while True:
                                columnas1 = int  (input ("Columnas de la 1era matriz: "))
                                print ("Tamaño de la segunda matriz")
                                filas2 = int (input ("Filas de la 2da matriz: "))
                                if columnas1 == filas2:
                                    break
                            columnas2 = int  (input ("Columnas de la 2da matriz: "))
                            r = multimatrix (filas1, columnas1, filas2, columnas2)
                            for fila in r:
                                print (fila)
                        case _:
                             print ("Opción inválida")
                    sino = input ("¿Desea continuar en matrices? s/n: ").lower()
                    if sino == "n": 
                        break
            case _:
                print ("Opción inválida")
        continuar = input ("¿Desea continuar? s/n: ").lower()
        if continuar == "n": 
            break
if __name__ == "__main__":
    main()