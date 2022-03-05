def phoneWord2Num(word: str) -> int:
    d = {
        'abc': 2,
        'def': 3,
        'ghi': 4,
        'jkl': 5,
        'mno': 6,
        'pqrs': 7,
        'tuv': 8,
        'wxyz': 9
    }
    value = 0
    for i in range(7):
        ch = word[i].lower()
        digit = -1
        for k, v in d.items():
            if ch in k:
                digit = v
                break
        value += digit * (10 ** (6 - i))
    return value


print(phoneWord2Num("FLOWERS"))
print(phoneWord2Num("PrOGrAM"))
print(phoneWord2Num("Battery"))
