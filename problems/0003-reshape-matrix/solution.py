import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
    
	
	if len(a) * len(a[0]) != new_shape[0]*new_shape[1]:
		return []
	x=np.array(a).reshape(new_shape).tolist()
		
	#x = np.array(matrix).reshape(new_shape).tolist()
	return x