#!/usr/bin/env python
# coding: utf-8

# In[1]:


# QUESTION 1 Create a list of the first 20 positive integers
positive_integers = list(range(1, 21))

# Print the list
print(positive_integers)


# In[2]:


# QUESTION 2 Create a list of the first 20 positive integers
positive_integers = list(range(1, 21))

# Access the first element
first_element = positive_integers[0]

# Access the middle element (in a list of 20 elements, the middle would be the 10th and 11th elements)
middle_element_1 = positive_integers[len(positive_integers) // 2 - 1]
middle_element_2 = positive_integers[len(positive_integers) // 2]

# Access the last element
last_element = positive_integers[-1]

# Print the first, middle, and last elements
print("First element:", first_element)
print("Middle elements:", middle_element_1, middle_element_2)
print("Last element:", last_element)


# In[3]:


# QUESTION 3 Create a list of the first 20 positive integers
positive_integers = list(range(1, 21))

# Slice and print the first five elements
first_five = positive_integers[:5]
print("First five elements:", first_five)

# Slice and print the last five elements
last_five = positive_integers[-5:]
print("Last five elements:", last_five)

# Slice and print the elements from index 5 to 15
elements_5_to_15 = positive_integers[5:16]
print("Elements from index 5 to 15:", elements_5_to_15)


# In[4]:


# QUESTÃO 4 Criar uma lista contendo os quadrados dos primeiros 10 números inteiros positivos
quadrados = [x**2 for x in range(1, 11)]

# Imprimir a nova lista
print("Quadrados dos primeiros 10 números inteiros positivos:", quadrados)


# In[5]:


# QUESTÃO 5 Lista original dos primeiros 20 números inteiros positivos
positive_integers = list(range(1, 21))

# Criar uma nova lista contendo apenas os números pares
even_numbers = [x for x in positive_integers if x % 2 == 0]

# Imprimir a nova lista
print("Números pares da lista original:", even_numbers)


# In[6]:


import random

# QUESTÃO 6 Criar uma lista de números aleatórios
random_numbers = [random.randint(1, 100) for _ in range(15)]

# Ordenar a lista em ordem crescente
random_numbers.sort()
print("Lista ordenada em ordem crescente:", random_numbers)

# Ordenar a lista em ordem decrescente
random_numbers.sort(reverse=True)
print("Lista ordenada em ordem decrescente:", random_numbers)

# Remover os duplicados convertendo para um conjunto e depois de volta para uma lista
unique_numbers = list(set(random_numbers))

# Opcional: Ordenar a lista única em ordem crescente para uma apresentação mais clara
unique_numbers.sort()

# Imprimir a lista modificada
print("Lista sem duplicados:", unique_numbers)


# In[7]:


# QUESTÃO 7 Criar uma lista aninhada representando uma matriz 3x3
matriz_3x3 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Imprimir a matriz
print("Matriz 3x3:")
for linha in matriz_3x3:
    print(linha)

# Acessar e imprimir o elemento na segunda linha e terceira coluna
elemento = matriz_3x3[1][2]
print("\nElemento na segunda linha e terceira coluna:", elemento)


# In[8]:


# QUESTÃO 8 Criar uma lista de dicionários, cada um representando um aluno
students = [
    {'name': 'Alice', 'score': 88},
    {'name': 'Bob', 'score': 92},
    {'name': 'Charlie', 'score': 85},
    {'name': 'David', 'score': 95},
    {'name': 'Eva', 'score': 90}
]

# Ordenar a lista de dicionários pelo 'score' em ordem decrescente
students_sorted = sorted(students, key=lambda x: x['score'], reverse=True)

# Imprimir a lista ordenada
print("Lista de alunos ordenada por pontuação (score) em ordem decrescente:")
for student in students_sorted:
    print(student)


# In[10]:


# QUESTÃO 9

def transpor_matriz(matriz):
    # Usar list comprehension para transpor a matriz
    transposta = [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]
    return transposta

# Matriz 3x3 original
matriz_original = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Transpor a matriz
matriz_transposta = transpor_matriz(matriz_original)

# Imprimir a matriz original
print("Matriz original:")
for linha in matriz_original:
    print(linha)

# Imprimir a matriz transposta
print("\nMatriz transposta:")
for linha in matriz_transposta:
    print(linha)


# In[11]:


# QUESTÃO 10


def achatar_lista(lista_aninhada):
    # Inicializa uma lista para armazenar os elementos achatados
    lista_achatada = []

    # Itera sobre os elementos da lista aninhada
    for item in lista_aninhada:
        if isinstance(item, list):
            # Se o item é uma lista, chama a função recursivamente
            lista_achatada.extend(achatar_lista(item))
        else:
            # Caso contrário, adiciona o item diretamente
            lista_achatada.append(item)
    
    return lista_achatada

# Lista aninhada original
lista_aninhada = [
    [1, 2, [3, 4]],
    [5, [6, [7, 8]]],
    9
]

# Achatar a lista
lista_achatada = achatar_lista(lista_aninhada)

# Imprimir a lista original
print("Lista aninhada original:")
print(lista_aninhada)

# Imprimir a lista achatada
print("\nLista achatada:")
print(lista_achatada)


# In[12]:


# QUESTÃO 11 Criar uma lista dos primeiros 10 números inteiros positivos
numeros = list(range(1, 11))

# Remover os elementos nos índices 2, 4 e 6
indices_para_remover = [6, 4, 2]  # Remover em ordem reversa para manter a consistência dos índices
for indice in sorted(indices_para_remover, reverse=True):
    del numeros[indice]

# Inserir o elemento '99' no índice 5
numeros.insert(5, 99)

# Imprimir a lista modificada
print("Lista modificada:")
print(numeros)


# In[13]:


# QUESTÃO 11 Criar duas listas de mesmo comprimento
lista1 = [1, 2, 3, 4, 5]
lista2 = ['a', 'b', 'c', 'd', 'e']

# Usar a função zip para combinar as listas em uma lista de tuplas
lista_combinada = list(zip(lista1, lista2))

# Imprimir o resultado
print("Lista combinada usando zip:")
print(lista_combinada)


# In[15]:


#QUESTÃO 12

def reverter_lista(lista):
    # Retornar uma nova lista com os elementos na ordem inversa
    lista_reversa = lista[::-1]
    return lista_reversa

# Lista original
lista_original = [1, 2, 3, 4, 5]

# Reverter a lista
lista_reversa = reverter_lista(lista_original)

# Imprimir a lista original
print("Lista original:")
print(lista_original)

# Imprimir a lista revertida
print("\nLista revertida:")
print(lista_reversa)


# In[16]:


#QUESTÃO 13

def rotacionar_lista(lista, n):
    # Calcula o valor de n efetivo para evitar rotações desnecessárias
    n = n % len(lista)  # Garante que n esteja dentro do intervalo da lista
    # Rotaciona a lista usando fatiamento
    lista_rotacionada = lista[-n:] + lista[:-n]
    return lista_rotacionada

# Lista original
lista_original = [1, 2, 3, 4, 5]

# Número de posições para rotacionar
n = 2

# Rotacionar a lista
lista_rotacionada = rotacionar_lista(lista_original, n)

# Imprimir a lista original
print("Lista original:")
print(lista_original)

# Imprimir a lista rotacionada
print("\nLista rotacionada:")
print(lista_rotacionada)


# In[17]:


#QUESTÃO 14

def interseccao_listas(lista1, lista2):
    # Converte as listas em conjuntos e realiza a interseção
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)
    interseccao = list(conjunto1 & conjunto2)
    return interseccao

# Listas de exemplo
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

# Obter a lista de interseção
lista_interseccao = interseccao_listas(lista1, lista2)

# Imprimir a lista de interseção
print("Lista de interseção:")
print(lista_interseccao)


# In[ ]:




