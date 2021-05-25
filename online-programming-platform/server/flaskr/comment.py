from flask import Blueprint, render_template, redirect,request
from . import db
from flask_cors import *
import json

comment = Blueprint('comment',__name__)

def query_db(query, args=(), one=False):
        cur = db.get_db().execute(query, args)
        rv = cur.fetchall()
        cur.close()
        return (rv[0] if rv else None) if one else rv

@comment.route('/comment_add',methods=['GET','POST'])
@cross_origin()
def comment_add():
    if request.method == 'POST': 
        questionID=request.json.get("questionID")
        senderID=request.json.get("senderID")
        content=request.json.get("commentContent")
        isSub=request.json.get("isSublayer")
        layerid=request.json.get("layerID")
        # 0.写sql
        connection = db.get_db()  
        #插入数据
        query_in="INSERT INTO comment(questionID,username,content,isSublayer,layer) values('{}','{}','{}','{}','{}')".format(questionID,senderID,content,isSub,layerid)
        try:
            connection.execute(query_in)
            connection.commit()
        except Exception as e:
            return dict(ifSuccess=False,msg="New comment added failed!")
        else:
            return  dict(ifSuccess=True,msg = "true") 
    else:
        return dict(ifSuccess=False,msg = "Permission denied!") 
 
@comment.route('/comment_search',methods=['GET','POST'])
@cross_origin()
def comment_search():
    if request.method=='POST':
        username=request.json.get("username") 
        usertype=request.json.get("userType") 
        qid=request.json.get("questionID") 
        query="SELECT * FROM comment WHERE questionID='{}'".format(qid)
        result = query_db(query)
        temp=[]
        length=len(result) 
        for i in range(length):   #对每条数据库信息进行处理
            item=dict(result[i])  
            temp.append(item)
        return_info=dict(ifSuccess=True,questionID=qid,msg="Success!")
        return_info['commentList']=tuple(temp)
        json.dumps(return_info)   #转换成json格式
        return return_info  
    else:
        return dict(ifSuccess=False,questionID=-1,msg = "Permission denied!",commentList=[]) 


