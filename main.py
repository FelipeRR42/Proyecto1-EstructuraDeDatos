#Iportar librerias
import pandas
import time
import random
start_time = time.time()
print("Process inicio --- %s seconds ---" % (time.time() - start_time))

# Creacion de Clases

class Nodo:

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
		if aux_head != None:
			return aux_head.dato

		return aux_head

	def recorrer(self):
		aux_head = self.head
		if aux_head is None:
			return
		while aux_head != None:
			print(aux_head.dato, "\n------------------------------------------------------------------------------------------------------------------------")
			aux_head = aux_head.sig

	def eliminar(self, nodo:Nodo):
		if nodo.ant != None:
			nodo.ant.sig = nodo.sig
		else:
			self.head = nodo.sig

		if nodo.sig != None:
			nodo.sig.ant = nodo.ant
		self.cantidad -= 1


class Post:
    post_id: str
    owner: str
    caption: str

    def __init__(self, post_id: str, owner:str, caption: str, cant_likes: int):
        self.post_id = post_id
        self.caption = caption
        self.owner = owner
        self.cant_likes = cant_likes
        self.usuarios_likes = ListaEnlazada()


class Usuario:
	username: str

	def __init__(self, username: str):
		self.username = username
		self.amigos = ListaEnlazada()
		self.post_usuario = []

#Creacion de Funciones

#Compara dos listas enlazadas y devuelve una lista con los elementos en común
def comparacion(lista1:ListaEnlazada, lista2:ListaEnlazada)->ListaEnlazada:
    interseccion = ListaEnlazada()
    aux = None
    #se usara la lista con menos enlementos para recorrer
    if lista1.cantidad < lista2.cantidad:
        aux = lista1.head
        while aux != None:
            if lista2.buscar(aux.dato) != None:
                interseccion.insertar(aux.dato)
            aux = aux.sig
    else:
        aux = lista2.head
        while aux != None:
            if lista1.buscar(aux.dato) != None:
                interseccion.insertar(aux.dato)
            aux = aux.sig

    return interseccion


#Lectura y procesamiento de datos
def lectura_datos(nombre_archivo)->tuple:
    datos = pandas.read_csv(nombre_archivo, usecols=[0,2,6,8], nrows=10000)

    usuarios = {}
    posts = {}

    #Creacion de usuarios
    for fila in datos.itertuples(index=False):
        post_id = fila[0]
        caption = fila[1]
        username = fila[2]
        cantidad_likes = fila[3]

        if username not in usuarios:
            usuarios[username] = Usuario(username)
        post = Post(post_id, username, caption, cantidad_likes)
        posts[post_id] = post
        usuarios[username].post_usuario.append(post)

    return usuarios, posts

#Compara dos listas enlazadas y devuelve una lista con los elementos en común
def comparacion(lista1:ListaEnlazada, lista2:ListaEnlazada)->ListaEnlazada:
    interseccion = ListaEnlazada()
    aux = None
    #se usara la lista con menos enlementos para recorrer
    if lista1.cantidad < lista2.cantidad:
        aux = lista1.head
        while aux != None:
            if lista2.buscar(aux.dato) != None:
                interseccion.insertar(aux.dato)
            aux = aux.sig
    else:
        aux = lista2.head
        while aux != None:
            if lista1.buscar(aux.dato) != None:
                interseccion.insertar(aux.dato)
            aux = aux.sig

    return interseccion

#Creacion de indice invertido de post:
def crear_indice_post(posts:dict)->dict:
    indice_post = {}
    for post in posts.values():
        for palabra in str(post.caption).lower().split(): 
                palabra = palabra.strip(".?,#$!¿&[]}{/() ")
                if palabra not in stopwords:
                    if palabra not in indice_post:
                        indice_post[palabra] = ListaEnlazada()
                    indice_post[palabra].insertar_sin_repeticion(post.caption)
    return indice_post


#Lee terminos ingresados en la consola e imprime los post que contienen esos termninos
def consulta_indice_post(indice_post: dict):

    consulta = input("Ingrese una palabra para buscar en los captions: ").lower().strip(".?,#$!¿&[]}{/() ")
    consulta = consulta.split()
    for palabra in consulta:
        if palabra in stopwords:
            consulta.remove(palabra)

    try:
        aux_list = indice_post[consulta[0]]
        for i in range(1,len(consulta)):
            aux_list = comparacion(aux_list, indice_post[consulta[i]])
    except:
        aux_list = ListaEnlazada()

    print(f"Post que tienen los terminos {consulta}: ")
    aux_list.recorrer()



