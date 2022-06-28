from ammp.physics import systems

import numpy as np
import pytest
from ammp.physics.bodies import Rigidbody
from ammp.physics.reference import CartesianReference
from ammp.ui.systemViewer import SystemViewerGraphic
from scipy.spatial.transform import Rotation


@pytest.fixture
def simple_two_body_system_static():
    """
    Generate a root CartesianReference and two bodies and return them in a
    tuple of the form (CartesianReference, [body1, body2]). All the values
    are static.
    """
    ref_position = np.array([0, 0, 0])
    ref_rotation = Rotation.from_matrix(np.identity(3))
    reference = CartesianReference(ref_position, ref_rotation, None)

    body1_position = np.array([0, 0, 0])
    body1_rotation = Rotation.from_matrix(np.identity(3))
    body1 = Rigidbody(body1_position, body1_rotation, reference)

    body2_position = np.array([10, 0, 0])
    body2_rotation = Rotation.from_rotvec(np.pi/4 * np.array([0, 0, 1]))
    body2 = Rigidbody(body2_position, body2_rotation, reference)

    return reference, [body1, body2]


class TestSystem:
    """
    Tests for the System class
    """
    def test_constructor(self):
        """
        Test the constructor
        """
        system = systems.System()

        # nothing to test here (just for completeness)
        assert True

    def test_draw_sv(self):
        """
        Test the draw_sv method.
        """
        system = systems.System()
        sv_graphic = SystemViewerGraphic()

        with pytest.raises(NotImplementedError):
            system.draw_sv(sv_graphic)


class TestSystemDisplay:
    def test_constructor(self, simple_two_body_system_static):
        """
        Test the constructor of SystemDisplay
        """
        bodies = simple_two_body_system_static[1]
        system = systems.SystemDisplay(bodies)

        assert system.bodies == bodies
