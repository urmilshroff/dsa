def dfs(root):
    if root == goal:
        print(f'Goal node found! ({goal})')

    elif root not in visited:
        print(f'Visiting {root} and its children...')
        visited.append(root)
        for node in tree.get(root).get('children'):
            if node is not None:
                dfs(node)


visited = []
tree = {
    'A': {'children': ['B', 'E', 'F']},
    'B': {'children': ['D', 'E']},
    'C': {'children': ['B']},
    'D': {'children': ['C', 'E']},
    'E': {'children': []},
    'F': {'children': []},
}

start = 'A'
goal = 'F'

dfs(start)
