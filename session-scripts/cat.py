
import sys

def cat_unix(file_name):
    
    print (open(file_name).read())
    
    
if __name__ == "__main__":
    
    for file_name in sys.argv[1:]:
        cat_unix(file_name)