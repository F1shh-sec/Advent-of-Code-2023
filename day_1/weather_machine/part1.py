def determine_floor(input):
    with open(input) as file:
        total = 0
        for line in file:
            for char in line:
                if char == "(":
                    total = total + 1
                else:
                    total = total -1
            print(total)

def main():
    determine_floor("input.txt")


if __name__ == "__main__":
    main()