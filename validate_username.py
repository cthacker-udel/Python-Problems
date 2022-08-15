import re


def validate_username(username):
    MIN_MATCH_LENGTH = 1
    return len(list(re.compile('\w{4,16}', re.MULTILINE).finditer(username))) >= MIN_MATCH_LENGTH


if __name__ == '__main__':
    print(validate_username('hhh'))
