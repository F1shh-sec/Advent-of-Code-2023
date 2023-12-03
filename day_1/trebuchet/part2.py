import re


def get_numbers(line):
    words = re.findall("(1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine)", line)
    new_reg = "(" + "(1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine)"[::-1][1:-1] + ")"
    words2 = re.findall(new_reg, line[::-1])
    if words != []:
        first_number = word_to_num(words[0])
        second_number = word_to_num(words2[0])
        return int(str(first_number) + str(second_number))
    else: 
        return 0


def word_to_num(word):
    number = 0
    match word:
        case "one" | "eno":
            number = 1
        case "two"| "owt":
            number = 2
        case "three" | "eerht":
            number = 3
        case "four" | "ruof":
            number = 4
        case "five" | "evif":
            number = 5
        case "six" | "xis":
            number = 6
        case "seven"| "neves":
            number = 7
        case "eight" | "thgie":
            number = 8
        case "nine" | "enin":
            number = 9
        case default:
            number = int(word)
    return number



def main():
    print("Hello There")
    with open("input.txt") as file:
        total = 0
        for line in file:
            total = total + get_numbers(line)
        print("Total:", total)


if __name__ == "__main__":
    main()