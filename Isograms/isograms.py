def is_isogram(string):
    test = sorted(string.lower())
    swapped = True

    while swapped:
        swapped = False
        for i in range(len(test) - 1):
            if test[i] == test[i + 1]:
                return swapped
    return True


result = is_isogram("shfldJ")

print(result)