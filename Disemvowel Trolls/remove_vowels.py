def disemvowel(string_):
    test = ["A", "E", "I", "O", "U"]
    for s in string_:
        if s.upper() in test:
            string_ = string_.replace(s, "")
    return string_


print(disemvowel("""No offense but,
Your writing is among the worst I've ever read"""))
