
import json
from setuptools import setup

with open('package.json') as fp:
  package = json.load(fp)

setup(
  name = 'houdini_nodeshape_converter',
  version = '0.0.1',
  author = 'Niklas Rosenstein',
  author_email = 'rosensteinniklas@gmail.com',
  py_modules = ['houdini_nodeshape_converter'],
  install_requires = [x+y for x, y in package['python-dependencies'].items()],
  entry_points = {
    'console_scripts': [
      'houdini-nodeshape-converter=houdini_nodeshape_converter:main'
    ]
  }
)