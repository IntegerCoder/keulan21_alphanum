def phoneWord2Num(word: str) -> int:
    chrs = 'abcdefghijklmnopqrstuvwxyz'
    nums = '22233344455566677778889999'
    value = 0
    for i in range(7):
        ch = word[i].lower()
        k = chrs.index(ch)
        digit = int(nums[k])
        value += digit * (10 ** (6 - i))
    return value


print(phoneWord2Num("FLOWERS"))
print(phoneWord2Num("PrOGrAM"))
print(phoneWord2Num("Battery"))
