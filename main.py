import itertools
import string
from typing import *

import boto3

route53domains = boto3.client('route53domains', region_name='us-east-1', aws_access_key_id='your access key',
                              aws_secret_access_key='your secret key')


def generate_names(character_pool: Iterable, min_length: int, max_length: int):
    names = []
    for i in range(min_length, max_length + 1):
        names += list(
            map(''.join, filter(lambda e: e[0] != '-' and e[-1] != '-', itertools.product(character_pool, repeat=i))))
    return names


def check_domain_availability(domain_name: str):
    return route53domains.check_domain_availability(DomainName=domain_name)['Availability'] == 'AVAILABLE'


if __name__ == '__main__':
    domain_names = generate_names(string.ascii_lowercase + string.digits + '-', 2, 3)
    top_level_domains = ['.com']
    answer = []
    for name in domain_names:
        for tld in top_level_domains:
            if check_domain_availability(name + tld):
                answer.append(name + tld)
                print(name + tld)
