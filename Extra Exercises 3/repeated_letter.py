def repeated_letter(s):
    for ch in s:
        if s.count(ch) > 1:
            return ch