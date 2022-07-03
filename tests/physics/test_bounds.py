from ammp.physics.bounds import BoundingBox, BoundingSphere

import numpy as np
import pytest
import random
from ammp.physics.reference import CartesianReference
from scipy.spatial.transform import Rotation


@pytest.fixture
def root_reference():
    """
    Creates a root reference at [0, 0, 0] and no rotation

    :return: the root reference
    :rtype: ammp.physics.reference.CartesianReference
    """
    position = np.array([0, 0, 0])
    rotation = Rotation.from_matrix(np.identity(3))
    reference = CartesianReference(position, rotation, None)

    return reference


@pytest.fixture
def generic_bounding_box(root_reference):
    """
    Creates a generic bounding box with 8 vertices defined in the root_refernce

    :return: A dictionary with the BoundingBox and some expected values.
        Specifically {'BoundingBox': BoundingBox, 'center': center}
    :rtype: dict
    """
    vertices = [
        np.array([0., 0., 0.]),
        np.array([1., 0., 0.]),
        np.array([1., 2., 0.]),
        np.array([0., 2., 0.]),
        np.array([0., 1., 1.]),
        np.array([1., 1., 1.]),
        np.array([1., 3., 1.]),
        np.array([0., 3., 1.])
    ]

    center = np.array([0.5, 1.5, 0.5])

    bounding_box = BoundingBox(vertices, root_reference)

    return {'BoundingBox': bounding_box, 'center': center}


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


class TestBoundingBox:
    """
    Tests for the BoundingBox class
    """
    def test_constructor(self, root_reference):
        """
        Test the constructor for the BoundingSphere class
        """
        vertices = [np.random.rand(3) for i in range(6)]
        reference = root_reference

        bounding_box = BoundingBox(vertices, reference)

        assert all([np.allclose(x, y) for x, y in
                    zip(bounding_box.vertices, vertices)])
        assert bounding_box.reference == reference

    def test_bounding_sphere_center_static(self, generic_bounding_box):
        """
        Test the .bounding_sphere_center method with static values.
        """
        bounding_box = generic_bounding_box['BoundingBox']
        center = generic_bounding_box['center']

        radius = np.sqrt(0.5**2 + 1.5**2 + 0.5**2)

        bounding_sphere = bounding_box.bounding_sphere_center()

        assert np.allclose(bounding_sphere.position, center, 1e-12)
        assert np.isclose(bounding_sphere.radius, radius, rtol=1e-12)

    def test_center_random(self, root_reference):
        """
        Test the .center() method with random values.
        """
        vertices = [np.random.random(3) * random.randint(1, 100) for _ in
                    range(8)]

        bounding_box = BoundingBox(vertices, root_reference)

        center = np.array(vertices[0])
        center += vertices[1]
        center += vertices[2]
        center += vertices[3]
        center += vertices[4]
        center += vertices[5]
        center += vertices[6]
        center += vertices[7]

        center /= 8

        print('t')
        print('t')

        assert np.allclose(bounding_box.center(), center, 1e-12)

    def test_center_static(self, generic_bounding_box):
        """
        Test the .center() method with static values.
        """
        bounding_box = generic_bounding_box['BoundingBox']
        center = generic_bounding_box['center']

        assert np.allclose(bounding_box.center(), center, 1e-12)
