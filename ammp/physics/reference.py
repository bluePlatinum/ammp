

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

    def ref_transform_from(self, vector):
        """
        Placeholder method child classes should overwrite this
        """
        error_msg = 'The method was not overwritten by the Reference child ' \
                    'class. Therefore it is imposible to determine' \
                    'the transformation correctly.'
        raise ValueError(error_msg)

    def ref_transform_to(self, vector):
        """
        Placeholder method child classes should overwrite this
        """
        error_msg = 'The method was not overwritten by the Reference child ' \
                    'class. Therefore it is imposible to determine' \
                    'the transformation correctly.'
        raise ValueError(error_msg)

    def root_transform_from(self, vector):
        """
        Transforms a vector expressed in this frame of reference into the root
        frame of reference

        :param vector: the vector to be transformed (this frame of reference)
        :type vector: numpy.ndarray
        :return: transformed vector
        :rtype: numpy.ndarray
        """
        if self.parent_reference is None:
            return self.ref_transform_from(vector)
        else:
            parent_vector = self.ref_transform_from(vector)
            return self.parent_reference.root_transform_from(parent_vector)

    def root_transform_to(self, vector):
        """
        Transforms a vector expressed in the root frame of reference into this
        frame of reference.

        :param vector: the vector to be transformed (root frame of reference)
        :type vector: numpy.ndarray
        :return: transformed vector (this frame of reference)
        :rtype: numpy.ndarray
        """
        # check if parent reference is root
        if self.parent_reference.parent_reference is None:
            return self.ref_transform_to(vector)
        else:
            parent_vector = self.parent_reference.root_transform_to(vector)
            return self.ref_transform_to(parent_vector)


class CartesianReference(Reference):
    """
    Creates a cartesian frame of reference.

    :param position: The position of the reference expressed in vectors of
        the root reference.
    :type position: Numpy array
    :param rotation: To rotation of the reference expressed
    :tpye position: scipy rotation
    :param parent_reference: The parent reference of the reference. This is the
        frame of reference in which the position and rotation of this
        Reference is defined.
    :type parent_reference: Reference or CartesianReference
    """
    def __init__(self, position, rotation, parent_reference):
        """
        Constructor method
        """
        super().__init__(position, rotation, parent_reference)

    def ref_transform_from(self, vector):
        """
        Transforms a vector expressed in this frame of reference into the
        parent frame of reference.

        :param vector: the vector to be transformed (this frame of reference)
        :type vector: numpy.ndarray
        :return: transformed vector
        :rtype: numpy.ndarray
        """
        return self.rotation.apply(vector) + self.position

    def ref_transform_to(self, vector):
        """
        Transforms a vector expressed in the parent frame of reference to this
        frame of reference

        :param vector: a vector to be transformed
        :type vector: numpy.ndarray
        :return: transformed vector
        :rtype: numpy.ndarray
        """
        inverse = self.rotation.inv()
        return inverse.apply(vector - self.position)
