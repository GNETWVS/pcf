import numpy as np


def generate_plane_segment(p, l, n, d):
    """Generate a cloud of random points in a square plane segment.

    Args:
        p (np.array): a 3-tuple of floats giving the center of the plane segment.
        l (float): length of the sides of the square.
        n (np.array): a 3-tuple giving the normal of the plane.
        m (float): number of points in the plane

    Returns:
        np.array: mx3 list of points
    """
    pass


def test_generate_plane_segment():
    seg = generate_plane_segment((0., 0., 0.), 1.0, (0., 0., 1.), 100)
    assert seg

