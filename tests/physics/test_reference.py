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
        """
        position = np.random.rand(3)
        rotation = Rotation.from_matrix(np.random.rand(3, 3))
        ref = reference.Reference(position, rotation, root_reference)

        assert (ref.position == position).all()
        assert ref.rotation == rotation
        assert ref.parent_reference == root_reference

    def test_ref_transform_from(self, root_reference):
        """
        Tests the Reference.ref_tranform_from method. By default this should
        throw an error when beeing called.
        """
        position = np.random.rand(3)
        rotation = Rotation.from_matrix(np.random.rand(3, 3))
        ref = reference.Reference(position, rotation, root_reference)

        with pytest.raises(ValueError):
            ref.ref_transform_from(np.random.rand(3))

    def test_ref_tranform_to(self, root_reference):
        """
        Tests the Reference.ref_tranform_to method. By default this should
        throw an error when beeing called.
        """
        position = np.random.rand(3)
        rotation = Rotation.from_matrix(np.random.rand(3, 3))
        ref = reference.Reference(position, rotation, root_reference)

        with pytest.raises(ValueError):
            ref.ref_transform_to(np.random.rand(3))


class TestCartesianReference:
    def test_constructor(self, root_reference):
        """
        Test the constructor of the physics.CartesianReference class
        """
        position = np.random.rand(3)
        rotation = Rotation.from_matrix(np.random.rand(3, 3))
        ref = reference.Reference(position, rotation, root_reference)

        assert (ref.position == position).all()
        assert ref.rotation == rotation
        assert ref.parent_reference == root_reference

    def test_ref_transform_to(self, system_set_static):
        """
        Test the CartesianReferenec.ref_transform_to method with a static
        system.
        """
        references = system_set_static
        vector = np.array([3, 4, 5])
        expected_r = vector
        expected_1 = np.array([2, 4.94974747, 2.12132034])
        expected_2 = np.array([4, -3, 2])
        expected_3 = np.array([4, -3, 2])

        assert np.allclose(references[0].ref_transform_to(vector), expected_r,
                           1e-12)
        assert np.allclose(references[1].ref_transform_to(vector), expected_1,
                           1e-12)
        assert np.allclose(references[2].ref_transform_to(vector), expected_2,
                           1e-12)
        assert np.allclose(references[3].ref_transform_to(vector), expected_3,
                           1e-12)

    def test_ref_transform_from(self, system_set_static):
        """
        Test the CartesianReference.ref_transform_from method with a static
        system.
        """
        references = system_set_static
        expec = np.array([3, 4, 5])
        vector_r = expec
        vector_1 = np.array([2, 4.94974747, 2.12132034])
        vector_2 = np.array([4, -3, 2])
        vector_3 = np.array([4, -3, 2])

        assert np.allclose(references[0].ref_transform_from(vector_r), expec,
                           1e-12)
        assert np.allclose(references[1].ref_transform_from(vector_1), expec,
                           1e-12)
        assert np.allclose(references[2].ref_transform_from(vector_2), expec,
                           1e-12)
        assert np.allclose(references[3].ref_transform_from(vector_3), expec,
                           1e-12)

    def test_ref_transform_bidirectional(self, system_set_static):
        """
        Test the CartesianReference.ref_transform_to and .ref_transform_from
        methods by transforming a vector into and back from a reference.
        """
        references = system_set_static
        vector = np.random.rand(3)

        trans_r = references[0].ref_transform_to(vector)
        trans_1 = references[1].ref_transform_to(vector)
        trans_2 = references[2].ref_transform_to(vector)
        trans_3 = references[3].ref_transform_to(vector)

        assert np.allclose(references[0].ref_transform_from(trans_r), vector,
                           1e-12)
        assert np.allclose(references[1].ref_transform_from(trans_1), vector,
                           1e-12)
        assert np.allclose(references[2].ref_transform_from(trans_2), vector,
                           1e-12)
        assert np.allclose(references[3].ref_transform_from(trans_3), vector,
                           1e-12)

    def test_root_transform_from_single(self, system_set_static):
        """
        Test the Reference.root_transform_from method with random
        values but static CartisianReferences. This test does not rely on any
        other methods from CartesianReference except the constructor.
        """
        # root = system_set_static[0]     not needed just for clarity
        # parent = system_set_static[2]   not needed just for clarity
        child = system_set_static[4]
        # The child is the exact inverse of the parent so any vector expressed
        # in the child reference should be exactly the same as in the root
        # reference.

        vector = np.random.rand(3)
        assert np.allclose(child.root_transform_from(vector), vector, 1e-12)

    def test_root_transform_from(self, system_set_static):
        """
        Test the CartesianReference.root_transform_from method with random
        values but static CartesianReferences. This test relies on the validity
        of the .ref_transform_to method.
        """
        references = system_set_static
        vector = np.random.rand(3)

        trans_r = references[0].ref_transform_to(vector)
        trans_1 = references[1].ref_transform_to(vector)
        trans_2 = references[2].ref_transform_to(vector)
        trans_3 = references[3].ref_transform_to(trans_2)  # parent is ref_2
        trans_4 = references[4].ref_transform_to(trans_2)  # parent is ref_2

        assert np.allclose(references[0].root_transform_from(trans_r), vector,
                           1e-12)
        assert np.allclose(references[1].root_transform_from(trans_1), vector,
                           1e-12)
        assert np.allclose(references[2].root_transform_from(trans_2), vector,
                           1e-12)
        assert np.allclose(references[3].root_transform_from(trans_3), vector,
                           1e-12)
        assert np.allclose(references[4].root_transform_from(trans_4), vector,
                           1e-12)
