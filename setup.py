from setuptools import find_packages,setup # setuptools is basically a package that provides tools from packaginf python projects and find_packages is a function which finds packages in your project
from typing import List
HYPEN_E_DOT= "-e."
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    return requirements
    

setup(
    name="visibility project",
    version="0.0.2",
    author="vibhanshu",
    author_mail="vibhanshugupta875@gmail.com",
    install_requirements=get_requirements("requirement.txt"),
    packages=find_packages()
)