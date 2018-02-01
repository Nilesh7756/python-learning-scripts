
def yes(arg):
    while True:
        print(arg)
        
if __name__ == "__main__":
    yes(" ".join(sys.argv[1:]))