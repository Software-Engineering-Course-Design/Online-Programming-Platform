from flask import Blueprint, render_template, redirect,request
from . import db

login = Blueprint('login',__name__)

def query_db(query, args=(), one=False):
        cur = db.get_db().execute(query, args)
        rv = cur.fetchall()
        cur.close()
        return (rv[0] if rv else None) if one else rv

@login.route('/login_info',methods=['GET','POST'])
def login_info():
    if request.method == 'POST': 
            username=request.json.get("username") 
            password=request.json.get("password") 
            # 0.写sql
            query = "SELECT * FROM user WHERE username='{}'".format(username)
            #通过用户的id来查询用户资料（one=True返回第一条数据）
            result = query_db(query,one=True) 
            if result is None:
                return  dict(ifExist=False,usertype=2,msg = "user doesn't exist")
            else:
                password_match=result['password']
                if password_match==password:
                    userType=result['usertype']
                    msg="success"
                    return dict(ifExist=True,userType=userType,msg=msg)
                else:
                    return dict(ifExist=True,userType=result['usertype'],msg="Fail!Wrong password!")
    else:
        return dict(ifExist=False,usertype=2,msg = "permission denied!")
 
    return 'user_add'

