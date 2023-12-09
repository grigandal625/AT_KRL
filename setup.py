from setuptools import setup, find_packages

import json
import os

def read_pipenv_dependencies(fname):
    # Получаем из Pipfile.lock зависимости по умолчанию.
    filepath = os.path.join(os.path.dirname(__file__), fname)
    with open(filepath) as lockfile:
        lockjson = json.load(lockfile)
        return [dependency for dependency in lockjson.get('default')]

if __name__ == '__main__':
    setup(
        name='at-krl',
        version=os.getenv('PACKAGE_VERSION', '0.0.dev0'),
        package_dir={'': 'src'},
        packages=find_packages('src', include=[
            'at_krl*'
        ]),
        description='AT-TECHNOLOGY knowledge representation language parsing and processing package.',
        install_requires=[
              *read_pipenv_dependencies('Pipfile.lock'),
        ]
    )