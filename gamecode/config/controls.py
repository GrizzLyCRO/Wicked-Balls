import yaml
import os
script_dir = os.path.dirname(__file__)
rel_path = "binds.yaml"
abs_file_path = os.path.join(script_dir, rel_path)
stream = open(abs_file_path, 'r')
profiles = yaml.load(stream)

print profiles[0]