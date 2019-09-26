list = []
size = 5

print(f'Creating blank list of size {size}')
for i in range(size):
    list.append(None)
print(list)

print('\nAssigning values to list')
for i in range(size):
    list[i] = i * 10
print(list)

print('\nAppending 30 to end of list (pos 5)')
list.append(30)
print(list)

print('\nRemoving first item matching parameter value (pos 3, not 5)')
list.remove(30)
print(list)

print('\nRemoving item in position 3 (40)')
list.remove(list[3])
print(list)

print('\nPopping item in specified position 2 (20)')
list.pop(2)
print(list)

print('\nDeleting item in pos 1 (10)')
del list[1]
print(list)
