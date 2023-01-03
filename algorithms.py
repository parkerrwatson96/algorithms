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
    queue = 0

    visited.append(node)
    queue.append(node)

    while queue:
        curr_node = queue.pop(0)
        for neighbor in graph[curr_node]:
            if neighbor not in visited:
                visited.append(curr_node)
                queue.append(curr_node)
