import func_1er_nivel_return as f1r

def normal(x):
    return x

def cuadrado(x):
    return x * x

def suma_todos(limite, f):
    ''' sumatorio pasando funciones como param'''

    resultado = 0
    for i in range(limite + 1):
        resultado += f(i)
    return resultado





print(suma_todos(10, normal))
print(suma_todos(10, cuadrado))
print(f1r.maximo([1,2,3,10,5,6]))
print(f1r.media([0,1,2,3,4]))
z = f1r.return_funcion("med")
z([0,1,2,3,4]) 
print("Pasando al print directamente la devo de restur_funcion: {}".format(f1r.return_funcion("med")([0,1,2,3,4])))