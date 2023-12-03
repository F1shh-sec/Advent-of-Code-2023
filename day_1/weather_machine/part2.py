def determine_floor(input):
    with open(input) as file:
        floor = 0
        position = 1
        for line in file:
            print("Length of line", len(line))
            for char in line:
                position = position + 1
                if char == "(":
                    floor = floor + 1
                    if floor < 0:
                        print("Position: ", position - 1)
                        break
                else:
                    floor = floor -1
                    if floor < 0:
                        print("Position: ", position - 1)
                        break
            print("Floor: ", floor)

def main():
    determine_floor("input.txt")


if __name__ == "__main__":
    main()