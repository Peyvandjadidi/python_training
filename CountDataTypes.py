# Given a function that accepts unlimited arguments, check and count how many data types
# are in those arguments. Finally return the total in a list.
# List order is: [int, str, bool, list, tuple, dictionary]

def count_Datatypes(*args):
    listOrders = [int,str,bool,list,tuple,dict]
    mylst = [type(i) for i in args]
    res = [mylst.count(x) for x in listOrders]
    return res

print(count_Datatypes([1,2,3],"hi",{},[7],"hey"))




