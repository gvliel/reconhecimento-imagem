# Explicação linha por linha do código refatorado

## Código analisado

def calcular_soma_e_quantidade(numeros):

Cria uma função chamada calcular_soma_e_quantidade.

Recebe uma lista chamada numeros.

---

soma_total = sum(numeros)

Soma todos os valores da lista.

---

quantidade_itens = len(numeros)

Conta quantos elementos existem.

---

return {
    "soma": soma_total,
    "quantidade": quantidade_itens
}

Retorna um dicionário contendo:

- soma total
- quantidade de itens

---

valores = [10, 20, 30, 40]

Cria lista de teste.

---

resultado = calcular_soma_e_quantidade(valores)

Executa a função.

---

print(resultado)

Mostra o resultado final.