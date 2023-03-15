import pytest
from typing import Final
import array as arr
from persistence import mean_cos
from persistence import persistence_length
from persistence import kuhn_segment

EPS: Final[float] = 1e-8
bond_length: float = 1.0
k_array: arr = arr.array('d', [0., 1., 2., 3., 4., 5., 6., 7., 8. ,9., 10., 15., 20.])
cos_array: arr = arr.array('d', [0., 0.31303529, 0.53731472, 0.67163649, 0.75067115, 0.8000908, 0.83334562, 
                        0.85714452, 0.87500023, 0.88888892, 0.900, 0.93333333, 0.95])
prst_array: arr = arr.array('d', [0., 0.86100061, 1.60986193, 2.5123228, 3.48690104, 4.48370068, 5.48525859,
                          6.48724085, 7.48889012, 8.49018949, 9.49122199, 14.49425105, 19.49572575])
kuhn_array: arr = arr.array('d', [1., 1.91135768, 3.32259268, 5.09081076, 7.02153462, 9.00454226, 11.00088484,
                           13.00016298, 15.00002881, 17.00000493, 19.00000082, 29., 39.])

def test_mean_cos():
    for k in k_array:
        result = mean_cos(k)
        assert abs(result - cos_array[k_array.index(k)]) < EPS

def test_persistence_length():
    for k in k_array:
        result = persistence_length(k,length_bond=bond_length)
        assert abs(result - prst_array[k_array.index(k)]) < EPS

def test_kuhn_segment():
    for k in k_array:
        result = kuhn_segment(k, length_bond=bond_length)
        assert abs(result - kuhn_array[k_array.index(k)]) < EPS