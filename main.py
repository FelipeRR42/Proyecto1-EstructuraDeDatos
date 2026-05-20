import pandas

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

	def insertar(self, nodo):

		#if self.buscar(nodo.dato) != None:
		nodo.sig = self.head
		if self.head != None:
			self.head.ant = nodo
		self.head = nodo


	def buscar(self, dato):
		aux_head = self.head
		while (aux_head != None) and (aux_head.dato != dato):
			aux_head = aux_head.sig
		return aux_head

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

class Post:
  post_id: str
  caption: str
  like: list[str]

  def __init__(self, post_id: str,caption: str):
    self.post_id = post_id
    self.caption = caption
    self.like = []

class Usuario:
  username: str
  following: list[str]
  post_usuario: list[Post]

  def __init__(self, username: str):
    self.username = username
    self.following = []
    self.post_usuario = []




caption = pandas.read_csv("reddit_opinion_democrats.csv", usecols=[2], nrows=100000)["self_text"].tolist()

dicc = {}
for comentario in caption:
	for palabra in str(comentario).lower().split():
		if palabra.strip(".?,#$!¿&[]{} ") not in dicc:
			dicc[palabra.strip(".?,#$!¿&[]{} ")] = ListaEnlazada()

		dicc[palabra.strip(".?,#$!¿&[]{} ")].insertar(Nodo(comentario))

print(dicc["amen"].recorrer())

#print(dicc["amen."].head)
#dicc["amen."].recorrer()






"""

datos = pandas.read_csv("reddit_opinion_democrats.csv", usecols=[0,2,6])

usuarios = {}


for fila in datos.itertuples(index=False):
	post_id = fila[0]
	caption = fila[1]
	username = fila[2]

	if username not in usuarios:
		usuarios[username] = Usuario(username)
		usuarios[username].post_usuario.append(Post(post_id, caption))

	else:
		usuarios[username].post_usuario.append(Post(post_id, caption))

print(len(usuarios))
"""










"""
for i in indices:

	newUsuario = Usuario(datos.loc[i].tolist()[2])
	newPost    = Post(datos.loc[i].tolist()[0],datos.loc[i].tolist()[1])

	if newUsuario.username not in lista_nombres_usuarios:
		lista_usuarios.append(newUsuario)
		lista_nombres_usuarios.append(newUsuario.username)

		newUsuario.post_usuario.append(newPost)

	else:

		for i in range(len(lista_nombres_usuarios)):

			if newUsuario.username == lista_usuarios[i].username:

				lista_usuarios[i].post_usuario.append(newPost)
"""


"""
post_id = datos[header_datos[0]].tolist()
caption = datos[header_datos[1]].tolist()
username = datos[header_datos[2]].tolist()

lista_usuarios = []
lista_nombres_usuarios = []
"""




"""
for i in range(len(username)):
	newUsuario = Usuario(username[i])
	newPost = Post(post_id[i], caption[i])

	if (newUsuario.username not in lista_nombres_usuarios):

		lista_usuarios.append(newUsuario)
		lista_nombres_usuarios.append(newUsuario.username)
		newUsuario.post_usuario.append(newPost)

	else:
"""

"""
lista_usuarios = []
lista_nombres_usuarios = []
lista_post = []
lista_id_post = []

for i in range(len(username)):

	create_user = Usuario(username[i])
	create_post = Post(post_id[i], caption[i])

	contador = 0

	if post_id[i] not in lista_id_post:
		lista_id_post.append(post_id)
		lista_post.append(create_post)

		if username[i] not in lista_nombres_usuarios:
			lista_nombres_usuarios.append(username[i])
			create_user.post_usuario.append(create_post)
			lista_usuarios.append(create_user)

		else:
			for usuario in lista_usuarios:

				if usuario.username == username[i]:
					usuario.post_usuario.append(create_post)

	else: 

		break
#print(lista_usuarios)
"""



"""
for i in range(len(username)):

	post = Post(username[i],post_id[i],caption[i]) #Falta añadir el atribitu likes, que es una lista de nombres de usuario

	if post_id[i] not in lista_id_post:
		lista_id_post.append(post_id[i])
		lista_post.append(post)
		usuario = Usuario(username[i])  #Falta añadir el atribituto following, que es una lista de nombres de usuario
		usuario.post_usuario.append(post)
		lista_usuarios.append(usuario)

"""





"""
#Lista de Usarios y lista de Posts
for i in range(len(owner_id)):
  post = Post(owner_id[i],post_id[i],caption[i]) #Falta añadir el atribitu likes, que es una lista de nombres de usuario
  if post_id[i] not in lista_id_post:
    lista_id_post.append(post_id[i])
    lista_post.append(post)

    if owner_id[i] not in lista_id_usuarios:
      lista_id_usuarios.append(owner_id[i])
      usuario = Usuario(owner_id[i],owner_username[i])  #Falta añadir el atribituto following, que es una lista de nombres de usuario
      usuario.post_usuario.append(post)
      lista_usuarios.append(usuario)

    #Dado que están ordenadas por owner_id
    else:
      usuario.post_usuario.append(post)

owner_username = datos[header_datos[6]].tolist()
owner_id = []
owner_username = []
post_id = []
descripcion = []

def leerDatos(nombreArchivo: string)->void:
	try:
		archivo = open(nombreArchivo, "r",encoding="utf-8")
	except Exception as e:
		print(e)
	else:
		encabezado = archivo.readline()
		for lineaArchivo in archivo.readline():

			datos = lineaArchivo.strip().split(",")

			owner_id.append(datos[0])
			#owner_username.append(datos[1])
			#post_id.append(datos[2])
			#descripcion.append(datos[4])

leerDatos("reddit_opinion_democrats.csv")

print(owner_id)
"""
