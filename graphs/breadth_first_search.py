def bfs(root):
    found = False
    print(f'Visiting {root}...')
    visited.append(root)

    for parent in visited:
        for child in tree.get(parent).get('children'):
            if child == goal:
                print(f'Goal node found! ({goal})')
                found = True
                break
            elif child not in visited:
                print(f'Visiting {child}...')
                visited.append(child)

        if found:
            break


visited = []
tree = {
    'A': {'children': ['B', 'E', 'F']},
    'B': {'children': ['D', 'E']},
    'C': {'children': ['B']},
    'D': {'children': ['E', 'C']},
    'E': {'children': []},
    'F': {'children': []},
}

start = 'A'
goal = 'C'

bfs(start)
