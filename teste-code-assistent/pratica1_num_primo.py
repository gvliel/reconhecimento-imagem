def eh_primo(numero):
    """
    Verifica se um número é primo.
    Retorna True se for primo e False se não for.
    """

    if numero <= 1:
        return False

    for divisor in range(2, int(numero ** 0.5) + 1):
        if numero % divisor == 0:
            return False

    return True


valor = int(input("Digite um número: "))

if eh_primo(valor):
    print("O número é primo.")
else:
    print("O número não é primo.")