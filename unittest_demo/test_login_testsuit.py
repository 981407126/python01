import unittest
from project.project import login
import sys
from unittest_demo.HTMLTestRunner import HTMLTestRunner
class Testjoin(unittest.TestCase):

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
    suit_a = unittest.TestLoader().discover('.',pattern='test_login_*')
    print(suit_a)
    test_report = './test_report.html'
    with open(test_report, 'wb') as f:
        runer = HTMLTestRunner(f, title='测试报告', description='测试报告描述')
        runer.run(suit_a)
