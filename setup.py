from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages
setup(
        name = "runmanager",
        packages = find_packages(),
        install_requires = ['zprocess', 'qtutils']
)

