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




def create_degeneracy_order(graph_obj):
    graph = graph_obj.get_adj_list()
    degree = {v: len(neighbors) for v, neighbors in graph.items()}
    ordering = []
    visited = set()

    while len(visited) < len(graph):
        min_deg_node = None
        min_deg = float("inf")

        for v in graph:
            if v not in visited and degree[v] < min_deg:
                min_deg = degree[v]
                min_deg_node = v

        if min_deg_node is None:
            break

        visited.add(min_deg_node)
        ordering.append(min_deg_node)

        for neighbor in graph[min_deg_node]:
            if neighbor not in visited:
                degree[neighbor] -= 1

    return ordering

def count_triangles(graph):
    count = 0
    degen_list = create_degeneracy_order(graph)
    graph_adj_list = graph.get_adj_list()
    order_index = {v: i for i, v in enumerate(degen_list)}

    forward_neighbors = {
        u: [v for v in graph_adj_list[u] if order_index[u] < order_index[v]]
        for u in graph_adj_list
    }

    for u in degen_list:
        # u_neighbors = [v for v in graph_adj_list[u] if order_index[u] < order_index[v]]
        # neighbor_set = set(u_neighbors)
        # for v in u_neighbors:
        #     v_neighbors = [w for w in graph_adj_list[v] if order_index[v] < order_index[w]]
        #     for w in v_neighbors:
        #         if w in neighbor_set:
        #             count += 1
        u_set = set(forward_neighbors[u])
        for v in forward_neighbors[u]:
            v_set = set(forward_neighbors[v])
            count += len(u_set & v_set)

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