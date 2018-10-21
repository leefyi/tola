#!/usr/local/bin python
# coding=utf-8
# @Time    : 2018/10/21 下午8:07
# @Author  : lifangyi
# @File    : setup.py
# @Software: PyCharm

from setuptools import find_packages, setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):

    def run_tests(self):
        import pytest
        errno = pytest.main([])
        exit(errno)


setup(
    name='Tola',
    version=0.1,
    url='http://www.dongwm.com/',
    author='Dong Weiming',
    license='BSD',
    packages=find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    zip_safe=True,
    test_suite='tests',
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)