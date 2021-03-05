class Person :
    namelst = []
    fmlylst = []
    agelst = []
    def __init__(self,firstname,lastName,age):
        self.firstname = firstname
        self.lstName = lastName
        self.age = age
        Person.namelst.append(self.firstname)
        Person.fmlylst.append(self.lstName)
        Person.agelst.append(self.age)


def people_sort(lst , attr):
    if attr == 'firstname':
        lst = sorted(Person.namelst)
    elif attr == 'lastname':
        lst = sorted(Person.fmlylst)
    elif attr == 'age' :
        lst = sorted(Person.agelst)
    return lst

p1 = Person("Michael", "Smith", 40)
p2 = Person("Alice", "Waters", 21)
p3 = Person("Zoey", "Jones", 29)
res = people_sort([p1, p2, p3], "firstname")
# Alice, Michael, Zoey
print(res)

res2 = people_sort([p1, p2, p3], "lastname")
# Jones, Smith, Waters
print(res2)

res3 = people_sort([p1, p2, p3], "age")
# 21, 29, 40
print(res3)


