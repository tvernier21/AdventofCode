#from helper import *
import sys


def part1(inlist, YEAR):
    cutoff = (YEAR+1)//2

    x = 0
    # Split the list into upper and lower half
    for i in range(len(inlist)):
        if inlist[i] >= cutoff:
            inlist[x], inlist[i] = inlist[i], inlist[x]
            x += 1

    # Find the compatible items in the upper and lower halfs
    for i in range(x):
        if inlist[i] == cutoff and cutoff%2 == 0: 
            for j in range(i+1, x): 
                if inlist[i] + inlist[j] == YEAR:
                    return inlist[i], inlist[j]
        else:
            for j in range(x, len(inlist)):
                if inlist[i] + inlist[j] == YEAR:
                    return inlist[i], inlist[j]

    return 0, 0


def part2(inlist, YEAR):

    for i in range(len(inlist) - 2):
        a = inlist[i]
        b, c = part1(inlist[i+1:], YEAR-a)

        if b + c == YEAR-a:
            return a, b, c 

    return 0,0,0


def read_file(filename):

    items = []

    with open(filename) as fin:
        for line in fin.readlines():
            items.append(int(line))

        fin.close()

    return items


def main():
    year = 2020

    filename = sys.argv[1]
    data = read_file(filename)
    result1 = part1(data, year)
    result2 = part2(data, year)


    print(result1)
    print(result1[0] * result1[1])
    print(result2[0] * result2[1] * result2[2])


main()
