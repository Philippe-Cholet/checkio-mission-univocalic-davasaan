from tests import TESTS
from inspector import inspector
try:
    from my_solution import *
    with open('my_solution.py', encoding='utf-8') as f:
        code = f.read()
except (ModuleNotFoundError, FileNotFoundError):
    print('You need to name your python file "my_solution".')
    exit(0)

print('...Inspect your code...')
great_code, inspector_message = inspector(code, 'python-3')
print(inspector_message)
if not great_code:
    exit(0)

all_tests = (
    (test['show']['python-3'], test['answer'])
    for tests in TESTS.values()
    for test in tests
)

for code, answer in all_tests:
    user_result = eval(code)
    if user_result != answer:
        print(f'You failed the test: {code!r}.')
        print(f'Your result: {user_result}')
        print(f'Right result: {answer}')
        break
else:
    print('Well done! You passed all tests.')
