import numpy as np
import itertools


def are_isomorphic(m_0: list[list[int]], m_1: list[list[int]]) -> bool:
	matrix_0 = np.array(m_0)
	matrix_1 = np.array(m_1)

	# Testa todas as permutações pra ver bate com a outra matriz
	n = matrix_0.shape[0]
	for perm in itertools.permutations(range(n)):
		indices: list[int] = list(perm)
		permuted_matrix = matrix_1[indices][:, indices]
		if np.all(permuted_matrix == matrix_0):
			return True

	return False


def is_regular(adjacency_matrix: list[list[int]]) -> bool:
	"""Todos os vértices têm que ter o mesmo grau"""
	degree = sum(adjacency_matrix[0])
	for row in adjacency_matrix:
		if sum(row) != degree:
			return False
	return True


def is_wheel(incidence_matrix: list[list[int]]) -> bool:
	"""1 vértice de grau n-1 e n-1 vértices de grau 3"""
	n_vertices = len(incidence_matrix)
	n_edges = len(incidence_matrix[0])
	if n_edges != (n_vertices - 1) * 2:
		return False

	row_sums: list[int] = [sum(row) for row in incidence_matrix]

	transpose = zip(*incidence_matrix)
	col_sums: list[int] = [sum(row) for row in transpose]

	n = n_vertices
	count_n = row_sums.count(n - 1)
	count_3 = row_sums.count(3)
	if count_n == 1 and count_3 == n - 1:
		return True

	return False


import numpy as np


def generate_incidence_matrix_for_bipartite_graph(m: int, n: int) -> list[list[int]]:
	"""Faz a matriz com 0s, depois bota 1 onde precisa"""
	incidence_matrix = np.zeros((m + n, m * n))

	for i in range(m):
		for j in range(n):
			incidence_matrix[i][i*n + j] = 1
			incidence_matrix[m + j][i*n + j] = 1
	return incidence_matrix
