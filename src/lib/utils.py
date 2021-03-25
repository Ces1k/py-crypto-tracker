import logging
from pathlib import Path

import yaml

MODULE_LOGGER = logging.getLogger(Path(__file__).name)


def get_root_dir():
    root_dir = Path(__file__).parent.parent.parent
    return root_dir


def load_yaml(path):
    with open(path, "r") as yaml_file:
        return yaml.safe_load(yaml_file)
