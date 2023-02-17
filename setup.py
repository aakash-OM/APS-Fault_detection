#useful for distribution of source code as Liberary format.

from setuptools import find_packages,setup

REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements()->List[str]:
    
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
    requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
    #repla

setup(
    name="sensor",
    version="0.0.1",
    author="Aakash",
    author_email="aakashmittal0207@gmail.com",
    packages = find_packages(), #this find_packages search for Python source code wherever it finds that code it will convert into packages.  
    install_requires=get_requirements(),
)