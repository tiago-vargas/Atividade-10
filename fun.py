import numpy as np
import itertools


def are_isomorphic(m_0: list[list[int]], m_1: list[list[int]]):
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


def is_regular(adjacency_matrix: list[list[int]]):
	# Todos os vértices têm que ter o mesmo grau
	degree = sum(adjacency_matrix[0])
	for row in adjacency_matrix:
		if sum(row) != degree:
			return False
	return True
