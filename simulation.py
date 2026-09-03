# ==========================================
# CORIOLIS PHYSICS SIMULATOR
# simulation.py
# ==========================================

import math

from physics import (
    circular_position,
    circular_velocity,
    velocity_vector,
    centripetal_acceleration_vector
)


class Particle:
    """
    Represents a particle in our simulation.
    """

    def __init__(
        self,
        center_x,
        center_y,
        radius,
        omega
    ):

        self.center_x = center_x
        self.center_y = center_y

        self.radius = radius
        self.omega = omega

        self.angle = 0.0

        self.x = center_x + radius
        self.y = center_y

    def update(self, dt):
        """
        Update the particle's angular position.
        """

        self.angle += self.omega * dt

        self.x, self.y = circular_position(
            self.center_x,
            self.center_y,
            self.radius,
            self.angle
        )

    def get_velocity(self):
        """
        Return the particle's velocity vector.
        """

        return velocity_vector(
            self.omega,
            self.radius,
            self.angle
        )

    def get_speed(self):
        """
        Return the magnitude of velocity.
        """

        return circular_velocity(
            self.omega,
            self.radius
        )

    def get_centripetal_acceleration(self):
        """
        Return centripetal acceleration vector.
        """

        return centripetal_acceleration_vector(
            self.omega,
            self.radius,
            self.angle
        )

    def reset(self):
        """
        Reset particle to starting position.
        """

        self.angle = 0.0

        self.x, self.y = circular_position(
            self.center_x,
            self.center_y,
            self.radius,
            self.angle
        )
