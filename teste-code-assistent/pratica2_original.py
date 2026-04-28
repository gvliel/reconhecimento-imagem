def f(a):
    s = 0

    for i in range(len(a)):
        s += a[i]

    return s, len(a)


lista = [10, 20, 30, 40]

r = f(lista)

print(r)