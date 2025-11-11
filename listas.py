### 1- Fatiamento avançado

lista = ["p", "y", "t", "h", "o", "n"]

print(lista[2:]) #imprime a partir da posição 2 da lista até o final
print(lista[:2]) #imprime a lista até a posição 2
print(lista[1:3]) #imprime a lista a partir da posição 1 até a posição 3
print(lista[0:3:2]) #imprime a lista a partir da posição 0 até a 3, pulando a impressão de 2 em 2
print(lista[::]) #imprime toda a lista
print(lista[::-1]) #imprime toda a lista invertida

print()

#-------------------------------------------------------------------------------------------------------
### 2- Iteração com for e enumerate (Iteração básica sobre elementos)

casa = ["banheiro", "sala", "cozinha", "quarto"]

for comodo in casa: #armazena cada item da casa em comodo
    print(comodo)

print()

for indice, comodo in enumerate(casa): #função enumerate (indica o indice do objeto dentro do for)
    print(f"{indice}: {comodo}")

print()

#-------------------------------------------------------------------------------------------------------
### 3- Filtragem com List Comprehensions

numeros = [1,5,25,10,30,20,6,60,2,80,7,90,33,56]
pares = []
for numero in numeros:
    if numero % 2 == 0: #verificação se o número é par
        pares.append(numero) #append adiciona os valores a lista "pares"
print(pares)

#forma simplificada
pares = [numero for numero in numeros if numero % 2 ==0]
print(pares)

print()

#-------------------------------------------------------------------------------------------------------
### 4- Transformação de Dados

quadrado=[]
for numero in numeros:
    quadrado.append(numero ** 2) #elevando os numeros ao quadrado e adicionando os resultados a lista "quadrado"
print(quadrado)

#forma simplificada
quadrado = [numero ** 2 for numero in numeros]
print(quadrado)

print()

#-------------------------------------------------------------------------------------------------------
### 5- Métodos Built-in de Listas

l2=lista.copy() #cria uma cópia da lista e armazena em l2
l2.append(" ") #append para adicionar valores na l2
l2.append("Learning")
l2.append(1)
print(l2)
l2.clear() #limpa todos os valores da lista
print(l2)

print()

lista_c = [1,2,2,3,3,3,4,4,4,4,4,4]
print(lista_c.count(4)) #count para retornar a quantidade de valores na lista
lista.extend([" ", "l", "e", "a", "r", "n", "i", "n", "g"]) #extend para juntar uma lista dentro de outra
print(lista)
lista.pop() #tira o ultimo elemento da lista
lista.pop() #tira o ultimo elemento da lista
lista.pop(0) #tira o elemento 0 da lista
print(lista)
lista.reverse() #altera a ordem da lista
print(lista)
lista.sort() #ordena a lista em ordem alfabética
print(lista)
print(len(lista)) #len indica qual o tamanho da lista