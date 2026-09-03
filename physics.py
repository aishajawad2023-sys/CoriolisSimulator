# ==========================================
# CORIOLIS PHYSICS SIMULATOR
# physics.py
# ==========================================

import math
import numpy as np


def circular_velocity(omega, radius):
    """
    Linear velocity for uniform circular motion.

    v = omega * r
    """
    return omega * radius


def centripetal_acceleration(velocity, radius):
    """
    Centripetal acceleration.

    a_c = v^2 / r
    """
    if radius == 0:
        return 0.0

    return velocity ** 2 / radius


def centripetal_acceleration_omega(omega, radius):
    """
    Alternative form of centripetal acceleration.

    a_c = omega^2 * r
    """
    return omega ** 2 * radius


def centripetal_force(mass, velocity, radius):
    """
    Centripetal force.

    F_c = m v^2 / r
    """
    if radius == 0:
        return 0.0

    return mass * velocity ** 2 / radius


def circular_position(center_x, center_y, radius, angle):
    """
    Calculate the position of a particle moving
    around a circle.
    """

    x = center_x + radius * math.cos(angle)
    y = center_y + radius * math.sin(angle)

    return x, y


def velocity_vector(omega, radius, angle):
    """
    Velocity vector for counterclockwise circular motion.

    vx = -omega*r*sin(theta)
    vy =  omega*r*cos(theta)
    """

    vx = -omega * radius * math.sin(angle)
    vy = omega * radius * math.cos(angle)

    return np.array([vx, vy])


def centripetal_acceleration_vector(
    omega,
    radius,
    angle
):
    """
    Centripetal acceleration vector.

    It points toward the center.
    """

    ax = -omega ** 2 * radius * math.cos(angle)
    ay = -omega ** 2 * radius * math.sin(angle)

    return np.array([ax, ay])


def coriolis_acceleration(
    omega_vector,
    velocity_vector
):
    """
    Coriolis acceleration:

        a_C = -2 (Omega x v)

    omega_vector and velocity_vector
    are 3-dimensional NumPy vectors.
    """

    return -2 * np.cross(
        omega_vector,
        velocity_vector
    )
