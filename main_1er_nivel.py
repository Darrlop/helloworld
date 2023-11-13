# Se usará este fichero como llamadas a otros y definición directa de un par de funciones
#import func_1er_nivel_return as f1r
from func_1er_nivel_return import *

print(suma_todos(10, normal))
print(suma_todos(10, cuadrado))
#print(f1r.maximo([1,2,3,10,5,6]))
#print(maximo([1,2,3,10,5,6]))
print(media([0,1,2,3,4]))
z = return_funcion("med")
z([0,1,2,3,4]) 
print("Pasando al print directamente la devo de return_funcion: {}".format(return_funcion("med")([0,1,2,3,4])))