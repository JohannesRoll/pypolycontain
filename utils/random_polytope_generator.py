import numpy as np
from pypolycontain.lib.zonotope import zonotope
from pypolycontain.lib.polytope import polytope
from pypolycontain.lib.AH_polytope import AH_polytope, to_AH_polytope

def get_uniform_random_zonotopes(zonotope_count, dim, centroid_range=None, generator_range = 10, return_type = 'AH_polytope'):
    polytopes = []
    if centroid_range is None:
        centroid_range = zonotope_count*5
    for i in range(zonotope_count):
        m = np.random.random_integers(dim, 2*dim)
        G = (np.random.rand(dim, m) - 0.5) * generator_range * 1
        x = 2*(np.random.rand(dim,1) - 0.5)*centroid_range
        if return_type == 'AH_polytope':
            polytopes.append(to_AH_polytope(zonotope(x, G)))
        elif return_type == 'zonotope':
            polytopes.append(zonotope(x, G))
        else:
            raise NotImplementedError
    return polytopes