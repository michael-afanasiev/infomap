"""
InfoMap

A simple set of scripts to plot colour-coded infographic maps.
"""

from setuptools import setup, find_packages

setup(
    name='infomap',
    version=0.1,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'cartopy'
    ],
    entry_points='''
    [console_scripts]
    infomap=infomap.main:cli
    '''
)
