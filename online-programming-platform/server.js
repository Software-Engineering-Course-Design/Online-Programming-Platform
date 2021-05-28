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
app.post('/questionList', (request, response) => {
    response.setHeader('Access-Control-Allow-Origin', '*');
    const data = {
        id_arr: [11, 22, 33, 44],
        heading_arr: ['h1', 'h2', 'h3', 'h4'],
        question_arr: ['q1', 'q2', 'q3', 'q4'],
        

    };
    let str = JSON.stringify(data);
    response.send(str);
});
app.post('/viewResult', (request, response) => {
    response.setHeader('Access-Control-Allow-Origin', '*');
    const data = {
        id_arr: [11, 22, 33, 44],
        msg: {
            "join": [{
                    "sessionID": 1,
                    "hr_name": "aaa",
                    "questionNumber": 3,
                    "time": 1.5
                },
                {
                    "sessionID": 2,
                    "hr_name": "bbb",
                    "questionNumber": 2,
                    "time": 1
                }
            ],
            "notjoin": [{
                    "sessionID": 3,
                    "hr_name": "aaa",
                    "questionNumber": 3,
                    "time": 1.5
                },
                {
                    "sessionID": 2,
                    "hr_name": "bbb",
                    "questionNumber": 2,
                    "time": 1
                }
            ]
        }
    };
    let str = JSON.stringify(data);
    console.log(data);
    response.send(str);
});
app.post('/interviewList', (request, response) => {
    response.setHeader('Access-Control-Allow-Origin', '*');
    const data = {
        join: [{
            "sessionID": 1,
            "hr_username": "aaa",
            "questionNumber": 3,
            "status": 150,
            "score":100,
        },
        {
            "sessionID": 2,
            "hr_username": "bbb",
            "questionNumber": 2,
            "status": 1,
            "score":80,
        }
    ],
    //可参加
    notjoin: [{
            "sessionID": 3,
            "hr_username": "提前10分钟",
            "questionNumber": 3,
            "startTime":'2021-05-28 19:30:00',
            "endTime":'2021-05-28 22:50:00',
            "time": 300
        },
        {
            "sessionID": 2,
            "hr_username": "迟到十五分钟",
            "questionNumber": 2,
            "startTime":'2021-05-28 18:40:00',
            "endTime":'2021-05-28 20:30:00',
            "time": 300
        },
        {
            "sessionID": 56,
            "hr_username": "没开始",
            "questionNumber": 6,
            "startTime":'2021-05-29 17:50:00',
            "endTime":'2021-05-29 18:50:00',
            "time": 300
        },
        {
            "sessionID": 6,
            "hr_username": "已结束",
            "questionNumber": 6,
            "startTime":'2021-05-22 17:50:00',
            "endTime":'2021-05-22 18:50:00',
            "time": 300
        },
    ]
    };
    let str = JSON.stringify(data);
    response.send(str);
});
app.listen(8000, () => {
    console.log("listening 8000……");
});