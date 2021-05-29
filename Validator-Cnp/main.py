def verify_sex(cnp):

    if cnp[0] in ['7', '1', '2', '3', '4', '5', '6', '8', '9']:
        return True
    return False


def verify_birth_date(cnp):

    if 0 < int(cnp[3:5]) <= 12:
        if 0 < int(cnp[5:7]) <= 31:
            return True
    return False


def verify_region(cnp):

    if 0 < int(cnp[7:9]) <= 46 or int(cnp[7:9]) in [51,52]:
        return True
    return False


def verify_nnn(cnp):

    if cnp[9:12] != "000":
        return True
    return False


def verify_c(cnp):
    number = '279146358279'
    res = 0
    for a, b in zip(number, cnp):
        res += int(a) * int(b)
    res = res % 11
    if res == 10:
        if cnp[12] == '1':
            return True
        return False
    elif int(cnp[12]) == res:
        return True
    return False


if __name__ == '__main__':

    not_valid_cnp = True

    while not_valid_cnp is True:
        cnp = input("Please enter a valid cnp or 'exit' to close the program")
        if cnp == 'exit':
            break
        if cnp.isdecimal() is not True:
            print("Cnp contains just digits.")
            continue
        if len(cnp) != 13:
            print("A valid cnp contains 13 digits.")
        if verify_sex(cnp) is not True:
            continue
        if verify_birth_date(cnp) is not True:
            continue
        if verify_region(cnp) is not True:
            continue
        if verify_nnn(cnp) is not True:
            continue
        if verify_c(cnp) is not True:
            continue
        not_valid_cnp = False

