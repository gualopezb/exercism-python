def is_paired(input_string):
    symbols_opening_and_closing = {"{": "}", "(": ")", "[": "]"}
    string_symbols = []
    for character in input_string:
        if character in symbols_opening_and_closing.keys():
            string_symbols.append(character)
        elif character in symbols_opening_and_closing.values():
            if string_symbols:
                current_symbol = string_symbols.pop()
            else:
                return False
            if character != symbols_opening_and_closing[current_symbol]:
                return False
    return not string_symbols
