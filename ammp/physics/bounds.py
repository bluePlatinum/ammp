

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
