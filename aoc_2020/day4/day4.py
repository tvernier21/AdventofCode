import sys

def read_file(filename):

    passports = []

    with open(filename) as fin:
        passport = ""
        for line in fin.readlines():
            if line == "\n":
                passports.append(passport)
                passport = ""
            passport += " " + line.strip()

        passports.append(passport)
        fin.close()

    return passports

def analyze1(passports):
    valid = 0
    for passport in passports:
        items = passport.split()
        if len(items) == 8:
            valid += 1
        elif "cid:" not in passport and len(items) >= 7:
            valid += 1

    return valid

def validate_passport(passport):
    items = passport.split()

    if len(items) < 7:
        return False
    elif len(items) == 7 and "cid:" in passport:
        print(passport)
        return False

    for item in items:
        field, value = item.split(':')
        if field == "byr":
            if int(value) < 1920 or int(value) > 2002:
                return False
        elif field == "iyr":
            if int(value) < 2010 or int(value) > 2020:
                return False
        elif field == "eyr":
            if int(value) < 2020 or int(value) > 2030:
                return False
        elif field == "hgt":
            if value[-2:] == "cm":
                if int(value[:-2]) < 150 or int(value[:-2]) > 193:
                    return False
            elif value[-2:] == "in":
                if int(value[:-2]) < 59 or int(value[:-2]) > 76:
                    return False
            else:
                return False
        elif field == "hcl":
            if value[0] != "#":
                return False
            if len(value[1:]) == 6:
                for i in range(1, len(value)):
                    if value[i] not in "abcdef0123456789":
                        return False
            else:
                return False
        elif field == "ecl":
            if value not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                return False
        elif field == "pid":
            if len(value) != 9:
                return False

    return True

def analyze2(passports):
    valid = 0
    for passport in passports:
        if validate_passport(passport):
            valid += 1
    return valid

if __name__ == "__main__":
    filename = sys.argv[1]
    passports = read_file(filename)
    print(analyze1(passports))
    print(analyze2(passports))
