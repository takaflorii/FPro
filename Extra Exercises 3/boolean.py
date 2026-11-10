def validate(grade):
    return type(grade) in (int, float) and 0 <= grade <= 100