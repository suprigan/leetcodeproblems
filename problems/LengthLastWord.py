def lengthOfLastWord(s):
    s = s.split()
    lw = s[-1]
    return len(lw)


s = "Hello World"
print(lengthOfLastWord(s))