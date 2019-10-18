def selection_sort(unsorted):
    for i in range(len(unsorted)):
        min_pos = i

        for j in range(i + 1, len(unsorted)):
            if unsorted[j] < unsorted[min_pos]:
                min_pos = j

        if unsorted[min_pos] != unsorted[i]:
            unsorted[i], unsorted[min_pos] = unsorted[min_pos], unsorted[i]

    return unsorted


unsorted = [2, 4, 1, 7, 5, 3, 9, 0, 8, 6]
print(f'Unsorted list: {unsorted}')

sorted = selection_sort(unsorted)
print(f'Sorted list: {sorted}')
