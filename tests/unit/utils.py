import os
import json
import logging
from typing import Dict

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Config:
    def __init__(self, config_file: str):
        self.config_file = config_file

    def load_config(self) -> Dict:
        with open(self.config_file, 'r') as f:
            return json.load(f)

    def save_config(self, data: Dict) -> None:
        with open(self.config_file, 'w') as f:
            json.dump(data, f, indent=4)

class ConfigManager:
    def __init__(self, config_file: str):
        self.config = Config(config_file)

    def get_config(self) -> Dict:
        return self.config.load_config()

    def set_config(self, data: Dict) -> None:
        self.config.save_config(data)

class ConfigLoader:
    def __init__(self, config_file: str):
        self.config_file = config_file

    def load_config(self) -> Dict:
        return self.config_file

    def save_config(self, data: Dict) -> None:
        self.config_file = data

class ConfigLoaderManager:
    def __init__(self, config_file: str):
        self.config_file = config_file

    def load_config(self) -> Dict:
        return ConfigLoader(self.config_file).get_config()

    def save_config(self, data: Dict) -> None:
        ConfigLoader(self.config_file).save_config(data)