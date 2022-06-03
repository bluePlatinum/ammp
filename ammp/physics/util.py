import numpy as np


class Quat:
    """
    Creates a normalized Quaternion of the form (x, y, z, Re). Mainly used for
    rotation.

    :param quat: A array representing the quaternion as (x, y, z, Re)
    :type quat: numpy.ndarray
    """
    def __init__(self, quat):
        """
        Constructor Method

        :param quat: A array representing the quaternion as (x, y, z, Re)
        :type quat: numpy.ndarray
        """
        quat = quat / np.linalg.norm(quat)  # normalize the vector
        self._quat = quat

    @classmethod
    def from_angle_axis(cls, angle, axis):
        """
        Create a Quat object from an angle in radians and a rotation axis.

        :param angle: The angle for the rotation
        :type angle: number
        :param axis: The axis of the rotation
        :type axis: array or numpy.ndarray
        :return: Quat object
        :rtype: Quat
        """
        axis = axis / np.linalg.norm(axis)  # normalize the vector
        quat = np.array([*(np.sin(angle) * axis), np.cos(angle)])
        return cls(quat)

    def as_array(self):
        """
        Returns the Quaternion represented as an array of the form
        (x, y, z, Re).

        :return: array representing the Quat
        :rtype: numpy.ndarray
        """
        return self._quat

    # TODO: create as_angle_axis() method
