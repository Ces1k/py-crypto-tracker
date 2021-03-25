from pathlib import Path

from src.lib.utils import get_root_dir


def get_tests_root_dir():
    return get_root_dir().joinpath("tests")


def get_test_data_root_dir():
    return get_tests_root_dir().joinpath("test_data")
