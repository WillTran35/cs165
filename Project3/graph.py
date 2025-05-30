# explanations for member functions are provided in requirements.py
# each file that uses a graph should import it from this file.

from collections.abc import Iterable

class Graph:
	def __init__(self, num_nodes: int, edges: Iterable[tuple[int, int]]):
		self.num_nodes = num_nodes
		self.edges = edges
		self.adj_list = {}

		for i in edges:
			if i[0] not in self.adj_list:
				self.adj_list[i[0]] = [i[1]]
			else:
				self.adj_list[i[0]].append(i[1])

			if i[1] not in self.adj_list:
				self.adj_list[i[1]] = [i[0]]
			else:
				self.adj_list[i[1]].append(i[0])

	def get_num_nodes(self) -> int:
		# my_set = set()
		# for i in self.edges:
		# 	my_set.add(i[0])
		# 	my_set.add(i[1])

		return self.num_nodes

	def get_num_edges(self) -> int:
		count = 0
		for i in self.edges:
			count += 1

		return count

	def get_neighbors(self, node: int) -> Iterable[int]:
		"""given a node index, return an iterable type over the collection of its neighbors. the iterable type can be a
		list, set, generator, etc. each neighbor should appear exactly once."""
		if node not in self.adj_list:
			return []
		else:
			return self.adj_list[node]

	def get_adj_list (self):
		return self.adj_list

	def get_edges(self):
		return self.edges
	# feel free to define new methods in addition to the above
	# fill in the definitions of each required member function (above),
	# and for any additional member functions you define
