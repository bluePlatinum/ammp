import numpy as np


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

    def bounding_sphere_center(self):
        """
        Returns a bounding sphere, which contains all the vertices of the
        bounding box, with the center of the sphere at the center of the
        bounding box.

        :return: a bounding sphere with concentrical with the bounding box
        :rtype: BoundingSphere
        """
        center = self.center()
        radius = 0
        for vertex in self.vertices:
            vector = vertex - center
            if np.linalg.norm(vector) > radius:
                radius = np.linalg.norm(vector)

        return BoundingSphere(center, radius, self.reference)

    def center(self):
        """
        Returns the center of the BoundingBox. This is calculated by using
        the Center of Mass equation and just weighing every vertex identically
        with m=1.

        :return: the center of the bounding box in the self.reference reference
        :rtype: numpy.ndarray
        """
        center_point = np.array([0., 0., 0.])
        for vertex in self.vertices:
            center_point += vertex
        center_point = center_point / len(self.vertices)
        return center_point
