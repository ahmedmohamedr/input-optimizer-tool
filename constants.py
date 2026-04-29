GAMEMODES = {'casual': 'Easy', 'competitive': 'Hard', 'hardcore': 'Extreme'}

DEFAULT_SETTINGS = {
    'resolution': (1920, 1080),
    'volume': 75,
    'brightness': 50,
    'fullscreen': True,
}

KEYBINDINGS = {
    'move_left': 'A',
    'move_right': 'D',
    'jump': 'SPACE',
    'crouch': 'CTRL',
    'shoot': 'LEFT_MOUSE',
}

FPS_LIMITS = [30, 60, 120, 144]

def get_game_mode_description(mode):
    return GAMEMODES.get(mode, 'Unknown mode')


def get_default_setting(setting):
    return DEFAULT_SETTINGS.get(setting, 'Not Found')


def is_valid_key_binding(key):
    return key in KEYBINDINGS.values()


def is_valid_fps_limit(limit):
    return limit in FPS_LIMITS