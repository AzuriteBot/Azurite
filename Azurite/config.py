import os
import yaml
from Azurite import Logger
baseDir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
moduleDir = os.path.join(baseDir, 'modules')

class config():
    def __init__(self, name):
        super().__init__()
        self.name = name
    def make_config_folder(self):
        os.makedirs(name=self.name, exist_ok=True)
    def get_config(self, config_name):
        if not os.path.exists(os.path.join(moduleDir, self.name, config_name)):
            Logger.ERROR("config file not exists!")
            return None
        with open(os.path.join(moduleDir, self.name, config_name)) as f:
            return yaml.load(stream=f, Loader=yaml.SafeLoader)


