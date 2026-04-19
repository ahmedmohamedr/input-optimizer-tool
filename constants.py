FPS_LIMIT = 60

RESOLUTIONS = {
    '1080p': (1920, 1080),
    '1440p': (2560, 1440),
    '4k': (3840, 2160),
    '720p': (1280, 720)
}

# Player input mappings
PLAYER_INPUTS = {
    'W': 'MOVE_UP',
    'S': 'MOVE_DOWN',
    'A': 'MOVE_LEFT',
    'D': 'MOVE_RIGHT',
    'SPACE': 'JUMP',
    'CTRL': 'CROUCH'
}

# Game state constants
GAME_STATES = {
    'LOADING': 0,
    'PLAYING': 1,
    'PAUSED': 2,
    'GAME_OVER': 3
}

# Audio settings
DEFAULT_VOLUME = 0.5
MAX_VOLUME = 1.0
MIN_VOLUME = 0.0

# Control sensitivity settings
MOUSE_SENSITIVITY = 1.0
KEYBOARD_SENSITIVITY = 1.0

# Graphics settings
GRAPHICS_OPTIONS = {
    'LOW': 1,
    'MEDIUM': 2,
    'HIGH': 3,
    'ULTRA': 4
}

# Define color codes
COLORS = {
    'WHITE': (255, 255, 255),
    'BLACK': (0, 0, 0),
    'RED': (255, 0, 0),
    'GREEN': (0, 255, 0),
    'BLUE': (0, 0, 255)
}
