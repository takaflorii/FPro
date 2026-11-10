def strong(password):
    if len(password) < 8:
        return False
    
    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False
    tem_simbolo = False
    
    for char in password:
        if char.isupper():
            tem_maiuscula = True
        elif char.islower():
            tem_minuscula = True
        elif char.isdigit():
            tem_numero = True
        else:
            tem_simbolo = True
            
    return tem_maiuscula and tem_minuscula and tem_numero and tem_simbolo