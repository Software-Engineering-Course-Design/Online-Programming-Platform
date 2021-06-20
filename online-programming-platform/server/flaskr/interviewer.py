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
        id_arr = []
        for i in range(len(h_id_arr)):   # 对每条数据库信息进行处理
            item = dict(h_id_arr[i])
            temp.append(item)

        for k in range(len(temp)):
            temp1 = []
            dict1 = temp[k]
            questionID = dict1['questionID']
            heading = dict1['heading']
            temp1.append(questionID)
            temp1.append(heading)
            id_arr.append(temp1)
        return_info = dict(question_num=question_num[0], interviewer_num=interviewer_num[0], id_arr=id_arr)
        #return_info['id_arr'] = tuple(temp)
        json.dumps(return_info)   # 转换成json格式
        return return_info

    else:
        return dict(ifSuccess=False, msg="页面超时，网络发生故障")


# 面试题详情
@interviewer.route('/questionID', methods=['POST'])
@cross_origin()
def questionID():
    if request.method == 'POST':
        uid = request.json.get("uid")  # 获取questionID
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
            id_arr = "SELECT distinct applicant FROM code WHERE code is not null AND questionID={}".format(uid)
            id_arr = query_db(id_arr)
            temp = []
            h_id_arr = []
            for i in range(len(id_arr)):  # 对每条数据库信息进行处理
                item = dict(id_arr[i])
                temp.append(item)
            for k in range(len(temp)):
                dict1 = temp[k]
                applicant = dict1['applicant']
                h_id_arr.append(applicant)
            return_info = dict(username=username, heading=heading, question=body, questionID=uid, id_arr=h_id_arr)
            #return_info['h_id_arr'] = tuple(temp)
            json.dumps(return_info)  # 转换成json格式
            return return_info

    else:
        return dict(msg="查询失败，网络发生故障")

# 查看某面试题的所有已提交代码
@interviewer.route('/questionID_code', methods=['POST'])
@cross_origin()
def questionID_code():
    if request.method == 'POST':
        questionID = request.json.get("questionID")  # 获取questionID
        query = "SELECT * FROM code WHERE questionID={}".format(questionID)
        # 通过questionID来查询面试题详情（one=True返回第一条数据）
        result = query_db(query)
        temp = []
        info = []
        for i in range(len(result)):
            item = dict(result[i])
            temp.append(item)
        for j in range(len(temp)):
            dict1 = temp[j]
            applicant = dict1['applicant']
            code = dict1['code']
            result = dict1['result']
            return_info = dict(applicant=applicant, code=code, result=result)
            info.append(return_info)
        return dict(info=info)
    else:
        return dict(msg="查询失败，网络发生故障")


"""
{
    "info":[{"applicant":"b",
        "code":"111",
        "result":"ac"
        },
        {
        "applicant":"d",
        "code":"111",
        "result":"ac"
        }],
}
"""

