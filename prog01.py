def suma_numeros(hasta, inicio = 0):

	resultado = 0

	for i in range(inicio, hasta + 1):
		resultado += 1
	return resultado


inicial = int(input("Número inicial: "))
final = int(input("Número final: "))
print(suma_numeros(final, inicial))
