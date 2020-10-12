#!/usr/bin/env python

import setuptools


setuptools.setup(
    description="Cartist",
    version='0.1.0',
    python_requires='>=3.6',
    name='cartist',
    entry_points={
        'console_scripts': [],
    },
    install_requires=[],
    packages=setuptools.find_packages(include=['cartist', ]),
    zip_safe=False,
)
