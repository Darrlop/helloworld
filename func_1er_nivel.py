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