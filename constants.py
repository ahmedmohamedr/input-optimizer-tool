SCREEN_RESOLUTIONS = {
    '720p': (1280, 720),
    '1080p': (1920, 1080),
    '1440p': (2560, 1440),
    '4k': (3840, 2160),
    '8k': (7680, 4320)
}

FPS_LIMITS = {
    'low': 30,
    'medium': 60,
    'high': 120,
    'ultra': 240
}

GRAPHIC_SETTINGS = {
    'low': 'Low quality textures and effects',
    'medium': 'Balanced quality and performance',
    'high': 'High quality textures and effects',
    'ultra': 'Maximum settings with no performance compromise'
}

DEFAULT_SETTINGS = {
    'resolution': '1080p',
    'fps_limit': 'high',
    'graphics': 'medium'
}

ERROR_MESSAGES = {
    'invalid_resolution': 'Resolution not supported!',
    'invalid_fps': 'FPS limit must be one of: low, medium, high, ultra',
    'invalid_graphic_setting': 'Graphic setting not recognized'
}