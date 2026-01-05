from functools import lru_cache

def parse_input():
    with open('11i.txt') as file:
        graph = {}
        for line in file.read().split('\n'):
            id, connections_s = line.split(': ')
            connections = set(connections_s.split())
            graph[id] = set(connections)

        graph['out'] = set()
        return graph


def solve() -> int:
    graph = parse_input()
    
    @lru_cache(maxsize=None)
    def dfs(node, v_fft, v_dac):
        if node == 'out' and v_fft and v_dac:
            return 1
        total = 0
        for child in graph.get(node, set()):
            total += dfs(child, v_fft or node == 'fft', v_dac or node == 'dac')
        return total
    
    return dfs('svr', False, False)

print(solve())