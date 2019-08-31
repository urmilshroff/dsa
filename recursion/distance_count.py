def distance_count(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return distance_count(n - 1) + distance_count(n - 2) + distance_count(n - 3)


n = 3
print(f'There are {distance_count(n)} ways to travel a distance of {n} units')
