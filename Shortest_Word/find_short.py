def find_short(s):
    s = s.split()
    lower = len(s[0])
    for i in s:
        # print(len(i))
        if len(i) <= lower:
            lower = len(i)
    return lower # l: shortest word length


print(find_short("bitcoin take over the world maybe who knows perhaps"))


def find_short2(s):
    return min([len(i) for i in s.split()])


print(find_short2("bitcoin take over the world maybe who knows perhaps"))
