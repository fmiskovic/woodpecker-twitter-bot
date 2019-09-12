import os
from configparser import ConfigParser


class BotConfig:
    """Interact with configuration variables."""

    cfg_parser = ConfigParser()
    cfg_file_path = (os.path.join(os.getcwd(), 'config.ini'))

    @classmethod
    def initialize(cls):
        """Start config by reading config.ini."""
        cls.cfg_parser.read(cls.cfg_file_path)

    @classmethod
    def get_property_value(cls, key):
        """Get value from environment variable or config.ini."""
        value = os.getenv(key)
        if value is None:
            value = cls.cfg_parser.get('BOT', key)
        return value

    @classmethod
    def get_property_values(cls, key):
        """Get values from environment variable or config.ini."""
        result = []
        value = os.getenv(key)
        if value is None:
            value = cls.cfg_parser.get('BOT', key)

        if value is not None:
            result = value.split(',')
        return result
