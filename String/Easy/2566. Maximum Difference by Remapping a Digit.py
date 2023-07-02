def minMaxDifference(num):
    digs = str(num)
    digs_min = ''
    digs_max = ''
    for d in digs:
        if d != '9':
            digs_max = digs.replace(d, '9')
            break
        digs_max = str(num)

    for d in digs:
        if d != '0':
            digs_min = digs.replace(d, '0')
            break
        digs_min = '0'

    return int(digs_max) - int(digs_min)


print(minMaxDifference(11891))
print(minMaxDifference(90))
print(minMaxDifference(0))
print(minMaxDifference(111111))
print(minMaxDifference(99999))
