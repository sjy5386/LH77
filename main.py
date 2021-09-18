import itertools
import string


def generate_names(character_pool, min_length, max_length):
    names = []
    for i in range(min_length, max_length + 1):
        names += list(
            map(''.join, filter(lambda e: e[0] != '-' and e[-1] != '-', itertools.product(character_pool, repeat=i))))
    return names


if __name__ == '__main__':
    print(generate_names(string.ascii_lowercase + string.digits + '-', 2, 3))
