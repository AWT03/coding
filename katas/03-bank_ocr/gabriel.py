number_0 = " _ " \
           "| |" \
           "|_|"
number_1 = "   " \
           "  |" \
           "  |"
number_2 = " _ " \
           " _|" \
           "|_ "
number_3 = " _ " \
           " _|" \
           " _|"
number_4 = "   " \
           "|_|" \
           "  |"
number_5 = " _ " \
           "|_ " \
           " _|"
number_6 = " _ " \
           "|_ " \
           "|_|"
number_7 = " _ " \
           "  |" \
           "  |"
number_8 = " _ " \
           "|_|" \
           "|_|"
number_9 = " _ " \
           "|_|" \
           " _|"

translator = {
    number_0: "0",
    number_1: "1",
    number_2: "2",
    number_3: "3",
    number_4: "4",
    number_5: "5",
    number_6: "6",
    number_7: "7",
    number_8: "8",
    number_9: "9"
}

often_mistakes = {
    "0": ["8"],
    "1": ["7"],
    "2": ["3"],
    "3": ["9"],
    "4": ["4"],
    "5": ["6", "9"],
    "6": ["5", "8"],
    "7": ["1"],
    "8": ["0", "6", "9"],
    "9": ["5", "8", "3"],
    "?": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
}


def validate_account_number(account_number):
    if "?" in account_number:
        return False
    checksum = 0
    for index, char in enumerate(reversed(list(account_number))):
        checksum += (index+1) * int(char)
    return checksum % 11 == 0


def translate_numbers(numbers):
    account_number = ''
    for number in numbers:
        try:
            account_number += translator[numbers[number]]
        except KeyError:
            account_number += "?"
    return account_number


def read_file(file_path):
    f = open(file_path)
    numbers = {0: '', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: ''}
    for line in f:
        index = 0
        for i in range(0, 27, 3):
            if (not line[i:i+3] and line != "\n") or line == "\n":
                numbers[index] += "   "
            else:
                numbers[index] += line[i:i + 3].replace("\n", " ")
            index += 1
    f.close()
    return translate_numbers(numbers)


def get_status(file_path):
    account_number = read_file(file_path)
    if "?" in account_number:
        return account_number + " ILL"
    if not validate_account_number(account_number):
        return account_number + " ERR"
    return account_number


def get_possibles(file_path):
    account_number = read_file(file_path)
    possible_values = []
    if "?" in account_number or not validate_account_number(account_number):
        for index, char in enumerate(account_number):
            for rotation in often_mistakes[char]:
                possible = list(account_number)
                possible[index] = rotation
                if validate_account_number("".join(possible)):
                    possible_values.append("".join(possible))
    if not possible_values:
        return account_number + " ILL"
    elif len(possible_values) == 1:
        return possible_values[0]
    else:
        return account_number + " AMB " + str(sorted(possible_values))
