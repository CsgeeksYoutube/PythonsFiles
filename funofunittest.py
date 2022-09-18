def text(filename):
    lines=0
    chars=0
    with open(filename,'r') as f:
        for line in f:
            lines +=1
            chars += len(line)
    return (lines, chars)