import sys

def hashnum(str):
    sum = 0
    for c in str:
        sum += ord(c)
    return sum % 10

if __name__ == '__main__':
    print(hashnum(sys.argv[1]))
