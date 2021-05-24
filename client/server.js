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
app.post('/server', (request, response) => {
    response.setHeader('Access-Control-Allow-Origin', '*');
    response.send("helloxxxxx post");
});
app.post('/check', (request, response) => {
    response.setHeader('Access-Control-Allow-Origin', '*');
    const data = {
        exist: 1,
        msg: '用户名已存在！'
    };
    let str = JSON.stringify(data);
    //response.send(`handle(${str})`);
    response.send(str);
});
app.get('/testget', (request, response) => {
    response.setHeader('Access-Control-Allow-Origin', '*');
    const data = {
        exist: 1,
        msg: '用户名已存在！'
    };
    let str = JSON.stringify(data);
    response.send(data);
});
app.post('/questionList', (request, response) => {
    response.setHeader('Access-Control-Allow-Origin', '*');
    const data = {
        id_arr:[11,22,33,44],
        heading_arr:['h1','h2','h3','h4'],
        question_arr:['q1','q2','q3','q4'],
    };
    let str = JSON.stringify(data);
    response.send(str);
});
app.listen(8000, () => {
    console.log("listening 8000……");
});