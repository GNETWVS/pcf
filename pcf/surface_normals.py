import numpy as np
import numpy.linalg as la


def angle(v1, v2):
    """ Returns the angle in radians between vectors 'v1' and 'v2', without
    screwing up near 0 and 90 degrees.
    From https://newtonexcelbach.com/2014/03/01/
        the-angle-between-two-vectors-python-version/"""
    cosang = np.dot(v1, v2)
    sinang = la.norm(np.cross(v1, v2))
    return np.arctan2(sinang, cosang)


if __name__ == '__main__':
    pass
