from ammp.physics import bodies

import random
import numpy as np


def test_rigidbody_constructor():
    """
    Test the constructor for the bodies class.
    :return: None
    """
    position = np.array([random.random() for i in range(3)])
    rotation = np.array([random.random() for i in range(3)])
    body = bodies.Rigidbody(position, rotation)

    assert body.position.all() == position.all()
    assert body.rotation.all() == rotation.all()
