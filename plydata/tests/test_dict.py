import numpy as np

from plydata import mutate


def test_mutate():
    x = np.array([1, 2, 3])
    y = np.array([4, 5, 6])
    d = {'x': x}

    # No args
    d >> mutate()
    assert len(d) == 1

    # All types of args
    d >> mutate(('x*2', 'x*2'),
                ('x*3', 'x*3'),
                x_sq='x**2',
                x_cumsum='np.cumsum(x)',
                y=y)

    assert len(d) == 6
    assert all(d['x*2'] == x*2)
    assert all(d['x*3'] == x*3)
    assert all(d['x_sq'] == x**2)
    assert all(d['x_cumsum'] == np.cumsum(x))
    assert all(d['y'] == y)
