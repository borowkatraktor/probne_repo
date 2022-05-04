print('hej, tu nowe repo')


def merged(list1, list2):
    list1.extend(list2)
    for element in list1[:]:
        if list1.count(element) >= 2:
            list1.remove(element)
    return list1

list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]

print(merged(list1, list2))


print('a to zmiana dla nowej gałęzi')
print('hej kocham cię')
