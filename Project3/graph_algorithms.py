# explanations for these functions are provided in requirements.py
# from Project3 import requirements
import random


from graph import Graph

def bfs(graph, start):
    """breadth first search: """
    distances = {x: -1 for x in graph}  # initialize all distances to -1, meaning not visited
    distances[start] = 0
    queue = [start]
    front = 0

    while front < len(queue):
        node = queue[front]
        front += 1

        for neighbor in graph[node]:
            if distances[neighbor] == -1:
                distances[neighbor] = distances[node] + 1
                queue.append(neighbor)

    return distances

def get_key(distances:dict, target):
    # print(distances)
    for key, value in distances.items():
        if target == value:
            return key

def get_diameter(graph: Graph) -> int:
    """return the approximate graph diameter using a heuristic function."""
    if not graph:
        return 0

    graph_list = graph.get_adj_list()
    max_value = 0
    start = random.choice(list(graph_list.keys()))  # choose random node
    distances = bfs(graph_list, start)  # dictionary of all paths from start node
    farthest = max(distances.values())  # gets max distance
    # print(start, farthest)
    farthest_key = get_key(distances, farthest) # get the corresponding key to that distance

    while farthest > max_value:
        max_value = farthest
        # print(f"farthest key: {farthest_key}")
        distances = bfs(graph_list, farthest_key)
        farthest = max(bfs(graph_list, farthest_key).values())
        farthest_key = get_key(distances, farthest)

    return max_value


def compute_denominator(graph):
    graph_adj_list = graph.get_adj_list()
    sum = 0
    for i in graph_adj_list:
        degree = len(graph_adj_list[i])
        sum += degree * (degree - 1) / 2
    return sum




# def create_degeneracy_order(graph_obj):
#     graph = graph_obj.get_adj_list()
#     degree = {v: len(neighbors) for v, neighbors in graph.items()}
#     ordering = []
#     visited = set()
#
#     while len(visited) < len(graph):
#         min_deg_node = None
#         min_deg = float("inf")
#
#         for v in graph:
#             if v not in visited and degree[v] < min_deg:
#                 min_deg = degree[v]
#                 min_deg_node = v
#
#         if min_deg_node is None:
#             break
#
#         visited.add(min_deg_node)
#         ordering.append(min_deg_node)
#
#         for neighbor in graph[min_deg_node]:
#             if neighbor not in visited:
#                 degree[neighbor] -= 1
#
#     return ordering

def create_degeneracy_order(graph_obj):
    from collections import deque

    graph = graph_obj.get_adj_list()
    n = len(graph)
    degrees = {v: len(neighs) for v, neighs in graph.items()}
    max_deg = max(degrees.values(), default=0)

    buckets = [deque() for _ in range(max_deg + 1)]
    for node, deg in degrees.items():
        buckets[deg].append(node)

    ordering = []
    visited = set()

    for _ in range(n):
        for deg in range(max_deg + 1):
            if buckets[deg]:
                u = buckets[deg].pop()
                break
        ordering.append(u)
        visited.add(u)
        for v in graph[u]:
            if v not in visited:
                d = degrees[v]
                degrees[v] -= 1
                buckets[d].remove(v)
                buckets[d - 1].append(v)

    return ordering

def count_triangles(graph):
    degen_list = create_degeneracy_order(graph)
    graph_adj_list = graph.get_adj_list()
    order_index = {v: i for i, v in enumerate(degen_list)}

    forward = {
        u: sorted([v for v in graph_adj_list[u] if order_index[u] < order_index[v]])
        for u in graph_adj_list
    }

    count = 0

    for u in degen_list:
        list1 = forward[u]
        for v in list1:
            list2 = forward[v]
            i = j = 0
            while i < len(list1) and j < len(list2):
                if list1[i] == list2[j]:
                    count += 1
                    i += 1
                    j += 1
                elif list1[i] < list2[j]:
                    i += 1
                else:
                    j += 1

    return count




def get_clustering_coefficient(graph: Graph) -> float:
    # C = 3*number of triangles / number of 2-edge paths

    return 3 * count_triangles(graph) / compute_denominator(graph)

def get_degree_distribution(graph: Graph) -> dict[int, int]:
    histogram = {}
    graph_adj_list = graph.get_adj_list()
    for i in graph_adj_list.keys():
        degree = len(graph_adj_list[i])
        if degree not in histogram:
            histogram[degree] = 1
        else:
            histogram[degree] += 1

    return histogram
# if __name__ == "__main__":
#     graph = requirements.Graph(10,
#                                {(0, 3), (0, 7), (1, 4), (1, 5), (1, 6), (2, 3), (2, 7), (3, 4), (3, 8), (3, 9), (4, 5),
#                                 (4, 9), (5, 6), (8, 9)})
#     # print(graph.get_adj_list())
#     # print(get_diameter(graph))
#
#     print(create_degeneracy_order(graph))