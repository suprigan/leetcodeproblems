def climbStairs(n):
    c = 0
    i = 1
    k = 1
    p = 1
    if n == 1:
        c = 1
    while i < n:
        c = p + k
        p = k
        k = c
        i += 1
    return c

n = 1
print(climbStairs(n))
