def count_chars(s, ch):
    ocorrencias = s.count(ch)

    if ocorrencias > 0:
        return ocorrencias
    else:
        return -1