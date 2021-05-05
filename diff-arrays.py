#Your goal in this kata is to implement a difference function,
# which subtracts one list from another and returns the result.
#It should remove all values from list a, which are present in list b keeping their order.

def array_diff(a, b):
    for i in set(a) :
        for x in set(b) :
            if i == x :
                for num in range(a.count(i)):
                    a.remove(i)
    return a


print(array_diff([1,2,2], [2]))
print(array_diff([1,2,3], [1, 2]))

# There are also shorter solution for this :  filter(lambda i: i not in b, a)








