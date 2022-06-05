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


@pytest.fixture
def system_set_static():
    """
    Creates a static system of references for testing.
    """
    # Create root reference
    position = np.array([0, 0, 0])
    rotation = Rotation.from_matrix(np.identity(3))
    root_ref = reference.CartesianReference(position, rotation, None)

    # Create first reference
    position = np.array([1, 2, 0])
    rotation = Rotation.from_rotvec(np.pi/4 * np.array([1, 0, 0]))
    first_ref = reference.CartesianReference(position, rotation, root_ref)

    # Create second reference
    position = np.array([0, 0, 3])
    rotation = Rotation.from_rotvec(np.pi/2 * np.array([0, 0, 1]))
    second_ref = reference.CartesianReference(position, rotation, root_ref)

    # Create third reference
    position = np.array([0, 0, 3])
    rotation = Rotation.from_rotvec(np.pi/2 * np.array([0, 0, 1]))
    third_ref = reference.CartesianReference(position, rotation, second_ref)

    # Create fourth reference
    position = np.array([0, 0, -3])
    rotation = Rotation.from_rotvec(-np.pi/2 * np.array([0, 0, 1]))
    fourth_ref = reference.CartesianReference(position, rotation, second_ref)

    return root_ref, first_ref, second_ref, third_ref, fourth_ref


class TestReference:
    def test_constructor(self, root_reference):
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


class TestCartesianReference:
    def test_constructor(self, root_reference):
        """
        Test the constructor of the physics.CartesianReference class
        :return: None
        """
        position = np.random.rand(3)
        rotation = Rotation.from_matrix(np.random.rand(3, 3))
        ref = reference.Reference(position, rotation, root_reference)

        assert ref.position.all() == position.all()
        assert ref.rotation == rotation
        assert ref.parent_reference == root_reference

    def test_transform_to(self, system_set_static):
        """
        Test the CartesianReferenec.ref_transform_to method with a static system.
        """
        references = system_set_static
        vector = np.array([3, 4, 5])
        expected_r = vector
        expected_1 = np.array([2, 4.94974747, 2.12132034])
        expected_2 = np.array([4, -3, 2])
        expected_3 = np.array([4, -3, 2])

        assert references[0].ref_transform_to(vector).all() == expected_r.all()
        assert references[1].ref_transform_to(vector).all() == expected_1.all()
        assert references[2].ref_transform_to(vector).all() == expected_2.all()
        assert references[3].ref_transform_to(vector).all() == expected_3.all()
