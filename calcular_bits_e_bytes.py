print('''BIT é a menor unidade de medida computacional!
Escolha uma unidade abaixo para saber quantos bits possui a mesma... 
[1] - Byte
[2] - Kilobyte
[3] - Megabyte
[4] - Gigabyte
[5] - Terabyte
[6] - Pentabyte
[7] - Hexabyte
[8] - Yotabyte
''')

unidade = int(input("Informe a unidade desejada: "))

if unidade == 1:
    byte = 1 * 8
    print("1 byte possui {} bits.".format(byte))

if unidade == 2:
    kilobyte = 2 ** 10
    print("1 kilobyte possui {} bits.".format(kilobyte))

if unidade == 3:
    byte = 1 * 8
    print("1 byte possui {} bits.".format(byte))

if unidade == 4:
    byte = 1 * 8
    print("1 byte possui {} bits.".format(byte))

if unidade == 5:
    byte = 1 * 8
    print("1 byte possui {} bits.".format(byte))

if unidade == 6:
    byte = 1 * 8
    print("1 byte possui {} bits.".format(byte))

if unidade == 7:
    hexabyte = 2 ** 60
    print("1 Hexabyte possui {} bits.".format(hexabyte))

if unidade == 8:
    yotabyte = 2 ** 80
    print("1 Yotabyte possui {} bits.".format(yotabyte))