import random

from_user = '''
try:
    {0} = USER_GLOBAL['{0}']
except KeyError:
    raise NotImplementedError("Where is '{0}'?")
'''

init_code = from_user.format('davasaan')

run_test = '''
RET['code_result'] = {}
'''


def prepare_test(code, answer):
    return {
        'test_code': {
            'python-3': init_code + run_test.format(code),
        },
        'show': {
            'python-3': code,
        },
        'answer': answer,
    }


TESTS = {
    '1. Basic': [0, 9, 41, 65, 79],
    '2. Random': random.sample(range(1000), 10),
    '3. Big random': random.sample(range(2000000001), 30),
}

TESTS = {
    category: [
        prepare_test(f'davasaan({nb})', nb // 10)
        for nb in numbers
    ]
    for category, numbers in TESTS.items()
}


if __name__ == '__main__':
    # from pprint import pprint
    # pprint(TESTS, width=200)

    for tests in TESTS.values():
        for test in tests:
            # print(test['test_code']['python-3'])
            print(test['show']['python-3'])
