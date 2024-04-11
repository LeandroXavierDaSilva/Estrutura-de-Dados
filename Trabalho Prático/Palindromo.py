# Problema 02: Escreva uma função em python que usa uma pilha para verificar se uma string é um palíndromo.

from Stack import Stack

def verificaPalindromo(string):
    s = Stack()

    for char in string:
        s.push(char)

    for char in string:
        if s.pop() != char:
            return False        
    return True

# Exemplo de uso
string = "roma amor"
if verifica_palindromo(string):
    print(f"A string '{string}' é um palíndromo.")
else:
    print(f"A string '{string}' não é um palíndromo.")
