def phoneWord2Num(word: str) -> int:
    value = 0
    for i in range(7):
        ch = word[i].lower()
        if ch in ['a', 'b', 'c']:
            digit = 2
        elif ch in ['d', 'e', 'f']:
            digit = 3
        elif ch in ['g', 'h', 'i']:
            digit = 4
        elif ch in ['j', 'k', 'l']:
            digit = 5
        elif ch in ['m', 'n', 'o']:
            digit = 6
        elif ch in ['p', 'q', 'r', 's']:
            digit = 7
        elif ch in ['t', 'u', 'v']:
            digit = 8
        elif ch in ['w', 'x', 'y', 'z']:
            digit = 9
        value += digit * (10 ** (6 - i))
    return value


print(phoneWord2Num("FLOWERS"))
print(phoneWord2Num("PrOGrAM"))
print(phoneWord2Num("Battery"))
