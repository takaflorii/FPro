cars = {
    "AA-00-AA": (12000, ["Joel"], ["2019-Lisboa", "2021-Porto"], 2018),
    "BB-11-BB": (18000, ["Rute"], [], 2019),
    "CC-22-CC": (42000, ["Sara", "Quim"], ["2023-Coimbra"], 2023),
    "DD-33-DD": (11500, ["Rosa", "Rita", "Inês"], ["2018-Braga"], 2017),
    "EE-44-EE": (21750, ["João"], ["2022-Viseu", "2023-Porto"], 2022)
}

def unique_owner(cars):
    primeiro_dono = []
    for m, items in cars.items():
        p, d, a, y = items
        if len(d)== 1:
            primeiro_dono.append(m)
    return primeiro_dono

def unique_owner_cities_acc(cars):
    cidades = set()
    dono_unico = unique_owner(cars)
    for carro in dono_unico:
        p, d, a, y = cars[carro]
        for elmnt in a:
            elmnt = elmnt.split("-")
            city = elmnt[1]
            cidades.add(city)
    return cidades
