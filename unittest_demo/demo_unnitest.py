"""
TestCase:测试用例
TestSuite:测试套件
TestTextRuner:执行测试
TestLoader:用来加载TestCase到TestSuite中,批量运行测试用例

"""

"""
测试过程中，最小的单元就是测试用例(TestCase) . 在unittest做测试时，需要遵循如下规则：
所编写的测试用例，必须是一个类，而且必须继承TestCase类 。
每个测试方法，都是以test开头
编写测试类，建议以Test开头
编写的模块，建议小写test开头
"""

import unittest
from project.project import login
import sys
class Testjoin(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("初始化类方法")
    def setUp(self) -> None:
        print("开始运行方法:")

    def test_lojin_success(self):
        except_value = 0
        actual_value = login('admin','123456').get('code')
        self.assertEqual(except_value,actual_value)

    def test_user_wrong(self):
        except_value = 1
        actual_value = login('abc', '1234567').get('code')
        self.assertEqual(except_value, actual_value)

    def test_password_is_null(self):
        except_value = 1
        actual_value = login('admin', 'None').get('code')
        self.assertEqual(except_value, actual_value)

if __name__ == '__main__':
    unittest.main()