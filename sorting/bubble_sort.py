def bubble_sort(unsorted):
    for i in range(len(unsorted) - 1):
        for j in range(len(unsorted) - 1 - i):
            if unsorted[j] > unsorted[j + 1]:
                unsorted[j], unsorted[j + 1] = unsorted[j + 1], unsorted[j]

    return unsorted


unsorted = [2, 4, 1, 7, 5, 3, 9, 0, 8, 6]
print(f'Unsorted list: {unsorted}')

sorted = bubble_sort(unsorted)
print(f'Sorted list: {sorted}')
