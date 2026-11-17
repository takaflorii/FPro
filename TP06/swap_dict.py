def switch_dict(adict):
    switched = {}
    for key, value in adict.items():
        if value not in switched:
            switched[value] = []
        switched[value].append(key)
    return switched