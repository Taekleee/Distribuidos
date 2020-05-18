#Escribiendo datos en memcached
from pymemcache.client import base
import time 
#Se crea el cliente y se le entrega el número de puerto (por defecto es 11211)
client = base.Client(('localhost', 11211))
list1 = [3,4]
list2 = ["u","l"]

client.set("Ejemplo1",4)
client.set("Ejemplo2","Soy un ejemplo")




