import redis

#Se llama al cliente de redis
r = redis.Redis(host='localhost', port=6379, db=0)

#Se agregan datos a la memoria
r.set('foo', 'bar')
r.set('Prueba1', 'resultado1')

#Se llama a un valor
result = r.get('foo')
print(result)

#Se asigna un ttl a la llave
r.expire('foo',1)
print(r.get('foo'))

#Se pregunta por el tiempo de vida de la llave
#Si es > 0 tiene.
#Si es -2 No existe la llave o expiró
#Si es -1 No tiene. 
print(r.ttl('foo'))