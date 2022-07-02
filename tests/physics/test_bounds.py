from ammp.physics.bounds import BoundingSphere

import numpy as np
import pytest
import random
from ammp.physics.reference import CartesianReference
from scipy.spatial.transform import Rotation


@pytest.fixture
def root_reference():
    """
    Creates a root reference at [0, 0, 0] and no rotation
    """
    position = np.array([0, 0, 0])
    rotation = Rotation.from_matrix(np.identity(3))
    reference = CartesianReference(position, rotation, None)

    return reference


class TestBoundingSphere:
    """
    Tests for the BoundingSphere class
    """
    def test_constructor(self, root_reference):
        """
        Test the constructor for the BoundingSphere class
        """
        position = np.random.rand(3)
        radius = random.random() * random.randint(1, 100)
        reference = root_reference

        bounding_sphere = BoundingSphere(position, radius, reference)

        assert np.allclose(bounding_sphere.position, position, 1e-12)
        assert bounding_sphere.radius == radius
        assert bounding_sphere.reference == reference
