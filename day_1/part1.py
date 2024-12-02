import math

def main():
    first = []
    second = []
    with open('input.txt', 'r') as file:
        for line in file:
            splitLine = line.split()
            first.append( int(splitLine[0]))
            second.append( int(splitLine[1]))
    first.sort()
    second.sort()

    diff = 0
    for index in range(len(first)):
        diff += abs(first[index] - second[index])
    print(diff)

if __name__ == "__main__":
    main()