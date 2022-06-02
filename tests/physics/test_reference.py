from ammp.physics import reference

import numpy as np
from scipy.spatial.transform import Rotation


def test_reference_constructor():
    """
    Test the constructor of the physics.Reference class
    :return: None
    """
    position = np.random.rand(3)
    rotation = Rotation.from_matrix(np.random.rand(3, 3))
    ref = reference.Reference(position, rotation)

    assert ref.position.all() == position.all()
    assert ref.rotation == rotation
