def is_isogram(string):
    for letter in string:
        if string.count(letter) > 1: return False
    return True


result = is_isogram("shfldJJ")

print(result)