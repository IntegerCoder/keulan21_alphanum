def phoneWord2Num(word: str) -> int:
    chrs = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    nums = [2]*3 + [3]*3 + [4]*3 + [5]*3 + [6]*3 + [7]*4 + [8]*3 + [9]*4
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
