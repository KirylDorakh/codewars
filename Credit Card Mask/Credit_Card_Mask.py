def maskify(cc):
    # return "#"*(len(cc)-4) + cc[-4:]
    ln = len(cc)
    if ln <= 4: return cc
    return ''.join('#'*(ln-4)) + cc[-4:]


print(maskify("4556364607935616"))