def selection_sort(unsorted):
    for i in range(len(unsorted) - 1):
        for j in range(i + 1, len(unsorted)):
            if unsorted[j] < unsorted[i]:
                unsorted[i], unsorted[j] = unsorted[j], unsorted[i]

    return unsorted


unsorted = [2, 4, 1, 7, 5, 3, 9, 0, 8, 6]
print(f'Unsorted list: {unsorted}')

sorted = selection_sort(unsorted)
print(f'Sorted list: {sorted}')
