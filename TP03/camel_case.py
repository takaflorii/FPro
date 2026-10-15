import string


def camel_case(phrase):
    result = ""
    current_word = ""
    word_count = 0

    for char in phrase:
        if char in string.ascii_letters:
            current_word += char
        else:
            if current_word:
                word_count += 1
                if word_count == 1:
                    result += current_word.lower()
                else:
                    result += current_word.capitalize()
                current_word = ""

    if current_word:
        word_count += 1
        if word_count == 1:
            result += current_word.lower()
        else:
            result += current_word.capitalize()

    return result