# Debug com IA

## Erro identificado

Erro de sintaxe.

## Causa

Na definição da função faltou o caractere `:` no final.

Errado:

def somar(a, b)

Correto:

def somar(a, b):

## Código corrigido

def somar(a, b):
    return a + b

print(somar(5, 3))

## Resultado esperado

8