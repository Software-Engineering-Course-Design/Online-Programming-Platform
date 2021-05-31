from flask import Blueprint, request
from . import db
from flask_cors import *
import sqlite3
import json
from datetime import datetime

interviewer = Blueprint('interviewer', __name__)


def query_db(query, args=(), one=False):
    cur = db.get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


# 面试官首页
@interviewer.route('/interviewer_info', methods=['GET'])
@cross_origin()
def interviewer_info():
    if request.method == 'GET':
        question_num = "SELECT count(*) FROM question"
        interviewer_num = "SELECT count(id) FROM user WHERE usertype=False"
        h_id_arr = "SELECT questionID, heading FROM question"

        question_num = query_db(question_num, one=True)
        interviewer_num = query_db(interviewer_num, one=True)
        h_id_arr = query_db(h_id_arr)

        question_num = tuple(question_num)
        interviewer_num = tuple(interviewer_num)

        # 面试题数组（返回所有面试题标题、questionID）
        temp = []
        for i in range(len(h_id_arr)):   # 对每条数据库信息进行处理
            item = dict(h_id_arr[i])
            temp.append(item)
        return_info = dict(question_num=question_num[0], interviewer_num=interviewer_num[0])
        return_info['h_id_arr'] = tuple(temp)
        json.dumps(return_info)   # 转换成json格式
        return return_info

    else:
        return dict(ifSuccess=False, msg="页面超时，网络发生故障")


# 面试题详情
@interviewer.route('/questionID', methods=['GET'])
@cross_origin()
def questionID():
    if request.method == 'GET':
        # name = request.args.get('name', '')
        uid = request.args.get('uid')  # 获取questionID
        query = "SELECT * FROM question WHERE questionID={}".format(uid)
        # 通过questionID来查询面试题详情（one=True返回第一条数据）
        result = query_db(query, one=True)
        if result is None:
            return dict(message="查询失败，不存在该面试题")
        else:
            heading = result['heading']
            body = result['body']
            username = result['username']

            # 面试者数组（返回提交了该题的面试者用户ID）
            id_arr = "SELECT applicant FROM code WHERE code is not null AND questionID={}".format(uid)
            id_arr = query_db(id_arr)
            temp = []
            for i in range(len(id_arr)):  # 对每条数据库信息进行处理
                item = dict(id_arr[i])
                temp.append(item)
            return_info = dict(username=username, heading=heading, body=body, questionID=uid)
            return_info['h_id_arr'] = tuple(temp)
            json.dumps(return_info)  # 转换成json格式
            return return_info

    else:
        return dict(msg="查询失败，网络发生故障")


# 点击某个用户ID即触发请求，显示该面试者提交的代码以及批改结果
@interviewer.route('/code', methods=['POST'])
@cross_origin()
def code():
    if request.method == 'POST':
        applicant = request.json.get("applicant")
        questionID = request.json.get("questionID")
        query = "SELECT * FROM code WHERE questionID={} or applicant='{}'".format(questionID, applicant)
        query = query_db(query, one=True)
        if query is None:
            return dict(message="查询失败，不存在该用户提交的代码")
        else:
            code = query['code']
            result = query['result']
            return dict(code=code, result=result)
    else:
        return dict(msg="查询失败，网络发生故障")


# 面试官新建面试题
@interviewer.route('/add_question', methods=['POST'])
@cross_origin()
def add_question():
    if request.method == 'POST':
        username = request.json.get("username")
        heading = request.json.get("heading")
        question=request.json.get("question")
        body = request.json.get("question")
        answer = request.json.get("answer")
        query = "SELECT * FROM question WHERE heading='{}'".format(heading)
        # 通过面试题标题来查询题目是否存在（one=True返回第一条数据）
        result = query_db(query, one=True)
        if result is None:  # 数据库里没有该面试题，加到数据库
            connection = db.get_db()
            query = "INSERT INTO question(username, heading, body, answer) values('{}','{}','{}','{}')"\
                .format(username, heading, body, answer)
            connection.execute(query)
            connection.commit()
            return dict(ifSuccess=True, msg="新建成功")
        else:  # 数据库里有该题目
            return dict(ifSuccess=False, msg="新建失败，该面试题已存在")
    else:
        return dict(ifSuccess=False, msg="新建失败，网络发生故障")


# 面试官修改面试题目
@interviewer.route('/edit_question', methods=['POST'])
@cross_origin()
def edit_question():
    if request.method == 'POST':
        if request.method == 'POST':
            username = request.json.get("username")
            questionID = request.json.get("questionID")
            heading = request.json.get("newHeading")
            body = request.json.get("newQuestion")
            query = "SELECT * FROM question WHERE questionID={}".format(questionID)
            # 通过questionID来查询题目详情（one=True返回第一条数据）
            result = query_db(query, one=True)
            if result is None:  # 数据库里没有该面试题
                return dict(ifSuccess=False, msg="修改失败,不存在该面试题")
            else:  # 数据库里有该面试题
                connection = db.get_db()
                query = "UPDATE question SET heading='{}', body='{}' WHERE questionID={}"\
                    .format(heading, body, questionID)
                connection.execute(query)
                connection.commit()
                return dict(ifSuccess=True, msg="修改成功")
        else:
            return dict(ifSuccess=False, msg="修改失败，网络发生故障")


