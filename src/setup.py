#!/usr/bin/python
# -*- coding: utf-8 -*-

# /*
#  * ----------------------------------------------------------------------------
#  * "THE BEER-WARE LICENSE" (Revision 42):
#  * <fruh> wrote this file.  As long as you retain this notice you
#  * can do whatever you want with this stuff. If we meet some day, and you think
#  * this stuff is worth it, you can buy me a beer in return.   Poul-Henning Kamp
#  * ----------------------------------------------------------------------------
#  */

import liketits
from setuptools import setup

setup(
    name='tits',
    version=liketits.VERSION,
    description='Show ASCII art pictures like tits 8). By default random tits are slowly printed, but you can select one or print funny one.',
    keywords='tits ascii art',
    url='https://github.com/FrUh/tits',
    author='fruh',
    author_email='frantisek.uhrecky@gmail.com',
    license='BEER-WARE',
    packages=['liketits'],
    scripts=["tits"],
    zip_safe=False
)