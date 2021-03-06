#Given two sentences, return whether they are shadows of each other.
#This means that all of the word lengths are the same, but the corresponding words don't share any common letters.
def shadow_sentence(a, b):
    a_lst = a.split()
    b_lst = b.split()
    if len(a_lst) != len(b_lst):
        return False
    for i,j in zip(a_lst,b_lst):
        if len(i) != len(j) or bool(set(i)&set(j)):
            return False
    return True

# print(shadow_sentence("they are round", "fold two times"))
# print(shadow_sentence("own a boat", "buy my wine"))






