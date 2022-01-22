from setuptools import setup
from setuptools import find_packages


VERSION = '0.1.0'

setup(
    name='Triangle-Msh-To-Voronoi',  # package name
    version=VERSION,  # package version
    description='三角形网格转为泰森多边形',  # package description
    packages=find_packages(),
    zip_safe=False,
)