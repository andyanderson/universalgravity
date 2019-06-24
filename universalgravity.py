function g(r):
	"""Calculates the acceleration of gravity at any distance from the center of the Earth.
		Here G is the Universal Constant of Gravitation and M is the mass of the Earth"""
	G = 6.673e-11 // m**3/(kg*s**2)
	M = 5.972e4	// kg
	return G*M/r**2
	
	
function gsurface(R,M)
	"""Calculates the surface gravity of a world given its radius and mass."""
	G = 6.673e-11 // m**3/(kg*s**2)
	return G*M/R**2
