# explanations for member functions are provided in requirements.py
# each file that uses a graph should import it from this file.

from collections.abc import Iterable

class Graph:
	def __init__(self, num_nodes: int, edges: Iterable[tuple[int, int]]):
		self.num_nodes = num_nodes
		self.edges = edges

	def get_num_nodes(self) -> int:
		my_set = set()
		for i in self.edges:
			my_set.add(i[0])
			my_set.add(i[1])

		return len(my_set)

	def get_num_edges(self) -> int:
		count = 0
		for i in self.edges:
			count += 1

		return count

	def get_neighbors(self, node: int) -> Iterable[int]:
		raise NotImplementedError

	# feel free to define new methods in addition to the above
	# fill in the definitions of each required member function (above),
	# and for any additional member functions you define
