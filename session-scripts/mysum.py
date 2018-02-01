
import sys

def multi_int(num):
    s = 0
    for i in num:
        s += int(i)
    return s
        
if __name__ == "__main__":
    
    print (sum(sys.argv[1:]))