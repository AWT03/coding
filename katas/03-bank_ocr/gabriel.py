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


def validate_account_number(account_number):
    if "?" in account_number:
        return False
    checksum = 0
    for index, char in enumerate(reversed(list(account_number))):
        checksum += (index+1) * int(char)
    return checksum % 11 == 0


def get_numbers(file):
    numbers = {0: '', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: ''}
    for line in file:
        index = 0
        for i in range(0, 27, 3):
            if (not line[i:i + 3] and line != "\n") or line == "\n":
                numbers[index] += "   "
            else:
                numbers[index] += line[i:i + 3].replace("\n", " ")
            index += 1
    return numbers


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
    numbers = get_numbers(f)
    f.close()
    return translate_numbers(numbers)


def get_status(file_path):
    account_number = read_file(file_path)
    if "?" in account_number:
        return account_number + " ILL"
    if not validate_account_number(account_number):
        return account_number + " ERR"
    return account_number


def do_rotation(number):
    list_possible = []
    for index, char in enumerate(number):
        possible = list(number)
        for value in [" ", "_", "|"]:
            possible[index] = value
            if "".join(possible) in translator:
                list_possible.append(translator["".join(possible)])
    return list(dict.fromkeys(list_possible))


def get_values(numbers, index):
    account_number = translate_numbers(numbers)
    possible_values = []
    for option in do_rotation(numbers[index]):
        possible = list(account_number)
        possible[index] = option
        if validate_account_number("".join(possible)):
            possible_values.append("".join(possible))
    return possible_values


def get_possibles(file_path):
    f = open(file_path)
    numbers = get_numbers(f)
    f.close()
    account_number = translate_numbers(numbers)
    possible_values = []
    if "?" in account_number:
        for index in [i for i, e in enumerate(list(account_number)) if e == "?"]:
            possible_values += get_values(numbers, index)
    elif not validate_account_number(account_number):
        for index in range(len(account_number)):
            possible_values += get_values(numbers, index)
    if not possible_values:
        return account_number + " ILL"
    elif len(possible_values) == 1:
        return possible_values[0]
    else:
        return account_number + " AMB " + str(sorted(possible_values))

