import algorithms as A

def test_dfs():
    graph = {
        '5' : ['3','7'],
        '3' : ['2', '4'],
        '7' : ['8'],
        '2' : [],
        '4' : ['8'],
        '8' : []
    }

    visited = set()
    A.dfs(visited, graph, '5')
    print(visited)

if __name__ == "__main__":
    test_dfs()