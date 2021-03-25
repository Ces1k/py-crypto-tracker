from setuptools import setup, find_packages

AUTHOR = "Ces1k"
NAME = "py-crypto-tracker"


setup(
    name=NAME,
    version="0.0.1",
    description="Crypto currency tracker written in Python",
    author=AUTHOR,
    url=f"https://github.com/{AUTHOR}/{NAME}",
    entry_points={
        "console_scripts": [
            "track = src.main:main",
            "tracker = src.main:main",
        ]
    },
    install_requires=[
        "pyyaml",
        "requests",
    ],
    extras_require={
        "dev": [
            "black",
            "flake8",
            "pytest",
            "pytest-cov",
            "pytest-mock",
        ]
    },
    packages=find_packages(),
    python_requires=">=3.7",
)
