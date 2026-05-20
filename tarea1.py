import pandas as pd
import random
#Creacion de clases
class Nodo():
    def __init__(self):
        self.siguiente = None
        self.anterior = None


class Lista_Enlazada ():
    def __init__(self):
        self.head = None
    
    def insertar_elemento(self, nuevo_nodo):
        nuevo_nodo.siguiente = self.head

        if self.head != None:
            self.head.anterior = nuevo_nodo

        self.head = nuevo_nodo
    
    def buscar_elemento(self, dato):
        pass

    def esta_elemento(self, dato):
        pass

    def mostrar_elementos(self):
        pass

class NodoUsuario(Nodo):
    def __init__(self, Usuario):
        super().__init__()
        self.Usuario = Usuario



class lista_amigos(Lista_Enlazada):       #Lista de usuarios existe para facilitir el metodo mostrar elementos
    def __init__(self):
        super().__init__()

    def buscar_usuario(self, username):
        actual = self.head
        while actual != None and actual.username != username:
            actual = actual.siguiente

        return actual

    def esta_usuario(self, username):
        actual = self.head
        
        while actual != None and actual.username != username:
            actual = actual.siguiente
        
        if actual == None:
            return False
        
        else:
            return True

    def mostrar_elementos(self):
        actual = self.head

        while actual != None:
            print(f"{actual.Usuario.username}", end="  ")
            actual = actual.siguiente
            """
                print("Posts:")
                for post in actual.lista_posts:
                    print(f" {post}")
                print("Amigos:")
                for amigo in actual.lista_amigos:
                    print(f" {amigo}")
                actual = actual.siguiente
            """

class Usuario:
  username: str
  following: lista_amigos
  #post_usuario: list[Post]

  def __init__(self, username: str):
    self.username = username
    self.following = lista_amigos()
    self.post_usuario = []

class Post:
  owner_id: int
  post_id: str
  caption: str
  like: list[str]

  def __init__(self, post_id: str, owner: Usuario, caption: str, cant_likes: int):
    self.post_id = post_id
    self.owner = owner
    self.caption = caption
    self.cant_likes = cant_likes
    self.like = []






"""
#Creacion de usuarios
Lista_amigos = lista_amigos()
usuario1 = NodoUsuario("Juan", ["Post 1", "Post 2"], ["Maria", "Pedro", "Maria", "Luis"])
usuario2 = NodoUsuario("Maria", ["Post A", "Post B"], ["Juan", "Pedro"])
usuario3 = NodoUsuario("Pedro", ["Post X", "Post Y"], ["Juan", "Maria"])


Lista_amigos.insertar_elemento(usuario1) 
Lista_amigos.insertar_elemento(usuario2)
Lista_amigos.insertar_elemento(usuario3)

Lista_amigos.mostrar_elementos()
buscar = usuario1 is Lista_amigos.buscar_usuario("Pedro")
print(buscar)
nodo_buscado = Lista_amigos.buscar_usuario("Juan")
print(f"\nNodo buscado: {nodo_buscado.lista_amigos}")

"""

#Lectura del dataset
datos = pd.read_csv("reddit_opinion_democrats.csv", usecols=[0,2,6,8] )
header_datos = datos.columns.tolist()

post_id = datos[header_datos[0]].tolist()
caption = datos[header_datos[1]].tolist()
username = datos[header_datos[2]].tolist()
cant_likes = datos[header_datos[3]].tolist()



#Creacion de usuarios y posts a partir del dataset, sin repeticiones
lista_usuarios = []
lista_posts = []


"""
set_usuarios = set()
for i in range(len(post_id)):
    if username[i] not in set_usuarios:
        set_usuarios.add(username[i])
        usuario = Usuario(username[i])
        lista_usuarios.append(usuario)

    post = Post(post_id[i], usuario, caption[i], cant_likes[i])   
    usuario.post_usuario.append(post)
    lista_posts.append(post)
del set_usuarios
"""


"""
#Prueba de rendimiento
for usuario in lista_usuarios:
    print(f"Usuario: {usuario.username}")
    for post in usuario.post_usuario:
        print(f"Posts: {post.caption}")
"""

"""
for usuario in lista_usuarios:
    usuario.following = lista_amigos()
    cantidad_amigos = random.randint(0, 500)
    amigos = random.sample(lista_usuarios, cantidad_amigos)
    
    if usuario in amigos:
        amigos.remove(usuario)
    #print(len(amigos))
    for amigo in amigos:
        
        usuario.following.insertar_elemento(NodoUsuario(amigo))
        #usuario.following.mostrar_elementos()

print("Usuarios y sus amigos:")
print(lista_usuarios[0].following.mostrar_elementos())
"""

"""
for usuario in lista_usuarios:

    print("\n")
    print(f"Usuario: {usuario.username}")
    print("Amigos: ", end="")
    usuario.following.mostrar_elementos()
"""
