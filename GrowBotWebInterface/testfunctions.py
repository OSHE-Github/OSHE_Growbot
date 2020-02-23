def hellonameloop(name, i):
    i = int(i)
    result = "Name repeated %s times - " % i
    for x in range(i):
        result += str(name)
        if x == i-1:
            result += "."
        else:
            result += ", "
    return result
