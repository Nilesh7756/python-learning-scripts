import sys

def head(filename, n):
    f = open(filename)
    for i in range(n):
        print(f.readline())

if __name__ == "__main__":    
    head(sys.argv[2], int(sys.argv[1]))