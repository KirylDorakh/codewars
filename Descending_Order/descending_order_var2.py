def descending_order(num):
    result = int(''.join(sorted(str(num), reverse=True)))
    return result


r = descending_order(187493262)

print(r)
