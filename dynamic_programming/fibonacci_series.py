def iterative(n):
    if n == 0:
        iterative_arr[1] = None

    elif n != 1:
        for i in range(2, n):
            iterative_arr[i] = iterative_arr[i - 1] + iterative_arr[i - 2]

    return iterative_arr


def recursive(n):
    if n <= 1:
        return n

    else:
        if recursive_arr[n - 1] is None:
            recursive_arr[n - 1] = recursive(n - 1)

        if recursive_arr[n - 2] is None:
            recursive_arr[n - 2] = recursive(n - 2)

        recursive_arr[n] = recursive_arr[n - 1] + recursive_arr[n - 2]
        print(recursive_arr[n])
        return recursive_arr[n]


n = 7
iterative_arr = [None for i in range(n)]
recursive_arr = [None for i in range(n + 1)]

iterative_arr[0], iterative_arr[1] = 0, 1
recursive_arr[0], recursive_arr[1] = 0, 1

print(f'Fibonacci series of {n} using iterative:')
print(iterative(n))
print(f'Fibonacci series of {n} using recursive:')
print(recursive(n))
