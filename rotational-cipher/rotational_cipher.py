def rotate(text, key):
    first_letter = "a"
    translated_letters = []
    for char in text:
        if char.isalpha():
            if char.upper() == char:
                first_letter = first_letter.upper()
            else:
                first_letter = first_letter.lower()
            translated_char = chr(ord(first_letter) + (ord(char) + key) % ord(first_letter) % 26)
            translated_letters.append(translated_char)
        else:
            translated_letters.append(char)
    return "".join(translated_letters)
