
#Importar librerias
import pandas
import random

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
		if aux_head is None:        #La lista esta vacia, asi que no la recorre
			return
		if type(aux_head.dato) is Usuario:
			while aux_head != None:
				print(f"Nombre Usuario: {aux_head.dato.username}\n-------------------------------------------------------------------------")
				aux_head = aux_head.sig

		elif type(aux_head.dato) is Post:
			while aux_head != None:
				print(f"Post ID: {aux_head.dato.post_id}, Owner: {aux_head.dato.owner}, Caption: {aux_head.dato.caption}, Likes: {aux_head.dato.cant_likes}\n-------------------------------------------------------------------------")
				aux_head = aux_head.sig
		else:
			while aux_head != None:
				print(f"{aux_head.dato}\n-------------------------------------------------------------------------")
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
		self.post_usuario = ListaEnlazada()

#Creacion de Funciones

#Lectura y procesamiento de datos
def lectura_datos(nombre_archivo)->tuple:
    datos = pandas.read_csv(nombre_archivo, usecols=[0,2,6,8], nrows=30000)

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
        usuarios[username].post_usuario.insertar(post)

    return usuarios, posts

#Creacion de la lista de amigos para cada usuario
def creacion_amigos(usuarios:dict):

    lista_usuarios = list(usuarios.values())

    for usuario in usuarios.values():
        cantidad_amigos = random.randint(0, 50)
        amigos = random.sample(lista_usuarios, cantidad_amigos)

        if usuario in amigos:
            amigos.remove(usuario)

        for amigo in amigos:
            usuario.amigos.insertar(amigo)  #sample no repite elementos

#Creacion de la lista de usuarios que dieron like a los post
def creacion_likes(usuarios:dict, posts:dict):
    lista_usuarios = list(usuarios.values())

    for post in posts.values():
        try:
            usuarios_like = random.sample(lista_usuarios, abs(post.cant_likes))
        except ValueError:                                                                     #Si hay más cantidad de likes que de usuarios
            
            post.cant_likes = len(lista_usuarios)
            usuarios_like = random.sample(lista_usuarios, post.cant_likes)
        for usuario in usuarios_like:
            post.usuarios_likes.insertar(usuario)


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
                palabra = palabra.strip(".?,#$!¿&[]}{/()*+-:;\"\\='¿¡%|~` ")
                if palabra not in indice_post:
                    indice_post[palabra] = ListaEnlazada()
                indice_post[palabra].insertar_sin_repeticion(post)
    return indice_post


#Lee terminos ingresados en la consola e imprime los post que contienen esos termninos
def consulta_indice_post(indice_post: dict, stopwords:list):

    consulta = input("Ingrese una palabra para buscar en los captions: ").lower().strip(".?,#$!¿&[]}{/()*+-:;\"\\='¿¡%|~` ")
    consulta = consulta.split()
    consulta_sin_stopwords = []
    for palabra in consulta:
        if palabra not  in stopwords:
            consulta_sin_stopwords.append(palabra)
    consulta = consulta_sin_stopwords
    if consulta == []:
        print("Solo ha ingresado stopword, termino/s en demasiados posts")
        return
    for termino in consulta:
        if termino not in indice_post:
            print(f"No hay post que incluyan el termino {termino}")
            return

    aux_list = indice_post[consulta[0]]
    for i in range(1,len(consulta)):
        aux_list = comparacion(aux_list, indice_post[consulta[i]])

    print(f"Post que tienen los terminos {consulta}: ")
    aux_list.recorrer()


#Crea un indice invertido de un usuario y sus amigos
def crear_indice_amigos(usuarios:dict)->dict:
    indice_amigos = {}
    for usuario in usuarios.values():
       indice_amigos[usuario.username] = usuario.amigos

    return indice_amigos
#Rellena el atributo amigos de cada usuario con una lista de amigos aleatorios, debido a carencias del dataset

def consulta_indice_amigos(indice_amigos: dict):
    consulta = input("Ingrese un username: ")
    consulta = consulta.strip()

    try:
        amigos = indice_amigos[consulta]
        print(f"Amigos de {consulta}: ")
        amigos.recorrer()
    except AttributeError:
        print(f"No se encontro un usuario con ese nombre {consulta}")
    except KeyError:
        print(f"No se encontró el usuario {consulta}")

#Elimina las stopwords del indice invertido de posts
def crear_lista_stopwords(indice_post: dict)->list:
    lista_aux = []
    for palabra in indice_post.keys():
        lista_aux.append((palabra, indice_post[palabra].cantidad))

    lista_aux.sort(key=lambda x: x[1], reverse=True)
    stopwords = [x[0] for x in lista_aux[:100]]
    return stopwords

#Elimia las stopwords del indice invertido de posts
def eliminar_stopwords_indice(stopwords:list):
    for stopword in stopwords:
        del indice_post[stopword]




usuarios, posts = lectura_datos("reddit_opinion_democrats.csv")

indice_post = crear_indice_post(posts)

creacion_amigos(usuarios)

creacion_likes(usuarios, posts)

indice_amigos = crear_indice_amigos(usuarios)

stopwords = crear_lista_stopwords(indice_post)

termino = ""

while termino.lower().strip() !="s":
    consulta_indice_post(indice_post,stopwords)

    consulta_indice_amigos(indice_amigos)

    termino = input("Desea finalizar la busqueda? Escriba s para terminar y cualquier otra tecla para continuar: ")


