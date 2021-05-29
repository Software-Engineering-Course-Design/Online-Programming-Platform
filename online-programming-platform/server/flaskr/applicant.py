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
		#status True已参加 False未参加
		query = "SELECT distinct sessionID, username, questionNumber, startTime, endTime, TimeUsed FROM interview WHERE applicant='{}' AND status='False'".format(interviewee)
		result = query_db(query) 
		#print(result['sessionID'])sssssss
		temp=[]
		length=len(result)  #对每条数据库信息进行处理
		for i in range(length):  
			item=dict(result[i])  
			temp.append(item)
		notjoin_list=dict(notjoinlist=tuple(temp))
		json.dumps(notjoin_list)
		return notjoin_list

@applicant.route('/question_message',methods=['GET','POST'])
@cross_origin()
def question_message():
	if request.method == 'POST':
		sessionID  = request.json.get("sessionID")
		# 0.写sql
		query = "SELECT questionID, heading, body FROM question WHERE questionID in (SELECT questionID FROM interview WHERE sessionID='{}')".format(sessionID)
		result = query_db(query) 
		temp=[]
		length=len(result)  #对每条数据库信息进行处理
		for i in range(length):  
			item=dict(result[i])  
			temp.append(item)
		question_list=dict(question_list=tuple(temp))
		json.dumps(question_list)
		return question_list

@applicant.route('/commit_code',methods=['GET','POST'])
@cross_origin()
def commit_code():
	if request.method == 'POST':
		username  = request.json.get("username")#面试者用户ID
		sessionID  = request.json.get("sessionID")#场次
		questionID = request.json.get("questionID")#问题ID
		code = reques.json.get("code")#代码内容
		questionStatus = reques.json.get("questionStatus")#代码提交状态，默认false
		# 0.写sql
		query = "SELECT questionID, heading, body FROM question WHERE questionID in (SELECT questionID FROM interview WHERE sessionID='{}')".format(sessionID)
		result = query_db(query) 
		temp=[]
		length=len(result)  #对每条数据库信息进行处理
		for i in range(length):  
			item=dict(result[i])  
			temp.append(item)
		question_list=dict(question_list=tuple(temp))
		json.dumps(question_list)
		return question_list