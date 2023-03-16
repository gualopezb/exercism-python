def translate(text):
    return " ".join([pig(word) for word in text.split(" ")])


def pig(word):
    vowels = "aieou"
    if word[0] not in vowels and word[1:3] == "qu":
        return word[3:] + word[:3] + "ay"
    if word[0] in vowels:
        return word + "ay"
    if word[:2] in ["yt", "xr"]:
        return word + "ay"
    if word[:2] in ["qu"]:
        return word[2:] + word[:2] + "ay"
    if set(vowels) - set(word) == set(vowels) and "yt" not in word:
        return word[1:] + word[:1] + "ay"
    return pig(word[1:] + word[0])
