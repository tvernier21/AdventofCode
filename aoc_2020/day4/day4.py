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

def analyze2(passports):
    invalid = 0
    for passport in passports:
        items = passport.split()
        flag = False
        if len(items) == 8:
            flag = True
        elif "cid:" not in passport and len(items) >= 7:
            flag = True

        if flag == True:
            for item in items:
                field, value = item.split(':')
                if field == "byr" and int(value) < 1920 or int(value) > 2002:
                    invalid += 1
                    break
                elif field == "iyr" and int(value) < 2010 or int(value) > 2020:
                    invalid += 1
                    break
                elif field == "eyr" and int(value) < 2020 or int(value) > 2030:
                    invalid += 1
                    break
                elif field == "hgt":
                    if value[-2:] == "cm" and int(value[:-2]) < 150 or int(value[:-2]) > 193:
                        invalid += 1
                        break
                    elif value[-2:] == "in" and int(value[:-2]) < 59 or int(value[:-2]) > 76:
                        invalid += 1
                        break
                elif field == "hcl":
        else:
            invalid += 1


    return len(passports) - invalid

if __name__ == "__main__":
    filename = sys.argv[1]
    passports = read_file(filename)
    print(analyze1(passports))