# 发起一场面试
@interviewer.route('/initial_interview', methods=['POST'])
@cross_origin()
def initial_interview():
    if request.method == 'POST':
        username = request.json.get("username")
        applicant = request.json.get("applicant")  # 数组
        questionNumber = request.json.get("questionNumber")
        questionID = request.json.get("questionID")  # 数组
        createWay = request.json.get("createWay")
        startTime = request.json.get("startTime")
        endTime = request.json.get("endTime")
        query = "SELECT max(sessionID) FROM interview"
        # 通过用户的id来查询用户资料（one=True返回第一条数据）
        result = query_db(query, one=True)
        sessionID = tuple(result)[0]
        status = False  # 面试状态初始为未参加状态

        startTime = datetime.strptime(startTime, '%Y-%m-%d %H:%M:%S')
        endTime = datetime.strptime(endTime, '%Y-%m-%d %H:%M:%S')
        # 计算用时
        timeUsed = (endTime - startTime).total_seconds()

        m, s = divmod(timeUsed, 60)
        h, m = divmod(m, 60)
        timeUsed = "%02d:%02d:%02d" % (h, m, s)

        if sessionID is None:
            sessionID = 0
        sessionID += 1
        for k in range(len(applicant)):
            query = "SELECT id FROM user WHERE username='{}'".format(applicant[k])
            query = query_db(query, one=True)
            if query is None:
                return dict(ifSuccess=False, msg="邀请失败，邀请用户不存在")
        if len(questionID) == questionNumber:
            connection = db.get_db()
            for i in range(questionNumber):
                for j in range(len(applicant)):
                    query = "INSERT INTO interview(sessionID,username,applicant, questionNumber, questionID, createWay, status, startTime, endTime, timeUsed) " \
                            "values({},'{}','{}',{},{},{},{},'{}','{}','{}')"\
                        .format(sessionID, username, applicant[j], questionNumber, questionID[i], createWay, status, startTime, endTime, timeUsed)
                    connection.execute(query)
                    connection.commit()
            return dict(ifSuccess=True, msg="邀请成功", sessionID=sessionID)
        else:
            return dict(ifSuccess=False, msg="邀请失败，面试题错误")
    else:
        return dict(ifSuccess=False, msg="邀请失败，网络发生故障")


'''{
    "username":"a",
    "applicant":["d","b"],
    "questionNumber":2,
    "questionID":[1,2],
    "createWay":true,
    "startTime":"2004-01-01 02:34:56",
    "endTime":"2004-01-01 03:34:56"
}'''


# 面试官批改提交代码
@interviewer.route('/check_code', methods=['POST'])
@cross_origin()
def check_code():
    if request.method == 'POST':
        username = request.json.get("username")
        result_detail = request.json.get("result")
        sessionID = request.json.get("sessionID")
        connection = db.get_db()
        for i in range(len(result_detail)):
            dict1 = result_detail[i]
            applicant = dict1['examineeID']
            answer = dict1['answer']

            for j in range(len(answer)):
                dict2 = answer[j]
                questionID = dict2["idx"]
                result = dict2["value"]
                query = "SELECT result FROM code WHERE applicant='{}' AND questionID={} AND sessionID={}".format(applicant, questionID, sessionID)
                result_before = query_db(query, one=True)
                result_before = tuple(result_before)
                print('3', result_before[0])
                if result_before[0] == '0':
                    # query = "INSERT INTO code(result,username,questionID) values('{}','{}','{}')"\
                     # .format(result, username, questionID)
                    query = "UPDATE code SET result='{}' WHERE applicant='{}' AND questionID={} AND sessionID={}" \
                        .format(result, applicant, questionID, sessionID)
                    connection.execute(query)
                    connection.commit()
                    print('success')
                else:
                    return dict(ifSuccess=False, msg="该代码已被批改过，不可重复批改")
        return dict(ifSuccess=True, msg="批改成功!")

    else:
        return dict(ifSuccess=False, msg="批改失败，网络发生故障")


"""
{
    "username":"a",
    "result":[{
        "examineeID":"d",
        "answer":[
            {
            "idx":1,
            "value":"ac"
        },{
            "idx":2,
            "value":"ac"
        }
        ]
    },{
        "examineeID":"b",
        "answer":[
            {
            "idx":1,
            "value":"ac"
        },{
            "idx":2,
            "value":"ac"
        }
        ]
    }],
    
    "sessionID":1
}
"""