# 🐍 Manipulação de Listas em Python

Exercícios completos sobre operações com listas em Python, desde conceitos básicos até técnicas avançadas.

## 🎯 Objetivo
Demonstrar domínio completo na manipulação de listas, incluindo fatiamento, iteração, métodos built-in e list comprehensions.

## 📚 Conteúdo

### 🔍 [listas.py](listas.py) - **Operações Completas com Listas**

#### 1. **Fatiamento Avançado (Slicing)**
```python
lista = ["p", "y", "t", "h", "o", "n"]
print(lista[2:])    # ["t", "h", "o", "n"]
print(lista[::-1])  # ["n", "o", "h", "t", "y", "p"] - inversão

2. Iteração com for e enumerate
Iteração básica sobre elementos

Uso de enumerate() para acessar índices e valores

Aplicação prática em lista de cômodos de casa

3. Filtragem com List Comprehensions
python
# Filtra números pares - forma tradicional vs. simplificada
pares = [numero for numero in numeros if numero % 2 == 0]
4. Transformação de Dados
python
# Eleva números ao quadrado
quadrado = [numero ** 2 for numero in numeros]
5. Métodos Built-in de Listas
.copy() - criação de cópias independentes

.append() - adição de elementos

.clear() - limpeza da lista

.count() - contagem de ocorrências

.extend() - extensão com outra lista

.pop() - remoção por índice

.reverse() - inversão da ordem

.sort() - ordenação

len() - tamanho da lista

🛠️ Técnicas Demonstradas
✅ Fatiamento (Slicing)
python
lista[início:fim:passo]
Índices positivos e negativos

Omissão de parâmetros

Passo negativo para inversão

✅ List Comprehensions
python
[expressão for item in lista if condição]
Filtragem: elementos que atendem condições

Transformação: aplicação de operações

Sintaxe concisa e eficiente

✅ Métodos Essenciais
Manipulação: append(), pop(), extend()

Informação: count(), len()

Ordenação: sort(), reverse()

Cópia: copy() vs atribuição direta

🚀 Como Executar
bash
# Execute o arquivo
python listas.py
📈 Habilidades Desenvolvidas
✅ Fatiamento avançado com múltiplos parâmetros

✅ Iteração eficiente com enumerate()

✅ List comprehensions para código conciso

✅ Manipulação completa com métodos built-in

✅ Cópia vs referência em estruturas de dados

✅ Transformação e filtragem de dados

## 👨‍💻 Autor
**Richard** - [https://github.com/TSRichard]

Estudante de programação em transição de carreira. Certificado pela Santander Academy e atualmente aprofundando estudos em Python através da DIO. Buscando primeira oportunidade como desenvolvedor.