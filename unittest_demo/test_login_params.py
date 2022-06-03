# 测试用例参数化(测试用例过多导致冗余:代码重复，数据不同)
import unittest

from parameterized import parameterized             # 将列表中数据用一条测试用例循环运行，起到多条测试数据的作用

from project.project import login


lst_data = [(0,'admin','123456'),(0,'dev','123456'),(1,'dev','123456')]

class TestLogin(unittest.TestCase):

    @parameterized.expand(lst_data)
    def test_lojin(self,except_value,username,password):

        actual_value = login(username,password).get('code')
        self.assertEqual(except_value,actual_value)

if __name__ == '__main__':
        unittest.main




