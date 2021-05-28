from flask import Blueprint, render_template, redirect,request
from . import db
from flask_cors import *
import json

applicant = Blueprint('applicant',__name__)

def query_db(query, args=(), one=False):
        cur = db.get_db().execute(query, args)
        rv = cur.fetchall()
        cur.close()
        return (rv[0] if rv else None) if one else rv

@applicant.route('/join_message',methods=['GET','POST'])
@cross_origin()
def join_message():
	if request.method == 'POST':
		interviewee=request.json.get("username") 
		# 0.写sql
		query = "SELECT sessionID, username, questionNumber,  FROM interview WHERE applicant='{}' AND status='True'".format(interviewee)
		result = query_db(query) 
		#print(result['sessionID'])sssssss
		temp=[]
		length=len(result)  #对每条数据库信息进行处理
		for i in range(length):  
			item=dict(result[i])  
			temp.append(item)
		return_info=dict(joinlist=tuple(temp))
		json.dumps(return_info)
		return return_info

