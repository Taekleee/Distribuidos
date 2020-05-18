from pymemcache.client import base

#Si no se encuentra en caché va a buscar a la base de datos
def do_some_query():
	print("El resultado no se encuentra en caché")
	print("Accediendo a la base de datos")
	return 42

#Se crea el cliente y se le entrega el número de puerto (por defecto es 11211)
client = base.Client(('localhost', 11211))
result = client.get('consulta2')


#Se agrega un valor a la caché
client.set("ley",4)
client.set("consulta",2)

#Se pregunta por un valor que no se encuentra el la caché


#Si el valor no está en la caché, se llama a la base de datos
#y se agrega el valor encontrado a la caché
if result is None:
    result = do_some_query()
    client.set('consulta2', result)

print(result)

'''
Ejemplos de consultas:
list1 = [1,2,3]

client.set("Ejemplo",list1)
client.set("Ejemplo", "timepo", 3600) 


'''