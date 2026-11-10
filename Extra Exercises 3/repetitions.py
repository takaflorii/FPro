def repeat(text, num):
    i = 0
    frase = text
    while i < (num-1):
        frase = frase + "-" + text
        i +=1
    return frase