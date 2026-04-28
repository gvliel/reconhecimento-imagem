# Melhorias realizadas na refatoração

## Código original apresentava:

- Nome de função sem significado (`f`)
- Nome de variável genérica (`a`, `s`, `r`)
- Uso desnecessário de `range(len(lista))`
- Retorno em tupla sem identificação
- Falta de documentação

## Código refatorado:

### Nomes melhores

- `f` virou `calcular_soma_e_quantidade`
- `a` virou `numeros`
- `s` virou `soma_total`

### Melhor legibilidade

Foi utilizado:

sum(numeros)

Ao invés de loop manual.

### Retorno organizado

Agora retorna dicionário:

{
 "soma": valor,
 "quantidade": valor
}

### Documentação

Adicionado docstring explicando a função.