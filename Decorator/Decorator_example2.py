def funcion_decoradora(funcion):
	def wrapper():
		print("Este es el primer mensaje...")
		funcion()
		print("Este es el ultimo mensaje ;)")
	return wrapper

# def zumbido():
# 	print("Buzzzzzz")

#zumbido = funcion_decoradora(zumbido)

@funcion_decoradora
def zumbido():
	print("Buzzzzzz")

zumbido()



# def f1(fun): # f1 es el empresario que recibe los contratos, pero su empleado (la funcion dentro de él) es quien hará todo el trabajo (el trabajo de decorar). el empresario solo puede recibir un contrato (osea, solo puede recibir el nombre de una funcion como argumento)
#     def wrapper(): # esta es la funcion que hará todo el trabajo (el empleado), dentro de esta funcion se llamará a la funcion que queremos decorar, y debe tener los mismos algumentos que tiene la funcion que queremos decorar
#         print('started') # aqui ya estamos dentro de la funcion que hará el trabajo de decorar y es en este cuerpo el lugar en donde podemos usar los argumentos que tiene la funcion que hara el trabajo de decorar
#         fun() # despues de usar los argumentos pues ya podemos llamar a la funcion que queriamos decorar. y la debemos llamar con todo y sus argumentos
#         print('ended') # esto es solo broche de oro.
#     return wrapper # aqui debemos llamar a la funcion que hizo todo el trabajo de decorar para que el empresario pueda entregar lo que se pidió

# @f1 # esta es una forma en la que python permite llamar a la empresa 'decoradora' para poder decorar a la funcion que esta debajo de él.
# def f(): #aqui declaramos la funcion que queremos decorar y le decimos que haga todo lo que nosotros queremos que haga. y los argumentos de esta funcion deben ser los mismos que se le entregaran al empleado que lo va a decorar
#     print('Hello') #en este caso solo quiero que la funcion imprima en pantalla la palabra 'Hello'

# # ahora ya podemos usar nuestra funcion que queriamos decorar. en este punto la funcion ya está decorada. la debemos llamar con todo y sus argumentos que nosotros establecimos
# f()

# print()
# #---------------------------------------------------------------------------------------------
# #---------------- E J E M P L O para que termine todo amarre bien -----------------------------
# #---------------------------------------------------------------------------------------------


# la funcion check es el empresario que se compromete a entregar algo decorado (una funcion). lo que el empleado debe hacer en este problema es verificar que el divisor no sea cero, y si lo es, pues despliega un mensaje.
def check(fun):
    def result(a, b): # esta funcion (empleado) debe contener los mismos argumentos que la funcion que queremos decorar.
        if b == 0: # aqui este empleado va a checar si el divisor es cero, y su es pues imprime un mensaje, y seguido de eso le agregamos return para que el mensaje para ser desplegado en pantalla
            return ("Can't divide by 0") 
        else:
            return fun(a, b) # aqui llamamos a la función que queriamos decorar, y la llamamos con todo y sus argumentos pues para que haga todo lo que debe hacer si su divisor No es cero
    return result #debemos regesar la funcion que hizo todo el trabajo de decorar pues para que la decoracion pueda ser devuelta. Cabe mencionar que la accion de decorar para este problema fue lo de checar si el divisor es cero o no. 

@check # la funcion check esta recibiendo a la funcion que esta debajo de el.
def divide(a, b): # esta es la funcion que queremos decorar. esta funcion lo que hace es recibir dos numeros como argumentos y devolver la divicion de esos numeros
    return (a / b)

#ahora ya podemos llamar a nuestra funcion. y cabe mencionar que ya esta decorada.
print(divide(10, 2)) # aqui lo que pasará es que se nos devolverá la divicion. osea, 5
print(divide(7, 0)) # aqui sabemos que se nos devolverá el mensaje de que No podemos dividir entre cero