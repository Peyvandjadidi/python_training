#creat a function which returns the amount of duplicates in a string
def duplicates(str):
    dup = 0
    init = 0
    for i in range(0,len(str)) :
        init += 1
        if len(str) == init :
            break
        for j in range(init,len(str)):
            if str[i] == str[j] :
                dup += 1
                break
    return dup

print(duplicates("hellow world"))
#l duplicated 2 times + o duplicated 1 time = 3