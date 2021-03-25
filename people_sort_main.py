#Given a list of people objects, create a function that sorts the list by an attribute name. The attribute to sort by will be given as a string.

The Person class will only include these attributes in the following order
class Person :
    def __init__(self,firstname,lastName,age):
        self.firstname = firstname
        self.lastName = lastName
        self.age = age
        self.attr = ['firstname','lastName','age']

def person_sort(lst,attr):
    global res
    if attr == 'firstname' :
        namelst = []
        lst.sort(key=lambda n: n.firstname)
        for obj in lst :
            p = obj.firstname
            namelst.append(p)
        return namelst
    elif attr == 'lastName' :
        fmlylst = []
        lst.sort(key=lambda n: n.lastName)
        for obj in lst :
            p = obj.lastName
            fmlylst.append(p)
        return fmlylst
    elif attr == 'age' :
        agelst=[]
        lst.sort(key=lambda n : n.age)
        for obj in lst :
            p = obj.age
            agelst.append(p)
        return agelst



p1 = Person("Michael", "Smith", 40)
p2 = Person("Alice", "Waters", 21)
p3 = Person("Zoey", "Jones", 29)
print(person_sort([p1,p2,p3],'firstname')) #Alice,Michael,Zoey
print(person_sort([p1,p2,p3],'lastName'))
print(person_sort([p1,p2,p3],'age'))
