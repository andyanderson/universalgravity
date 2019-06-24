function g(r):
	"""Calculates the acceleration of gravity at any distance from the center of the Earth.
		Here G is the Universal Constant of Gravitation and M is the mass of the Earth"""
	G = 6.673e-11 // m**3/(kg*s**2)
	M = 5.972e4	// kg
	return G*M/r**2