def mySqrt(x):
    k = 0
    i = 0
    while i*i <= x:
        k = i
        i += 1
    return k

x = 80
print(mySqrt(x))


# n=math.floor(math.sqrt(x))