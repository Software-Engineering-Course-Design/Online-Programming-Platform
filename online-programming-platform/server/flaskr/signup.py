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
@cross_orgin()
def signup_info():
    if request.method == 'POST': 
#
            username=request.json.get("username") 
            userType=request.json.get("userType")
            password=request.json.get("password") 
            checkpwd=request.json.get("checkpwd")
            hr_code=request.json.get("hr_code")

            if password!=checkpwd:
                return dict(ifExist=True, msg="fail! password and checkpwd are not same!")
            if userType=="true" and hr_code!="666666":
                return dict(ifExist=True, msg="fail! hr_code is wrong!")
            
            # 0.写sql
            query = "SELECT * FROM user WHERE username='{}'".format(username)
            #print(query)
            #通过用户的id来查询用户资料（one=True返回第一条数据）
            result = query_db(query,one=True) 
            #print(result['username'])
            if result is None:#数据库里没有该用户，加到数据库
                connection = db.get_db()
                query = "INSERT INTO user(usertype,username,password) values('{}','{}','{}')".format(userType,username,password)
                connection.execute(query)
                connection.commit()
                return  dict(ifExist=False,msg = "success")
            else:#数据库里有该用户
                return dict(ifExist=True, msg="fail! user already existed!")
 
    return 'user_add'

@signup.route('/signup_test',methods=['GET','POST'])
@cross_orgin()
def signup_test():
    if request.method == 'POST': 
        return 'aaa'