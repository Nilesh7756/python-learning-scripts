import sys

def echo_fun(name):
    print (name)

echo_fun(" ".join(sys.argv[1:]))