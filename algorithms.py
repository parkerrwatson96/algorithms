def dfs(visited, graph, node):
    '''
    A recursive implementation of depth-first search. Populates visited in depth-first order.

    params:
        - visited: set
        - graph: dict<str,List[str]>
        - node: str
    '''
    if node not in visited:
        visited.add(node)
        for neighbor in graph[node]:
            return dfs(visited, graph, neighbor)

def bfs(visited, graph, node):
    '''
    Populates visited in breadth-first order.
    
    params:
        - visited: List
        - graph: dict<str,List[str]>
        - node: str
    '''
    queue = []

    visited.append(node)
    queue.append(node)

    while queue:
        curr_node = queue.pop(0)
        for neighbor in graph[curr_node]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

def bubble_sort(aList):
    '''
    Sorts aList using bubble sort method. Not recommended for actual use.

    params:
        - aList: List
    '''
    n = len(aList)
    for i in range(n):
        sorted = True
        for j in range(n - i - 1):
            if aList[j] > aList[j + 1]:
                aList[j], aList[j + 1] = aList[j + 1], aList[j]
                sorted = False

        if sorted:
            break

    return aList