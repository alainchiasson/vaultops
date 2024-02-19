import argparse
import json
import os

class _Config:
    def __init__(self):
        """ Load the config file and parse the command line arguments. File takes precedence"""

        # Get command line arguments first
        parser = argparse.ArgumentParser(description = 'MyApp')
        parser.add_argument('-c', '--config', help='Config file', default='config.json')
        parser.add_argument('-v', '--vault_url', help='Vault URL')
        self.args = parser.parse_args()
        
        with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), getattr(self.args, 'config'))) as json_config_file:
            self.config = json.load(json_config_file)

    def __getattr__(self, name):
        try:
            return self.config[name]
        except KeyError:
            return getattr(self.args, name)


config = _Config()
