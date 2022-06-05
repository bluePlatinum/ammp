from ammp.physics import util

import math
import numpy as np
import pytest
import random

# Fixtures
# ========


@pytest.fixture
def quat_set_random():
    testset = list()
    for i in range(3):
        quat = np.random.rand(4)
        test_object = util.Quat(quat)
        testset.append((quat, test_object))
    return testset


@pytest.fixture
def quat_set_angle_static():
    parameters = list()
    parameters.append((0, np.array([1, 0, 0])))
    parameters.append((np.pi / 4, np.array([1, 1, 0])))
    parameters.append((np.pi / 2, np.array([0, 0, 5])))

    results = list()
    results.append(np.array([0, 0, 0, 1]))
    results.append(np.array([0.5, 0.5, 0, math.sqrt(2) / 2]))
    results.append(np.array([0, 0, 1, 0]))

    return [(parameters[i], results[i]) for i in range(len(results))]

# ========


class TestQuat:
    """
    Tests for Quat class
    """
    def test_constructor(self):
        """
        Test the Quat constructor

        :return: None
        """
        quat = np.random.rand(4)
        test_object = util.Quat(quat)

        assert test_object._quat.all() == quat.all()

    def test_constructor_normalization(self):
        """
        Test the normalization of the Quat constructor

        :return: None
        """
        quat = np.random.rand(4) * random.randint(1, 100)
        quat_norm = quat / np.linalg.norm(quat)
        test_object = util.Quat(quat)

        assert test_object._quat.all() == quat_norm.all()

    def test_from_angle_axis_static(self, quat_set_angle_static):
        """
        Test Quat.from_angle_axis method with static values.

        :return: None
        """
        for test in quat_set_angle_static:
            test_object = util.Quat.from_angle_axis(*test[0])
            assert test_object._quat.all() == test[1].all()

    def test_from_anggle_axis_random(self):
        """
        Test Quat.from_angle_axis method with random values.

        :return: None
        """
        angle = random.random() * 2 * np.pi
        axis = np.random.rand(3)
        axis_norm = axis / np.linalg.norm(axis)
        expected = np.array([*(np.sin(angle) * axis_norm), np.cos(angle)])
        test_object = util.Quat.from_angle_axis(angle, axis)

        assert test_object._quat.all() == expected.all()

    def test_as_array(self, quat_set_random):
        """
        Test Quat.as_array method with random values.

        :return: None
        """
        for test in quat_set_random:
            assert test[1].as_array().all() == test[0].all()

    def test_as_angle_axis_static(self, quat_set_angle_static):
        """
        Test Quat.as_angle_axis method with static values.

        :return: None
        """
        for test in quat_set_angle_static:
            test_object = util.Quat.from_angle_axis(*test[0])
            angle_axis = test_object.as_angle_axis()

            assert math.isclose(angle_axis[0], test[0][0], rel_tol=1e-12)
            if angle_axis[0] != 0:
                assert angle_axis[1].all() == test[0][1].all()

    def test_as_angle_axis_random(self):
        """
        Test Quat.as_angle_axis method with random values.

        :return: None
        """
        angle = random.random() * 2 * np.pi
        angle_expected = np.arccos(np.cos(angle))  # expected angle in 0-2pi
        axis = np.random.rand(3)
        axis_norm = axis / np.linalg.norm(axis)
        test_object = util.Quat.from_angle_axis(angle, axis)
        angle_axis = test_object.as_angle_axis()

        assert math.isclose(angle_axis[0], angle_expected, rel_tol=1e-12)
        if angle != 0:
            assert angle_axis[1].all() == axis_norm.all()
