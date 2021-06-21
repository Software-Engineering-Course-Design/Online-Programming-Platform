from flask import Blueprint, render_template, redirect,request
from . import db
from flask_cors import *

signup = Blueprint('signup',__name__)

def query_db(query, args=(), one=False):
        cur = db.get_db().execute(query, args)
        rv = cur.fetchall()
        cur.close()
        return (rv[0] if rv else None) if one else rv

@signup.route('/signup_info',methods=['GET','POST'])
@cross_origin()
def signup_info():
    if request.method == 'POST': 

#
            username=request.json.get("username") 
            userType=request.json.get("userType")
            password=request.json.get("password") 
            checkpwd=request.json.get("checkpwd")
            hr_code=request.json.get("hr_code")
            print(sqlite3.sqlite_version)
   #         print(type(password))
   #        print(len(password))
   #         print(password.isalpha())
            if password!=checkpwd:
                return dict(ifExist=True, msg="错误！密码和确认密码不相同！!")
            if userType==True and hr_code!="666666":
                return dict(ifExist=True, msg="邀请码错误！")


            if len(password)<5:
            	if password.isalpha() or password.isdigit():
            		return dict(ifExist=True, msg="请输入至少5位的密码，且密码不能仅包含字母或数字！")
            	else:
            		return dict(ifExist=True, msg="请输入至少5位的密码！")
            if len(password)>=5:
            	if password.isalpha() or password.isdigit():
            		return dict(ifExist=True, msg="密码不能仅包含字母或数字！")         	
            
            # 0.写sql
            query = "SELECT * FROM user WHERE username='{}'".format(username)
            #print(query)
            #通过用户的id来查询用户资料（one=True返回第一条数据）
            result = query_db(query,one=True) 
            print(result)
            if result is None:#数据库里没有该用户，加到数据库
                print('here')
                connection = db.get_db()
                query = "INSERT INTO user(usertype,username,password) values({},'{}','{}')".format(userType,username,password)
                connection.execute(query)
                connection.commit()
                return  dict(ifExist=False,msg = "注册成功！")
            else:#数据库里有该用户
                print('fail')
                return dict(ifExist=True, msg="用户已存在!")
 
    return 'user_add'

@signup.route('/signup_test',methods=['GET','POST'])
@cross_origin()
def signup_test():
    if request.method == 'POST': 
        return 'aaa'