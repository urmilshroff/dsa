def binary_search(list, low, mid, high):
    if n == list[mid]:
        print(f'{n} found in position {mid}')

    elif n < list[mid]:
        binary_search(list, low, int((low + mid) / 2), mid)

    elif n > list[mid]:
        binary_search(list, mid, int((mid + high) / 2), high)


list = [00, 10, 20, 30, 40, 50, 60, 70, 80, 90]
list.sort()
print(f'List is {list}')
n = 70
binary_search(list, 0, int(len(list) / 2), len(list))
