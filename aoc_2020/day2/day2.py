import sys

def read_file(filename):

    policies = []
    passwords = []

    with open(filename) as fin:
        for line in fin.readlines():
            policy, password = line.split(':')
            passwords.append(password.strip())
            policies.append(policy)
        fin.close()

    return policies, passwords

def analyze1(policies, password):
    valid = 0
    for policy, password in zip(policies, password):
        range, letter = policy.split(' ')
        lower, upper = range.split('-')

        num_letter = password.count(letter)
        if num_letter >= int(lower) and num_letter <= int(upper):
            valid += 1
    return valid

def analyze2(policies, password):
    valid = 0
    for policy, password in zip(policies, password):
        range, letter = policy.split(' ')
        idx1, idx2 = range.split('-')

        flag = False
        if int(idx1) <= len(password) and password[int(idx1)-1] == letter:
            flag = True
        if int(idx2) <= len(password) and password[int(idx2)-1] == letter:
            if flag == True:
                flag = False
            else:
                flag = True
        if flag:
            valid += 1


    return valid


if __name__ == "__main__":
    filename = sys.argv[1]
    policies, passwords = read_file(filename)
    print(analyze1(policies, passwords))
    print(analyze2(policies, passwords))
