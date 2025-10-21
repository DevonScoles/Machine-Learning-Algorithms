def bfs(graph, node):
    visited = []
    queue = []

    visited.append(node)
    queue.append(node)

    while queue:
        print("queue: ",queue)
        print("visited: ", visited)
        s = queue.pop(0)

        for n in graph[s]:
            if n not in visited:
                visited.append(n)
                queue.append(n)

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

bfs(testGraph, 'A')
