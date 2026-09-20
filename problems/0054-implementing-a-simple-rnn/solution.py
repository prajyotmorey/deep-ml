import numpy as np

def rnn_forward(input_sequence: list[list[float]], initial_hidden_state: list[float], Wx: list[list[float]], Wh: list[list[float]], b: list[float]) -> list[float]:
	
	for input_ in input_sequence:
		ht=np.tanh(np.array(Wx) @ np.array(input_) + np.array(Wh) @ np.array(initial_hidden_state)+np.array(b)) 
		initial_hidden_state=ht
	final_hidden_state=ht
	return final_hidden_state