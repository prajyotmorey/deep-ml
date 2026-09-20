import numpy as np
def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	matrix=np.array(matrix)
	out_mat=np.dot(matrix,scalar)
	return out_mat