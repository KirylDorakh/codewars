def disemvowel(string):
    return "".join(c for c in string if c.lower() not in "aeiou")


print(disemvowel("""No offense but,
Your writing is among the worst I've ever read"""))
