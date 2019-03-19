# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='autofeat',
    version='0.0.1',
    description='autofeat',
    long_description=readme,
    author='Franziska Horn',
    author_email='neutatz@gmail.com',
    url='https://github.com/cod3licious/autofeat',
    license=license,
    #package_data={'config': ['fastsklearnfeature/configuration/resources']},
    include_package_data=True,
    install_requires=["numpy", "pandas", "scikit-learn", "sympy", "pint", "joblib"],
    packages=find_packages(exclude=('tests', 'docs'))
)