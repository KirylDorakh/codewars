def is_isogram(string):
    return len(string) == len(set(string.lower()))


result = is_isogram("shfldJjj")

print(result)