# 面试官查看面试情况
@interviewer.route('/interview_info', methods=['POST'])
@cross_origin()
def interview_info():
    if request.method == 'POST':
        username = request.json.get("username")
        query1 = "SELECT distinct sessionID FROM interview WHERE username='{}'".format(username)
        sessionID = query_db(query1)
        temp1 = []
        for i in range(len(sessionID)):  # 对每条数据库信息进行处理
            item = dict(sessionID[i])
            temp1.append(item)  # temp1：得到该面试官的所有sessionID
        print(temp1)
        read_session = []
        unread_session = []

        for i in range(len(temp1)):
            dict1 = temp1[i]
            sessionID = dict1['sessionID']
            print(sessionID)
            query2 = "SELECT result FROM code WHERE sessionID='{}'".format(sessionID)
            result = query_db(query2)
            temp2 = []
            for j in range(len(result)):
                item = dict(result[j])
                temp2.append(item)  # temp2：得到第i个面试的所有代码的批改情况
            print(temp2)

            for k in range(len(temp2)):
                dict2 = temp2[k]
                result = dict2['result']  # result：得到第i个面试的第k个代码的批改情况
                if result == '0':  # 若某个代码未批改，则认为该场面试未被批改
                    unread_session.append(sessionID)
                    break
                if k == len(temp2) - 1:  # 若第i场面试的代码均被批改，则认为该场面试已批改
                    read_session.append(sessionID)
        read = []
        unread = []
        for i in range(len(unread_session)):
            query3 = "SELECT distinct startTime, endTime FROM interview WHERE sessionID='{}'".format(unread_session[i])
            unread_info1 = query_db(query3, one=True)
            startTime = unread_info1['startTime']
            endTime = unread_info1['endTime']
            query4 = "SELECT questionID FROM interview WHERE sessionID='{}'".format(unread_session[i])
            unread_info2 = query_db(query4)
            temp3 = []
            content = []
            for j in range(len(unread_info2)):
                item = dict(unread_info2[j])
                temp3.append(item)  # temp3：得到第i场未批改面试的所有questionID
            for k in range(len(temp3)):
                dict1 = temp3[k]
                questionID = dict1['questionID']
                content.append(questionID)
            return_info = dict(sessionID=unread_session[i], content=content, startTime=startTime, endTime=endTime)
            unread.append(return_info)

        for i in range(len(read_session)):
            query3 = "SELECT distinct startTime, endTime FROM interview WHERE sessionID='{}'".format(read_session[i])
            read_info1 = query_db(query3, one=True)
            startTime = read_info1['startTime']
            endTime = read_info1['endTime']
            query4 = "SELECT distinct questionID FROM interview WHERE sessionID='{}'".format(read_session[i])
            read_info2 = query_db(query4)
            temp3 = []
            content = []
            for j in range(len(read_info2)):
                item = dict(read_info2[j])
                temp3.append(item)  # temp3：得到第i场已批改面试的所有questionID
            for k in range(len(temp3)):
                dict1 = temp3[k]
                questionID = dict1['questionID']
                content.append(questionID)
            return_info = dict(sessionID=read_session[i], content=content, startTime=startTime, endTime=endTime)
            read.append(return_info)
        print(unread, read)
        return dict(unread=unread, read=read)
    
    else:
        return dict(msg="查询失败，网络发生故障")


# 点击某个用户ID即触发请求，显示该面试者提交的代码以及批改结果
@interviewer.route('/code', methods=['POST'])
@cross_origin()
def code():
    if request.method == 'POST':
        applicant = request.json.get("applicant")
        questionID = request.json.get("questionID")
        sessionID = request.json.get("sessionID")
        query = "SELECT * FROM code WHERE questionID={} and applicant='{}' and sessionID={}".format(questionID, applicant, sessionID)
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
        #question=request.json.get("question")
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
        #createWay = request.json.get("createWay")
        createWay = True
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
                    query = "INSERT INTO interview(sessionID,username,applicant, questionNumber, questionID, status," \
                            " createWay, startTime, endTime, timeUsed) values({},'{}','{}',{},{},{},{},'{}','{}','{}')"\
                        .format(sessionID, username, applicant[j], questionNumber, questionID[i], status, createWay, startTime, endTime, timeUsed)
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
        '''
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
                    return dict(ifSuccess=False, msg="该代码已被批改过，不可重复批改")'''

        for i in range(len(result_detail)):
            dict1 = result_detail[i]
            applicant = dict1['applicant']
            questionID = dict1['questionID']
            result = dict1['value']
            print(applicant, result, questionID)
            query = "SELECT result FROM code WHERE applicant='{}' AND questionID={} AND sessionID={}".format(applicant,
                                                                                                             questionID,
                                                                                                             sessionID)
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

"""
{
    "username":"a",
    "result":[{
        "applicant":"d",
        "questionID":1,
        "value":"ac"
        }
        ,{
        "applicant":"b",
        "questionID":1,
        "value":"ac"
    }],
    
    "sessionID":1
}"""
