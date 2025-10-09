from setuptools import setup, find_packages
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="MLOPS-projects - 5",
    version="0.1",
    author="rohit",
    package = find_packages(),
    install_requires = requirements


)