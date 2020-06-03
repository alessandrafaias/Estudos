#################Strings Advanced 2#
#################F.Strings#
'''
first_name = 'Alessandra'
last_name = 'Faias'

sentence = 'My name is {} {}'.format(first_name, last_name)
print(sentence)
'''
'''
first_name = 'Alessandra'
last_name = 'Faias'

sentence = f'My name is {first_name.upper()} {last_name.upper()}'
print(sentence)
'''
'''
person = {'name': 'Jenn', 'age': 23}

sentence = f"My name is {person['name']} and I am {person['age']} years old"
print(sentence)
'''
'''
calculation = f'4 times 11 is equal to {4 * 11}'
print(calculation)
'''
'''
for n in range(1,11):
	sentence = f'The value is {n:02}'
	print(sentence)
'''
'''
pi = 3.14159265

sentence = f'Pi is equal to {pi:.4f}'
print(sentence)
'''
'''
from datetime import datetime

birthday = datetime(1992, 2, 5)

sentence = f'Ale has a birthday on {birthday:%B %d, %Y}'
print(sentence)
'''