def xor(a, b):
    result = []
    for i in range(1, len(b)):
        result.append('0' if a[i] == b[i] else '1')
    return ''.join(result)

def crc(data, divisor):
    pick = len(divisor)
    tmp = data[0:pick]

    while pick < len(data):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + data[pick]
        else:
            tmp = xor('0'*pick, tmp) + data[pick]
        pick += 1

    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0'*pick, tmp)

    return tmp

data = "1101011011"
divisor = "10011"

print("CRC remainder:", crc(data, divisor))
