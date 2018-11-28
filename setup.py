# ---------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the MIT License. See LICENSE.txt in the project root for license information.
# ---------------------------------------------------------------------------------------------

from os import path

from setuptools import find_packages, setup

with open(path.join(path.abspath(path.dirname(__file__)), 'README.md'), 'r') as rf:
    LONG_DESCRIPTION = rf.read()

setup(
    # PEP8: Packages should also have short, all-lowercase names, the use of underscores is discouraged
    name='pylintfileheader',
    version='0.0.2',
    packages=find_packages(exclude=['*test']),
    description='Enables pylint to force a consistent file header.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='https://github.com/HaaLeo/pylint-file-header',
    author='Leo Hanisch',
    license='MIT',
    package_data={'pylintfileheader': ['ThirdPartyNotices.txt']},
    install_requires=[],
    project_urls={
        'Issue Tracker': 'https://github.com/HaaLeo/pylint-file-header/issues',
        'Changelog': 'https://github.com/HaaLeo/pylint-file-header/blob/master/CHANGELOG.md'
    },
    python_requires='>=2.7',
    keywords=[
        'pylintfileheader',
        'pylint',
        'file',
        'module',
        'header'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ]
)
