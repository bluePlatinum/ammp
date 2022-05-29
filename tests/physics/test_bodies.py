import ammp.physics.bodies as bodies

import numpy as np
import random


def test_rigidbody_constructor():
    position = np.array([random.random() for i in range(3)])
    rotation = np.array([random.random() for i in range(3)])
    body = bodies.Rigidbody(position, rotation)

    assert body.position.all() == position.all()
    assert body.rotation.all() == rotation.all()
