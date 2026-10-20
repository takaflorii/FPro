def rm_letter_rev(ch, s):
    result = ""
    for caracter in s:
        if caracter != ch:
            result = caracter + result
    return result

print(rm_letter_rev("a", "ana likes banana"))