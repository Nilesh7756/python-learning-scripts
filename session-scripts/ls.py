import os
import sys

def os_ls(path):
    ls = os.listdir(path)

    for ls_unix in ls:
        print (ls_unix)
        
if __name__ == "__main__":
    if len(sys.argv)==1:
        ls(os.getcwd())
    else:
        ls(sys.argv[1])