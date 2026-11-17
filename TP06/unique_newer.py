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

def unique_owner_newer(cars, year):
    novo_unico = []
    dono_unico = unique_owner(cars)
    for carro in dono_unico:
        p, d, a, y = cars[carro]
        if y > year:
            novo_unico.append(carro)
    return novo_unico