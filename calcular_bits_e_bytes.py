print('''\nBIT é a menor unidade de medida computacional!
Equivale a 1 caractere.\n
Escolha uma unidade abaixo para saber quantos bits a mesma possui...\n 
[1] - Byte
[2] - KiloByte
[3] - MegaByte
[4] - GigaByte
[5] - TeraByte
[6] - PetaByte
[7] - ExaByte
[8] - ZettaByte
[9] - YottaByte
''')

unidade = int(input("Informe a unidade desejada: "))

# Byte.
if unidade == 1:
    byte = 8 * 1
    print("\n1 Byte possui {} bits.\n".format(byte))

# KiloByte.
if unidade == 2:
    kilobyte = 8 * 1
    bit = 2 ** 10
    print("\n-> 1 Kilobyte possui {} Bytes.".format(kilobyte))
    print("-> 1 Kilobyte possui {} Bits.\n".format(bit))

# MegaByte.
if unidade == 3:
    megabyte = 1 * 1024
    bit = 2 ** 20
    print("\n-> 1 Megabyte possui {} Kilobytes.".format(megabyte))
    print("-> 1 Megabyte possui {} Bits.\n".format(bit))

# GigaByte.
if unidade == 4:
    gigabyte = 1 * 1024
    bit = 2 ** 30
    print("\n-> 1 GigaByte possui {} MegaBytes.".format(gigabyte))
    print("-> 1 GigaByte possui {} Bits.\n".format(bit))

# TeraByte.
if unidade == 5:
    terabyte = 1 * 1024
    bit = 2 ** 40
    print("\n-> 1 TeraByte possui {} GigaBytes.".format(terabyte))
    print("-> 1 TeraByte possui {} Bits.\n".format(bit))

# PetaByte.
if unidade == 6:
    petabyte = 1 * 1024
    bit = 2 ** 50
    print("\n-> 1 PetaByte possui {} TeraBytes.".format(petabyte))
    print("-> 1 PetaByte possui {} Bits.\n".format(bit))

# 7. ExaByte
if unidade == 7:
    exabyte = 1 * 1024
    bit = 2 ** 60
    print("\n-> 1 ExaByte possui {} PetaBytes.".format(exabyte))
    print("-> 1 ExaByte possui {} Bits.\n".format(bit))

# 8. ZettaByte
if unidade == 8:
    zettabyte = 1 * 1024
    bit = 2 ** 70
    print("\n-> 1 ZettaByte possui {} ExaBytes.".format(zettabyte))
    print("-> 1 ZettaByte possui {} Bits.\n".format(bit))

# 9. YottaByte
if unidade == 9:
    yottabyte = 1 * 1024
    bit = 2 ** 80
    print("\n-> 1 YottaByte possui {} ZettaBytes.".format(yottabyte))
    print("-> 1 YottaByte possui {} Bits.\n".format(bit))