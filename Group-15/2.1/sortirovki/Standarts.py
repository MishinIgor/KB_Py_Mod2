arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_arr = sorted(arr)
print(sorted_arr)

arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
arr.sort()
print(arr)

arr = (3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5)
sorted_arr = sorted(arr)
print(sorted_arr)

# Сортировка словаря по ключам
d = {'apple': 10, 'orange': 20, 'banana': 5, 'peach': 15}
sorted_d = dict(sorted(d.items()))
print(sorted_d)


# Сортировка словаря по значениям
sorted_d = dict(sorted(d.items(), key=lambda x: x[1]))
print(sorted_d)

s = {3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5}
sorted_s = sorted(s)
print(sorted_s)
