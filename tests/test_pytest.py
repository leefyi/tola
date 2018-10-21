#!/usr/local/bin python
# coding=utf-8
# @Time    : 2018/10/18 下午10:01
# @Author  : lifangyi
# @File    : test_pytest.py
# @Software: PyCharm

import pytest


@pytest.fixture  # 创建测试环境，可以用来做setUp和tearDown的工作
def setup_math():
    import math
    return math


@pytest.fixture(scope='function')
def setup_function(request):
    def teardown_function():
        print('teardown function called.')
    request.addfinalizer(teardown_function)  # 这个内嵌的函数做tearDown工作
    print('setup_function called.')


def test_func(setup_function):
    print('Test_Func called.')


def test_setup_math(setup_math):
    # pytest 不需要使用self.assertXXX这样的方法，直接使用Python内置的断言语句assert即可
    assert setup_math.pow(2, 3) == 8


class TestClass(object):
    def test_in(self):
        assert 'h' in 'hello'

    def test_two(self, setup_math):
        assert setup_math.ceil(10) == 11.0

    # def test_raise_exit(self):
    #     raise SystemExit(1)
    #
    # def test_mytest(self):
    #     with pytest.raises(SystemExit): # 用来测试抛出的异常
    #         TestClass.test_raise_exit(self)


@pytest.mark.parametrize('test_input,expected', [
    ('1+3', 4),
    ('2*4', 8),
    ('1==2', False),
])
def test_eval(test_input, expected):
    assert eval(test_input) == expected
