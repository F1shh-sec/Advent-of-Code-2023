
def get_numbers(line):

    firstDigit = 0
    secondDigit = 0
    for character in line:
        if character.isnumeric():
            firstDigit = character
            # print(character)
            break
    for character in reversed(line):
        if character.isnumeric():
            secondDigit = character
            # print(character)
            break
    print(line, " ", int(str(firstDigit) + str(secondDigit)))
    return int(str(firstDigit) + str(secondDigit))





def main():
    print("Hello There")
    with open("input.txt") as file:
        total = 0
        for line in file:
            total = total + get_numbers(line)
            print(total)


if __name__ == "__main__":
    main()