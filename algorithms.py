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
    Sorts aList using bubble sort method + early stopping. Not recommended for actual use.

    params:
        - aList: List
    '''
    n = len(aList)
    for i in range(n):
        sorted = True
        for j in range(n-i-1):
            if aList[j] > aList[j+1]:
                aList[j], aList[j+1] = aList[j+1], aList[j]
                sorted = False

        if sorted:
            break

    return aList

def insertion_sort(aList):
    '''
    Sorts aList using insertion sort method. Not recommeded for actual use

    params:
        - aList: List
    '''
    for i in range(1, len(aList)):
        key_item = aList[i]
        j = i - 1

        while j >= 0 and aList[j] > key_item:
            aList[j+1] = aList[j]
            j -= 1

        aList[j+1] = key_item

    return aList


def merge_sort(aList):
    if len(aList) < 2:
        return aList

    midpoint = len(aList) // 2

    return merge(merge_sort(aList[:midpoint]), merge_sort(aList[midpoint:]))


def merge(left, right):
    if len(left) == 0:
        return right

    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    while len(result) < len(left) + len(right):
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result