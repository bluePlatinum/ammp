

class Reference:
    """
    Creates a frame of reference. This is mainly a super class from which
    specific types of references inherit.

    :param position: The position of the reference expressed in vectors of
        the root reference.
    :type position: Numpy array
    :param rotation: To rotation of the reference expressed
    :tpye position: scipy rotation
    :param parent_reference: The parent reference of the reference. This is the
        frame of reference in which the position and rotation of this
        Reference is defined.
    :type parent_reference: Reference
    """
    def __init__(self, position, rotation, parent_reference):
        """
        Constructor method
        """
        self.position = position
        self.rotation = rotation
        self.parent_reference = parent_reference
