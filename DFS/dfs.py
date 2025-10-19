def dfs(graph, node):

    visited = []
    stack = []

    visited.append(node)
    stack.append(node)

    while stack:
        topNode = stack.pop()
        if topNode not in visited: 
            visited.append(topNode)

        for n in reversed(graph[topNode]):
            stack.append(n)
            
    print(visited)

testGraph = {
    'A' : ['B','C'],
    'B' : ['D', 'E', 'F'],
    'C' : ['G'],
    'D' : [],
    'E' : [],
    'F' : ['H'],
    'G' : ['I'],
    'H' : [],
    'I' : []
}

firstNode = list(testGraph.keys())[0]

dfs(testGraph, firstNode)
