

class Reference:
    """
    Creates a frame of reference. This is mainly a super class from which
    specific types of references inherit.

    :param position: The position of the reference expressed in vectors of
        the root reference.
    :type position: Numpy array
    :param rotation: To rotation of the reference expressed
    :tpye position: scipy rotation
    """
    def __init__(self, position, rotation):
        """
        Constructor method
        """
        self.position = position
        self.rotation = rotation
