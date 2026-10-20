def is_anagram(a, b):
    s1 = a.strip().upper().replace(" ", "")
    s2 = b.strip().upper().replace(" ", "")

    if len(s1) != len(s2):
        return False
    for letra in s1:
        if s1.count(letra) != s2.count(letra):
            return False
    return True
