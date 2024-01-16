def disemvowel(s):
    for i in "aeiouAEIOU":
        s = s.replace(i, '')
    return s


print(disemvowel("""No offense but,
Your writing is among the worst I've ever read"""))
