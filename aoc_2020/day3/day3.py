import sys

def read_file(filename):

    forest = []

    with open(filename) as fin:
        for line in fin.readlines():
            forest.append(line.strip())
        fin.close()

    return forest

def analyze1(forest):
    num = 0  # number of trees we run into
    x_len = len(forest[0]) # Width of forest, without expansion
    x = 0

    for y in range(len(forest)):
        if forest[y][x] == "#":
            num += 1
        x = (x + 3) % x_len

    return num

def analyze2(forest, slopes):
    num = 1
    x_len = len(forest[0]) # Width of forest, without expansion

    for y_slope, x_slope in slopes:
        x = 0
        temp_num = 0
        for y in range(0, len(forest), y_slope):
            if forest[y][x] == "#":
                temp_num += 1
            x = (x + x_slope) % x_len

        num *= temp_num

    return num


if __name__ == "__main__":
    filename = sys.argv[1]
    forest = read_file(filename)
    print(analyze1(forest))
    slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    print(analyze2(forest, slopes))
