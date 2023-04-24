def get_first_word(text='Function'):
    if type(text) != str:
        return False
    words = text.split()
    if len(words) == 0:
        return 'String is empty!'
    return words[0]


print(get_first_word())
print(get_first_word(123))
print(get_first_word('check func'))
print(get_first_word('check'))
print(get_first_word('check '))
print(get_first_word(''))
print(get_first_word('   '))


def aver_of_nums(*args):
    return f'Average: {round(sum(args) / len(args))}'


print(aver_of_nums(7, 2, 5))


def check_password(password: str = ''):
    num = False
    char = False
    if len(password) >= 6:
        for i in password:
            if i.isdecimal():
                num = True
            if i.isalpha():
                char = True
        if num and char:
            return True
        else:
            return False
    else:
        return False


print(check_password('fddsdsaa'))
print(check_password('1234567'))
print(check_password('123abcd'))
print(check_password('12abc'))
print(check_password())
