bob = [['name', 'Bob Smith'], ['age', 42], ['pay', 10000]]
sue = [['name', 'Sue Jones'], ['age', 45], ['pay', 20000]]
people = [bob, sue]
for person in people:
    print(person[0][1], person[2][1])

[person[0][1] for person in people]

for person in people:
    print(person[0][1].split()[-1])
    person[2][1] *= 1.10

for person in people: print(person[2])

for person in people:
    for (name, value) in person:
        if name == 'name': print(value)

def field(record, label):
    for (fname, fvalue) in record:
        if fname == label:
            return fvalue

# find any field by name
field(bob, 'name')
field(sue, 'pay')

for rec in people:
    print(field(rec, 'age'))