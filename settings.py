# ==========================================
# CORIOLIS PHYSICS SIMULATOR
# settings.py
# ==========================================

# Window
WIDTH = 1200
HEIGHT = 750

FPS = 60

# Colors
BACKGROUND = (18, 20, 28)
WHITE = (240, 240, 240)
GRAY = (120, 120, 120)

RED = (240, 80, 80)
GREEN = (80, 220, 120)
BLUE = (80, 150, 240)
YELLOW = (240, 210, 80)
PURPLE = (190, 100, 240)

# Simulation
DEFAULT_RADIUS = 200.0
DEFAULT_OMEGA = 1.0
DEFAULT_MASS = 1.0

# Physics
GRAVITY = 9.81

# Earth
EARTH_RADIUS = 6_371_000.0
EARTH_DAY = 86_400.0

EARTH_OMEGA = 2 * 3.141592653589793 / EARTH_DAY
