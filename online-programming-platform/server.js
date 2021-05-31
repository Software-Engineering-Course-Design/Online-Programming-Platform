const express = require('express');
const app = express();
app.use((req, res, next) => {
    //设置请求头
    res.set({
        'Access-Control-Allow-Credentials': true,
        'Access-Control-Max-Age': 1728000,
        'Access-Control-Allow-Origin': req.headers.origin || '*',
        'Access-Control-Allow-Headers': 'X-Requested-With,Content-Type',
        'Access-Control-Allow-Methods': 'PUT,POST,GET,DELETE,OPTIONS',
        'Content-Type': 'application/json; charset=utf-8'
    })
    req.method === 'OPTIONS' ? res.status(204).end() : next()
})
app.post('/submitCode', (request, response) => {
    response.setHeader('Access-Control-Allow-Origin', '*');
    const data = {
        ifSuccess: true,
        msg: '提交代码成功！'
    };
    let str = JSON.stringify(data);
    response.send(str);
});
app.post('/signup', (request, response) => {
    response.setHeader('Access-Control-Allow-Origin', '*');
    const data = {
        ifExist: true,
        msg: '用户名已存在！'
    };
    let str = JSON.stringify(data);
    //response.send(`handle(${str})`);
    response.send(str);
});
app.post('/login', (request, response) => {
    response.setHeader('Access-Control-Allow-Origin', '*');
    console.log(request);
    const data = {
        ifExist: false,
        msg: '登录成功！'
    };
    let str = JSON.stringify(data);
    //response.send(`handle(${str})`);
    response.send(str);
});
app.post('/handin', (request, response) => {
    response.setHeader('Access-Control-Allow-Origin', '*');
    const data = {
        ifSuccess: true,
        msg: '交卷成功！'
    };
    let str = JSON.stringify(data);
    response.send(data);
});
app.post('/submitJudge', (request, response) => {
    response.setHeader('Access-Control-Allow-Origin', '*');
    // const data = {
    //     ifExist: true,
    //     msg: '您已提交过一次，不能重复提交哦！'
    // };
    const data = {
        ifExist: false,
        msg: '可以提交！'
    };
    let str = JSON.stringify(data);
    response.send(data);
});
app.post('/questionList', (request, response) => {
    response.setHeader('Access-Control-Allow-Origin', '*');
    const data = {
        question_list: [{
                "body": "write a Stack",
                "heading": "Stack",
                "questionID": 3
            },
            {
                "body": "reverse the Linklist",
                "heading": "Linklsit",
                "questionID": 4
            }
        ]
    };
    let str = JSON.stringify(data);
    response.send(str);
});
app.post('/viewResult', (request, response) => {
    response.setHeader('Access-Control-Allow-Origin', '*');
    const data = {
        interview_result_list: [{
                "answer": "answer1",
                "body": "body1",
                "code": "console.log('第一行')↵↵↵↵console.log('2')",
                "heading": "Stack",
                "questionID": 1,
                "result": 0
            },
            {
                "answer": "answer2",
                "body": "body2",
                "code": null,
                "heading": "Queue",
                "questionID": 2,
                "result": "AC"
            }
        ]
    };
    let str = JSON.stringify(data);
    response.send(str);
});
app.post('/interviewList', (request, response) => {
    response.setHeader('Access-Control-Allow-Origin', '*');
    const data = {
        join: [{
                "sessionID": 1,
                "hr_username": "aaa",
                "questionNumber": 3,
                "startTime": '2021-05-28 17:30:00',
                "endTime": '2021-05-28 22:50:00',
                "status": true,
                "score": 100,
            },
            {
                "sessionID": 2,
                "hr_username": "bbb",
                "questionNumber": 2,
                "startTime": '2021-05-28 18:00:00',
                "endTime": '2021-05-28 22:50:00',
                "status": false,
                "score": -1,
            }
        ],
        //可参加
        notjoin: [{
                "sessionID": 3,
                "hr_username": "提前10分钟",
                "questionNumber": 3,
                "startTime": '2021-05-31 19:35:00',
                "endTime": '2021-05-31 22:50:00',
                "timeUsed": 300
            },
            {
                "sessionID": 2,
                "hr_username": "测试交卷",
                "questionNumber": 2,
                "startTime": '2021-05-31 18:00:00',
                "endTime": '2021-05-31 22:06:00',
                "timeUsed": 300
            },
            {
                "sessionID": 56,
                "hr_username": "没开始",
                "questionNumber": 6,
                "startTime": '2021-05-31 17:50:00',
                "endTime": '2021-05-31 18:50:00',
                "timeUsed": 300
            },
            {
                "sessionID": 6,
                "hr_username": "已结束",
                "questionNumber": 6,
                "startTime": '2021-05-22 17:50:00',
                "endTime": '2021-05-22 18:50:00',
                "timeUsed": 300
            },
        ]
    };
    let str = JSON.stringify(data);
    response.send(str);
});
app.listen(8000, () => {
    console.log("listening 8000……");
});