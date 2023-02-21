def plusOne(digits):
    k = 0
    dig = []
    for i in range(len(digits)):
        k += digits[i]*10**(len(digits)-i-1)
    k = k + 1
    print(k)
    x = [int(a) for a in str(k)]
    return x
    # while k:
    #     dig += [k % 10]
    #     k //= 10
    # return dig[::-1] or [0]


digits = [1,2,3]
print(plusOne(digits))