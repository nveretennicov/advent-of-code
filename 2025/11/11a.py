def parse_input():
    with open('11i.txt') as file:
        graph = {}
        for line in file.read().split('\n'):
            id, connections_s = line.split(': ')
            connections = set(connections_s.split())
            graph[id] = [connections, 0]

        graph['out'] = [set(), 0]
        return graph

def find_path_count(start, end, graph):
    graph[start][1] = 1
    inspected_nodes = {start}
    while inspected_nodes:
        new_inspected_nodes = set()        
        for id in inspected_nodes:
            connections, count = graph[id]
            for connection in connections:
                graph[connection][1] += count
            new_inspected_nodes |= connections

        inspected_nodes = new_inspected_nodes

    path_count = graph[end][1]
    return path_count

def solve() -> int:
    graph = parse_input()
    return find_path_count('you', 'out', graph)

print(solve())