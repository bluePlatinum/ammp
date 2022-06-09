

class Rigidbody:
    """
    This class is used to handle basic rigidbody Physics. (No collisions
    though)

    :param position: The position of the rigidbody expressed in the frame of
        reference given by the argument reference.
    :type position: numpy.ndarray
    :param rotation: The rotation of the rigidbody expressed in the frame of
        reference given by the argument reference.
    :type rotation: scipy.spatial.transform.rotation.Rotation
    :param reference: The frame of reference in which the Rigidbody resides.
    :type reference: ammp.reference.Reference
    """
    def __init__(self, position, rotation, reference):
        """
        Constructor method
        """
        self.position = position
        self.rotation = rotation
        self.reference = reference
