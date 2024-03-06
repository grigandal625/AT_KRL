from setuptools import setup, find_packages

import json
import os

root = os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir))
os.chdir(root)

def read_pipenv_dependencies(fname):
    filepath = os.path.join(os.path.dirname(__file__), fname)
    with open(filepath) as lockfile:
        lockjson = json.load(lockfile)
        return [dependency for dependency in lockjson.get('default')]

if __name__ == '__main__':
    setup(
        name='at-krl',
        version=os.getenv('PACKAGE_VERSION', '0.0.dev8'),
        packages=find_packages(where='src'),
        package_dir={'': 'src'},
        description='AT-TECHNOLOGY knowledge representation language parsing and processing package.',
        install_requires=[
              *read_pipenv_dependencies('Pipfile.lock'),
        ]
    )