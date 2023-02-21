def addBinary(a, b):
    a = a[::-1]
    b = b[::-1]
    c = []
    r = 0
    k = max(len(a),len(b))
    m = min(len(a), len(b))
    a = [int(elem) for elem in a]
    b = [int(elem) for elem in b]
    for i in range(k-m):
        if len(a) > len(b):
            b.append(0)
        else:
            a.append(0)
    for i in range(k):
        d = a[i] + b[i] + r
        r = 0
        if d < 2:
            c.append(d)
        elif d == 2:
            d = 0
            r = 1
            c.append(d)
        else:
            d = 1
            r = 1
            c.append(d)
    if r == 1:
        c.append(r)
    c = c[::-1]
    c = ''.join([str(elem) for elem in c])
    return c




a = "101111"
b = "10"
print(addBinary(a, b))

# a, b = a[::-1], b[::-1]
# c = ""
# r = 0
# for i in range(max(len(a), len(b))):
#     digitA = ord(a[i]) + ord("0") if i < len(a) else 0
#     digitB = ord(b[i]) + ord("0") if i < len(b) else 0
#
#     d = digitA + digitB + r
#     pr = str(d % 2)
#     c = pr + c
#     r = d // 2
#     print(r)
#     if r:
#         c = "1" + c
# return c