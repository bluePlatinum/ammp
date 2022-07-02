

class BoundingSphere:
    """
    Holds information about a bounding sphere.

    :param position: the position of the center of the sphere
    :type position: numpy.ndarray
    :param radius: the radius of the bounding sphere
    :type radius: float
    :param reference: the reference in which the center position is defined
    :type reference: ammp.reference.Reference
    """
    def __init__(self, position, radius, reference):
        """
        Constructor method
        """
        self.position = position
        self.radius = radius
        self.reference = reference


class BoundingBox:
    """
    Holds information about a bounding box.

    :param vertices: A list of vertices defining the box. Imagine a cube, then
        0-3 represent the lower 4 vertices and 4-7 the upper 4. Furthermore,
        the vertices are arranged in ascending order when going
        counterclockwise on the top or bottom surfaces.
    :type vertices: list[numpy.ndarray]
    :param reference: the reference in which te vertices are defined
    :type reference: ammp.reference.Reference
    """
    def __init__(self, vertices, reference):
        """
        Constructor method
        """
        self.vertices = vertices
        self.reference = reference
