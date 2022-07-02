from ammp.physics import bodies

import numpy as np
import pytest
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


class TestRigidbody:
    """
    Tests for the Rigidbody class.
    """
    def test_constructor(self, root_reference):
        """
        Test the constructor for the bodies class.
        """
        position = np.random.rand(3)
        rotation = Rotation.from_matrix(np.random.rand(3, 3))

        body = bodies.Rigidbody(position, rotation, root_reference)

        assert np.allclose(body.position, position, 1e-12)
        assert body.rotation == rotation
        assert body.reference == root_reference


class TestSphericalBody:
    """
    Tests for the SphericalBody class.
    """
    def test_constructor(self, root_reference):
        """
        Test the constructor for the SphericalBody class
        """
        position = np.random.rand(3)
        rotation = Rotation.from_matrix(np.random.rand(3, 3))

        body = bodies.Rigidbody(position, rotation, root_reference)

        assert np.allclose(body.position, position, 1e-12)
        assert body.rotation == rotation
        assert body.reference == root_reference
