import random
import string

def gerar_senha(tamanho, caracteres):
    senha = ''
    for i in range(tamanho):
        senha += random.choice(caracteres)
    return senha

caracteres = string.ascii_letters + string.digits + string.punctuation

tamanho = int(input('Digite o tamanho da senha desejada: '))

senha = gerar_senha(tamanho, caracteres)

print('Senha gerada:', senha)
