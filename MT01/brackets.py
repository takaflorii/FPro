def is_balanced(text):
    apenas_parenteses = ""
    for ch in text:
        if ch in "()[]{}":
            apenas_parenteses = apenas_parenteses + ch
            
    texto = apenas_parenteses

    encontrou_par = True
    while encontrou_par:
        encontrou_par = False
        
        i = texto.find("()")
        if i != -1:
            texto = texto[:i] + texto[i+2:]
            encontrou_par = True
            continue
            
        i = texto.find("[]")
        if i != -1:
            texto = texto[:i] + texto[i+2:]
            encontrou_par = True
            continue
            
        i = texto.find("{}")
        if i != -1:
            texto = texto[:i] + texto[i+2:]
            encontrou_par = True
            continue

    return texto == ""