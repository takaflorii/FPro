def flatten(lst):
    lista = []
    for n in lst:
        if isinstance(n, int):
            lista.append(n)
        elif isinstance(n,list):
            for e in n:
                if isinstance(e, int):
                    lista.append(e)
    return lista
