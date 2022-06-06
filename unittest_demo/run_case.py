import unittest
import sys
from HTMLTestRunner import  HTMLTestRunner
user_list = [{'role': 'admin', 'account': 'admin', 'password': '123456', 'dept': 'tester'}, {'role': 'user', 'account': 'dev', 'password': '123456', 'dept': 'dev'}, {'account': 'csc', 'password': '123456', 'role': 'test', 'dept': 'test'}]
result = {"code":0,"message":""}
def login(username,password):

    global login_status

    # 用户名或密码为空的情况
    if username is None or username == "":
        result.update({"code":1,"message":"用户名不能为空"})
        return result
    if password is None or username == "":
        result.update({"code":1,"message":"密码不能为空"})
        return result

    # 登录成功的情况
    for user_info in user_list:
        if username == user_info.get('account') and password == user_info.get('password'):
            result.update({"message":"登录成功!","user_list":user_list})
            login_status = 1
            return result

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
    suit_a = unittest.TestSuite()
    suit_a.addTest(Testjoin('test_lojin_success'))
    suit_a.addTest(Testjoin('test_user_wrong'))
    suit_a.addTest(Testjoin('test_password_is_null'))
    test_report = './test_report.html'
    with open(test_report, 'wb') as f:
        runer = HTMLTestRunner(f, title='测试报告', description='测试报告描述')
        runer.run(suit_a)