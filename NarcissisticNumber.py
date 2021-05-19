#A Narcissistic Number is a positive number which is the sum of its own digits, each raised to the power of the number of digits in a given base. In this Kata,
# we will restrict ourselves to decimal (base 10).
# For example, take 153 (3 digits), which is narcisstic:
# 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
# and 1652 (4 digits), which isn't:
# 1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938

def narcissistic(value):
    global check
    strValue = str(value)
    expo_value = len(strValue)
    total = 0
    for i in strValue:
        check = pow(int(i),expo_value)
        total += check
    return total == value


print(narcissistic(153)) #True
print(narcissistic(7)) #True, '7 is narcissistic'
print(narcissistic(371)) #True, '371 is narcissistic
print(narcissistic(122)) #False, '122 is not narcissistic'
print(narcissistic(4887)) #False, '4887 is not narcissistic'





