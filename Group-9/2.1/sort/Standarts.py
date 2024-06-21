arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_arr = sorted(arr)
print(sorted_arr)

arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
arr.sort()
print(arr)

# Сортировка словаря по ключам
d = {'apple': 10, 'orange': 20, 'banana': 5, 'peach': 15}
sorted_d = dict(sorted(d.items()))
print(sorted_d)


# Сортировка словаря по значениям
sorted_d = dict(sorted(d.items(), key=lambda x: x[1]))
print(sorted_d)

t = (3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5)	
sorted_t = sorted(t)
print(tuple(sorted_t))

t_list = [(3, 1), (4, 2), (0,-2),(9,12),(1, 3), (5, 4)]
sorted_t_list = sorted(t_list, key=lambda x: x[0])
print(sorted_t_list)

s = {3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5}
sorted_s = sorted(s)
print(set(sorted_s))

