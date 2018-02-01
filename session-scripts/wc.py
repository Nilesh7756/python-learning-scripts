import sys

def count_words(file):
    return len(open(file).read().split())

def count_chars(file):
    return len(open(file).read())

def count_lines(file):
    return len(open(file).readlines())


if __name__ == "__main__":
    file = sys.argv[1]
    print(count_lines(file), count_words(file), count_chars(file), file)