def crear_indice_amigos(usuarios:dict)->dict:
    indice_amigos = {}
    for usuario in usuarios.values():
       indice_amigos[usuario.username] = usuario.amigos

    return indice_amigos
#Rellena el atributo amigos de cada usaurio con una lista de amigos aleatorios, debido a carencias del dataset

def consulta_indice_amigos(indice_amigos: dict):
    consulta = input("Ingrese un username: ")


    try:
        amigos = indice_amigos[consulta]
        print(f"Amigos de {consulta}: ")
        amigos.recorrer()
    except AttributeError:
        print(f"No se encontro un usuario con ese nombre {consulta}")
    except KeyError:
        print(f"No se encontró el usuario {consulta}")

def creacion_amigos(usuarios:dict):

    lista_usuarios = list(usuarios.keys())

    for usuario in usuarios.values():
        usuario.amigos = ListaEnlazada()
        cantidad_amigos = random.randint(0, 50)
        amigos = random.sample(lista_usuarios, cantidad_amigos)

        if usuario in amigos:
            amigos.remove(usuario)

        for amigo in amigos:
            usuario.amigos.insertar(amigo)

def creacion_likes(usuarios:dict, posts:dict):
    lista_usuarios = list(usuarios.keys())
    for post in posts.values():
        post.usuarios_likes = ListaEnlazada()
        try:
            usuarios_like = random.sample(lista_usuarios, abs(post.cant_likes))
        except:
            post.cant_likes = len(lista_usuarios)
            usuarios_like = random.sample(lista_usuarios, post.cant_likes)
            for usuario in usuarios_like:
                post.usuarios_likes.insertar(usuario)

    usuarios[lista_usuarios[0]].post_usuario[0].usuarios_likes.recorrer()


stopwords = ["about", "above", "across", "after", "against", "along", "among", 
    "around", "as", "at", "before", "behind", "below", "beneath", 
    "beside", "between", "beyond", "but", "by", "despite", "down", 
    "during", "except", "for", "from", "in", "inside", "into", "like", 
    "near", "of", "off", "on", "onto", "out", "outside", "over", 
    "past", "regarding", "since", "through", "throughout", "to", 
    "toward", "under", "underneath", "until", "up", "upon", "with", 
    "within", "without",                                #preposiciones

    "i", "me", "my", "mine", "myself",
    "you", "your", "yours", "yourself", "yourselves",
    "he", "him", "his", "himself",
    "she", "her", "hers", "herself",
    "it", "its", "itself",
    "we", "us", "our", "ours", "ourselves",
    "they", "them", "their", "theirs", "themselves"
                                                        #pronombres
    "the", "that","this","these","a","an"               #articulos

    "for","nor","and", "but","or","yet","so"     #conjunciones
    ] 

usuarios, posts = lectura_datos("reddit_opinion_democrats.csv")
print("Fin leer datos, Inicio crear indice post --- %s seconds ---" % (time.time() - start_time))
indice_post = crear_indice_post(posts)
print("Fin crear indice post , inicio creacion amigos --- %s seconds ---" % (time.time() - start_time))
creacion_amigos(usuarios)
print("Fin creacion amigos, inicio creacion likes --- %s seconds ---" % (time.time() - start_time))
creacion_likes(usuarios, posts)
print("Fin creacion likes, inicio crear indice amigos --- %s seconds ---" % (time.time() - start_time))
indice_amigos = crear_indice_amigos(usuarios)
print("Fin crear indice amigos --- %s seconds ---" % (time.time() - start_time))

try:
    print("Inicio consulta indice post --- %s seconds ---" % (time.time() - start_time))
    consulta_indice_post(indice_post)
    print("Fin consulta indice post, Inicio consulta indice amigos  --- %s seconds ---" % (time.time() - start_time))
    consulta_indice_amigos(indice_amigos)
    print("Fin consulta indice amigos --- %s seconds ---" % (time.time() - start_time))
except AttributeError:
    print("No se enocntraroh post con esos ternminos")

print("Process final --- %s seconds ---" % (time.time() - start_time))


