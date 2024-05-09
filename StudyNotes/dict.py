bob = {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'dev'}
sue = {'name': 'Sue Jones', 'age': 45, 'pay': 40000, 'job': 'hdw'}

bob['name'], sue['pay']
# ('Bob Smith', 40000)
# not bob[0], sue[2]
bob['name'].split()[-1]
# 'Smith'
sue['pay'] *= 1.10
sue['pay']
# 44000.0

# Other ways to make dictionaries
bob1 = dict(name='Bob Smith', age=42, pay=30000, job='dev')
sue1 = dict(name='Sue Jones', age=45, pay=40000, job='hdw')
bob1
# {'pay': 30000, 'job': 'dev', 'age': 42, 'name': 'Bob Smith'}
sue1
# {'pay': 40000, 'job': 'hdw', 'age': 45, 'name': 'Sue Jones'}
sue1 = {}
sue1['name'] = 'Sue Jones'
sue1['age'] = 45
sue1['pay'] = 40000
sue1['job'] = 'hdw'
sue1
# {'job': 'hdw', 'pay': 40000, 'age': 45, 'name': 'Sue Jones'}


# and by zipping together name/value lists:
names = ['name', 'age', 'pay', 'job']
values = ['Sue Jones', 45, 40000, 'hdw']
list(zip(names, values))
# [('name', 'Sue Jones'), ('age', 45), ('pay', 40000), ('job', 'hdw')]
sue2 = dict(zip(names, values))
sue2
# {'job': 'hdw', 'pay': 40000, 'age': 45, 'name': 'Sue Jones'}

# (handy to initialize an empty dictionary):
fields = ('name', 'age', 'job', 'pay')
record = dict.fromkeys(fields, '?')
record
# {'job': '?', 'pay': '?', 'age': '?', 'name': '?'}

bob
# {'pay': 30000, 'job': 'dev', 'age': 42, 'name': 'Bob Smith'}
sue
# {'job': 'hdw', 'pay': 40000, 'age': 45, 'name': 'Sue Jones'}
people = [bob, sue]
for person in people:
    print(person['name'], person['pay'], sep=', ')
# reference in a list
# all name, pay
# Bob Smith, 30000
# Sue Jones, 40000
for person in people:
    if person['name'] == 'Sue Jones':
        print(person['pay'])
# fetch sue's pay
# 40000
# Iteration tools using "lambda"
names = [person['name'] for person in people]
names
# ['Bob Smith', 'Sue Jones']# collect names
list(map((lambda x: x['name']), people))
# ['Bob Smith', 'Sue Jones']# ditto, generate
sum(person['pay'] for person in people)
# 70000

[rec['name'] for rec in people if rec['age'] >= 45]
# ['Sue Jones']
# SQL-ish query
[(rec['age'] ** 2 if rec['age'] >= 45 else rec['age']) for rec in people]
# [42, 2025]
G = (rec['name'] for rec in people if rec['age'] >= 45)
next(G)
# 'Sue Jones'
G = ((rec['age'] ** 2 if rec['age'] >= 45 else rec['age']) for rec in people)
G.__next__()
# 42