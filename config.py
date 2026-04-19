import os

class Config:
    def __init__(self):
        self.settings = {
            'resolution': '1920x1080',
            'fullscreen': True,
            'volume': 75,
            'brightness': 50,
            'language': 'en'
        }

    def load_settings(self):
        env_file = os.path.join(os.getcwd(), '.env')
        if os.path.exists(env_file):
            with open(env_file) as f:
                for line in f:
                    key, value = line.strip().split('=')
                    if key in self.settings:
                        self.settings[key] = self.parse_value(value)

    @staticmethod
    def parse_value(value):
        if value.isdigit():
            return int(value)
        elif value.lower() in ['true', 'false']:
            return value.lower() == 'true'
        return value

    def save_settings(self):
        with open(os.path.join(os.getcwd(), '.env'), 'w') as f:
            for key, value in self.settings.items():
                f.write(f'{key}={value}\n')

config = Config()
config.load_settings()