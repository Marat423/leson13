def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)

print_params()
print_params(b=25)
print_params(c = [1,2,3])

values_list = [23, 'qwerty', False]
values_dict = {'a' : 2, 'b' : 33, 'c' : 24}


print_params(*values_list)
print_params(**values_dict)

values_list2 = [54.32, 'строка']

print_params(*values_list2, 42)