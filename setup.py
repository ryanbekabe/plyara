# Copyright 2014 Christian Buia
# Copyright 2020 plyara Maintainers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""
import pathlib
from setuptools import find_packages, setup

here = pathlib.Path().cwd()

setup(
    name='plyara',
    version='3.0.0',
    description='Parse YARA rules.',
    # long_description=long_description,   Add this back, but markdown.
    url='https://github.com/plyara/plyara',
    author='plyara Maintainers',
    license='Apache License 2.0',
    test_suite='tests.unit_tests',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='malware analysis yara',
    packages=find_packages(exclude=['docs', 'examples', 'tests']),
    install_requires=[
        'sly'
    ],
    entry_points={
        'console_scripts': [
            'plyara=plyara.command_line:main',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/plyara/plyara/issues',
        'Source': 'https://github.com/plyara/plyara',
    },
)
