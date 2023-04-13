dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
r = input('Введите римское число: ')

result = 0
k = 0
for i in r[::-1]:
    if dict[i] >= k:
        result += dict[i]
        k = dict[i]
    else:
        result -= dict[i]
print(result)
