from ammp.physics import reference

import numpy as np
import pytest
from scipy.spatial.transform import Rotation


@pytest.fixture
def root_reference():
    """
    Creates a random root reference.
    """
    position = np.random.rand(3)
    rotation = Rotation.from_matrix(np.random.rand(3, 3))
    ref = reference.Reference(position, rotation, None)
    return ref


def test_reference_constructor(root_reference):
    """
    Test the constructor of the physics.Reference class
    :return: None
    """
    position = np.random.rand(3)
    rotation = Rotation.from_matrix(np.random.rand(3, 3))
    ref = reference.Reference(position, rotation, root_reference)

    assert ref.position.all() == position.all()
    assert ref.rotation == rotation
    assert ref.parent_reference == root_reference
