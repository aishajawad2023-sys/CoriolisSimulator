# ==========================================
# CORIOLIS PHYSICS SIMULATOR
# main.py
# ==========================================

import pygame

from settings import (
    WIDTH,
    HEIGHT,
    FPS,
    BACKGROUND,
    WHITE,
    GRAY,
    RED,
    BLUE,
    DEFAULT_RADIUS,
    DEFAULT_OMEGA,
    DEFAULT_MASS
)

from simulation import Particle

from physics import (
    centripetal_acceleration_omega
)

from ui import (
    draw_text,
    draw_vector
)


# ------------------------------------------
# INITIALIZE
# ------------------------------------------

pygame.init()

screen = pygame.display.set_mode(
    (WIDTH, HEIGHT)
)

pygame.display.set_caption(
    "Coriolis Physics Simulator"
)

clock = pygame.time.Clock()

font = pygame.font.Font(
    None,
    28
)

small_font = pygame.font.Font(
    None,
    22
)


# ------------------------------------------
# SIMULATION PARAMETERS
# ------------------------------------------

center_x = WIDTH // 2
center_y = HEIGHT // 2

radius = DEFAULT_RADIUS
omega = DEFAULT_OMEGA
mass = DEFAULT_MASS

particle = Particle(
    center_x,
    center_y,
    radius,
    omega
)

paused = False


# ------------------------------------------
# MAIN LOOP
# ------------------------------------------

running = True

while running:

    # --------------------------------------
    # TIME
    # --------------------------------------

    dt = clock.get_time() / 1000.0


    # --------------------------------------
    # EVENTS
    # --------------------------------------

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            # Pause
            if event.key == pygame.K_SPACE:
                paused = not paused

            # Reset
            if event.key == pygame.K_r:
                particle.reset()


    # --------------------------------------
    # KEYBOARD CONTROLS
    # --------------------------------------

    keys = pygame.key.get_pressed()

    # Change radius
    if keys[pygame.K_UP]:
        radius += 100 * dt

    if keys[pygame.K_DOWN]:
        radius -= 100 * dt

    # Change angular velocity
    if keys[pygame.K_RIGHT]:
        omega += 0.5 * dt

    if keys[pygame.K_LEFT]:
        omega -= 0.5 * dt


    # Keep values reasonable
    radius = max(50, min(radius, 300))

    omega = max(
        0.1,
        min(omega, 5.0)
    )


    # --------------------------------------
    # UPDATE PARTICLE PARAMETERS
    # --------------------------------------

    particle.radius = radius
    particle.omega = omega

    if not paused:
        particle.update(dt)


    # --------------------------------------
    # PHYSICS
    # --------------------------------------

    velocity = particle.get_speed()

    centripetal_acceleration = (
        centripetal_acceleration_omega(
            omega,
            radius
        )
    )

    velocity_vector = (
        particle.get_velocity()
    )

    acceleration_vector = (
        particle.get_centripetal_acceleration()
    )


    # --------------------------------------
    # DRAW BACKGROUND
    # --------------------------------------

    screen.fill(BACKGROUND)


    # --------------------------------------
    # DRAW CIRCLE
    # --------------------------------------

    pygame.draw.circle(
        screen,
        GRAY,
        (center_x, center_y),
        int(radius),
        3
    )


    # --------------------------------------
    # DRAW CENTER
    # --------------------------------------

    pygame.draw.circle(
        screen,
        WHITE,
        (center_x, center_y),
        6
    )


    # --------------------------------------
    # DRAW PARTICLE
    # --------------------------------------

    pygame.draw.circle(
        screen,
        RED,
        (
            int(particle.x),
            int(particle.y)
        ),
        12
    )


    # --------------------------------------
    # DRAW VELOCITY VECTOR
    # --------------------------------------

    draw_vector(
        screen,
        (particle.x, particle.y),
        velocity_vector,
        BLUE,
        scale=3
    )


    # --------------------------------------
    # DRAW CENTRIPETAL ACCELERATION
    # --------------------------------------

    draw_vector(
        screen,
        (particle.x, particle.y),
        acceleration_vector,
        RED,
        scale=10
    )


    # --------------------------------------
    # INFORMATION PANEL
    # --------------------------------------

    draw_text(
        screen,
        "CIRCULAR MOTION",
        25,
        20,
        font,
        WHITE
    )

    draw_text(
        screen,
        f"Radius: {radius:.1f} m",
        25,
        60,
        small_font,
        WHITE
    )

    draw_text(
        screen,
        f"Angular velocity: {omega:.2f} rad/s",
        25,
        90,
        small_font,
        WHITE
    )

    draw_text(
        screen,
        f"Speed: {velocity:.2f} m/s",
        25,
        120,
        small_font,
        WHITE
    )

    draw_text(
        screen,
        f"Centripetal acceleration: "
        f"{centripetal_acceleration:.2f} m/s²",
        25,
        150,
        small_font,
        WHITE
    )


    # --------------------------------------
    # CONTROLS
    # --------------------------------------

    draw_text(
        screen,
        "↑ ↓  Radius",
        25,
        HEIGHT - 100,
        small_font,
        WHITE
    )

    draw_text(
        screen,
        "← →  Angular velocity",
        25,
        HEIGHT - 70,
        small_font,
        WHITE
    )

    draw_text(
        screen,
        "SPACE  Pause     R  Reset",
        25,
        HEIGHT - 40,
        small_font,
        WHITE
    )


    # --------------------------------------
    # PAUSE INDICATOR
    # --------------------------------------

    if paused:

        draw_text(
            screen,
            "PAUSED",
            WIDTH // 2 - 50,
            30,
            font,
            WHITE
        )


    # --------------------------------------
    # DISPLAY
    # --------------------------------------

    pygame.display.flip()

    clock.tick(FPS)


# ------------------------------------------
# EXIT
# ------------------------------------------

pygame.quit()
