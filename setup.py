from setuptools import find_packages,setup
from typing import List
Hypen_e = '-e .'
def get_requirments(file_path:str)->List[str]:
    '''
    this function will return the list of the requirments 
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        [req.replace("\n","")for req in requirements]
        if Hypen_e in requirements:
            requirements.remove(Hypen_e)
    return requirements

setup(
name = 'mlproject0',
version='0.0.1',
author='Nikhil',
author_email='nikhilpareek1998@gmail.com',
packages=find_packages(),
install_requires=get_requirments('requirment.txt')
)