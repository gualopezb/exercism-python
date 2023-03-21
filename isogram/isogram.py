def is_isogram(string):
    counts = {}
    trimmed_string = string.lower().split()
    trimmed_string = "".join(trimmed_string).split("-")
    for char in "".join(trimmed_string):
        current = counts.get(char, 0)
        counts[char] = current + 1
    return all(char == 1 for char in counts.values())
