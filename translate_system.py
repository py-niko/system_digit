# bin(), oct(), hex()


def translate(num):
    num_bin = bin(num)
    num_oct = oct(num)
    num_hex = hex(num)


    print(num_bin[2:], num_oct[2:], num_hex[2:].upper(), sep = '\n')

translate(int(input()))