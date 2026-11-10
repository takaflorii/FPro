def longest(s):
    palavras = s.split()
    comprimento = 0
    for word in palavras:
        if len(word) > comprimento:
            comprimento = len(word)
    return comprimento
