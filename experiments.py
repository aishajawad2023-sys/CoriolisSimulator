# ==========================================
# CORIOLIS PHYSICS SIMULATOR
# experiments.py
# ==========================================

from physics import (
    centripetal_acceleration_omega,
    centripetal_force
)


def radius_experiment(
    omega,
    radii
):
    """
    Calculate centripetal acceleration
    for a range of radii.
    """

    results = []

    for radius in radii:

        acceleration = (
            centripetal_acceleration_omega(
                omega,
                radius
            )
        )

        results.append(
            (radius, acceleration)
        )

    return results


def velocity_experiment(
    mass,
    radius,
    velocities
):
    """
    Calculate centripetal force
    for a range of velocities.
    """

    results = []

    for velocity in velocities:

        force = centripetal_force(
            mass,
            velocity,
            radius
        )

        results.append(
            (velocity, force)
        )

    return results
