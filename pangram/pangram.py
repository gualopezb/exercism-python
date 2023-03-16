import string


def is_pangram(sentence):
    stripped_sentence = sentence.replace(" ", "").lower()
    counts = {}
    for char in stripped_sentence:
        current = counts.get(char, 0)
        counts[char] = current + 1
    alphabet = string.ascii_lowercase
    return all(ele in counts for ele in alphabet)
