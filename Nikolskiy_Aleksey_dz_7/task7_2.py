import os
import yaml
from task7_1 import make_dirs

HOME = os.path.split(os.path.abspath(__file__))[0]

with open('files/config.yaml') as f:
    list_dir = yaml.safe_load(f)


make_dirs(HOME, list_dir)


