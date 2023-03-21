from random import choice, randint, shuffle
from string import digits, punctuation, ascii_uppercase, ascii_lowercase

def generate_password(min_l = 8, max_l = 20):
    lenth = randint(min_l, max_l)
    password = ''
    lst = ['digits', 'punctuation', 'ascii_uppercase', 'ascii_lowercase']
    shuffle(lst)
    interval = 3
    max_lenth = None
    for i in range(4):
        i = lst[i]

        max_lenth = randint(1, lenth - interval)
        if interval == 0:
            max_lenth = lenth

        if i == 'digits':
            for _ in range(max_lenth):
                password += choice(digits)
                lenth -= 1
            interval -= 1
        elif i == 'punctuation':
            for _ in range(max_lenth):
                password += choice(punctuation)
                lenth -= 1
            interval -= 1
        elif i == 'ascii_uppercase':
            for _ in range(max_lenth):
                password += choice(ascii_uppercase)
                lenth -= 1
            interval -= 1
        elif i == 'ascii_lowercase':
            for _ in range(max_lenth):
                password += choice(ascii_lowercase)
                lenth -= 1
            interval -= 1
    password = list(password)
    shuffle(password)
    password = "".join(password)

    return password


if __name__ == "__main__":
    print(generate_password())

