def maximo(lista_num):
    ''' devuelve el númeor mayor de los pasados en una lista'''
    mayor = 0

    if lista_num == []:
        mayor = 0
    else:
        for elemento in lista_num:
            #if mayor < elemento:
            #    mayor = elemento
            # Uso un if ternario sólo por probar. En este caso no es útil porque siempre hay que poner else
            mayor = elemento if mayor < elemento else mayor
    return mayor


def minimo(lista_num):
    ''' devuelve el númeor menos de los pasados en una lista'''
    menor = 0

    if lista_num == []:
        menor = 0
    else:
        for elemento in lista_num:
            if menor < elemento:
                menor = elemento
    return menor

def media(lista_num):
    '''Obtiene la media de los número pasados como parámetro'''
    resultado = 0

    for i in lista_num:
        resultado += i
    resultado = resultado / len(lista_num)
    return resultado


funciones = {
    'max' :maximo,
    'mini': minimo,
    'med': media
    }

def return_funcion(nombre):
    ''' Devuelve una funcion en base al diminutivo usado como clave en el dicc 'funciones' '''
    nombre = nombre.lower()
    if nombre in funciones.keys():
        return funciones[nombre]
    return none
