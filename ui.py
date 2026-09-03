# ==========================================
# CORIOLIS PHYSICS SIMULATOR
# ui.py
# ==========================================

import pygame


def draw_text(
    screen,
    text,
    x,
    y,
    font,
    color=(240, 240, 240)
):
    """
    Draw text on the screen.
    """

    surface = font.render(
        str(text),
        True,
        color
    )

    screen.blit(
        surface,
        (x, y)
    )


def draw_vector(
    screen,
    start,
    vector,
    color,
    scale=1.0,
    width=3
):
    """
    Draw a vector with an arrowhead.

    start  = starting (x, y)
    vector = NumPy-style [x, y]
    """

    x1, y1 = start

    x2 = x1 + vector[0] * scale
    y2 = y1 + vector[1] * scale

    pygame.draw.line(
        screen,
        color,
        (x1, y1),
        (x2, y2),
        width
    )

    # Arrowhead
    angle = pygame.math.Vector2(
        x2 - x1,
        y2 - y1
    ).angle_to(
        pygame.math.Vector2(1, 0)
    )

    arrow_length = 12

    left = pygame.math.Vector2(
        arrow_length,
        0
    ).rotate(-angle + 150)

    right = pygame.math.Vector2(
        arrow_length,
        0
    ).rotate(-angle - 150)

    pygame.draw.polygon(
        screen,
        color,
        [
            (x2, y2),
            (x2 + left.x, y2 + left.y),
            (x2 + right.x, y2 + right.y)
        ]
    )
