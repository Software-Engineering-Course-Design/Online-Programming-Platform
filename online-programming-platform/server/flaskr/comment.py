from flask import Blueprint, render_template, redirect,request
from . import db

comment = Blueprint('comment',__name__)

def query_db(query, args=(), one=False):
        cur = db.get_db().execute(query, args)
        rv = cur.fetchall()
        cur.close()
        return (rv[0] if rv else None) if one else rv

@comment.route('/comment_add',methods=['GET','POST'])
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
            connection.execute(query_in)
            connection.commit()
            return  dict(ifSuccess=True,msg = "true") 

    else:
        return dict(ifExist=False,usertype=2,msg = "user doesn't exist") 
 
@comment.route('/comment_search',methods=['GET','POST'])
def comment_search():
     if request.method=='GET':
         username=request.json.get("username") 
         usertype=request.json.get("userType") 
         qid=request.json.get("questionID") 
         query="SELECT * FROM comment WHERE questionID='{}'".format(qid)
         result = query_db(query)
         print(len(result))  #后续根据长度发送dict
         return dict(result[0])

