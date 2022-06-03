"""
需求-迭代1:登录功能
1.定义两条用户数据，要求用户数据的属性包括用户角色，用户账号，密码，部门
2.要求返回的格式是字典形式，包含两个字段:code和message，code为0代表成功，为1代表失败；message给出相应的提示
3.用户通过控制台输入用户名和密码，判断用户名和密码是否和定义的数据一样，若匹配则返回登陆成功消息体
4.若用户名输入为空或密码输入为空，都给出相应的提示，用户名不能为空
5.若用户名或密码不匹配，都给出登陆失败，请检查您的用户名或密码是否填写正确提示
"""
"""
需求-迭代2:用户查询功能
1.用户查询功能必须是在登陆以后才能用，否则给出权限不足提示
2.若输入的用户名正确，返回登录用户的信息，password字段不显示
3.若输入的用户名不正确，给出无法查询的结果提示
4.查询支持模糊查询
"""
from datetime import datetime
def from_file_get_data(file_name):
    f = None
    try:
        f = open(file_name,"r")
        line = f.readline()
        user_data = eval(line)
        return user_data
    except Exception as e:
        print(e)
    finally:
        if not f:
            f.close()

def save_data(file_name,file_content):
    f = None
    try:
        f = open(file_name,'w')
        f.write(str(file_content))
    except Exception as e:
        print(e)
    finally:
        if not f:
            f.close()
# 1.定义用户默认数据
# user_list = [{'role': 'admin', 'account': 'admin', 'password': '123456', 'dept': 'tester'},{'role': 'user', 'account': 'dev', 'password': '123456', 'dept': 'dev'}]

user_list = []
user_list= user_list if user_list else from_file_get_data('user_data')
# 2.定义默认返回结果
result = {"code":0,"message":""}
# 3.定义登录功能
def login(usrname,password):

    # 用户名或密码为空
    if usrname is None or usrname == "":
        result.update({"code":1,"message":"用户名不能为空"})
        return result
    if password is None or password == "":
        result.update({"code":1,"message":"密码不能为空"})
        return result

    # 登陆成功
    for user_info in user_list:
        if username == user_info.get('account') and user_info.get('password'):
            result.update({"message":"登陆成功!","user_list":user_list})
            return result
     # 用户名密码不匹配
    result.update({"code":1,"message":"用户名或者密码错误"})
    return result

class User():

    def add_user(self,username,password='123456',**kwargs):
        user_dict = {}
        user_dict['account'] = username
        user_dict['password'] = password
        user_dict.update(**kwargs)
        user_list.append(user_dict)
        save_data('user_data',user_list)
        result.update({"message":"用户添加成功","add_time":datetime.now()})
# 用户查询功能
    def get_user(self,username):
    # 判断用户名是否登录
        if not result.get("code") :
            result.update({'code':11,'message':"用户未登录，无法查询"})
            return result
        result.update({"user_list":[]})
        lst = []
        for x in user_list:
            account = x.get("account")
            if username in account:
                x.pop("password")
                lst.append(x)
        if lst:
            result.update({"message":"用户查询成功","user_list":lst})
            return result
        result.update({"code":12,"message":"未查到用户，请重新输入"})
        return result




if __name__ == '__main__':

    # 1.进行循环，让用户做各种操作
    flag = True
    while flag:
        # 提供用户的各种选择，比如输入1代表登录操作，输入2代表查询操作，输入q代表推出操作
        vls = input("操作请输入对应的编号:"
              "\n 1:进行登录"
              "\n 2:查询用户，请输入用户名:"
              "\n 3:添加用户，请输入用户信息:"
              "\n q:退出操作")
        # 当输入未知符号后，进行重新输入
        if not vls in ('1','2','3','q','quite'):
            print("其他字符位置操作，请重新输入:\n",
                  "="*30)
            continue
        # 进行登录操作
        if vls == '1':
            username = input("请输入用户名:")
            password = input("请输入密码:")
            login_result = login(username,password)
            print(login_result)
            print("="*30)
            continue
        # 进行查询用户的情况
        if vls == '2':
            name = input("请输入查询用户名:")
            user = User()
            get_result = user.get_user(name)
            print(get_result)
            print("="*30)
            continue

        if vls == '3':
            name = input("请输入添加的用户名:")
            user = User()
            get_result = user.get_user(name)
            if 12 == get_result.get('code'):
                password = input("请输入用户密码")
                role = input("请输入用户角色")
                dept = input("请输入用户部门")
                User.add_user(name,password,role=role,dept=dept)
            if 0 == get_result.get('code'):
                result.update({'code':13,'message':"用户已存在无法添加"})
                print(result)
            print(get_result)
            print("="*30)
        # 是否退出
        if vls in ('q','quite'):
            flag = False
            print("退出成功!")






