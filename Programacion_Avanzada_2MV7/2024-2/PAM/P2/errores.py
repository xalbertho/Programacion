
arr = [1,2,3]


try:
    idx = int(input("Ingresa un indice: "))
    print(arr[idx])
    print(5/1)
     
except IndexError:
    print("Perdon usuario muy listo, pero solo se aceptan valores de 0 a 2")
except ZeroDivisionError:
    print("Upsss, no se puede dividir entre 0")
except KeyboardInterrupt:
    print("Programa interrumpido")  
#except:
#    print("Upss Error")  
else:
    print("Todo OK")
finally:
    print("Adios")