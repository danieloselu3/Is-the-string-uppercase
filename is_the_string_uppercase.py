import string

def is_uppercase(str):
    small_caps_alphabet = string.ascii_lowercase
    container = []
    for char in str:
        if char in small_caps_alphabet:
            container.append(char)
    return True if len(container) == 0 else False
