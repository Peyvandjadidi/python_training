#              1
#           3     5
#        7     9    11
#    13    15    17    19
# 21    23    25    27    29
# ..
#given a triangle like this and Calculate the sum of the numbers in
# the nth row of this triangle (starting at index 1) e.g.
#row_sum_odd_numbers(1); # 1
# row_sum_odd_numbers(2); # 3 + 5 = 8

def row_sum_odd_numbers(n):
    init = (n*n) - n + 1
    sum_lst = []
    sum_lst.append(init)
    for i in range(0,n-1):
        init+=2
        sum_lst.append(init)
    return sum(sum_lst)

print(row_sum_odd_numbers(2))
print(row_sum_odd_numbers(13))