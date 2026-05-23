import pandas
import time
import random
start_time = time.time()

# Creacion de Clases
class Nodo:
	sig: Nodo
	ant: Nodo

	def __init__(self, dato):
		self.dato = dato
		self.sig = None
		self.ant = None

class ListaEnlazada:

	def __init__(self):
		self.head = None
		self.cantidad = 0

	def insertar(self, dato):
		nuevo_nodo = Nodo(dato)
		#if self.buscar(nodo.dato) != None:
		nuevo_nodo.sig = self.head
		if self.head != None:
			self.head.ant = nuevo_nodo
		self.head = nuevo_nodo
		self.cantidad += 1

	def insertar_sin_repeticion(self, dato):
		if self.buscar(dato) != None:
			return

		else:
			nuevo_nodo = Nodo(dato)
			nuevo_nodo.sig = self.head
			if self.head != None:
				self.head.ant = nuevo_nodo
			self.head = nuevo_nodo
			self.cantidad += 1

	def buscar(self, dato):
		aux_head = self.head
		while (aux_head != None) and (aux_head.dato != dato):
			aux_head = aux_head.sig
		
		if aux_head == None:
			return None
		else:
			return aux_head.dato
		
		
		#return aux_head

	def recorrer(self):
		aux_head = self.head
		print("Inicio")
		while aux_head != None:
			print(aux_head.dato)
			print("-----------------------------------------------------")
			aux_head = aux_head.sig
		print("Final")

	def eliminar(self, nodo):
		if nodo.ant != None:
			nodo.ant.sig = nodo.sig
		else:
			self.head = nodo.sig

		if nodo.sig != None:
			nodo.sig.ant = nodo.ant
		self.cantidad -= 1






class Post:
	post_id: str
	caption: str

	def __init__(self, post_id: str,caption: str, cant_likes: int):
		self.post_id = post_id
		self.caption = caption
		self.cant_likes = cant_likes
		self.usuarios_likes = ListaEnlazada()
class Usuario:
	username: str

	def __init__(self, username: str):
		self.username = username
		self.amigos = []
		self.post_usuario = []

def comparacion(lista1, lista2):
	aux1 = lista1.head
	aux2 = lista2.head
	interseccion = ListaEnlazada()

	while aux1 != None:
		if lista2.buscar(aux1.dato) != None:
			interseccion.insertar(aux1.dato)
		aux1 = aux1.sig

	return interseccion


print("Process inicio --- %s seconds ---" % (time.time() - start_time))


datos = pandas.read_csv("reddit_opinion_democrats.csv", usecols=[0,2,6,8], nrows=5000)

usuarios = {}
dicc = {}

print("Process termino de leer --- %s seconds ---" % (time.time() - start_time))

for fila in datos.itertuples(index=False):
	post_id = fila[0]
	caption = fila[1]
	username = fila[2]
	cantidad_likes = fila[3]

	if username not in usuarios:
		usuarios[username] = Usuario(username)

	usuarios[username].post_usuario.append(Post(post_id, caption, cantidad_likes))

print("Process termino creacion usuarios --- %s seconds ---" % (time.time() - start_time))

for usuario in usuarios.values():
	for post in usuario.post_usuario:

		for palabra in str(post.caption).lower().split(): 
			palabra = palabra.strip(".?,#$!¿&[]}{/() ")
			if palabra not in dicc:
				dicc[palabra] = ListaEnlazada()
			dicc[palabra].insertar_sin_repeticion(post.caption)


print("Process consulta --- %s seconds ---" % (time.time() - start_time))



#dicc["and"].recorrer()

consulta = input("Ingrese una palabra para buscar en los captions: ").lower().strip(".?,#$!¿&[]}{/() ")

consulta = consulta.split()

print("Process termino consulta --- %s seconds ---" % (time.time() - start_time))

try:
	aux_list = dicc[consulta[0]]
	for i in range(1,len(consulta)):
		aux_list = comparacion(aux_list, dicc[consulta[i]])
except:
	aux_list = ListaEnlazada()
	

#aux_list.recorrer()

print("Process final --- %s seconds ---" % (time.time() - start_time))

lista_usuarios = list(usuarios.keys())

for usuario in usuarios.values():
	usuario.amigos = ListaEnlazada()
	cantidad_amigos = random.randint(0, 50)
	amigos = random.sample(lista_usuarios, cantidad_amigos)

	if usuario in amigos:
		amigos.remove(usuario)

	for amigo in amigos:
		usuario.amigos.insertar(amigo)


for usuario in usuarios.values():
	for post in usuario.post_usuario:
		post.usuarios_likes = ListaEnlazada()

		usuarios_like = random.sample(lista_usuarios, abs(post.cant_likes))
		for usuario in usuarios_like:
			post.usuarios_likes.insertar(usuario)

usuarios[lista_usuarios[0]].post_usuario[0].usuarios_likes.recorrer()
print(
usuarios[lista_usuarios[0]].post_usuario[0].usuarios_likes.cantidad)
