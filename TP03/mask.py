def mask_data(data, n_characters, position):
    length = len(data)

    if n_characters == 0:
        return data

    if n_characters < 0 or n_characters > length:
        return "*" * length

    if position == "begin":
        return "*" * n_characters + data[n_characters:]
    elif position == "end":
        return data[: length - n_characters] + "*" * n_characters

    return data