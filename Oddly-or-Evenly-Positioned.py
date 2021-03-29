# question : Create a function that returns the characters from a list or string (r) on odd or even positions
# , depending on the specifier s. The specifier will be "odd" for items on odd positions (1, 3, 5, ...) and
# "even" for items on even positions (2, 4, 6, ...).

def char_at_pos(r, s):
    global res
    if s == "even" :
        res = r[1::2]
    elif s == "odd" :
        res = r[::2]
    return res

print(list(char_at_pos([2, 4, 6, 8, 10], "even")))
#[4, 8]
# 4 & 8 occupy the 2nd & 4th positions
print(char_at_pos("EDABIT", "odd"))
# "EAI"


