items = [2,25,9,36]
divisor = 12
def divisble(items,divisor):
    for item in items:
        if item % divisor == 0:
            return item
    items.append(divisor)
    return divisor

dividend = divisble(items,divisor)
print("{items} contains {dividend} which is a multiple of {divisor}".format(**locals()))