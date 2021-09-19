import itertools
import string

import boto3

route53domains = boto3.client('route53domains', region_name='us-east-1', aws_access_key_id='your access key',
                              aws_secret_access_key='your secret key')


def generate_names(character_pool, min_length, max_length):
    names = []
    for i in range(min_length, max_length + 1):
        names += list(
            map(''.join, filter(lambda e: e[0] != '-' and e[-1] != '-', itertools.product(character_pool, repeat=i))))
    return names


def check_domain_availability(domain_name):
    return route53domains.check_domain_availability(DomainName=domain_name)['Availability'] == 'AVAILABLE'


if __name__ == '__main__':
    print(generate_names(string.ascii_lowercase + string.digits + '-', 2, 3))
    print(check_domain_availability('example.com'))
