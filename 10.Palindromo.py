# -*- coding: utf-8 -*-
# palindromo =  es una palabra que se lee igual al derecho y al reves

def palindrome2(word):
    # reversed_word = word[::] Se genera una palabra desde el principio hasta el final y si le colocamos -1 va de atrás para delante
    reversed_word = word[::-1] # para revertir la palabra se Genera caracteres que empiezan desde atrás para delante

    if reversed_word == word:
        return True
    return False


def palindrome(word):
    reversed_letters = []

    for letter in word:
        reversed_letters.insert(0, letter) # agregar una letra a reversed_letters
        
    reversed_word = ''.join(reversed_letters)

    # la variable word es la palabra al derecho
    # la variable reversed_word es la palabra al revés

    if reversed_word == word:
        return True
    
    return False

if __name__ == "__main__":
    word = str(input('Escribe una palabra-> '))

    # SE PUEDE UTILIZAR CUALQUIERA DE ESTAS FUNCIONES
    # result = palindrome(word)
    result = palindrome2(word)

    if result is True:
        print('{} si es un palindromo.'.format(word)) #format = Para llenar espacios en esta concatenación
    else:
        print('{} no es un palindromo.'.format(word))