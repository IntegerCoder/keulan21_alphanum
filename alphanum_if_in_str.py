def phoneWord2Num(word: str) -> int:
    value = 0
    for i in range(7):
        ch = word[i].lower()
        if ch in 'abc':
            digit = 2
        elif ch in 'def':
            digit = 3
        elif ch in 'ghi':
            digit = 4
        elif ch in 'jkl':
            digit = 5
        elif ch in 'mno':
            digit = 6
        elif ch in 'pqrs':
            digit = 7
        elif ch in 'tuv':
            digit = 8
        elif ch in 'wxyz':
            digit = 9
        value += digit * (10 ** (6 - i))
    return value


print(phoneWord2Num("FLOWERS"))
print(phoneWord2Num("PrOGrAM"))
print(phoneWord2Num("Battery"))
