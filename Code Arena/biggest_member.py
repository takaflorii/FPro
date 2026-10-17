def biggest_member(atuple):
    snorlax = atuple #O Snorlax é o maior
    
    for solosis in atuple:
        if type(solosis) == tuple:
            sub_maior = biggest_member(solosis)
            if len(sub_maior) > len(snorlax):
                snorlax = sub_maior
                
    return snorlax