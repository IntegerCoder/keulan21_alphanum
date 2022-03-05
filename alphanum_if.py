def phoneWord2Num(word: str) -> int:
    value = 0
    for i in range(7):
        ch = word[i].lower()
        if 'a' <= ch <= 'c':
            digit = 2
        elif 'd' <= ch <= 'f':
            digit = 3
        elif 'g' <= ch <= 'i':
            digit = 4
        elif 'j' <= ch <= 'l':
            digit = 5
        elif 'm' <= ch <= 'o':
            digit = 6
        elif 'p' <= ch <= 's':
            digit = 7
        elif 't' <= ch <= 'v':
            digit = 8
        elif 'w' <= ch <= 'z':
            digit = 9
        value += digit * (10 ** (6 - i))
    return value


print(phoneWord2Num("FLOWERS"))
print(phoneWord2Num("PrOGrAM"))
print(phoneWord2Num("Battery"))
