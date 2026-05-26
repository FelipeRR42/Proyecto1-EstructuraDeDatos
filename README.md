# Sistema de Gestión de Red Social con Índices Invertidos
 
## Descripción General
 
Infraestructura base para un sistema de gestión social (tomando como base la red social Reddit) usando el lenguaje Python. Permite modelar y visualizar la relación entre usuarios y sus amigos, además de relacionar a los post con sus palabras. Esto se consigue mediante la implementación de dos índices invertidos usando diccionarios de Python, cuyos valores son listas doblemente enlazadas creadas en Python.

 
- **Índice de Posts:** clave son las palabras que aparecen en los post, valor es la lista enlazada de los post donde aparece.

- **Índice de Amigos:** clave son el nombre de usuario, valor es la lista enlazada de sus amigos.

---
 
## Requisitos
 
- Python 3 instalado
- Librería pandas
- Librería random
- Librería matplotlib
- Dataset [Public Opinion on Democrats](https://www.kaggle.com/datasets/asaniczka/public-opinion-on-democrats-updated-daily) descargado desde Kaggle. El archivo debe llamarse reddit_opinion_democrats.csv y estar en la misma carpeta que main.py.
---
 
## Instrucciones de Ejecución
 
bash
python main.py

 
El programa realiza las siguientes etapas al iniciar:
 
1. Carga y limpieza del dataset (30.000 filas, columnas 0, 2, 6, 8).
2. Construcción del índice invertido de Posts.
3. Simulación aleatoria de la lista de amigos de cada usuario.
4. Simulación aleatoria de los usuarios que dieron like a cada Post.
5. Construcción del índice invertido de Amigos.
6. Identificación y eliminación de *stopwords* del índice.
7. Inicio del bucle interactivo de consultas.
---
 
## Descripción de Clases
 
### Nodo
Almacena un dato de cualquier tipo y tiene referencia al nodo anterior y al siguiente.

 
### ListaEnlazada
 Lista doblemente enlazada que mantiene una referencia a un nodo cabecera (head), además de cuántos elementos contiene (cantidad). Sus métodos son: 

| Método | Descripción |
|---|---|
| insertar(dato) | Inserta un nodo al inicio de la lista, sin evaluar repetición. |
| insertar_sin_repeticion(dato) |  Inserta un nodo al inicio de la lista siempre y cuando el dato no exista ya en la lista. |
| buscar(dato) | Recorre la lista buscando si algún nodo contiene el dato a buscar. Si lo encuentra retorna el nodo y si no retorna None. |
| recorrer() | Imprime en pantalla información de todos los nodos. |
| eliminar(nodo) | Elimina un nodo de la lista. |
 
### Post
Representa una publicación de Reddit. Atributos: post_id (identificador único), caption (texto del post), owner (autor), cant_likes (cantidad de likes), usuarios_likes (lista enlazada de usuarios que dieron like).
 
### Usuario
Representa el perfil de un usuario. Atributos: username (nombre de usuario), amigos (lista enlazada de sus amigos), post_usuario (lista enlazada de sus publicaciones).
 
---
 
## Descripción de Funciones
 
| Función | Descripción |
|---|---|
| lectura_datos(nombre_archivo) |  Procesa 30.000  datos del dataset (columnas 0,2,6,8) a través de la librería pandas. Retorna los diccionarios usuarios y posts. |
| creacion_amigos(usuarios) | Simula la red social asignando entre 0 y 50 amigos aleatorios a cada usuario, excluyendo al propio usuario. |
| creacion_likes(usuarios, posts) | Simula los likes de cada post asignando usuarios aleatorios. Ajusta cant_likes si supera el total de usuarios disponibles. |
| comparacion(lista1, lista2) | Retorna una nueva lista con la intersección de dos listas enlazadas |
| crear_indice_post(posts) | Construye el índice invertido de términos recorriendo el caption de cada Post. |
| crear_lista_stopwords(indice_post) | Retorna las 100 palabras más frecuentes del índice (usadas como stopwords). |
| eliminar_stopwords_indice(indice_post, stopwords) | Elimina las entradas del índice de posts que correspondan a stopwords. |
| consulta_indice_post(indice_post, stopwords) | Solicita términos por consola, filtra stopwords y muestra los Posts que contienen todos los términos. |
| crear_indice_amigos(usuarios) | Construye el índice invertido de amigos a partir de la lista amigos de cada usuario. |
| consulta_indice_amigos(indice_amigos) | Solicita un username por consola y muestra sus amigos. |
 
---
 
## Diagramas
 
### Usuarios y Post
 
```text
       Usuario
 ├── username
 ├── amigos ─────────► ListaEnlazada de Usuarios
 └── post_usuario ───► ListaEnlazada de Posts

Post
 ├── post_id
 ├── caption
 ├── owner
 ├── cant_likes
 └── usuarios_likes ─► ListaEnlazada de Usuarios


```
---
### Índice Invertido de Posts



```text
indice_post
│
├── "climate" ──► [PostA] ↔ [PostC] ↔ [PostF] ↔ None
│
├── "vote"    ──► [PostB] ↔ [PostC] ↔ None
│
├── "policy"  ──► [PostA] ↔ [PostD] ↔ None
│
└── ...
 

```
---
### Índice Invertido de Amigos
 ```text
 

indice_amigos (dict)
│
├── "user1" ──► [Usuario:user3] ↔ [Usuario:user7] ↔ None
│
├── "user2" ──► [Usuario:user1] ↔ [Usuario:user5] ↔ [Usuario:user9] ↔ None
│
└── ...
 

```
---
 
