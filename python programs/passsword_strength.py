t = int(input())
for y in range(t):
    s = input()
    cap = 0
    small = 0
    digit = 0
    special = 0
    for i in s:
        o = ord(i)
        if o >= 97 and o <= 122:
            small = 1
        elif o >= 65 and o <= 90:
            cap = 1
        elif o >= 48 and o <= 57:
            digit = 1
        elif (o == 33) or (o == 64) or (o == 35) or (o == 36) or (o == 37) or (o == 38):
            special = 1
        if (small+cap+digit+special) == 4:
            break

    print(small+cap+digit+special)