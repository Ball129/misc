import math

num = int(input())

ROMAN_MAP = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
ROMAN_MAP = {v: k for k, v in ROMAN_MAP.items()}

ans = ''
for k in [1000, 100, 10, 1]:
    val = math.floor(num / k)
    if val > 0:
        num -= val * k

    # print(val, num)

    if val == 4:
        ans += ROMAN_MAP[k] + ROMAN_MAP[k*5]

    elif val == 5:
        ans += ROMAN_MAP[5*k]

    elif val == 9:
        ans += ROMAN_MAP[k] + ROMAN_MAP[10*k]

    elif val > 5:
        ans += ROMAN_MAP[k*5] + (ROMAN_MAP[k] * (val - 5))

    elif val > 0:
        ans += ROMAN_MAP[k] * val

print(ans)

