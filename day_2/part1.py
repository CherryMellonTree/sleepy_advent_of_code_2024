import math

def main():
    data = []
    with open('input.txt', 'r') as file:
        for line in file:
            data.append(list(map(int, line.split())))
    total_safe = 0
    for entry in data:
        valid = True
        increasing = all(i < j for i, j in zip(entry, entry[1:]))
        decreasing = all(i > j for i, j in zip(entry, entry[1:]))
        valid = valid and (increasing or decreasing)

        valid_increase = all(abs(i - j) <= 3 and abs(i - j)>=1 for i, j in zip(entry, entry[1:]) )
        valid = valid and valid_increase

        if valid:
            total_safe+=1
    print(total_safe)

            



if __name__ == "__main__":
    main()