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
		#notjoin序列，没参加
		# 0.写sql
		#status True已参加 False未参加
		query = "SELECT distinct sessionID, username, questionNumber, startTime, endTime, TimeUsed FROM interview WHERE applicant='{}' AND status=0".format(interviewee)
		result = query_db(query) 
		#print(result['sessionID'])sssssss
		temp=[]
		length=len(result)  #对每条数据库信息进行处理
		for i in range(length):  
			item=dict(result[i])  
			temp.append(item)
		join_message_list=dict(notjoin=tuple(temp))

		#join序列 已参加
		query = "SELECT distinct sessionID, username, questionNumber, startTime, endTime FROM interview WHERE applicant='{}' AND status=1".format(interviewee)
		result = query_db(query) 
		#print(result['sessionID'])sssssss
		temp=[]
		length=len(result)  #对每条数据库信息进行处理
		for i in range(length):  
			score = 0
			AC_number = 0
			item=dict(result[i]) 

			#先把状态和分数置为true和-1
			item['status'] = 'true'
			item['score'] = 0

			temp_sessionID = item['sessionID']
			temp_questionNumber = item["questionNumber"]
			print("sessionID",temp_sessionID)
			print("questionnumber",temp_questionNumber)
			#查每一场的代码批改结果
			temp_query = "SELECT result FROM code WHERE applicant='{}' AND sessionID='{}'".format(interviewee, temp_sessionID)
			temp_result = query_db(temp_query) 
			#temp_temp=[]
			temp_length=len(temp_result)
			for j in range(temp_length):
				temp_item = dict(temp_result[j])
				print("result",temp_item['result'])

				if temp_item['result'] == '0':
					item['status'] = 'false';#有一道题没有批改，状态就是false未批改
					item['score'] = -1
					break;
				elif temp_item['result'] == 'AC':#有题目AC，AC数加一
					AC_number = AC_number+1

			if item['status'] == 'true':
				item['score'] = 100*AC_number/temp_questionNumber

			temp.append(item)
		join_message_list['join']=tuple(temp)

		json.dumps(join_message_list)
		return join_message_list

# @applicant.route('/join_message',methods=['GET','POST'])
# @cross_origin()
# def join_message():
# 	if request.method == 'POST':
# 		interviewee=request.json.get("username") 
# 		# 0.写sql
# 		#status True已参加 False未参加
# 		query = "SELECT distinct sessionID, username, questionNumber, startTime, endTime FROM interview WHERE applicant='{}' AND status='True'".format(interviewee)
# 		result = query_db(query) 
# 		#print(result['sessionID'])sssssss
# 		temp=[]
# 		length=len(result)  #对每条数据库信息进行处理
# 		for i in range(length):  
# 			score = 0
# 			AC_number = 0
# 			item=dict(result[i]) 

# 			item['status'] = 'true'
# 			item['score'] = 0

# 			temp_sessionID = item['sessionID']
# 			temp_questionNumber = item["questionNumber"]
# 			print("sessionID",temp_sessionID)
# 			print("questionnumber",temp_questionNumber)
# 			temp_query = "SELECT result FROM code WHERE applicant='{}' AND sessionID='{}'".format(interviewee, temp_sessionID)
# 			temp_result = query_db(temp_query) 
# 			temp_temp=[]
# 			temp_length=len(temp_result)
# 			for j in range(temp_length):
# 				temp_item = dict(temp_result[j])
# 				print("result",temp_item['result'])

# 				if temp_item['result'] == '0':
# 					item['status'] = 'false';#有一道题没有批改，状态就是false未批改
# 					item['score'] = -1
# 					break;
# 				elif temp_item['result'] == 'AC':
# 					AC_number = AC_number+1

# 			if item['status'] == 'true':
# 				item['score'] = 100*AC_number/temp_questionNumber

# 			temp.append(item)
# 		join_list=dict(joinlist=tuple(temp))
# 		json.dumps(join_list)
# 		return join_list



# 		#notjoin_list=dict(notjoinlist=tuple(temp))
# 		#json.dumps(notjoin_list)
# 		return '1'


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
		query = "UPDATE interview SET status=1 WHERE sessionID='{}' AND applicant='{}'".format(sessionID, applicant)
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

#代码只能提交一次，判断是否已经提交过了
@applicant.route('/submit_message',methods=['GET','POST'])
@cross_origin()
def submit_message():
	if request.method == 'POST':
		sessionID = request.json.get("sessionID")
		applicant = request.json.get("username")
		questionID = request.json.get("questionID")
		query = "SELECT * FROM code WHERE sessionID='{}' AND applicant='{}' AND questionID='{}'".format(sessionID, applicant, questionID)
		result = query_db(query,one=True) 
		#print(result['code'])
		if result['code'] is None:
			return  dict(ifExist=False,msg = "可提交")
		else:
			return  dict(ifExist=True,msg = "已提交过，不可重复提交")