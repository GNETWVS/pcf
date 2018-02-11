import laspy
import numpy as np
from pcf.surface_normals import angle as vangle
import pcf.transformations as xf


def generate_las(xyz, outfile):
    """Write a numpy array of 3d row vectors to a new .las file.

    Args:
        xyz (np.array): 3d row vectors
        outfile (str): path to output file. Existing files will be overwritten.
    """
    hdr = laspy.header.Header()
    outfile = laspy.file.File(outfile, mode="w", header=hdr)

    # populate the header with minimal info
    xmin = np.floor(np.min(xyz[:, 0]))
    ymin = np.floor(np.min(xyz[:, 1]))
    zmin = np.floor(np.min(xyz[:, 2]))
    outfile.header.offset = [xmin, ymin, zmin]
    outfile.header.scale = [0.001, 0.001, 0.001]

    # output points
    outfile.x = xyz[:, 0]
    outfile.y = xyz[:, 1]
    outfile.z = xyz[:, 2]

    outfile.close()


def generate_plane_segment(p, n, l, m):
    """Generate a cloud of random points in a square plane segment.

    Args:
        p (np.array): a 3-tuple of floats giving the center of the plane segment.
        n (np.array): a 3-tuple giving the normal of the plane.
        l (float): length of the sides of the square.
        m (float): number of points in the plane

    Returns:
        np.array: mx3 list of points
    """
    # Generate an lxl segment of the x-y plane, centered at the origin.
    # Let a(x-x_0) + b(y-y_0) + c(z-z_0) = 0
    # x_0=0, y_0=0, c=0 => ax + by = 0
    xyz = np.random.rand(3, m) * l
    xyz[2, :] = np.zeros(m)  # x-y plane
    xyz += np.array([-l/2., -l/2., 0]).reshape((3, 1))

    # rotate and translate
    zaxis = np.array([0., 0., 1.])
    rot_axis = np.cross(zaxis, n)
    rot_angle = vangle(zaxis, n)
    Rt = xf.rotation_matrix(rot_angle, rot_axis)
    Rt[:3, 3] = p  # insert translation
    xyz_h = np.vstack((xyz, np.ones((1, m))))
    xyz_transformed = np.dot(Rt, xyz_h)

    return xyz_transformed[:3, :]


def test_generate_plane_segment(test_artifact_dir):
    o = np.array([0., 0., 0.])
    n = np.array([1., 0., 0.])  # x-axis
    l = 1.0
    m = 10000
    seg = generate_plane_segment(o, n, l, m)
    assert seg.shape == (3, m)

    # dump the points to a .las so we can view them
    generate_las(seg.T, str(test_artifact_dir.join('plane_segment.las')))




