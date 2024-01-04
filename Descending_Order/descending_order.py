def descending_order(num):
    result = 0
    l: list[int] = []
    swapped = True

    if num == 0:
        return result
    if num < 0:
        num = num * -1

    while num:
        l.append(num % 10)
        num = num // 10

    # bubble sort
    while swapped:
        swapped = False
        for i in range(len(l) - 1):
            if l[i] < l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]
                swapped = True

    result = ''
    for i in l:
        result = result + str(i)

    return int(result)


r = descending_order(187493262)

print(r)
