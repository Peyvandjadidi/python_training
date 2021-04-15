class NestedIterator:
    def __init__(self,nestedList):
        def flatten(lst):
            if not isinstance(lst,list):
                return lst
            else:
                _lst = []
                for i in lst :
                    _lst.extend(i)
        self.nestedList = flatten(nestedList)

    def next(self):
        if self.hasNext():
            self.nestedList.pop(0)
        else:
            raise StopIteration

    def hasNext(self):
        if len(self.nestedList)> 0 :
            return True
        else:
            return False





x ,actual = NestedIterator([[1, 1], 2, [1, 1]]) , []
while x.hasNext():
    actual.append(x.next())
print(actual)

# def flattenNestedList(nestedList):
#     ''' Converts a nested list to a flat list '''
#     flatList = []
#     # Iterate over all the elements in given list
#     for elem in nestedList:
#         # Check if type of element is list
#         if isinstance(elem, list):
#             # Extend the flat list by adding contents of this element (list)
#             flatList.extend(elem)
#         else:
#             # Append the element to the list
#             flatList.append(elem)
#     return flatList

# print(flattenNestedList([[1, 1], 2, [1, 1]]))



