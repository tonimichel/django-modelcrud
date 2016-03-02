#! /usr/bin/env python
import os
from setuptools import setup, find_packages

def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''

setup(
    name='django-modelcrud',
    version='0.1',
    description='A lightweight approach to automate crud on django models.',
    long_description=read('README.rst'),
    license='MIT',
    keywords='django, crud, django admin alternative',
    author='Toni Michel',
    author_email='toni.michel@schnapptack.de',
    url="https://github.com/tonimichel/django-modelcrud.git",
    packages=find_packages(),
    package_dir={'modelcrud': 'modelcrud'},
    include_package_data=True,
    scripts=[],
    zip_safe=False,
    classifiers=[
        'License :: MIT',
        'Programming Language :: Python',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent'
    ],
    install_requires=[
        'Django>=1.9'
    ]
)
