def print_formatted(n):
    # your code goes here
    length = len(str(bin(n)).replace('0b',''))
    for i in range(1, n + 1):
        d = str(i).rjust(length, ' ')
        b = bin(i)[2:].rjust(length, ' ')
        o = oct(i)[2:].rjust(length, ' ')
        h = hex(i)[2:].rjust(length, ' ').upper()
        print(d, o, h, b)


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
