#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='gits',
    version='0.0.1',
    license='',
    description='',
    long_description=None,
    author='Peilonrayz',
    author_email='peilonrayz@gmail.com',
    url='https://github.com/Peilonrayz/gits',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='',
    entry_points={
        "console_scripts": [
            "gits=gits.__main__:main"
        ]
    },
)
