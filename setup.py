from setuptools import setup, find_packages
Hypen_E_Dot='-e .'
def get_requirements(file_path:str)->list[str]:
  requirements = []
  with open(file_path, 'r') as file_object:
    requirements=file_object.readlines()
    requirements=[req.replace("\n","") for req in requirements]
    if Hypen_E_Dot in requirements:
        requirements.remove(Hypen_E_Dot)
  return requirements


setup(
    name='StudentPerformaceML',
    version='1.0',
    author='Vamsi',
    author_email='',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
