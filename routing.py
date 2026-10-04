"""Simple-route selection helper."""
from math import inf

def fastest_simple_route(graph, source, target, max_links=3):
    """Return (delay, path) for the fastest simple path with <= max_links."""
    best = (inf, None)
    def dfs(node, path, delay):
        nonlocal best
        if delay >= best[0]: return
        if node == target:
            best = (delay, path[:]); return
        if len(path) - 1 >= max_links: return
        for nxt, weight in graph.get(node, []):
            if nxt not in path:
                dfs(nxt, path + [nxt], delay + weight)
    dfs(source, [source], 0.0)
    return best
