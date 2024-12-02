import math

def main():
    first = []
    second = {}

    with open('input.txt', 'r') as file:
        for line in file:
            splitLine = line.split()
            first.append(int(splitLine[0]))
            second[int(splitLine[1])] = second.get(int(splitLine[1]), 0) + 1

    sim_score = 0

    for value in first:
        sim_score += value * second.get(value, 0)

    print(sim_score)

if __name__ == "__main__":
    main()