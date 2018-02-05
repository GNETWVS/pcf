"""Sample that generates a new .las from scratch.
Found at https://gis.stackexchange.com/questions/158708/use-laspy-to-create-las-file-from-scratch-without-opening-an-existing-las-file-f"""
import laspy
import numpy as np

if __name__ == '__main__':

    hdr = laspy.header.Header()

    outfile = laspy.file.File("output.las", mode="w", header=hdr)
    allx = np.array([1.000, 2.000, 3.000, 3.000])  # Four Points
    ally = np.array([0.000, 0.000, 0.000, 3.000])
    allz = np.array([10.000, 10.000, 11.000, 11.000])

    xmin = np.floor(np.min(allx))
    ymin = np.floor(np.min(ally))
    zmin = np.floor(np.min(allz))

    outfile.header.offset = [xmin, ymin, zmin]
    outfile.header.scale = [0.001, 0.001, 0.001]

    outfile.x = allx
    outfile.y = ally
    outfile.z = allz

    outfile.close()
