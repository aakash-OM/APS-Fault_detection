
from setuptools import find_packages,setup

from typing import List

REQUIREMENT_FILE_NAME="requirements.txt"
HYPHEN_E_DOT = "-e ." #we added this to trigger setup.py file

def get_requirements()->List[str]: # -> :this function is going to return a list which will contain strings
    
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
    requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
    
    if HYPHEN_E_DOT in requirement_list:
        requirement_list.remove(HYPHEN_E_DOT)
    return requirement_list



setup(
    name="sensor",
    version="0.0.2",
    author="Aakash",
    author_email="aakashmittal0207@gmail.com",
    packages = find_packages(),  #this find_packages search for Python source code wherever it finds that code it will convert into packages.
    install_requires = get_requirements()
) 