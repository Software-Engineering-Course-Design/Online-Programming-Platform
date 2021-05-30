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

#面试者首页
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

#在线编程题目显示模块
#将该场次的面试题返回给前端，并把该用户该场次的面试设为已参加状态 
@applicant.route('/question_message',methods=['GET','POST'])
@cross_origin()
def question_message():
	if request.method == 'POST':
		sessionID  = request.json.get("sessionID")
		applicant = request.json.get("username")#面试者
		#改状态
		connection = db.get_db()
		query = "UPDATE interview SET status='True' WHERE sessionID='{}' AND applicant='{}'".format(sessionID, applicant)
		connection.execute(query)
		connection.commit()		
		#返回该场次的面试题信息
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

#提交
@applicant.route('/commit_code',methods=['GET','POST'])
@cross_origin()
def commit_code():
	if request.method == 'POST':
		applicant  = request.json.get("username")#面试者用户ID
		sessionID  = request.json.get("sessionID")#场次
		questionID = request.json.get("questionID")#问题ID
		code = request.json.get("code")#代码内容

		connection = db.get_db()
		query = "UPDATE code SET code='{}' WHERE sessionID='{}' AND questionID='{}' AND applicant ='{}'".format(code, sessionID, questionID, applicant )
		connection.execute(query)
		connection.commit()
		return dict(ifSuccess=True, msg="提交成功")
	else:
		return dict(ifSuccess=False, msg="提交失败，网络发生故障！")

#结束面试（场次）
#答题结束之后总交卷
@applicant.route('/end_session',methods=['GET','POST'])
@cross_origin()
def end_session():
	if request.method == 'POST':
		username  = request.json.get("username")#面试者用户ID
		sessionID  = request.json.get("sessionID")#场次
		submit_time = request.json.get("submit_time")
		return dict(ifSuccess=True, msg="交卷成功,已结束面试!")
	else:
		return dict(ifSuccess=False, msg="交卷失败，网络发生故障!")

#查看已参加的面试的结果
#按面试场次显示，按场次顺序显示题目标题，点击标题可查看面试题内容、提交代码内容、标准答案以及批改结果
@applicant.route('/interview_result',methods=['GET','POST'])
@cross_origin()
def interview_result():
	if request.method == 'POST':
		applicant  = request.json.get("username")#面试者用户ID
		sessionID  = request.json.get("sessionID")#场次
		query = "SELECT code.questionID, heading, body, code, answer, result FROM code inner join question on code.questionID=question.questionID WHERE sessionID='{}' AND applicant='{}'".format(sessionID, applicant)

		result = query_db(query) 
		temp=[]
		length=len(result)  #对每条数据库信息进行处理
		for i in range(length):  
			item=dict(result[i])  
			temp.append(item)
		interview_result_list=dict(interview_result_list=tuple(temp))
		json.dumps(interview_result_list)
		return interview_result_list