"""
The setup.py file is an essential part of packaging and distributing
Python projects. It is used by setuptools (or distilutils in older python)
to define the configuration of your project, such as its metadata, dependencies and more
"""

from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return the list of requirements...
    """
    requirement_list: List[str] = []
    try:
        with open('requirements.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                requirement = line.strip()
                # ignore -e .
                if requirement and requirement != "-e .":
                    requirement_list.append(requirement)
    except FileNotFoundError as e:
        print("requirements.txt not found")
    
    return requirement_list 


setup(
    name='Network Security',
    version='0.0.1',
    author='Anshul Khaire',
    author_email='anshulkhaire3303dll@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)