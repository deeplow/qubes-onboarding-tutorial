#!/usr/bin/env python3
''' Setup.py file '''
import os
import setuptools

def read_file(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()

setuptools.setup(
    name='tutorial_1_bundled_programs',
    version=read_file('version').strip(),
    author='deeplow',
    author_email='deeplower at protonmail.com',
    description='Bundled Programs for Qubes Integrated Tutorial 1',
    license='GPL2+',
    url='https://github.com/deeplow',
    keywords='integrated qubes tutorial',
    packages=("mock_filemanager",),
    package_data = {
            'mock_filemanager': ['*.ui', 'images/*'],
    },
    entry_points={
        'console_scripts': [
            'qubes-tutorial-mock-filemanager = mock_filemanager.mock_filemanager:main'
        ]
    }
)
