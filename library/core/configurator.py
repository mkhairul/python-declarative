import yaml
import os, inspect
import importlib

class Configurator:
    def __init__(self, configuration_file=''):
        self.config_file = ''

        if configuration_file == '':
            self.config_file = 'default.yml'

        file = open( os.path.join(os.getcwd(), self.config_file), 'r')
        self.contents = yaml.safe_load( file )
        print(self.contents)

    def run(self):
        for i in self.contents['jobs']:
            module = importlib.import_module('library.plugins.'+i)
            members = inspect.getmembers(module, inspect.isclass)
            # initialize the class
            class_ = getattr(module, members[0][0])
            instance_ = class_()
            for j in self.contents['jobs'][i]:
                method_name = j
                method_val = self.contents['jobs'][i][method_name]
                print(f"{method_name} = {method_val}")
                if hasattr(instance_, method_name):
                    getattr(instance_, method_name)(method_val)