def remove_leading(ip):
    partes = ip.split(".")
    partes_limpas = []
    for parte in partes:
        partes_limpas.append(str(int(parte)))
    return ".".join(partes_limpas)