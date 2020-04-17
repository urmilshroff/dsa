def merge_sort(list):
    if len(list) <= 1:
        return list

    else:
        mid = len(list) // 2
        left_list = merge_sort(list[:mid])
        right_list = merge_sort(list[mid:])

        return merge(left_list, right_list)


def merge(left_list, right_list):
    list = []
    i, j = 0, 0

    while i < len(left_list) and j < len(right_list):
        # merges each sub list
        if left_list[i] < right_list[j]:
            list.append(left_list[i])
            i += 1
        else:
            list.append(right_list[j])
            j += 1

        list += left_list[i:]
        list += right_list[j:]
        return list


unsorted = [2, 4, 1, 7, 5, 3, 9, 0, 8, 6]
print(f'Unsorted list: {unsorted}')

sorted = merge_sort(unsorted)
print(f'Sorted list: {sorted}') # broken
