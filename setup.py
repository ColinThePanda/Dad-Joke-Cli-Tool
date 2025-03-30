from setuptools import setup, find_packages

setup(
    name="dad-joke-cli",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "typer"
    ],
    entry_points={
        "console_scripts": [
            "dad-joke=dad_joke:main",  # Note: this matches your original file structure
        ],
    },
)