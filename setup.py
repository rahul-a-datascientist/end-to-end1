from setuptools import find_packages,setup
from typing import List

hyphen_dot='-e .'

def get_requirements(file_path:str)->List[str]:

  requirements=[]
  with open(file_path) as file_obj:
    requirements=file_obj.readlines()
    requirements=[req.strip('\n') for req in requirements]
    if hyphen_dot in requirements:
      requirements.remove(hyphen_dot)
  return requirements
setup(
  name='end-to-end1',
  version='0.0.1',
  author='rahul',
  author_email='rahul726224@gmail.com',
  packages=find_packages(),
  install_requires=get_requirements('requirements.txt')
)